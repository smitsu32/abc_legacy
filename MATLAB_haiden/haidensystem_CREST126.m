%% メインプログラム
%%

%% 事前設定
clearvars -except CREST126 Systemdata
addpath(genpath(fileparts(mfilename('fullpath'))));
if ~exist('CREST126','var')
    load('CREST126.mat');
end

%以下は適宜変更
YEAR=2022;
MONTH=1;
DAY_S=11;
DAY_E=DAY_S+1;
anglestart=31.5493536172605;%17.9476433915772;
load('Systemdata_CREST106.mat','Systemdata');

MyProgram.Function.moveActiveEditorPath(); %現在のフォルダを実行したファイルがあるパスに移動
MyProgram.Function.toolboxCheck('requirements.txt'); %必要ツールボックスの確認%今回だとoptimzationtoolboxが入っているか確認
Main.DayLoop = MyProgram.Function.simTimeSet(datetime(YEAR,MONTH,DAY_S),datetime(YEAR,MONTH,DAY_E),days(1),"intervaltime",'closed'); %日付ループ設定（days()を変更、closed,openにすると終わりの日は計算されない）
Main.FolderName =MyProgram.Function.resultFolderCreate(strcat(pwd,"/result"),["input","output"],'type',true,'rootStructName',{'resRoot'}); %計算する日にちフォルダを作成
DataInfo = MyProgram.Function.InfoCreate;%いつのこのパスを作ったか記録（フォルダ名に時間が入る）
save(fullfile(Main.FolderName.resRoot,'Main.mat'),'Main','DataInfo');%resultフォルダに保存


%% 各種機器設定
% 充電器（容量，効率，接続相）
nCharger=sum(Systemdata.Grid.Nodes.Charger); %充電器数
phase='rkb';
Charger=struct('Smax',zeros(1,nCharger),'effe',zeros(1,nCharger),'node',zeros(1,nCharger),'phase',repmat('r',1,nCharger));
for iChar=1:nCharger
    Charger.Smax(iChar)=10000;%kVA
    Charger.effe(iChar)=0.95;%効率
    Charger.node(iChar)=Systemdata.Grid.Nodes.Charger(iChar); %接続ノード
    Charger.phase(iChar)=phase(1);%相
end

% 蓄電池（kWh容量,1ノードあたりの台数）
nEss=nCharger;% (nNode-sum(TF))*SpecStruct.Ess.nEssPerNode;
Ess=struct('kWhCap',zeros(1,nEss));
for iEss=1:nEss
    Ess.kWhCap(iEss)=10000;%SpecStruct.Ess;　%値は後で書き直す
end


%%　各種データ読み込み
nNode =height(Systemdata.Grid.Nodes);%ノードの数
nBr =height(Systemdata.Grid.Edges);%ブランチの数
nLrt=nNode-sum(cellfun(@isempty,Systemdata.Grid.Nodes.LRT));
nSvr=nBr-sum(cellfun(@isempty,Systemdata.Grid.Edges.SVR));
TF=cellfun(@isempty,Systemdata.Grid.Edges.SVR); 
svr =Systemdata.Grid.Edges.SVR(not(TF));
ind=find(not(TF)>0);

% SVR
Svr=[];
fieldNames=fieldnames(svr{1});
for ifield=1:length(fieldNames)
    for iSVR=1:length(svr)
        Svr.(string(fieldNames(ifield)))(iSVR)=svr{iSVR}.(string(fieldNames(ifield)));
        Svr.br(iSVR)=ind(iSVR);
    end
end
%SVRの位置を変えるならここで（※神田だけ適用可能）
Svr.effNode=zeros(nNode,nSvr);
Svr.effNode(23:95,1) =true;
% Svr.effNode(8:14,2) =true;

% LRT
TF=cellfun(@isempty,Systemdata.Grid.Nodes.LRT);
ind=find(not(TF)>0);
lrt =Systemdata.Grid.Nodes.LRT(not(TF));
Lrt=[];
fieldNames=fieldnames(lrt{1});
for ifield=1:length(fieldNames)
    for iLRT=1:length(lrt)
        Lrt.(string(fieldNames(ifield)))(iLRT)=lrt{iLRT}.(string(fieldNames(ifield)));
        Lrt.node(iLRT)=ind(iLRT);
    end
end


%% 最適化設定
% 時間間隔を変えるときは87行のminutes()を変更
TimeInfo = MyProgram.Function.simTimeSet(Main.DayLoop.startTime,min(Main.DayLoop.endTime ...
    ,Main.DayLoop.startTime+days(1)),minutes(2),"intervaltime","openright");

%最適化に必要な諸々のデータを格納
Opt=struct('TimeInfo',TimeInfo,'nType',1,'hourDT',minutes(TimeInfo.dt)/60 ...
    ,'nTime',TimeInfo.nTime,'phase','r');
 Opt.nPhase =length(Opt.phase);

