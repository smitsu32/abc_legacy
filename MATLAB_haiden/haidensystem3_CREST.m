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

Charger=struct('Smax',10000,'Emax',10000,'ind',[],'effe',0.95); %kVA,kWh
Svr=struct('nTap',9,'defTap',5,'dVTap',75); %V
Lrt=struct('nTap',21,'defTap',11,'dVTap',30);
% nLrt=1;
Charger.ind=[]; Svr.ind=[]; 
for i=1:nNode
    Charger.ind=[Charger.ind, i*ones(Nodes.Charger(i))];
end
sort(Charger.ind);

Lrt.effNode=zeros(nNode,1);
Lrt.effNode(:,1)=true;

% 毎回変更すること(元データに足す予定です)
Svr.effNode=zeros(nNode,nSvr);
Svr.effNode(23:95,1) =true;
% Svr.effNode(8:14,2) =true;
% Svr.effNode(8:14,3) =true;
% Svr.effNode(8:14,4) =true;

%% Svr.effNode('SVRより末端側全てのノード' , '何番目のSVRか') =true;
%% 
% 最適化

prob=optimproblem;
%% 
% 変数

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
charPCh.UpperBound(1,:)=  0; %時刻帯域t=1は充電しないこととする（初期時間）
charPDch = optimvar ('charPDch',Opt.nTime,nCharger,'Type','continuous'...
    ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
charPDch.UpperBound(1,:)=  0;

%ばいなり（１：充電、０：放電）
charPDchU = optimvar ('charPDchU',Opt.nTime,nCharger,'Type','integer'...
    ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',ones(Opt.nTime,nCharger));

% 無効電力出力
charQInj = optimvar ('charQInj',Opt.nTime,nCharger,'Type','continuous'...
    ,'LowerBound',-Charger.Smax.*ones(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
charQInj.UpperBound(1,:)= 0;
%充電量 式(10)
EBat = optimvar('EBat',Opt.nTime,nCharger,'Type','continuous',...
    'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',Charger.Emax*ones(Opt.nTime,nCharger));


% 各ノードの情報(P,Q,V)
P = optimvar('P', Opt.nTime, nNode,'Type','continuous',...
    'LowerBound', -inf(Opt.nTime, nNode), 'UpperBound', inf(Opt.nTime, nNode)); % 実電力
Q = optimvar('Q', Opt.nTime, nNode,'Type','continuous',...
    'LowerBound', -inf(Opt.nTime, nNode), 'UpperBound', inf(Opt.nTime, nNode)); % 無効電力
% 式(8)
V = optimvar('V', Opt.nTime, nNode,'Type','continuous',...
    'LowerBound', Systemdata.Vol.lb*ones(Opt.nTime, nNode), 'UpperBound', Systemdata.Vol.ub*ones(Opt.nTime, nNode));   % 電圧
%% 
% 

% 以下dummy

%% 
% 目的関数

alpha=0.625;
beta=0.375;

prob.Objective = alpha*sum(LrtTapC(:))+beta*sum(SvrTapC(:));
%% 
% 

% 制約: LrtTapC >= abs(LrtTap(t) - LrtTap(t-1)) 
prob.Constraints.LRTNTapPlus = optimconstr(Opt.svrTime,1);
prob.Constraints.LRTNTapMinus = optimconstr(Opt.svrTime,1);
prob.Constraints.SVRNTapPlus = optimconstr(Opt.svrTime,nSvr);
prob.Constraints.SVRNTapMinus = optimconstr(Opt.svrTime,nSvr);

for t = 2:Opt.svrTime
    prob.Constraints.LRTNTapPlus(t,1) = ...
        LrtTapC(t-1) >= LrtTap(t) - LrtTap(t-1);
    prob.Constraints.LRTNTapMinus(t,1) = ...
        LrtTapC(t-1) >= -(LrtTap(t) - LrtTap(t-1));
    prob.Constraints.SVRNTapPlus(t,:) = ...
        SvrTapC(t-1,:) >= SvrTap(t,:) - SvrTap(t-1,:);
    prob.Constraints.SVRNTapMinus(t,:) = ...
        SvrTapC(t-1,:) >= -(SvrTap(t,:) - SvrTap(t-1,:));
end

% 周期的境界条件 (1つ目の制約を最後とつなぐ場合) 
prob.Constraints.LRTNTapPlus(1,1) = ...
    LrtTapC(end) >= LrtTap(1) - LrtTap(end);
prob.Constraints.LRTNTapMinus(1,1) = ...
    LrtTapC(end) >= -(LrtTap(1) - LrtTap(end));

% prob.Constraints.SVRNTapPlus_1 = optimconstr(Opt.svrTime,nSvr);
% prob.Constraints.SVRNTapMinus_1 = optimconstr(Opt.svrTime,nSvr);

prob.Constraints.SVRNTapPlus(1,:) = ...
    SvrTapC(end,:) >= SvrTap(1,:) - SvrTap(end,:);
prob.Constraints.SVRNTapMinus(1,:) = ...
    SvrTapC(end,:) >= -(SvrTap(1,:) - SvrTap(end,:));

%% 
% 
% 
% 制約条件
% 
% ・ノード制約条件 式(6)(7)

% Chargerの列インデックス管理
Pdemini = zeros(1, nNode);
Qdemini = zeros(1, nNode);

% 制約を格納するための2次元配列を作成
prob.Constraints.PowerP = optimconstr(Opt.nTime, nNode);
prob.Constraints.PowerQ = optimconstr(Opt.nTime, nNode);

% 各ノードの Pdem, Qdem を取得し、制約を追加
itemp=1;
for i = 1:nNode
    % ノードデータから Pdem, Qdem を取得
    Pdem = Nodes.dataTT{i, 1}.phasePr; % Pdemを取得
    Qdem = Nodes.dataTT{i, 1}.phaseQr; % Qdemを取得
    Pdemini(1, i) = Pdem(1);
    Qdemini(1, i) = Qdem(1);

    % Chargerがあるノードの場合
    if ismember(i, Charger.ind)
        prob.Constraints.PowerP(:, i) = P(:, i) == charPDch(:, itemp) - charPCh(:, itemp) - Pdem;
        prob.Constraints.PowerQ(:, i) = Q(:, i) == charQInj(:, itemp) - Qdem;
        item=itemp+1;
    else
        % Chargerがないノードの場合
        prob.Constraints.PowerP(:, i) = P(:, i) == -Pdem;
        prob.Constraints.PowerQ(:, i) = Q(:, i) == -Qdem;
    end
end

%% 
% 
%% 
% 
% 
% ・潮流方程式
% 
% 一次のテイラー展開で線形近似する（精度は怪しいが...）
% 
% $$h\left(P,Q,V,{\textrm{tap}}_{\textrm{LRT}} ,{\textrm{tap}}_{\textrm{SVR}} 
% \right)\approx h\left(P_0 ,Q_0 ,V_0 ,{\textrm{tap}}_{\textrm{LRT0}} ,{\textrm{tap}}_{\textrm{SVR0}} 
% \right)+\frac{\delta \;h}{\delta \;P}|_{\left(P_{0\;} ,Q_{0\;} ,V_{0\;} ,{\textrm{tap}}_{\textrm{LRT0}} 
% ,{\textrm{tap}}_{\textrm{SVR0}} \right)} \left(P-P_0 \right)+\frac{\delta \;h}{\delta 
% \;Q}|_{\left(P_{0\;} ,Q_{0\;} ,V_{0\;} ,{\textrm{tap}}_{\textrm{LRT0}} ,{\textrm{tap}}_{\textrm{SVR0}} 
% \right)} \left(Q-Q_0 \right)$$
% 
% $${\therefore \;\;h}_{\textrm{linear}} \left(P,Q,V,{\textrm{tap}}_{\textrm{LRT}} 
% ,{\textrm{tap}}_{\textrm{SVR}} \right)=h_0 +{\left(\frac{\delta \;h}{\delta 
% \;P}\right)}_0 \left(P-P_0 \right)+{\left(\frac{\delta \;h}{\delta \;Q}\right)}_0 
% \left(Q-Q_0 \right)$$

%
%Y行列拡張(n*1→n*n)
[NodeAdm_YRe, NodeAdm_YIm] = nodeadm(Edges.YRe, Edges.YIm, Systemdata, nNode, nBr);
NodeAdm=struct('YRe',NodeAdm_YRe,'YIm',NodeAdm_YIm);
clearvars NodeAdm_YRe NodeAdm_YIm
%% 
% 

%{
prob.Constraints.flow_constraint_P = optimconstr(Opt.nTime,nNode);
prob.Constraints.flow_constraint_Q = optimconstr(Opt.nTime,nNode);
prob.Constraints.flow_constraint = optimconstr(Opt.nTime,nNode);
% 初期値設定
P0 = zeros(1, nNode);    % 初期値（P）[kW] (1×nNode)
Q0 = zeros(1, nNode);    % 初期値（Q）[kvar] (1×nNode)
V0 = 6.6 * ones(1, nNode);     % 初期値（電圧）[kV] (1×nNode)
tap_LRT0 = Lrt.defTap * ones(1, nNode); % 初期値（LRTタップ）[tap11] (1×nNode)
tap_SVR0 = 0 * ones(1, nNode); % 初期値（SVRタップ）[tap1] (1×nNode)

% 時間軸に合わせて拡張
LrtTap_expanded = repmat(LrtTap', nNode, diffInterval)';  % (nTime, nNode)
SvrTap_expanded = repmat(SvrTap', nNode, diffInterval)';  % (nTime, nNode)

P0_expanded = repmat(P0, nTime, 1); % (nTime, nNode)
Q0_expanded = repmat(Q0, nTime, 1); % (nTime, nNode)
V0_expanded = repmat(V0, nTime, 1); % (nTime, nNode)
tap_LRT0_expanded = repmat(tap_LRT0, nTime, 1);  % (nTime, nNode)
tap_SVR0_expanded = repmat(tap_SVR0, nTime, 1);  % (nTime, nNode)

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

% 潮流方程式の線形化（アドミタンスを反映）
h_linear = @(P, Q, V, LrtTap_expanded, SvrTap_expanded) ...
    grad_P(P0, Q0, V0, tap_LRT0_expanded, tap_SVR0_expanded) * (P - P0) + ...
    grad_Q(P0, Q0, V0, tap_LRT0_expanded, tap_SVR0_expanded) * (Q - Q0) + ...
    grad_V(P0, Q0, V0, tap_LRT0_expanded, tap_SVR0_expanded) * (V - V0) + ...
    grad_tap_LRT(P0, Q0, V0, tap_LRT0_expanded, tap_SVR0_expanded) * (LrtTap_expanded - tap_LRT0_expanded) + ...
    grad_tap_SVR(P0, Q0, V0, tap_LRT0_expanded, tap_SVR0_expanded) * (SvrTap_expanded - tap_SVR0_expanded) + ...
    h_P(P0, Q0, V0, tap_LRT0_expanded, tap_SVR0_expanded);

% 潮流方程式の設定
deltaV = optimvar('deltaV', nTime, nNode, nNode); % 電圧差の最適化変数
P_ij = zeros(nTime, nNode); % P_ijの初期化
Q_ij = zeros(nTime, nNode); % Q_ijの初期化

% 電圧差の計算
prob.Constraints.deltaV_constraint = optimconstr(Opt.nTime,nNode,nNode);
% 電圧差の計算を制約条件として追加（ベクトル化）
[Vj, Vk] = ndgrid(1:nNode, 1:nNode); % インデックスのグリッドを作成
prob.Constraints.deltaV_constraint(:, :, :) = deltaV == V(:, Vj) - V(:, Vk);

% 線形近似による電力計算（次元の変更なし）
P_ij = sum(real(Y) .* deltaV, 3);
Q_ij = sum(imag(Y) .* deltaV, 3);

% 潮流方程式の制約を追加
prob.Constraints.flow_constraint_P = P == P0_expanded - P_ij;
prob.Constraints.flow_constraint_Q = Q == Q0_expanded - Q_ij;
prob.Constraints.flow_constraint = ...
    h_linear(P, Q, V, LrtTap_expanded, SvrTap_expanded) == 0;
%}
%% 
% 
%% 
% ・各ノードの蓄電池条件 式(9)(11)

prob.Constraints.Ebatbalance = optimconstr(Opt.nTime,nCharger);
eta=Charger.effe;

prob.Constraints.Ebatbalance(1,:) = EBat(1,:) == EBat(end,:);
for t = 2:nTime
    prob.Constraints.Ebatbalance(t,:) = EBat(t,:) == eta*charPCh(t,:) - charPDch(t,:)/eta + EBat(t-1,:);
end

%% 
% ・PCh,Pdchの同時禁止制約　式(12)(13)

prob.Constraints.PChrange = charPCh <= charPDch*Charger.Smax;
prob.Constraints.PDchrange = charPDch <= (1-charPDch)*Charger.Smax;
% PCh>=0 はoptimvarで済み

%% 
% ・PQの絶対値制約 式(14)　線形近似 (4*n個に)

% dummy
% Abs(線形制約とするために別変数として定義)
charPsum = optimvar ('charPsum',Opt.nTime,nCharger,'Type','continuous');
prob.Constraints.Pvar = charPsum == charPCh + charPDch;

% 分割数の設定
n = 4;

% 新しい絶対値変数の導入
charP_abs = optimvar('charP_abs', Opt.nTime, nCharger, n, 'LowerBound', 0);
charQInj_abs = optimvar('charQInj_abs', Opt.nTime, nCharger, n, 'LowerBound', 0);

% 絶対値の線形化制約
prob.Constraints.charPQ = optimconstr(Opt.nTime, nCharger, 4*n);
for i = 1:n
    prob.Constraints.charPQ(:,:,4*(i-1)+1) = charP_abs(:,:,i) >= charPsum;
    prob.Constraints.charPQ(:,:,4*(i-1)+2) = charP_abs(:,:,i) >= -charPsum;
    prob.Constraints.charPQ(:,:,4*(i-1)+3) = charQInj_abs(:,:,i) >= charQInj;
    prob.Constraints.charPQ(:,:,4*(i-1)+4) = charQInj_abs(:,:,i) >= -charQInj;
end

% 線形近似制約
prob.Constraints.SmaxIn = optimconstr(Opt.nTime, nCharger, n);
for i = 1:n
    prob.Constraints.SmaxIn(:,:,i) = charP_abs(:,:,i) + charQInj_abs(:,:,i) <= Charger.Smax / n;
end

%% 
% 
%% 
% 最適化計算

Strprob = prob2struct(prob);
[x, fval, exitflag, output]=intlinprog(Strprob);
%% 
% 
% 
% 関数

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
%% 
%