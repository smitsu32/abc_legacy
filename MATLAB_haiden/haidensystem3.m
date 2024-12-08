clear;
addpath(genpath(pwd));
% どのデータを読み取るか?(SVR.effNode以外は全て格納済)
load('Systemdata106.mat');

nTimeInterval=15;
svrTimeInterval=30;
diffInterval=svrTimeInterval/nTimeInterval;
nTime=60*24/nTimeInterval;
svrTime=60*24/svrTimeInterval;
Opt=struct('nTime',nTime,'svrTime',svrTime);

Edges=Systemdata.Grid.Edges;
Nodes=Systemdata.Grid.Nodes;
nCharger=sum(Nodes.Charger);
nNode=height(Nodes);
nBr=height(Edges);
nSvr=height(Edges)-sum(cellfun(@isempty,Edges.SVR));

Charger=struct('Smax',10000,'Emax',10000,'ind',[]);
Svr=struct('nTap',9,'defTap',5,'dVTap',75); %V
Lrt=struct('nTap',21,'defTap',11,'dVTap',30);
% nLrt=1;
Charger.ind=[]; Svr.ind=[]; 
for i=1:nNode
    Charger.ind=[Charger.ind, i*ones(Nodes.Charger(i))];
end
sort(Charger.ind);
Charger.Smax=10000; %kVA

Lrt.effNode=zeros(nNode,1);
Lrt.effNode(:,1)=true;

% 毎回変更すること(元データに足す予定です)
Svr.effNode=zeros(nNode,nSvr);
Svr.effNode(23:95,1) =true;
% Svr.effNode(8:14,2) =true;
% Svr.effNode(8:14,3) =true;
% Svr.effNode(8:14,4) =true;

%% Svr.effNode('SVRより末端側全てのノード' , '何番目のSVRか') =true;

%最適化
prob=optimproblem;
%変数
% 回数カウント
SvrTapC = optimvar ('SvrTapC',Opt.svrTime,nSvr,...
    'Type','integer','LowerBound',zeros(Opt.svrTime,nSvr),'UpperBound',ones(Opt.svrTime,nSvr));
LrtTapC = optimvar ('LrtTapC',Opt.svrTime,1,...
    'Type','integer','LowerBound',zeros(Opt.svrTime,1),'UpperBound',ones(Opt.svrTime,1));

% タップ位置 %Svr:-4~+4 Lrt:1~21
SvrTap = optimvar ('SvrTap',Opt.svrTime,nSvr,...
    'Type','integer','LowerBound',-(Svr.nTap-Svr.defTap).*ones(Opt.svrTime,nSvr),'UpperBound',(Svr.nTap-Svr.defTap).*ones(Opt.svrTime,nSvr));
LrtTap = optimvar ('LrtTap',Opt.svrTime,1,...
    'Type','integer','LowerBound',ones(Opt.svrTime,1),'UpperBound',Lrt.nTap.*ones(Opt.svrTime,1));