%　各変数はサイズを決めて初期化した方が実行が早くなるため結果格納用の構造体をMappingで定義
Mapping=struct(); 
%実部電流
    Mapping.netdemIr=struct('nRow',Opt.nTime,'nCol',nNode,'nPage',Opt.nPhase);
     %虚部電流
    Mapping.netdemIi=struct('nRow',Opt.nTime,'nCol',nNode,'nPage',Opt.nPhase);
    % 各SVRのタップ切り替え数
    Mapping.sSvrTap=struct('nRow',2,'nCol',nSvr,'nPage',1); %nRowに2つの値を割当(2個の式があって、低数値を2種類あてはめたい)
    % 各LRTのタップ切り替え数
    Mapping.sLrtTap=struct('nRow',2,'nCol',nLrt,'nPage',1); %nRowに2つの値を割当 
    %充電量
    Mapping.sEssE=struct('nRow',1,'nCol',nEss,'nPage',1); 
    %充電量
    Mapping.eEssE=struct('nRow',1,'nCol',nEss,'nPage',1); 
     %外気温
    Mapping.Temp=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
     %配電線温度初期値
    Mapping.Anglestart=struct('nRow',1,'nCol',1,'nPage',1);
    %下限制約で使う三つとIl,Ihの独立バイナリ
    Mapping.DummyIl=struct('nRow',Opt.nTime,'nCol',1,'nPage',1); 
    Mapping.DummyIh=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
    Mapping.rhs=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
    Mapping.binary=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
    %目的関数用
    Mapping.minESS = struct('nRow',1,'nCol',1,'nPage',1); 
    Mapping.minTapNum=struct('nRow',1,'nCol',1,'nPage',1);
    Mapping.minBrI = struct('nRow',1,'nCol',1,'nPage',1);

    % Mappingの各値を1000*rand+randで始まる連続値で初期化した構造体を作成
    MappingValue=MyProgram.OptFunction.mappingVarSet(Mapping,1000*rand+rand);


%%  最適化問題変数の作成
% 配電線温度に関する変数

% 配電線温度 [℃] :連続値
   UpperTemp=repmat(MappingValue.Temp,1,1,Opt.nPhase);
   angleline = optimvar ('angleline',Opt.nTime,1,Opt.nPhase,'Type','continuous' ...
       ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',UpperTemp);

% 配電線最終温度(anglemax):連続値 
   anglemax = optimvar ('anglemax',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));

% 240A超過バイナリ(B_linecap):バイナリ（通過電流値br_IAbsが240A以上：1 、240A未満：0）, integer 0<= <=1
      B_linecap = optimvar ('B_linecap',Opt.nTime,1,Opt.nPhase,'Type','integer'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',ones(Opt.nTime,1,Opt.nPhase)); % 240Aは過電流リレー整定値

% ダミー変数（240Aバイナリ*Br_Imax）(Dummy_Ihigh) （通過電流値br_IAbsが240A以上：Br_Imax 、240A未満：0）
   Dummy_Ih = optimvar ('Dummy_Ih',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));

% ダミー変数（brI_Abs－240Aバイナリ*Br_Imax）(Dummy_Ilow) (通過電流値br_IAbsが240A以上：Br_Imax-BrI_abs、240A未満：BrI_abs)
   Dummy_Il = optimvar ('Dummy_Il',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));

% ダミー変数（240Aバイナリ*θline(t-1)）(Dummy_anglehigh) （通過電流値br_IAbsが240A以上：1コマ前の配電線温度angleline(t-1) 、240A未満：0）
   Dummy_angleh = optimvar ('Dummy_angleh',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));

% ダミー変数（240Aバイナリ*θline(t-1)）(Dummy_anglelow)（通過電流値br_IAbsが240A以上：angleline(t-1) 、240A未満：0）
   Dummy_anglel = optimvar ('Dummy_anglel',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));


% ブランチ電流(BrI):連続値
% 実部, 虚部(-inf<= <=inf)
    brI_Re = optimvar ('brI_Re',Opt.nTime,nBr,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',-inf(Opt.nTime,nBr,Opt.nPhase),'UpperBound',inf(Opt.nTime,nBr,Opt.nPhase));
    brI_Im = optimvar ('brI_Im',Opt.nTime,nBr,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',-inf(Opt.nTime,nBr,Opt.nPhase),'UpperBound',inf(Opt.nTime,nBr,Opt.nPhase));

% 絶対値(実部, 虚部, 絶対値)
    brI_ReAbs = optimvar ('brI_ReAbs',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));
    brI_ImAbs = optimvar ('brI_ImAbs',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));
    brI_Abs = optimvar ('brI_Abs',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',400*ones(Opt.nTime,1,Opt.nPhase));


% 蓄電池(Ess)の充放電(EssP):連続値
   %充電[kW] Pch(-∞<= <=∞)
    charPCh = optimvar ('charPCh',Opt.nTime,nCharger,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
    charPCh.UpperBound(1,:)=  0; %時刻０は０
    %放電[kW] Pdch
    charPDch = optimvar ('charPDch',Opt.nTime,nCharger,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
    charPDch.UpperBound(1,:)=  0;
    %充放電バイナリ(充電:1 放電:0)
    charPDchU = optimvar ('charPDchU',Opt.nTime,nCharger,'Type','integer'...
        ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',ones(Opt.nTime,nCharger));
    %虚部充電量 Q[kvar] (-Smax<=Q<=Smax) Smax:インバータ容量[kVA]
    charQInj = optimvar ('charQInj',Opt.nTime,nCharger,'Type','continuous'...
        ,'LowerBound',-Charger.Smax.*ones(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
    % 上記の絶対値 Qabs[kvar] (0<=Qabs<=Smax)
   charQAbs = optimvar ('charQAbs',Opt.nTime,nCharger,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
    %充電器の充電可能量(S) 各充電器のEsseの最大値
    charCap= optimvar ('charCap',1,nCharger,'Type','continuous'...
        ,'LowerBound',zeros(1,nCharger),'UpperBound',Charger.Smax.*ones(1,nCharger));
    %現在の充電量(S) 各時刻のsqrt{(Pch+Pdch)^2+Q^2}
    EssE = optimvar ('EssE',Opt.nTime,nEss,'Type','continuous'...
        ,'LowerBound',-inf(Opt.nTime,nEss),'UpperBound',inf(Opt.nTime,nEss));


    EssE.LowerBound(end,:)=  MappingValue.eEssE;
    %蓄電池の充電可能量(E=kWh) 　　充電器の最大容量
    EssEmax= optimvar ('EssEmax',1,nEss,'Type','continuous'...
        ,'LowerBound',-inf(1,nEss),'UpperBound',inf(1,nEss));
    %蓄電池の充電量が不変の量
    EssEmin= optimvar ('EssEmin',1,nEss,'Type','continuous'...
        ,'LowerBound',-inf(1,nEss),'UpperBound',inf(1,nEss));

    %差分(充電量の変動差分)
    ESS_differenceabs = optimvar ('ESS_differenceabs',Opt.nTime,nEss,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nEss),'UpperBound',inf(Opt.nTime,nEss));


% ノード電圧(NodeV):連続値　max()
%nodeVr [V] 実部  　　　上下限に 線間電圧=相電圧/sqrt(3) を利用
    nodeV_Re = optimvar('nodeV_Re',Opt.nTime,nNode,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',Systemdata.Vol.lb/sqrt(3)*ones(Opt.nTime,nNode,Opt.nPhase),'UpperBound',Systemdata.Vol.ub/sqrt(3)*ones(Opt.nTime,nNode,Opt.nPhase));
%nodeVi[V]　　%虚部は線形では表せないため、実部で下限を満たすようにしている。
    nodeV_Im = optimvar('nodeV_Im',Opt.nTime,nNode,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',-inf(Opt.nTime,nNode,Opt.nPhase),'UpperBound',inf(Opt.nTime,nNode,Opt.nPhase));
%nodeV[V]   ノード電圧
    nodeV = optimvar('nodeV',Opt.nTime,nNode,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',Systemdata.Vol.lb/sqrt(3)*ones(Opt.nTime,nNode,Opt.nPhase),'UpperBound',Systemdata.Vol.ub/sqrt(3)*ones(Opt.nTime,nNode,Opt.nPhase));
%nodeVi_abs[v] 虚部絶対値
    nodeV_ImAbs = optimvar('nodeV_ImAbs',Opt.nTime,nNode,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nNode,Opt.nPhase),'UpperBound',inf(Opt.nTime,nNode,Opt.nPhase));
%nodedV[V] 1コマ前からの電圧変動値（絶対値）
    nodeDV = optimvar ('nodeDV',Opt.nTime,nNode,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nNode),'UpperBound',inf(Opt.nTime,nNode));
%nodedVmax[V] 各コマの6600Vからの電圧変動値（絶対値） 　　　目的関数用
    nodeAmbV = optimvar ('nodeAmbV',Opt.nTime,nNode,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nNode),'UpperBound',inf(Opt.nTime,nNode));
%Vmax[V]  各ノード許容電圧上限値
    nodeAmbV_Max = optimvar ('nodeAmbV_Max',Opt.nTime,nNode,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nNode),'UpperBound',inf(Opt.nTime,nNode));
%Vmin[v] 　各ノード許容電圧下限値
    nodeAmbV_Min = optimvar ('nodeAmbV_Min',Opt.nTime,nNode,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nNode),'UpperBound',inf(Opt.nTime,nNode));


%% 配電線温度に関する制約
% 定数
linecap=90;
%↑配電線温度の最小化を目的関数として得られたθの最大値から余裕をもつ値を設定
Ke=0.575844;
%電流が240A以下の場合の定数
A_alpha=0.000218954522582363;
B_alpha=-0.000175933602332071;
C_alpha=0.15404166631565;
A_beta=-0.0287418682697553;
B_beta=-0.00284260213397638;
C_beta=4.61844925964933;    
%電流が240A以上の場合の定数
D_alpha=0.000337623485826741;
E_alpha=-0.000703422308297201;
F_alpha=0.480230106409709;
D_beta=-0.0572224575989015;
E_beta=0.123754962864256;
F_beta=-73.6667867711607; 


% 配電線温度の等式制約
% 