% 電力
charPCh = optimvar ('charPCh',Opt.nTime,nCharger,'Type','continuous'...
    ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
charPCh.UpperBound(1,:)=  0; %時刻帯域t=1において充電しないこととする（初期値定義のため）
charPDch = optimvar ('charPDch',Opt.nTime,nCharger,'Type','continuous'...
    ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
charPDch.UpperBound(1,:)=  0;
% 無効電力出力
charQInj = optimvar ('charQInj',Opt.nTime,nCharger,'Type','continuous'...
    ,'LowerBound',-Charger.Smax.*ones(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
charQInj.UpperBound(1,:)= 0;

%ばいなり（１：放電、０：充電）
charPDchU = optimvar ('charPDchU',Opt.nTime,nCharger,'Type','integer'...
    ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',ones(Opt.nTime,nCharger));

% 各ノードの情報(P,Q,V)
P = optimvar('P', Opt.nTime, nNode,'Type','continuous',...
    'LowerBound', -inf(Opt.nTime, nNode), 'UpperBound', inf(Opt.nTime, nNode)); % 実電力
Q = optimvar('Q', Opt.nTime, nNode,'Type','continuous',...
    'LowerBound', -inf(Opt.nTime, nNode), 'UpperBound', inf(Opt.nTime, nNode)); % 無効電力
V = optimvar('V', Opt.nTime, nNode,'Type','continuous',...
    'LowerBound', 1*ones(Opt.nTime, nNode), 'UpperBound', 1*ones(Opt.nTime, nNode));   % 電圧





%目的関数
alpha=0.625;
beta=0.375;

prob.Objective = alpha*sum(LrtTapC(:))+beta*sum(SvrTapC(:));

% 制約: LrtTapC >= abs(LrtTap(t) - LrtTap(t-1))
for t = 2:Opt.svrTime
    prob.Constraints.(['LRTNTapPlus_', num2str(t)]) = ...
        LrtTapC(t-1) >= LrtTap(t) - LrtTap(t-1);
    prob.Constraints.(['LRTNTapMinus_', num2str(t)]) = ...
        LrtTapC(t-1) >= -(LrtTap(t) - LrtTap(t-1));
    for i = 1:nSvr
        prob.Constraints.(['SVRNTapPlus_', num2str(t),'_',num2str(i)]) = ...
            SvrTapC(t-1,i) >= SvrTap(t,i) - SvrTap(t-1,i);
        prob.Constraints.(['SVRNTapMinus_', num2str(t),'_',num2str(i)]) = ...
            SvrTapC(t-1,i) >= -(SvrTap(t,i) - SvrTap(t-1,i));
    end
end

% 周期的境界条件 (1つ目の制約を最後とつなぐ場合) 
prob.Constraints.LRTNTapPlus_1 = LrtTapC(end) >= LrtTap(1) - LrtTap(end);
prob.Constraints.LRTNTapMinus_1 = LrtTapC(end) >= -(LrtTap(1) - LrtTap(end));
for i = 1:nSvr
    prob.Constraints.(['SVRNTapPlus_1',num2str(i)]) = ...
        SvrTapC(end,i) >= SvrTap(1,i) - SvrTap(end,i);
    prob.Constraints.(['SVRNTapMinus_1',num2str(i)]) = ...
        SvrTapC(end,i) >= -(SvrTap(1,i) - SvrTap(end,i));
end

%制約条件
%・ノード制約条件
itemp = 1; % Chargerの列インデックス管理(列数がnode:98,charger:10と合わないため)
Pdemini = zeros(1, nNode);
Qdemini = zeros(1, nNode);

% Chargerインデックスを効率的に管理
isChargerNode = ismember(1:nNode, Charger.ind);

for i = 1:nNode
    disp(i)
    % ノードデータから Pdem, Qdem を取得
    Pdem = Nodes.dataTT{i, 1}.phasePr; % Pdemを取得
    Qdem = Nodes.dataTT{i, 1}.phaseQr; % Qdemを取得
    Pdemini(1, i) = Pdem(1);
    Qdemini(1, i) = Qdem(1);

    % Chargerがあるノードの場合
    if isChargerNode(i)
        for t = 1:Opt.nTime
            % Chargerノードの制約
            prob.Constraints.(['PowerP_', num2str(i), '_', num2str(t)]) = ...
                P(t, i) == charPDch(t, itemp) - charPCh(t, itemp) - Pdem(t);
            prob.Constraints.(['PowerQ_', num2str(i), '_', num2str(t)]) = ...
                Q(t, i) == charQInj(t, itemp) - Qdem(t);
        end
        itemp = itemp + 1;
    else
        % Chargerがないノードの場合
        for t = 1:Opt.nTime
            prob.Constraints.(['PowerP_', num2str(i), '_', num2str(t)]) = ...
                P(t, i) == -Pdem(t);
            prob.Constraints.(['PowerQ_', num2str(i), '_', num2str(t)]) = ...
                Q(t, i) == -Qdem(t);
        end
    end
end



%・潮流方程式
%一次のテイラー展開で線形近似する（精度は怪しいが...）

%
%Y行列拡張(n*1→n*n)
[NodeAdm_YRe, NodeAdm_YIm] = nodeadm(Edges.YRe, Edges.YIm, Systemdata, nNode, nBr);
NodeAdm=struct('YRe',NodeAdm_YRe,'YIm',NodeAdm_YIm);
clearvars NodeAdm_YRe NodeAdm_YIm

% 初期値設定
P0 = zeros(1, nNode);    % 初期値（P）[kW] (1×nNode)
Q0 = zeros(1, nNode);    % 初期値（Q）[kvar] (1×nNode)
V0 = 6.6 * ones(1, nNode);     % 初期値（電圧）[kV] (1×nNode)
tap_LRT0 = Lrt.defTap * ones(1, nNode); % 初期値（LRTタップ）[tap11] (1×nNode)
tap_SVR0 = 0 * ones(1, nNode); % 初期値（SVRタップ）[tap1] (1×nNode)

% 時間軸に合わせて拡張
LrtTap_expanded = repmat(LrtTap', 1, diffInterval);  % (nTime, 1)
SvrTap_expanded = repmat(SvrTap', 1, diffInterval);  % (nTime, nSvr)

P0_expanded = repmat(P0, Opt.nTime, 1); % (nTime, nNode)
Q0_expanded = repmat(Q0, Opt.nTime, 1); % (nTime, nNode)
V0_expanded = repmat(V0, Opt.nTime, 1); % (nTime, nNode)
tap_LRT0_expanded = repmat(tap_LRT0, Opt.nTime, 1);  % (nTime, nNode)
tap_SVR0_expanded = repmat(tap_SVR0, Opt.nTime, 1);  % (nTime, nNode)

% アドミタンス行列の準備
YRe = NodeAdm.YRe; % 実部 (nNode, nNode)
YIm = NodeAdm.YIm; % 虚部 (nNode, nNode)
Y = YRe + 1i * YIm; % 複素アドミタンス行列 (nNode, nNode)

% 潮流方程式の線形化（アドミタンスを反映）
h_P = @(P, Q, V, LrtTap_expanded, SvrTap_expanded) P + Q + V + LrtTap_expanded + SvrTap_expanded; % 仮の潮流関数
grad_P = @(P, Q, V, LrtTap_expanded, SvrTap_expanded) 1;  % 仮のPに対する勾配
grad_Q = @(P, Q, V, LrtTap_expanded, SvrTap_expanded) 1;  % 仮のQに対する勾配
grad_V = @(P, Q, V, LrtTap_expanded, SvrTap_expanded) 1;  % 仮のVに対する勾配
grad_tap_LRT = @(P, Q, V, LrtTap_expanded, SvrTap_expanded) Lrt.dVTap / 1000;  % 仮のLRTタップに対する勾配
grad_tap_SVR = @(P, Q, V, LrtTap_expanded, SvrTap_expanded) Svr.dVTap / 1000;  % 仮のSVRタップに対する勾配

% 初期値での関数値と勾配
h_0 = h_P(P0, Q0, V0, tap_LRT0_expanded, tap_SVR0_expanded); % 初期値での計算
grad_h_0_P = grad_P(P0, Q0, V0, tap_LRT0_expanded, tap_SVR0_expanded);
grad_h_0_Q = grad_Q(P0, Q0, V0, tap_LRT0_expanded, tap_SVR0_expanded);
grad_h_0_V = grad_V(P0, Q0, V0, tap_LRT0_expanded, tap_SVR0_expanded);
grad_h_0_tap_LRT = grad_tap_LRT(P0, Q0, V0, tap_LRT0_expanded, tap_SVR0_expanded);
grad_h_0_tap_SVR = grad_tap_SVR(P0, Q0, V0, tap_LRT0_expanded, tap_SVR0_expanded);

% 潮流方程式の線形化（インピーダンス考慮）
h_linear = @(P, Q, V, LrtTap, SvrTap) ...
    h_0 + grad_h_0_P .* (P - P0_expanded) + ...
    grad_h_0_Q .* (Q - Q0_expanded) + ...
    grad_h_0_V .* (V - V0_expanded) + ...
    grad_h_0_tap_LRT .* (LrtTap - tap_LRT0_expanded) + ...
    grad_h_0_tap_SVR .* (SvrTap - tap_SVR0_expanded);

% インピーダンスによる影響を潮流方程式に組み込む（線形化）
for t = 1:Opt.nTime
    disp(t)
    for j = 1:nNode
        % ノード間の電力フロー計算（インピーダンス考慮）
        P_ij = 0;
        Q_ij = 0;
        
        for k = 1:nNode
            % 電圧差とアドミタンスの積を用いた線形近似（電圧の差の線形近似）
            deltaV = V(t,j) - V(t,k); % 電圧差
            % 電力の計算（線形化）
            P_ij = P_ij + (real(Y(j, k)) * deltaV);  % (j, k) の位置を修正
            Q_ij = Q_ij + (imag(Y(j, k)) * deltaV);  % (j, k) の位置を修正
        end
        
        % 潮流方程式を追加（次元に注意）
        prob.Constraints.(['flow_constraint_P_' num2str(t) '_' num2str(j)]) = ...
            P(t, j) == P0_expanded(t, j) - P_ij;
        prob.Constraints.(['flow_constraint_Q_' num2str(t) '_' num2str(j)]) = ...
            Q(t, j) == Q0_expanded(t, j) - Q_ij;
        prob.Constraints.(['flow_constraint_' num2str(t) '_' num2str(j)]) = ...
            h_linear(P(t, j), Q(t, j), V(t, j), LrtTap_expanded(t, j), SvrTap_expanded(t, j)) == 0;
    end
end
%}

% 式(12),(13)
prob.Constraints.PChmin=optimconstr(Opt.nTime,nCharger);
prob.Constraints.PChmax=optimconstr(Opt.nTime,nCharger);
prob.Constraints.PDChmin=optimconstr(Opt.nTime,nCharger);
prob.Constraints.PDChmax=optimconstr(Opt.nTime,nCharger);
for t=1:Opt.nTime
    for i=1:nCharger
        prob.Constraints.PChmin(t,i) = charPCh(t,i) >= 0;
        prob.Constraints.PChmax(t,i) = charPCh(t,i) <= charPDchU(t,i) * Charger.Smax;
        prob.Constraints.PChmin(t,i) = charPDch(t,i) >= 0;
        prob.Constraints.PChmax(t,i) = charPCh(t,i) <= (1-charPDchU(t,i)) * Charger.Smax;
    end
end

% 式(14) 線形近似
prob.Constraints.PQbalance1=optimconstr(Opt.nTime,nCharger);
prob.Constraints.PQbalance2=optimconstr(Opt.nTime,nCharger);
prob.Constraints.PQbalance3=optimconstr(Opt.nTime,nCharger);
prob.Constraints.PQbalance4=optimconstr(Opt.nTime,nCharger);
for t=1:Opt.nTime
    for i=1:nCharger
        prob.Constraints.PQbalance1(t,i) = charQInj(t,i) - Smax + (charPCh(t,i)+charPDch(t,i)) <= 0;
        prob.Constraints.PQbalance1(t,i) = charQInj(t,i) + Smax - (charPCh(t,i)+charPDch(t,i)) <= 0;
        prob.Constraints.PQbalance1(t,i) = charQInj(t,i) - Smax - (charPCh(t,i)+charPDch(t,i)) <= 0;
        prob.Constraints.PQbalance1(t,i) = charQInj(t,i) + Smax + (charPCh(t,i)+charPDch(t,i)) <= 0;
    end
end



%関数
function [YReMatrix, YImMatrix] = nodeadm(YRe, YIm, Systemdata, nNode, nBr)
    % アドミタンス行列の初期化
    YReMatrix = zeros(nNode, nNode);
    YImMatrix = zeros(nNode, nNode);

    % 枝（Edges）のノード情報
    brNodes = Systemdata.Grid.Edges.EndNodes; % nBr x 2 の行列

    % オフダイアゴナル要素の設定（無向グラフ）
    for iBr = 1:nBr
        n1 = brNodes(iBr, 1); % 始点ノード
        n2 = brNodes(iBr, 2); % 終点ノード

        % 実部のアドミタンス
        YReMatrix(n1, n2) = YRe(iBr);
        YReMatrix(n2, n1) = YRe(iBr);

        % 虚部のアドミタンス
        YImMatrix(n1, n2) = YIm(iBr);
        YImMatrix(n2, n1) = YIm(iBr);
    end

    % ダイアゴナル要素の設定（自己アドミタンス）
    for iNode = 1:nNode
        YReMatrix(iNode, iNode) = -sum(YReMatrix(iNode, :), 2);
        YImMatrix(iNode, iNode) = -sum(YImMatrix(iNode, :), 2);
    end
end


