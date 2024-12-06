%% メインプログラム
%% 
%% 全体初期設定

load('Systemdata106.mat');
TT = Systemdata.Grid.Nodes.dataTT{1,1}.Time(1);
% YEAR=2018;
% MONTH=7;
% DAY_S=22;
% DAY_E=DAY_S+1;
YEAR=year(TT);
MONTH=month(TT);
DAY_S=day(TT);
DAY_E=DAY_S+1;
anglestart=31.5493536172605;%17.9476433915772;

MyProgram.Function.moveActiveEditorPath(); %現在のフォルダを実行したファイルがあるパスに移動
MyProgram.Function.toolboxCheck('requirements.txt'); %必要ツールボックスの確認%今回だとoptimzationtoolboxが入っているか確認
%↑パイソンも上記のような書き方↑
Main.Loop = MyProgram.Function.simLoopSet(); % 計算ループ設定（今は使っていない）
%計算対象日（2018年3月1日から10日）同じ日にすると一日計算
Main.DayLoop = MyProgram.Function.simTimeSet(datetime(YEAR,MONTH,DAY_S),datetime(YEAR,MONTH,DAY_E),days(1),"intervaltime",'closed'); %日付ループ設定（closed,openにすると終わりの日は計算されない）
%計算する日にちフォルダを作成
% Main.FolderName =MyProgram.Function.resultFolderCreate(strcat(pwd,"/result"),["input","output"],'type',true,'rootStructName',{'resRoot'});
% 
% Main.addPath=genpath('../OptimizationSolver');%最適化フォルダを作って
% addpath(Main.addPath);%パスを追加
% % DataInfo = MyProgram.Function.InfoCreate;%いつのこのパスを作ったか記録（フォルダ名に時間が入る）
% save(fullfile(Main.FolderName.resRoot,'Main.mat'),'Main','DataInfo');%resultフォルダに保存
%% 各種機器容量
% 充電器（容量，効率，接続相）

 %SpecStruct.Charger =struct('Smax',200,'effe',0.95,'phase','rkb');  %kVA
 % nCharger=2;
 nNode =height(Systemdata.Grid.Nodes);%ノードの数 add
 nCharger=sum(Systemdata.Grid.Nodes.Charger);%充電器の数 
 phase='r';%充電器一つ目が赤、二つ目が黒、三つ目が青
 %Charger=struct();%struct('Smax',200,'effe',0.95,'node',3);
 Charger=struct('Smax',zeros(1,nCharger),'effe',zeros(1,nCharger),'node',zeros(1,nCharger),'phase',repmat('r',1,nCharger));
 ind =arrayfun(@(i) i * ones(1, Systemdata.Grid.Nodes.Charger(i)), 1:nNode, 'UniformOutput', false);
 ind=[ind{:}];
 %充電器に関する値設定(同じ値を割り振り）
 for iChar=1:nCharger
     Charger.Smax(iChar)=10000;%kVA
     Charger.effe(iChar)=0.95;%効率
% if iChar==1
     Charger.node(iChar)=ind(iChar);%接続ノード
     Charger.phase(iChar)=phase(1);%相
%{
elseif iChar==3
     Charger.node(iChar)=8;%接続ノード
     Charger.phase(iChar)=phase(1);%相
elseif iChar==4
     Charger.node(iChar)=13;%接続ノード
     Charger.phase(iChar)=phase(1);%相
elseif iChar==5
     Charger.node(iChar)=13;%接続ノード
     Charger.phase(iChar)=phase(2);%相
elseif iChar==6
     Charger.node(iChar)=13;%接続ノード
     Charger.phase(iChar)=phase(3);%相
%}
end
 % end
%% 
% 蓄電池（kWh容量,1ブランチあたりの台数 ）

nEss=nCharger;% (nNode-sum(TF))*SpecStruct.Ess.nEssPerNode;
Ess=struct('kWhCap',zeros(1,nEss));
for iEss=1:nEss
    Ess.kWhCap(iEss)=10000;%SpecStruct.Ess;　%値は後で書き直す
    Ess.kWhCap(iEss)=10000;%SpecStruct.Ess;
end
%% 各種データ読み込み

%{
if exist('inputdata_after.mat',"file")==0%Kandaデータは重たいので最初だけ読む
% 系統データ

    load('KandaZafter.mat');
    Systemdata=Kanda;%神田ならKanda,員弁ならInabe
    clearvars Kanda
    %データ補間は既に行われている
% 充電器・蓄電池データ

   %特に変更必要なし
    DataInfo = MyProgram.Function.InfoCreate;

    save('inputdata_after.mat','Systemdata','DataInfo');
else
    load('inputdata_after.mat');
end
%copyfile('inputdata.mat',fullfile(Main.FolderName.input,'inputdata.mat'));
%}
%%
%神田のデータからSVRやLRT情報を作成
nNode =height(Systemdata.Grid.Nodes);%ノードの数
nBr =height(Systemdata.Grid.Edges);%ブランチの数
nLrt=nNode-sum(cellfun(@isempty,Systemdata.Grid.Nodes.LRT));
nSvr=nBr-sum(cellfun(@isempty,Systemdata.Grid.Edges.SVR));

TF=cellfun(@isempty,Systemdata.Grid.Edges.SVR);
svr =Systemdata.Grid.Edges.SVR(not(TF));
ind=find(not(TF)>0);

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
Svr.effNode(22:95,1) =true;
% Svr.effNode(8:14,2) =true;

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
% インピーダンスとアドミタンス行列の変更

%インピーダンス情報とアドミタンス行列を変更するならここで
%{
Systemdata.Grid.Edges.R=Systemdata.Grid.Edges.R*(125/60);
Systemdata.Grid.Edges.X=Systemdata.Grid.Edges.X*1.06302124152762;

Systemdata.Grid.Edges.Z=sqrt((Systemdata.Grid.Edges.R).^2+(Systemdata.Grid.Edges.X).^2);

[Systemdata.Grid.Edges.G,Systemdata.Grid.Edges.B]=node_adm_matrix(Systemdata.Grid.Edges.r,Systemdata.Grid.Edges.x,Systemdata.Grid.Edges.b,Systemdata.Grid.Edges.bc);
[Systemdata.Grid.Edges.YRe,Systemdata.Grid.Edges.YIm]=node_adm_matrix(Systemdata.Grid.Edges.R,Systemdata.Grid.Edges.X,Systemdata.Grid.Edges.b,Systemdata.Grid.Edges.bc);
%}
%アドミタンス行列読み取り不可能であったため、元のR,Xを書き換えた。
%% 最適化設定


TimeInfo = MyProgram.Function.simTimeSet(Main.DayLoop.startTime,min(Main.DayLoop.endTime,Main.DayLoop.startTime+days(1)),minutes(15),...
     "intervaltime","openright");

%最適化の情報を格納している特に使うのが、hourDT。これは最適の一コマあたりの時間hourDT=0.5で30分を指す。nTime=48。30*48=24時間
%phaseがその相を計算するかという変数（三相平衡でやるならrだけにする）
%つまりOptはマッピングに関係なく使用
Opt=struct('TimeInfo',TimeInfo,'nType',1,'hourDT',minutes(TimeInfo.dt)/60,'nTime',TimeInfo.nTime,'phase','r');
 Opt.nPhase =length(Opt.phase);

    Mapping=struct(); 
%% 
% nRowは、nColは対象数、nPageは定数値をあてはめる数

    %Mapping.minTapNum=struct('nRow',1,'nCol',1,'nPage',1);    
    %Mapping.minVolDif=struct('nRow',1,'nCol',1,'nPage',1);
    %Mapping.minLoss=struct('nRow',1,'nCol',1,'nPage',1);   

    Mapping.netdemIr=struct('nRow',Opt.nTime,'nCol',nNode,'nPage',Opt.nPhase);
    Mapping.netdemIi=struct('nRow',Opt.nTime,'nCol',nNode,'nPage',Opt.nPhase);
    %Mapping.netdemIrV=struct('nRow',Opt.nTime,'nCol',nNode,'nPage',Opt.nPhase);
    %Mapping.netdemIiV=struct('nRow',Opt.nTime,'nCol',nNode,'nPage',Opt.nPhase);    
    
    Mapping.sSvrTap=struct('nRow',2,'nCol',nSvr,'nPage',1); %nRowに2つの値を割当(2個の式があって、低数値を2種類あてはめたい)
    Mapping.sLrtTap=struct('nRow',2,'nCol',nLrt,'nPage',1); %nRowに2つの値を割当

    Mapping.sEssE=struct('nRow',1,'nCol',nEss,'nPage',1);
    Mapping.eEssE=struct('nRow',1,'nCol',nEss,'nPage',1);
%外気温と配電線温度初期値
    Mapping.Temp=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
    Mapping.Anglestart=struct('nRow',1,'nCol',1,'nPage',1);
   %下限制約で使う三つ
    Mapping.DummyIl=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
    Mapping.DummyIh=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
    Mapping.rhs=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
    Mapping.binary=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
    %Mapping.sTheta=struct('nRow',1,'nCol',1,'nPage',1);
   
    %以下の変数を書き換えてあげれば、マッピング機能停止 
   %目的関数を計算する式は一つなので、値は一つ
   Mapping.minESS = struct('nRow',1,'nCol',1,'nPage',1);
   Mapping.minTapNum=struct('nRow',1,'nCol',1,'nPage',1);
   %Mapping.minESSPQ=struct('nRow',1,'nCol',1,'nPage',1);
   %Mapping.minVolDif = struct('nRow',1,'nCol',1,'nPage',1);
   %Mapping.minAngle = struct('nRow',1,'nCol',1,'nPage',1);
   %Mapping.minESSkWh = struct('nRow',1,'nCol',1,'nPage',1);
   Mapping.minBrI = struct('nRow',1,'nCol',1,'nPage',1);
   MappingValue=MyProgram.OptFunction.mappingVarSet(Mapping,1000*rand+rand);   

% 最適化問題変数の作成
% 配電線温度に関する変数
% 配電線温度(angleline):連続値

   UpperTemp=repmat(MappingValue.Temp,1,1,Opt.nPhase);
   angleline = optimvar ('angleline',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));
%% 
% 配電線最終温度(anglemax):連続値

   anglemax = optimvar ('anglemax',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));
%% 
% 240A超過バイナリ(B_linecap):バイナリ（通過電流値br_IAbsが240A以上：1 、240A未満：0）

   B_linecap = optimvar ('B_linecap',Opt.nTime,1,Opt.nPhase,'Type','integer'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',ones(Opt.nTime,1,Opt.nPhase));
%% 
% ダミー変数（240Aバイナリ*Br_Imax）(Dummy_Ihigh)

   Dummy_Ih = optimvar ('Dummy_Ih',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));
%% 
% ダミー変数（brI_Abs－240Aバイナリ*Br_Imax）(Dummy_Ilow)

   Dummy_Il = optimvar ('Dummy_Il',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));
%% 
% ダミー変数（240Aバイナリ*θline(t-1)）(Dummy_anglehigh)

   Dummy_angleh = optimvar ('Dummy_angleh',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));
%% 
% ダミー変数（240Aバイナリ*θline(t-1)）(Dummy_anglelow)

   Dummy_anglel = optimvar ('Dummy_anglel',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));
% 
% ブランチ電流(BrI):連続値
% $-\infty \;\le {\textrm{BrI}}_i^{**} \left(t\right)\le \infty$  $i=1,2,\ldotp 
% \ldotp \ldotp ,\textrm{nBr}$:ブランチ数
% 
% 電流は実部$I_i^{\textrm{Re}} \left(t\right)$,虚部$I_i^{\textrm{Im}} \left(t\right)$,絶対値$I_i^{\textrm{abs}} 
% \left(t\right)$,(出力調整時: $I_i^{\textrm{ReUp}} \left(t\right)$,$I_i^{\textrm{ImUp}} 
% \left(t\right)$,$I_i^{\textrm{ReDn}} \left(t\right)$,$I_i^{\textrm{ImDn}} \left(t\right)$)
% 
% 電圧の計算で使われている箇所は残しておく

    brI_Re = optimvar ('brI_Re',Opt.nTime,                                                                                                                                                                                        nBr,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',-inf(Opt.nTime,nBr,Opt.nPhase),'UpperBound',inf(Opt.nTime,nBr,Opt.nPhase));

    brI_Im = optimvar ('brI_Im',Opt.nTime,nBr,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',-inf(Opt.nTime,nBr,Opt.nPhase),'UpperBound',inf(Opt.nTime,nBr,Opt.nPhase));

    %以下3つについて、対象とする配電線は一番変電所に近い配電線のみであるため、一つとした。
    brI_ReAbs = optimvar ('brI_ReAbs',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));

    brI_ImAbs = optimvar ('brI_ImAbs',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',inf(Opt.nTime,1,Opt.nPhase));

    brI_Abs = optimvar ('brI_Abs',Opt.nTime,1,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,1,Opt.nPhase),'UpperBound',240*ones(Opt.nTime,1,Opt.nPhase));
% 蓄電池(Ess)の充放電(EssP):連続値
% $0\;\le {\textrm{EssP}}_i^{**} \left(t\right)\le S_{i,\textrm{ESS},}$,   $i=1,2,\ldotp 
% \ldotp \ldotp ,\textrm{nResi}$:計画対象需要家数, $S_{i,\textrm{ESS},}$ 需要家$i$の蓄電池のkVA容量
% 
% $${{\textrm{EssP}}^{\textrm{abs}} }_i \left(t\right)=\max \left|{{\textrm{EssP}}^{\textrm{ch}} 
% }_i \left(t\right),{{\textrm{EssP}}^{\textrm{dch}} }_i \left(t\right)\right|$$
% 
% $0\;\le Q_{i,\textrm{ESS}}^{**} \left(t\right)\le S_{i,\textrm{ESS},}$,   
% $i=1,2,\ldotp \ldotp \ldotp ,\textrm{nResi}$:計画対象需要家数, $S_{i,\textrm{ESS},}$ 
% 需要家$i$の蓄電池のkVA容量
% 
% $${{\textrm{EssQ}}^{\textrm{abs}} }_i \left(t\right)=\max \left|{{\textrm{EssQ}} 
% }_i \left(t\right)\right|$$
% 
% $\;\;\;0\;\le {\textrm{EssE}}_i \left(t\right)\le \textrm{maxEss}E_i$   $\max 
% {\textrm{EssE}}_{i,}$:需要家$i$の蓄電池のkWh容量
% 
% $\;{{\textrm{Ess}}_{i,\textrm{ekWh}} \le \textrm{EssE}}_i \left(T\right)$  
% ${\textrm{Ess}}_{i,\textrm{ekWh}}$:計画終了時点の最低充電量(通常はSOC50%)

    %
    %Pch
    charPCh = optimvar ('charPCh',Opt.nTime,nCharger,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
    charPCh.UpperBound(1,:)=  0;
    %Pdch
    charPDch = optimvar ('charPDch',Opt.nTime,nCharger,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
    charPDch.UpperBound(1,:)=  0;
    %充放電バイナリ
    charPDchU = optimvar ('charPDchU',Opt.nTime,nCharger,'Type','integer'...
        ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',ones(Opt.nTime,nCharger));
    %Q
    charQInj = optimvar ('charQInj',Opt.nTime,nCharger,'Type','continuous'...
        ,'LowerBound',-Charger.Smax.*ones(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
    %Qabs
   charQAbs = optimvar ('charQAbs',Opt.nTime,nCharger,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nCharger),'UpperBound',Charger.Smax.*ones(Opt.nTime,nCharger));
    %充電器の充電可能量(S)
    charCap= optimvar ('charCap',1,nCharger,'Type','continuous'...
        ,'LowerBound',zeros(1,nCharger),'UpperBound',Charger.Smax.*ones(1,nCharger));
    %現在の充電量
    EssE = optimvar ('EssE',Opt.nTime,nEss,'Type','continuous'...
        ,'LowerBound',-inf(Opt.nTime,nEss),'UpperBound',inf(Opt.nTime,nEss));


    EssE.LowerBound(end,:)=  MappingValue.eEssE;
    %蓄電池の充電可能量(E)
    EssEmax= optimvar ('EssEmax',1,nEss,'Type','continuous'...
        ,'LowerBound',-inf(1,nEss),'UpperBound',inf(1,nEss));
    EssEmin= optimvar ('EssEmin',1,nEss,'Type','continuous'...
        ,'LowerBound',-inf(1,nEss),'UpperBound',inf(1,nEss));

    %差分
    ESS_differenceabs = optimvar ('ESS_differenceabs',Opt.nTime,nEss,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nEss),'UpperBound',inf(Opt.nTime,nEss));
    %}
% ノード電圧(NodeV):連続値
% $-\infty \;\le {\textrm{NodeV}}_i^{**} \left(t\right)\le \infty$  $i=1,2,\ldotp 
% \ldotp \ldotp ,\textrm{nNode}$:ノード数
% 
% 電圧は実部$V_i^{\textrm{Re}} \left(t\right)$,虚部$V_i^{\textrm{Im}} \left(t\right)$,絶対値$V_i^{\textrm{abs}} 
% \left(t\right)$,(出力調整時: $V_i^{\textrm{ReUp}} \left(t\right)$,$V_i^{\textrm{ImUp}} 
% \left(t\right)$,$V_i^{\textrm{ReDn}} \left(t\right)$,$V_i^{\textrm{ImDn}} \left(t\right)$)
% 
% 蓄電池がおかれている箇所の後ろ側は集約可能
% 
% しかし、電圧降下分は考慮しなければならない
% 
% ノードの集約は太陽光出力と負荷の情報を定数としておく

%nodeVr
    nodeV_Re = optimvar('nodeV_Re',Opt.nTime,nNode,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',Systemdata.Vol.lb/sqrt(3)*ones(Opt.nTime,nNode,Opt.nPhase),'UpperBound',Systemdata.Vol.ub/sqrt(3)*ones(Opt.nTime,nNode,Opt.nPhase));%
        %,'LowerBound',Systemdata.Vol.lb/sqrt(3)*ones(Opt.nTime,nNode,Opt.nPhase),'UpperBound',inf(Opt.nTime,nNode,Opt.nPhase));%
%nodeVi　　%虚部は線形では表せないため、実部で下限を満たすようにしている。
    nodeV_Im = optimvar('nodeV_Im',Opt.nTime,nNode,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',-inf(Opt.nTime,nNode,Opt.nPhase),'UpperBound',inf(Opt.nTime,nNode,Opt.nPhase));
%nodeV
    nodeV = optimvar('nodeV',Opt.nTime,nNode,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',Systemdata.Vol.lb/sqrt(3)*ones(Opt.nTime,nNode,Opt.nPhase),'UpperBound',Systemdata.Vol.ub/sqrt(3)*ones(Opt.nTime,nNode,Opt.nPhase));
        %,'LowerBound',Systemdata.Vol.lb/sqrt(3)*ones(Opt.nTime,nNode,Opt.nPhase),'UpperBound',Systemdata.Vol.ub/sqrt(3)*ones(Opt.nTime,nNode,Opt.nPhase));
%nodeVi_abs
    nodeV_ImAbs = optimvar('nodeV_ImAbs',Opt.nTime,nNode,Opt.nPhase,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nNode,Opt.nPhase),'UpperBound',inf(Opt.nTime,nNode,Opt.nPhase));
%nodedV
    nodeDV = optimvar ('nodeDV',Opt.nTime,nNode,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nNode),'UpperBound',inf(Opt.nTime,nNode));
%nodedVmax
    nodeAmbV = optimvar ('nodeAmbV',Opt.nTime,nNode,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nNode),'UpperBound',inf(Opt.nTime,nNode));
%Vmax
    nodeAmbV_Max = optimvar ('nodeAmbV_Max',Opt.nTime,nNode,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nNode),'UpperBound',inf(Opt.nTime,nNode));
%Vmin
    nodeAmbV_Min = optimvar ('nodeAmbV_Min',Opt.nTime,nNode,'Type','continuous'...
        ,'LowerBound',zeros(Opt.nTime,nNode),'UpperBound',inf(Opt.nTime,nNode));
% ノード電流(NodeI):連続値
% $-\infty \;\le {\textrm{NodeI}}_i^{**} \left(t\right)\le \infty$  $i=1,2,\ldotp 
% \ldotp \ldotp ,\textrm{nNode}$:ノード数    ノードに注入される電流値を示す（行列アドミッタンスの電流Iに相当）。

        nodeI_Re = optimvar('nodeI_Re',Opt.nTime,nNode,Opt.nPhase,'Type','continuous'...
            ,'LowerBound',-inf(Opt.nTime,nNode,Opt.nPhase),'UpperBound',inf(Opt.nTime,nNode,Opt.nPhase));

        nodeI_Im = optimvar ('nodeI_Im',Opt.nTime,nNode,Opt.nPhase,'Type','continuous'...
            ,'LowerBound',-inf(Opt.nTime,nNode,Opt.nPhase),'UpperBound',inf(Opt.nTime,nNode,Opt.nPhase));

% SVR動作(SVR):整数,素通しが0
% $-\textrm{SVRnTAP}\le {\textrm{SVR}}_i^{**} \left(t\right)\le \textrm{SVRnTAP}$  
% $i=1,2,\ldotp \ldotp \ldotp ,\textrm{nSVR}$:SVR数         
% 
% SvrTapは10分値で CはカウントのC

        SvrTap = optimvar ('SvrTap',Opt.nTime/2,nSvr,1,...
                'Type','integer','LowerBound',-(Svr.nTap-Svr.defTap).*ones(Opt.nTime/2,nSvr),'UpperBound',(Svr.nTap-Svr.defTap).*ones(Opt.nTime/2,nSvr));
%(Svr.nTap-Svr.defTap).*ones
        SvrTapC = optimvar ('SvrTapC',Opt.nTime/2,nSvr,1,...
                'Type','integer','LowerBound',zeros(Opt.nTime/2,nSvr),'UpperBound',ones(Opt.nTime/2,nSvr));
% LRT動作(LRT):整数,素通しが0
% $1\le {\textrm{SVR}}_i^{**} \left(t\right)\le \textrm{SVRnTAP}$  $i=1,2,\ldotp 
% \ldotp \ldotp ,\textrm{nSVR}$:SVR数         
% 
% LrtTapは10分値で

        %
        LrtTap = optimvar ('LrtTap',Opt.nTime/2,nLrt,1,...
                'Type','integer','LowerBound',ones(Opt.nTime/2,nLrt),'UpperBound',Lrt.nTap.*ones(Opt.nTime/2,nLrt));
%(Lrt.nTap-Lrt.defTap).*ones
        LrtTapC = optimvar ('LrtTapC',Opt.nTime/2,nLrt,1,...
                'Type','integer','LowerBound',zeros(Opt.nTime/2,nLrt),'UpperBound',ones(Opt.nTime/2,nLrt));
        %}
% 
%% 目的関数
% 目的関数は計算する順にプログラムを記載しなければならない

 Obj=struct();

 
%例
%   Obj.minTapNum   = sum(SvrTapC(:,:),"all")+sum(LrtTapC(:,:),"all");%SVRとLRTのタップ回数最小化
%  (変数は１次元目時間、２次元目対象。全ての時間全ての対象のタップ合計数)

%   Obj.minVolDif   = sum(nodeAmbV,"all");　ノードの相間の電圧変動の最小化
%% 
% 1.蓄電池容量最小化 min{S＋（ESS_max-ESS_min）}
% 
% max(charPCh(:,:),charPDCh(:,:))はP_abs

Obj.minESS  = sum(charCap(:,:),"all")+sum((EssEmax(:,:)-EssEmin(:,:)),"all");  
%% 
% 2.結果：タップ見せる用

Obj.minTapNum   = sum(SvrTapC(:,:),"all")+sum(LrtTapC(:,:),"all");
%お試し
%Obj.maxTapNum   = -(sum(SvrTapC(:,:),"all")+sum(LrtTapC(:,:),"all"));
%% 
% 3.次の時間の蓄電池容量との差分最小化 min(ESS_differenceabs)

%Obj.minESSPQ=sum((charPCh(:,:)+charPDch(:,:)),"all")+sum(charQAbs(:,:),"all");
%Obj.minESSkWh=sum(ESS_differenceabs,"all");
%% 
% 4.配電線通過電流最小化min(brI_Abs)

% Obj.minBrI=sum(brI_Abs(:,:,:),"all");
%% 
% 5.配電線温度最小化 min(angleline)

%Obj.minAngle=sum(angleline(:,:,:),"all");
%% 
% 6.基準値(6600V)からの電圧変動の最大値最小化 min(nodedVmax)このために無効電力出ている

%Obj.minVolDif=sum(nodeAmbV(:,:),"all"); %ノードの相間の電圧変動の最小化
%% 
% 

%   AR=sparse(diag(repmat(repelem(Systemdata.Grid.Edges.R,Opt.nTime),Opt.nPhase,1)));
%ソルバーベースの対角成分を抽出
%目的関数は二次までならできるようになった（2021a以降）
%Opt.hourDTは2分間隔運用なので1時間値に直している
    %Obj.minLoss     =sum(   Systemdata.Grid.Edges.R' .*ones(Opt.nTime,nBr,Opt.nPhase).*brI_Re.^2 ...
                    % +      Systemdata.Grid.Edges.R' .*ones(Opt.nTime,nBr,Opt.nPhase).*brI_Im.^2 ,"all")*Opt.hourDT/1e3%...
                     %+MappingValue.lambda*sum(EssE(end,:,:),"all");

    prob = optimproblem;%最適化問題の変数を作成
% 目的関数にマッピングする場合（目的関数が複数の場合必要）
%
fieldNames=fieldnames(Obj);

for iObj=1:(length(fieldNames)-1) %最後の目的関数は設定しない!!
    prob.Constraints.(string(fieldNames(iObj))) = ...%probの制約にランダムな値を入力
        Obj.(string(fieldNames(iObj))) <= MappingValue.(string(fieldNames(iObj)));
end
%}
%% 制約条件
% ノード制約
% LRTノード
% ${\textrm{NodeV}}_i^{\textrm{Re}} \left(t\right)-{\Delta V}_{\textrm{LRT}} 
% {\textrm{LRT}}_i \left(t\right)\textrm{＝SysVn}$ , ${\textrm{NodeV}}_i^{\textrm{Im}} 
% \left(t\right)\textrm{＝0}$

%
LRTVolRe=optimexpr(Opt.nTime,nLrt,Opt.nPhase);%/15不要
LRTVolIm=optimexpr(Opt.nTime,nLrt,Opt.nPhase);%/15不要
for iLRT=1:nLrt    
    % LRTノード
    LRTVolRe(1:Opt.nTime,iLRT,1:Opt.nPhase) = 1.0*nodeV_Re(1:Opt.nTime,Lrt.node(iLRT),:) ...
        - repmat(repelem(Lrt.dVTap/sqrt(3)*LrtTap(:,iLRT),2),1,1,Opt.nPhase);
    LRTVolIm(1:Opt.nTime,iLRT,1:Opt.nPhase) = 1.0*nodeV_Im(1:Opt.nTime,Lrt.node(iLRT),:);
end
prob.Constraints.LRTVolRe = LRTVolRe ==...
   repmat((Systemdata.Ref.Vn)/sqrt(3)*1000 - (Lrt.defTap)*Lrt.dVTap/sqrt(3),Opt.nTime,nLrt,Opt.nPhase);
prob.Constraints.LRTVolIm = LRTVolIm ==0; %基準電圧
%}

%% 
% ここでは、LRTノード（送り出し電圧とタップ位置の連動）とそれ以外のノードに分けて取り扱う
% 
% LRTノード以外
% $\sum_{\textrm{In}} {\textrm{BrI}}_{\textrm{In}}^{\textrm{Re}} \left(t\right)+{\textrm{NodeI}}_i^{\textrm{Re}} 
% \left(t\right)-\sum_{\textrm{Out}} {\textrm{BrI}}_{\textrm{Out}}^{\textrm{Re}} 
% \left(t\right)=0$ ${\textrm{BrI}}_{\textrm{In}}^{\textrm{Re}} \left(t\right)$;ノードiに流入する全ブランチ電流、${\textrm{BrI}}_{\textrm{Ount}}^{\textrm{Re}} 
% \left(t\right)$;ノードiから流出する全ブランチ電流　　（虚部はReをImに変更）

%
% LRTノード以外の制約
brIRe=optimexpr(Opt.nTime,nNode,Opt.nPhase);
brIIm=optimexpr(Opt.nTime,nNode,Opt.nPhase);

%ノード1はスラック（PQ指定をしない）ノード（LRTがあるノード）
%brIRe(:,1,:)=nodeI_Re(:,1,:);
%brIIm(:,1,:)=nodeI_Im(:,1,:);

for iNode=2:nNode
   if isempty(find(iNode==Lrt.node, 1))==1
    Ihigh=find(Systemdata.Grid.Edges.EndNodes(:,2)==iNode);
    Ilow=find(Systemdata.Grid.Edges.EndNodes(:,1)==iNode);
   
        %実部前半項
        brIRe(1:Opt.nTime,iNode,1:Opt.nPhase) =sum(brI_Re(:,Ihigh,1:Opt.nPhase),2)+nodeI_Re(:,iNode,1:Opt.nPhase); %流入分Ihigh
               
        %虚部前半項
         brIIm(1:Opt.nTime,iNode,1:Opt.nPhase) =sum(brI_Im(:,Ihigh,1:Opt.nPhase),2)+nodeI_Im(:,iNode,1:Opt.nPhase);%流入分in
        
        if isempty(Ilow)==0  %流出分Ilow
            %実部後半
            brIRe(1:Opt.nTime,iNode,1:Opt.nPhase) =brIRe(1:Opt.nTime,iNode,1:Opt.nPhase)-sum(brI_Re(:,Ilow,1:Opt.nPhase),2);
            %虚部後半
            brIIm(1:Opt.nTime,iNode,1:Opt.nPhase) =brIIm(1:Opt.nTime,iNode,1:Opt.nPhase)-sum(brI_Im(:,Ilow,1:Opt.nPhase),2);
        end        
   end
end

brIRe(1:Opt.nTime,2:nNode,1:Opt.nPhase)=brIRe(1:Opt.nTime,2:nNode,1:Opt.nPhase)...
    ;%+ MappingValue.netdemIrV(1:Opt.nTime,2:nNode,1:Opt.nPhase).*nodeV_Re(1:Opt.nTime,2:nNode,1:Opt.nPhase);

brIIm(1:Opt.nTime,2:nNode,1:Opt.nPhase)=brIIm(1:Opt.nTime,2:nNode,1:Opt.nPhase)...
    ;%+ MappingValue.netdemIiV(1:Opt.nTime,2:nNode,1:Opt.nPhase).*nodeV_Re(1:Opt.nTime,2:nNode,1:Opt.nPhase);

prob.Constraints.brIRe = brIRe ==0;
prob.Constraints.brIIm = brIIm ==0;
%}
% SVRの電圧制御範囲とアドミタンス行列

SVRV=optimexpr(Opt.nTime,nNode);%
% 影響を与えるノード
%
 for iSVR=1:nSvr
        for iTime=1:Opt.nTime/2
            SVRV(iTime,1:nNode,:)=SVRV(iTime,1:nNode,:)...
                +(Svr.dVTap(iSVR)/sqrt(3)*SvrTap(iTime,iSVR,:).*Svr.effNode(:,iSVR,:)');
        end
        
 end
%

NodeAdm.YRe=zeros(nNode,nNode);
NodeAdm.YIm=zeros(nNode,nNode);
%
brNodes=Systemdata.Grid.Edges.EndNodes(:,:);
for iBr=1:nBr    
    NodeAdm.YRe(brNodes(iBr,1),brNodes(iBr,2))=Systemdata.Grid.Edges.YRe(brNodes(iBr,1));
    NodeAdm.YRe(brNodes(iBr,2),brNodes(iBr,1))=Systemdata.Grid.Edges.YRe(brNodes(iBr,1));

    NodeAdm.YIm(brNodes(iBr,1),brNodes(iBr,2))=Systemdata.Grid.Edges.YIm(brNodes(iBr,1));
    NodeAdm.YIm(brNodes(iBr,2),brNodes(iBr,1))=Systemdata.Grid.Edges.YIm(brNodes(iBr,1));    
end
for iNode=1:nNode
    NodeAdm.YRe(iNode,iNode)=-sum(NodeAdm.YRe(iNode,:),2);
    NodeAdm.YIm(iNode,iNode)=-sum(NodeAdm.YIm(iNode,:),2);%Systemdata.Grid.Nodes.YIm(iNode,1);
end
%}
% 潮流方程式制約

%
nodeIReEq=optimexpr(Opt.nTime,nNode,Opt.nPhase);
nodeIImEq=optimexpr(Opt.nTime,nNode,Opt.nPhase);
SVRV=repelem(SVRV,2,1);

 for iTime=1:Opt.nTime
     for iPhase=1:Opt.nPhase
         nodeIReEq(iTime,:,iPhase)=-nodeI_Re(iTime,:,iPhase)*sqrt(3)... *1/sqrt(3) ... 
             + (NodeAdm.YRe(:,:)*(nodeV_Re(iTime,:,iPhase)-SVRV(iTime,:))')' ...
             -  (NodeAdm.YIm(:,:)*nodeV_Im(iTime,:,iPhase)')' ;

         nodeIImEq(iTime,:,iPhase)=-nodeI_Im(iTime,:,iPhase)*sqrt(3)... *1/sqrt(3) ... 
             + (NodeAdm.YRe(:,:)*nodeV_Im(iTime,:,iPhase)')' ...
             + (NodeAdm.YIm(:,:)*(nodeV_Re(iTime,:,iPhase)-SVRV(iTime,:))')' ;
     end
 end
prob.Constraints.nodeIReEq=nodeIReEq==0;
prob.Constraints.nodeIImEq=nodeIImEq==0;
%clearvars nodeIReEq nodeIImEq
 %}
% 電流値と定電力負荷、蓄電池などのノードバランス制約
% 実部 ${\textrm{NodeI}}_i^{\textrm{Re}} \left(t\right)-\frac{{\textrm{EssP}}_i^{\textrm{Dch}} 
% }{\textrm{sqrt}\left(3\right)*\textrm{SysVn}}+\frac{{\textrm{EssP}}_i^{\textrm{Ch}} 
% }{\textrm{sqrt}\left(3\right)*\textrm{SysVn}}+\frac{{\textrm{NodeV}}_i^{\textrm{Re}} 
% \left(t\right)}{\textrm{SysVn}*1000}{\textrm{NODEI}}_i^{\textrm{Re}} \left(t\right)=2*{\textrm{NODEI}}_i^{\textrm{Re}} 
% \left(t\right)$  
% 
% 虚部部 ${\textrm{NodeI}}_i^{\textrm{Im}} \left(t\right)-\frac{{\textrm{EssQ}}_i^{\textrm{Dch}} 
% }{\textrm{sqrt}\left(3\right)*\textrm{SysVn}}+\frac{{\textrm{NodeV}}_i^{\textrm{Re}} 
% \left(t\right)}{\textrm{SysVn}*1000}{\textrm{NODEI}}_i^{\textrm{Im}} \left(t\right)=-2*{\textrm{NODEI}}_i^{\textrm{Im}} 
% \left(t\right)$  
% 
% 定電力の模擬：電流の増減を$\left(1-\frac{{\textrm{NodeV}}_i^{\textrm{Re}} \left(t\right)-\textrm{SysVn}*1000}{\textrm{SysVn}*1000}\right){\textrm{NODEI}}_i^{**} 
% \left(t\right)$　で表現　${\textrm{NODEI}}_i^{\textrm{Re}} \left(t\right)$はノードにおける負荷

%
nodeIRe_bal=optimexpr(Opt.nTime,nNode,Opt.nPhase);
nodeIRe_bal(1:Opt.nTime,2:nNode,1:Opt.nPhase)=nodeI_Re(1:Opt.nTime,2:nNode,1:Opt.nPhase);

nodeIIm_bal=optimexpr(Opt.nTime,nNode,Opt.nPhase);
nodeIIm_bal(1:Opt.nTime,2:nNode,1:Opt.nPhase)=nodeI_Im(1:Opt.nTime,2:nNode,1:Opt.nPhase);
%         蓄電池設置

%
for iCha=1:nCharger
    iCharNode=Charger.node(iCha);
    
    type=find(Charger.phase(iCha)==phase);MappingValue.netdemIr
    if isempty(type)
        type=1:length(phase);
    end

    for iType=1:length(type)
        nodeIRe_bal(:,iCharNode,type(iType))=nodeIRe_bal(:,iCharNode,type(iType))...
            + ( sqrt(3)/(Systemdata.Ref.Vn)*charPCh(:,iCha)- sqrt(3)/(Systemdata.Ref.Vn)*charPDch(:,iCha));
        nodeIIm_bal(:,iCharNode,type(iType))=nodeIIm_bal(:,iCharNode,type(iType))-( sqrt(3)/(Systemdata.Ref.Vn)*charQInj(:,iCha,:));
    end
end
%}
prob.Constraints.nodeIRe_bal = nodeIRe_bal == MappingValue.netdemIr;      %beqの値を入れても可   
prob.Constraints.nodeIIm_bal = nodeIIm_bal == MappingValue.netdemIi;     

%clearvars nodeIRe_bal nodeIIm_bal
%}
% 電流の絶対値
% 実部

%
prob.Constraints=MyProgram.OptFunction.Xabs(prob.Constraints,"brIReAbs",brI_ReAbs,brI_Re(:,1,1),-brI_Re(:,1,1),0,0,"otherDirection","off");
% 虚部

prob.Constraints=MyProgram.OptFunction.Xabs(prob.Constraints,"brIImAbs",brI_ImAbs,brI_Im(:,1,1),-brI_Im(:,1,1),0,0,"otherDirection","off");
% 電流の最大値（nBr=1でとりあえずよい）
% $\sqrt{{\left({\textrm{BrI}}_{\textrm{abs}}^{\textrm{Re}} \left(t\right)\right)}^2 
% +{\left({\textrm{BrI}}_{\textrm{abs}}^{\textrm{Im}} \left(t\right)\right)}^2 
% }\le {\textrm{BrI}}_i^{\textrm{abs}} \left(t\right)$ を線形近似    $-{\textrm{App}}_{j,1} 
% {\textrm{BrI}}_{\textrm{abs}}^{\textrm{Re}} \left(t\right)+{\textrm{BrI}}_{\textrm{abs}}^{\textrm{Im}} 
% \left(t\right)-{{\textrm{App}}_{j,2} \textrm{BrI}}_a^{\textrm{abs}} \left(t\right)\le 
% 0$ $j=1,2,3\ldotp \ldotp \ldotp \textrm{nApp}$ :線形近似区間数

prob.Constraints=MyProgram.OptFunction.SLimit(prob.Constraints,"IabsLimit",20,brI_ReAbs,brI_ImAbs,brI_Abs);
%}
% 電圧変動
% 虚部の絶対値の算出

prob.Constraints=MyProgram.OptFunction.Xabs(prob.Constraints,"NodeVImAbs",nodeV_ImAbs,nodeV_Im,-nodeV_Im,0,0,"otherDirection","off");
% 最大値/最小値
% $${\textrm{app}\left(k,2\right)\textrm{NodeV}}_i^{\min } +\textrm{app}\left(k,1\right){\textrm{NodeV}}_i^{\textrm{Re}} 
% \left(t\right)+{\textrm{NodeV}}_i^{\textrm{Im},\textrm{Abs}} \left(t\right)\le 
% 0$$
% 
% $$-\textrm{app}\left(k,2\right){\textrm{NodeV}}_i^{\max } \left(t\right)-\textrm{app}\left(k,1\right){\textrm{NodeV}}_i^{\textrm{Re}} 
% \left(t\right)+{\textrm{NodeV}}_i^{\textrm{Im},\textrm{Abs}} \left(t\right)\le 
% 0$$

%{
tmp_nApp=201;
tmp_sApp=201-5;
tmp_appPara=lineApp(tmp_nApp); %区分線形近似パラメータ取得
for iApp=tmp_sApp:(tmp_nApp-1)    
    tmp_r=((iApp-tmp_sApp)*Opt.nTime +1) :( (iApp-tmp_sApp+1)*Opt.nTime ) ;
    Sys_opt.Cons.NodeVMax(tmp_r,1:nNode,1:Opt.nPhase) = ...
        -tmp_appPara(iApp,2)*repmat(Sys_opt.var.NodeV(:,:,"NodeV_Max"),Opt.nTime,1,Opt.nPhase)...
        -tmp_appPara(iApp,1)*nodeV_Re(:,:,1:Opt.nPhase)...
        +repmat(NodeV_ImAbs(:,:,1:3),1,1,1);%Opt.nPhase) ;    
end

Sys_opt.Cons.NodeVMin(1:Opt.nTime,1:nNode,1:Opt.nPhase) = ...
        +repmat(Sys_opt.var.NodeV(:,:,"NodeV_Min"),Opt.nTime,1,Opt.nPhase)...
        -repmat(nodeV_Re(:,:,1:3),1,1,1);%Opt.nPhase);
Sys_opt.prob.Constraints.NodeVMax = Sys_opt.Cons.NodeVMax <=0;
Sys_opt.prob.Constraints.NodeVMin = Sys_opt.Cons.NodeVMin <=0;
% 下の関数SLimitで記述済み
%} 

prob.Constraints.nodeVMin = nodeV_Re - nodeV<=0;%nodeV下限
prob.Constraints=MyProgram.OptFunction.SLimit(prob.Constraints,"nodeVMax",2,nodeV_Re,nodeV_ImAbs,nodeV);



% 変動量の算出（結果電圧の整形に活用）
% ${\textrm{NodeV}}_i^{\textrm{Re}} \left(t\right)-{\textrm{Node}\Delta V}_i 
% \left(t\right)\le \textrm{SysVn}$  および   $-{\textrm{NodeV}}_i^{\textrm{Re}} 
% \left(t\right)-{\textrm{Node}\Delta V}_i \left(t\right)\le -\textrm{SysVn}$

% 電圧変動算出
%
NodeVdV1 =  nodeV(:,:,:) - repmat(nodeDV(:,:),1,1,Opt.nPhase);
NodeVdV2 = -nodeV(:,:,:) - repmat(nodeDV(:,:),1,1,Opt.nPhase);

prob.Constraints.NodeVdV1 = NodeVdV1 <= Systemdata.Ref.Vn/sqrt(3)*1000*ones(Opt.nTime,nNode,Opt.nPhase) ;
prob.Constraints.NodeVdV2 = NodeVdV2 <=-Systemdata.Ref.Vn/sqrt(3)*1000*ones(Opt.nTime,nNode,Opt.nPhase) ;
%}

% 電圧不平衡
%次元数をそろえる（最大値はどの相でも同じなのでコピーして増やす）
NodeVAmbV1 =  nodeV(:,:,:) - repmat(nodeAmbV_Max(:,:),1,1,Opt.nPhase);
NodeVAmbV2 = -nodeV(:,:,:) + repmat(nodeAmbV_Min(:,:),1,1,Opt.nPhase);
NodeVAmbV =-nodeAmbV(:,:)+nodeAmbV_Max(:,:)-nodeAmbV_Min(:,:);

prob.Constraints.NodeVAmbV = NodeVAmbV == 0;
prob.Constraints.NodeVAmbV1 = NodeVAmbV1 <= 0 ;
prob.Constraints.NodeVAmbV2 = NodeVAmbV2 <= 0 ;

%clearvars NodeVAmbV1 NodeVAmbV2 NodeVAmbV
%}
% 配電線温度に関する制約
% 定数宣言

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
% $$\theta_{linei,i+1} {\left(t\right)}\ge \theta_{linemaxi,i+1} {\left(t\right)}*{\left(1-K_e 
% \right)}+\theta_{linei,i+1} {\left(t-1\right)}*K_e \ \ \ \left(K_e は定数\right)$$

Anglestart=repmat(MappingValue.Anglestart,Opt.nTime,1,Opt.nPhase);
prob.Constraints.AngleEq = angleline(1,:,:)-anglemax(1,:,:)*(1-Ke) == Anglestart(1,:,:);
prob.Constraints.AnglenEq = angleline(2:end,:,:)-anglemax(2:end,:,:)*(1-Ke)-angleline(1:(end-1),:,:)*Ke >=0;
% DRの有無判定またはOC制約
% $$I_{i,i+1} \left(t\right)\le 240\;\textrm{or}\;400$$
% 
% Upperbndで設定(DR切替で設定し直す必要あり)
% 配電線温度の最大制約
% $$\theta_{linei,i+1} \left(t\right)\le \theta_{linecapmax} -Temp\left(t\right)$$
% 
% Upperbndで設定
% 配電線最終温度の等式制約の準備
% $$\theta_{linemaxi,i+1} {\left(t\right)}=\alpha_{i,i+1} \left(t\right)*I_{i,i+1} 
% \left(t\right)+\beta_{i,i+1} \left(t\right)$$
% 
% αは最適化変数であるので最適化変数brImaxと掛け算はでsEssきない
% 
% ①if文は使えないのでバイナリをいれないといけない。
% 
% →バイナリ変数$B_{\textrm{linecap}}$(brImax$\ge 240A$：１、それ以外：０)の生成
% 
% 240Aで判定しなければならない
% 
% $$240*B_{\textrm{linecap}} \le I_{i,i+1} \left(t\right)\le M*B_{\textrm{linecap}} 
% +240$$

prob.Constraints.Bcaplb = 240*B_linecap(:,:,:)-brI_Abs(:,:,:) <=0;
prob.Constraints.Bcapub = brI_Abs(:,:,:)-100000*B_linecap(:,:,:)-240 <=0;
%% 
% ダミー変数Dummy_high(値は電流値)＝240Aを超えているかバイナリ*電流brImax→bigM定式化
% 
% $$Dummy_{\textrm{Ihigh}} \le M*B_{linecap}$$
% 
% $$-M*{\left(1-B_{linecap} \right)}\le Dummy_{\textrm{Ihigh}} -I_{i,i+1} {\left(t\right)}\le 
% 0$$

prob.Constraints.DummyIhigh1 = Dummy_Ih(:,:,:)-100000*B_linecap(:,:,:) <=0;
prob.Constraints.DummyIhigh2 = Dummy_Ih(:,:,:)-brI_Abs(:,:,:)-100000*B_linecap(:,:,:)+100000 >=0;
prob.Constraints.DummyIhigh3 = Dummy_Ih(:,:,:)-brI_Abs(:,:,:) <=0;
%% 
% BrImaxー（ダミー変数）で小さい方の電流値算出可能
% 
% $$Dummy_{low} =I_{i,i+1} {\left(t\right)}-Dummy_{high}$$

prob.Constraints.DummyIlow = brI_Abs(:,:,:)-Dummy_Ih(:,:,:)-Dummy_Il(:,:,:) == 0;
%% 
% ※240Aバイナリ×θline(t-1)が存在しているので上と同様にbigM定式化
% 
% $$Dummy_{\textrm{anglehigh}} \le M*B_{linecap}$$
% 
% $$-M*{\left(1-B_{linecap} \right)}\le Dummy_{\textrm{anglehigh}} -\theta_{linei,i+1} 
% \left(t-1\right)\le 0$$

prob.Constraints.Dummyangleh1 = Dummy_angleh(:,:,:)-100000*B_linecap(:,:,:) <=0;
prob.Constraints.Dummyangleh2 = Dummy_angleh(1,:,:)-angleline(1,:,:)-100000*B_linecap(1,:,:)+100000 >=0;
prob.Constraints.Dummyangleh3 = Dummy_angleh(2:end,:,:)-angleline(1:(end-1),:,:)-100000*B_linecap(2:end,:,:)+100000 >=0;
prob.Constraints.Dummyangleh4 = Dummy_angleh(1,:,:)-angleline(1,:,:) <=0;
prob.Constraints.Dummyangleh5 = Dummy_angleh(2:end,:,:)-angleline(1:(end-1),:,:) <=0;
%% 
% $$Dummy_{\textrm{anglelow}} =\theta_{linei,i+1} \left(t-1\right)-Dummy_{\textrm{anglehigh}}$$

prob.Constraints.Dummyanglel1 = angleline(1,:,:)-Dummy_angleh(1,:,:)-Dummy_anglel(1,:,:) ==0;
prob.Constraints.Dummyanglel2 = angleline(1:(end-1),:,:)-Dummy_angleh(2:end,:,:)-Dummy_anglel(2:end,:,:) ==0;
% Tempの読み込み

% Tempname=sprintf('Kuwana_Temp_2min/data_%d_%d.xlsx',YEAR,MONTH);
% Tempread=readmatrix(Tempname,'Range','H2:H22321');%桑名の1時間毎の気温
Tempname=sprintf('Kuwana_Temp_2min/data_%d.xlsx',MONTH);
Tempread=readmatrix(Tempname,'Range','O2:O2977');

Temp(:,:)=zeros(Opt.nTime,1);%Temp 初期値

for Temploop=1:1:Opt.nTime
    Temp(Temploop,1)=Tempread(Temploop+(DAY_S-1)*Opt.nTime,1);
end
%以下、参考
%Main.DayLoop = MyProgram.Function.simTimeSet...
    %(datetime(2018,3,1),datetime(2018,3,10),days(1),"intervaltime",'closed'); 
%日付ループ設定（openにすると終わりの日は計算されない
% 配電線最終温度の下限制約（上限はソルバーベースで）
% 配電線最終温度は以下の式で与えれられる
% 
% $$\begin{array}{l}\theta_{linemaxi,i+1} {\left(t\right)}=\alpha_{\textrm{low}} 
% *I_{\textrm{low}} +\beta_{\textrm{low}} *\left(1-B_{\textrm{linecap}} \right)+\alpha_{\textrm{high}} 
% *I_{\textrm{high}} +\beta_{\textrm{high}} *B_{\textrm{linecap}} \\\left.{\left(A\right.}_{\alpha 
% } *Temp{\left(t\right)}+B_{\alpha } *\theta_{linei,i+1} \left(t-1\right)+C_a 
% \right)*I_{\textrm{low}} +\left(A_{\beta } *Temp{\left(t\right)}+B_{\beta } 
% *\theta_{\textrm{low}} +C_{\beta } \right)-\left(A_{\beta } *Temp{\left(t\right)}+C_{\beta 
% } \right)*B_{\textrm{linecap}} \\\left.+{\left(D\right.}_{\alpha } *Temp{\left(t\right)}+E_{\alpha 
% } *\theta_{linei,i+1} \left(t-1\right)+F_a \right)*I_{\textrm{high}} +\left(D_{\beta 
% } *Temp{\left(t\right)}+F_{\beta } \right)*B_{\textrm{linecap}} +E_{\beta } 
% *\theta_{\textrm{high}} \end{array}$$
% 
% まとめると
% 
% 2次：$B_{\alpha } *\theta_{linei,i+1} \left(t-1\right)*I_{\textrm{low}}$と$E_{\alpha 
% } *\theta_{linei,i+1} \left(t-1\right)*I_{\textrm{high}}$
% 
% 1次：$\left.{\left(A\right.}_{\alpha } *Temp{\left(t\right)}+C_a \right)*I_{\textrm{low}}$と$\left.{\left(D\right.}_{\alpha 
% } *Temp{\left(t\right)}+F_a \right)*I_{\textrm{high}}$と$B_{\beta } *\theta_{\textrm{low}}$と$E_{\beta 
% } *\theta_{\textrm{high}}$と$\left(\left(D_{\beta } -A_{\beta } *\right)\textrm{Temp}\left(t\right)+\left(F_{\beta 
% } -C_{\beta } \right)\right)*B_{\textrm{linecap}}$
% 
% 定数：$A_{\beta } *Temp{\left(t\right)}+C_{\beta }$
% 
% 下限制約では、2次を排除するために$\theta_{linei,i+1} \left(t-1\right)$を別の値XXXに変更する。今回はXXX=90
% 
% よって下限制約では
% 
% 1次：$\left.{\left(A\right.}_{\alpha } *Temp{\left(t\right)}+\textrm{XXX}*B_{\alpha 
% } +C_a \right)*I_{\textrm{low}}$と$\left.{\left(D\right.}_{\alpha } *Temp{\left(t\right)}+\textrm{XXX}*E_{\alpha 
% } +F_a \right)*I_{\textrm{high}}$と$B_{\beta } *\theta_{\textrm{low}}$と$E_{\beta 
% } *\theta_{\textrm{high}}$と$\left(\left(D_{\beta } -A_{\beta } *\right)\textrm{Temp}\left(t\right)+\left(F_{\beta 
% } -C_{\beta } \right)\right)*B_{\textrm{linecap}}$
% 
% 定数：$A_{\beta } *Temp{\left(t\right)}+C_{\beta }$
% 
% 
% 
% Tempを含む係数はマッピングをする必要がある
% 
% →4つのマッピング変数が必要

%MappingValueのサイズに注意
%旧
% MappingValue.DummyIl     A_alpha*Temp+XXX*B_alpha+C_alpha
% MappingValue.DummyIh     D_alpha*Temp+XXX*E_alpha+F_alpha 
% MappingValue.binary      (D_beta-A_beta)*Temp+F_beta-C_beta
% MappingValue.rhs         -(A_beta*Temp+C_beta)

%新
% MappingValue.DummyIl     A_alpha*Temp+XXX*B_alpha+C_alpha
% MappingValue.DummyIh     D_alpha*Temp+XXX*E_alpha+F_alpha 
% MappingValue.binary      (D_beta-A_beta)*Temp+XXX*(E_beta-B_beta)+F_beta-C_beta
% MappingValue.rhs         -(A_beta*Temp+XXX*B_beta+C_beta)

OptDummyIl=repmat(MappingValue.DummyIl,1,1,Opt.nPhase);
OptDummyIh=repmat(MappingValue.DummyIh,1,1,Opt.nPhase);
Optbinary=repmat(MappingValue.binary,1,1,Opt.nPhase);
Optrhs=repmat(MappingValue.rhs,1,1,Opt.nPhase);
%{
prob.Constraints.Anglemax = -anglemax(1:Opt.nTime,:,:)...
+OptDummyIl(1:Opt.nTime,:,:).*Dummy_Il(1:Opt.nTime,:,:)+OptDummyIh(1:Opt.nTime,:,:).*Dummy_Ih(1:Opt.nTime,:,:)...
+B_beta*Dummy_anglel(1:Opt.nTime,:,:)+E_beta*Dummy_angleh(1:Opt.nTime,:,:)...
+Optbinary(1:Opt.nTime,:,:).*B_linecap(1:Opt.nTime,:,:)==Optrhs(1:Opt.nTime,:,:);
%}
prob.Constraints.Anglemax = -anglemax(1:Opt.nTime,:,:)...
+OptDummyIl(1:Opt.nTime,:,:).*Dummy_Il(1:Opt.nTime,:,:)+OptDummyIh(1:Opt.nTime,:,:).*Dummy_Ih(1:Opt.nTime,:,:)...
+Optbinary(1:Opt.nTime,:,:).*B_linecap(1:Opt.nTime,:,:)==Optrhs(1:Opt.nTime,:,:);
%{
%昔のやつ
prob.Constraints.nAnglemax = -anglemax(2:Opt.nTime,:,:)...
+OptbrI(2:Opt.nTime,:,:).*brI_Abs(2:Opt.nTime,:,:)+B_beta*angleline(1:(Opt.nTime-1),:,:)...
+OptDummy(2:Opt.nTime,:,:).*Dummy_high(2:Opt.nTime,:,:)+(E_beta-B_beta)*Dummy_angle(2:end,:,:)...
+OptB(2:Opt.nTime,:,:).*B_linecap(2:Opt.nTime,:,:)<=Optrhs(2:Opt.nTime,:,:);
%}
% 蓄電池に関する制約
% バイナリ制約(SOS1:Special Orders Set1)
% 充放電制約   

%{
prob.Constraints.PDchEq1=charPDch(:,1)-charPDch(:,2)==0;
prob.Constraints.PDchEq2=charPDch(:,2)-charPDch(:,3)==0;
prob.Constraints.PChEq1=charPCh(:,1)-charPCh(:,2)==0;
prob.Constraints.PChEq2=charPCh(:,2)-charPCh(:,3)==0;
prob.Constraints.QEq1=charQInj(:,1)-charQInj(:,2)==0;
prob.Constraints.QEq2=charQInj(:,2)-charQInj(:,3)==0;
%}
prob.Constraints=MyProgram.OptFunction.SOS1(prob.Constraints,"CharPChSOS1",Charger.Smax,charPDch,charPCh,charPDchU);
% 蓄電池容量制約
% 最大有効電力

prob.Constraints=MyProgram.OptFunction.Xabs(prob.Constraints,"CharPmax",Charger.Smax.*ones(Opt.nTime,nCharger),charPDch,charPCh,0,0);
% 最大無効電力

prob.Constraints=MyProgram.OptFunction.Xabs(prob.Constraints,"CharQmax",charQAbs,charQInj,-charQInj,0,0,"otherDirection","off");
% インバータ容量制約
% $-{{\textrm{EssP}}^{\textrm{abs}} }_i \left(t\right)+{{\textrm{EssQ}}^{\textrm{abs}} 
% }_i \left(t\right)-{{\textrm{EssCAP}}^{\textrm{kVA}} }_i \le 0$ $j=1,2,3\ldotp 
% \ldotp \ldotp \textrm{nApp}$ :線形近似区間数 (詳細は関数lineApp参照)

prob.Constraints=MyProgram.OptFunction.SLimit(prob.Constraints,"CharSlimit",3,charPDch+charPCh,charQAbs,charCap);
% Ess容量の制約

ESSmax=repmat(EssEmax,Opt.nTime,1);
ESSmin=repmat(EssEmin,Opt.nTime,1);
prob.Constraints.EssEmax=EssE(:,:)-ESSmax(:,:) <=0;
prob.Constraints.EssEmin=-EssE(:,:)+ESSmin(:,:) <=0;
%% 
% 
% Ess充電量に関する制約

inEssE=(Charger.effe(1,:).*ones(Opt.nTime,nCharger)).*charPCh(:,:);
outEssE=1./(Charger.effe(1,:).*ones(Opt.nTime,nCharger)) .*charPDch(:,:) ;
prob.Constraints=MyProgram.OptFunction.EnergyBalance(prob.Constraints,"EssEBalance",Opt.hourDT,MappingValue.sEssE,EssE,inEssE,outEssE);
% ESS差分

%L:左側 R:右側
prob.Constraints.ESSdifL = -EssE(1,:)-ESS_differenceabs(1,:) <=0;
prob.Constraints.ESSdifR = -ESS_differenceabs(1,:)+EssE(1,:) <=0;
prob.Constraints.ESSndifL = EssE(2:end,:)-EssE(1:(end-1),:)+ESS_differenceabs(2:end,:) >=0;
prob.Constraints.ESSndifR = ESS_differenceabs(2:end,:)-EssE(2:end,:)+EssE(1:(end-1),:) >=0;
%}
% LRT/SVRの動作に関する制約
% 動作回数のカウント
% ${\textrm{LRT}}_i \left(t\right)-{\textrm{LRT}}_i \left(t-1\right)-{\textrm{LRT}}_i^{\textrm{nTAP}} 
% \left(t\right)\le 0$ かつ  $-{\textrm{LRT}}_i \left(t\right)+{\textrm{LRT}}_i 
% \left(t-1\right)-{\textrm{LRT}}_i^{\textrm{nTAP}} \left(t\right)\le 0$
% 
% ※最初の時間 t=1では最後時間との差分をカウント。すなわち ${\textrm{LRT}}_i \left(\textrm{nT}\right)-{\textrm{LRT}}_i 
% \left(1\right)-{\textrm{LRT}}_i^{\textrm{nTAP}} \left(\textrm{nT}\right)\le 
% 0$ かつ  $-{\textrm{LRT}}_i \left(\textrm{nT}\right)+{\textrm{LRT}}_i \left(1\right)-{\textrm{LRT}}_i^{\textrm{nTAP}} 
% \left(\textrm{nT}\right)\le 0$

%
%LRTの動作回数のカウント
time=(2:Opt.nTime/2)';
time_before=time-1;
LRTNTap1(1,1:nLrt) = LrtTap(1,:) -LrtTapC(1,:) ;
LRTNTap2(1,1:nLrt) =-LrtTap(1,:) -LrtTapC(1,:) ;
LRTNTap1(time,1:nLrt) = LrtTap(time,:) -LrtTap(time_before,:) -LrtTapC(time,:).*Lrt.nTap;
LRTNTap2(time,1:nLrt) =-LrtTap(time,:) + LrtTap(time_before,:)-LrtTapC(time,:).*Lrt.nTap;

prob.Constraints.LRTNTap1 = LRTNTap1 <=[ MappingValue.sLrtTap(1,:);zeros(length(time),nLrt)];
prob.Constraints.LRTNTap2 = LRTNTap2 <=[ MappingValue.sLrtTap(2,:);zeros(length(time),nLrt)];
clearvars LRTNTap1 LRTNTap2
prob.Constraints.LRTNTapC = sum(LrtTapC(:,:),1) <=50;
%% 
% ${\textrm{SVR}}_i \left(t\right)-{\textrm{SVR}}_i \left(t-1\right)-{\textrm{SVR}}_i^{\textrm{nTAP}} 
% \left(t\right)\le 0$ かつ  $-{\textrm{SVR}}_i \left(t\right)+{\textrm{SVR}}_i 
% \left(t-1\right)-{\textrm{SVR}}_i^{\textrm{nTAP}} \left(t\right)\le 0$

% SVRの動作回数のカウント
SVRNTap1(1,1:nSvr) = SvrTap(1,:) -SvrTapC(1,:) ;
SVRNTap2(1,1:nSvr) =-SvrTap(1,:) -SvrTapC(1,:) ;

SVRNTap1(time,1:nSvr) = SvrTap(time,:,1)-SvrTap(time_before,:,1) -SvrTapC(time,:).*Svr.nTap(1,1);
SVRNTap2(time,1:nSvr) =-SvrTap(time,:,1) + SvrTap(time_before,:,1) -SvrTapC(time,:).*Svr.nTap(1,1);

prob.Constraints.SVRNTap1 = SVRNTap1 <=[ MappingValue.sSvrTap(1,:);zeros(length(time),nSvr)];
prob.Constraints.SVRNTap2 = SVRNTap2 <=[ MappingValue.sSvrTap(2,:);zeros(length(time),nSvr)];
clearvars SVRNTap1 SVRNTap2
for iSvr = 1:nSvr
    prob.Constraints.("SVR" + iSvr + "NTapC") = sum(SvrTapC(:,iSvr), 1) <= 50;
end
% prob.Constraints.SVR2NTapC = sum(SvrTapC(:,2),1) <=50;
%}
%}
%% 構造体への変換とマッピング（基本的に変更しない）

%目的関数で設定した変数をmappinglamudaで使用していないとエラー
%OptimzationStruct（probは問題ベースproblemはソルバーベース（qc以外））は全部入っている
%verIndexはxmapに関係するやつ
OptimizationStruct=MyProgram.OptFunction.prob2ProblemsSet(prob,Obj,MappingValue,'matfile','on');

%SValue=struct('LrtTap',Lrt.defTap,'SvrTap',0*ones(1,nSvr),'angleline',30*ones(1,3));
%SValue=struct('LrtTap',Lrt.defTap,'SvrTap',0*ones(1,nSvr),'angleline',resTT.angleline(Opt.nTime,:).*ones(1,3));
%SValue=struct('EssE',zeros(1,nEss),'LrtTap',Lrt.defTap,'SvrTap',0*ones(1,nSvr),'angleline',30*ones(1,3));
SValue=struct('EssE',Ess.kWhCap/2,'LrtTap',Lrt.defTap,'SvrTap',0*ones(1,nSvr),'angleline',anglestart*ones(1,1));
%結果のテーブルを作成（計画の最初の1行だけ作成）SValueを変えても最適化の結果は変わらない
[iniResTT,iniFvalTT,iniSolTT] = MyProgram.OptFunction.resTTcre(Obj,prob.Variables,...
                            Opt.nTime,SValue,{'有効電力','無効電力'},Main.DayLoop.startTime);
iniResTT.("有効電力")=zeros(1,3);
iniResTT.("無効電力")=zeros(1,3);

DataInfo = MyProgram.Function.InfoCreate;

% save(fullfile(Main.FolderName.input,'Optimization.mat'),'prob','OptimizationStruct','MappingValue','Mapping','DataInfo');
%----------------問題ベースはここまで----------
% 二次制約変数の作成（qcの作成はここ）
% 二次式制約への設定はhttps://www.orsj.or.jp/~archive/pdf/bul/Vol.44_05_237.pdfを参考

%
xVar=OptimizationStruct(1).varIndex;%xVarのθに関する部分やbrImaxを変更
%xVarはvarIndexという関数に帰ってくる変数（xVarの中に上で定義した最適化変数全てが入っている）
xVar.angleline=reshape(xVar.angleline,[Opt.nTime,1,Opt.nPhase]);
xVar.Dummy_Il=reshape(xVar.Dummy_Il,[Opt.nTime,1,Opt.nPhase]);
xVar.Dummy_Ih=reshape(xVar.Dummy_Ih,[Opt.nTime,1,Opt.nPhase]);
xVar.Dummy_anglel=reshape(xVar.Dummy_anglel,[Opt.nTime,1,Opt.nPhase]);
xVar.Dummy_angleh=reshape(xVar.Dummy_angleh,[Opt.nTime,1,Opt.nPhase]);
xVar.B_linecap=reshape(xVar.B_linecap,[Opt.nTime,1,Opt.nPhase]);

xNum=length(OptimizationStruct(1).problem.f);%Xのサイズを知りたい
if exist('qc.mat',"file")==0
    %tic
%以下、初期化
    for iTime=Opt.nTime*1:-1:1 %時間も変更
        qc(iTime).a = sparse(xNum+Opt.nTime,1); %新verではsparse->spdiagsを使うこと
        qc(iTime).Q = sparse(xNum+Opt.nTime,xNum+Opt.nTime);
        qc(iTime).rhs = 0;
    end
    %toc
    save('qc.mat','qc');
    %save('qc.mat','qc','-v7.3');%変数が2GBを超える場合はMATファイルVer7.3以降を使用
else
    load('qc.mat','qc');
end
% tic
% for iTime=1:Opt.nTime
%     qc(iTime).a(xNum+iTime) = -1;
%     qc(iTime).Q(xVar.CgsP(iTime),xVar.CgsP(iTime)) =  1;
% end
% toc
%}
%  
% 正味需要データの作成（マッピング不使用なら最適化設定の前へ）

%if exist('netdemTT.mat',"file")==0
dataTT=Systemdata.Grid.Nodes.dataTT{1};
%dataTT(datetime(2017,11,9):minutes(2):datetime(2017,11,9,23,28,0),:)=[]; %データ欠損
Time=dataTT.Time;

fieldNames={'Pr','Pk','Pb','Qr','Qk','Qb'};

netdemTT=timetable(Time);
for iField=1:length(fieldNames)
    netdemTT.(string(fieldNames(iField)))=zeros(length(Time),nNode);
end

for iNode=1:nNode
   dataTT=Systemdata.Grid.Nodes.dataTT{iNode};

   
   %rtime=timerange(datetime(2017,11,9),datetime(2017,11,10),"openright");
   %dataTT(rtime,:)=[];
    for iField=1:length(fieldNames)
        netdemTT.(string(fieldNames(iField)))(:,iNode)=dataTT.(string("phase"+fieldNames(iField)));
    end
end
netdemTT=retime(netdemTT,'regular','mean','TimeStep',Opt.TimeInfo.dt);
%PVによるパラメータ変更
%{
PVg=1.1;
netdemTT.Pr(:,11)=netdemTT.Pr(:,11)+(PVg-1)*(netdemTT.Pr(:,11)>0).*netdemTT.Pr(:,11);
netdemTT.Pr(:,13)=netdemTT.Pr(:,13)+(PVg-1)*(netdemTT.Pr(:,13)>0).*netdemTT.Pr(:,13);
netdemTT.Pk(:,11)=netdemTT.Pk(:,11)+(PVg-1)*(netdemTT.Pk(:,11)>0).*netdemTT.Pk(:,11);
netdemTT.Pk(:,13)=netdemTT.Pk(:,13)+(PVg-1)*(netdemTT.Pk(:,13)>0).*netdemTT.Pk(:,13);
netdemTT.Pb(:,11)=netdemTT.Pb(:,11)+(PVg-1)*(netdemTT.Pb(:,11)>0).*netdemTT.Pb(:,11);
netdemTT.Pb(:,13)=netdemTT.Pb(:,13)+(PVg-1)*(netdemTT.Pb(:,13)>0).*netdemTT.Pb(:,13);
%}
PVg=1.1;
for iChar=1:nCharger
    netdemTT.Pr(:,Charger.node(iChar))=...
        netdemTT.Pr(:,Charger.node(iChar))+(PVg-1)*(netdemTT.Pr(:,Charger.node(iChar))>0).*netdemTT.Pr(:,Charger.node(iChar));
    netdemTT.Pk(:,Charger.node(iChar))=...
        netdemTT.Pk(:,Charger.node(iChar))+(PVg-1)*(netdemTT.Pk(:,Charger.node(iChar))>0).*netdemTT.Pk(:,Charger.node(iChar));
    netdemTT.Pb(:,Charger.node(iChar))=...
        netdemTT.Pb(:,Charger.node(iChar))+(PVg-1)*(netdemTT.Pb(:,Charger.node(iChar))>0).*netdemTT.Pb(:,Charger.node(iChar));
end

data=netdemTT{:,:};
[row,col]=ind2sub(size(netdemTT{:,:}),find(isnan(data)));
netdem_errorTime=netdemTT.Time(row);
clear data;
% 欠損データの処理
netdemTT=fillmissing(netdemTT,'constant',0);


%{
    save('netdemTT.mat','netdemTT','DataInfo');
else
    load('netdemTT.mat','netdemTT');
end
%}
%% 計算プロセス

resTT=iniResTT;
fvalTT=iniFvalTT;
solTT=iniSolTT;

CalcTime.sDay=tic;
CalcTime.pDay=toc(CalcTime.sDay);

%Lambda=0:0.005:0.1;
%nLambda=length(Lambda);
%lambda=(iLambda-1)*0.005;

nTime=Main.DayLoop.nTime;               
% Result(1:nLambda)=struct('lambda',0,'Ploss',zeros(nTime,nLambda),'charQAbs',zeros(nTime,nLambda),'EssE',zeros(nTime,nLambda),...
%     'resTT',timetable,'resSumaryTT',timetable,'dayTT',timetable,'solTT',timetable,'fvalTT',timetable,'nodeVTT',timetable,'brITT',timetable);

%for iLambda=1:21
   % lambda=Lambda(iLambda)

   for iTime=Main.DayLoop.startTime:Main.DayLoop.dt:(Main.DayLoop.endTime-Opt.TimeInfo.nDay)

        clc;
        
        
        iTime

        
        TimeInfo=MyProgram.Function.simTimeSet(iTime,iTime+days(Opt.TimeInfo.nDay),Opt.TimeInfo.dt,"intervaltime","openright");

% マッピング値の割り当て（3相不平衡はここで）

        %Mapping.netdemIr=struct('nRow',Opt.nTime,'nCol',nNode,'nPage',Opt.nPhase);
        %Mapping.netdemIi=struct('nRow',Opt.nTime,'nCol',nNode,'nPage',Opt.nPhase);
%% 
% 3相不平衡時はrkbと設定
% 
% 3相平衡は今回、rkbで平均をとる
% 
% P_ave=(r,k,b)/3

        netdemTT.P_ave(:,:)=(netdemTT.Pr+netdemTT.Pk+netdemTT.Pb)./3;
        netdemTT.Q_ave(:,:)=(netdemTT.Qr+netdemTT.Qk+netdemTT.Qb)./3;
        netdemTT.Q_ave(:,:)=-abs(netdemTT.P_ave(:,:))*(sqrt(1-0.95^2)/0.95);%3より気持ち多いぐらい目安に。
        %netdemTT.Q_ave(:,:)=0;
        AssingedValue.netdemIr(:,:,1)  = netdemTT.P_ave(TimeInfo.timeRange,:)/(Systemdata.Ref.Vn/sqrt(3));
        AssingedValue.netdemIr(:,:,2)  = netdemTT.P_ave(TimeInfo.timeRange,:)/(Systemdata.Ref.Vn/sqrt(3));
        AssingedValue.netdemIr(:,:,3)  = netdemTT.P_ave(TimeInfo.timeRange,:)/(Systemdata.Ref.Vn/sqrt(3));
        AssingedValue.netdemIi(:,:,1)  = -netdemTT.Q_ave(TimeInfo.timeRange,:)/(Systemdata.Ref.Vn/sqrt(3));
        AssingedValue.netdemIi(:,:,2)  = -netdemTT.Q_ave(TimeInfo.timeRange,:)/(Systemdata.Ref.Vn/sqrt(3));
        AssingedValue.netdemIi(:,:,3)  = -netdemTT.Q_ave(TimeInfo.timeRange,:)/(Systemdata.Ref.Vn/sqrt(3));

        %簡易的な定電力負荷
        %AssingedValue.netdemIrV = -0.1*AssingedValue.netdemIr*1/(Systemdata.Ref.Vn/sqrt(3)*1000);
        %AssingedValue.netdemIiV = -0.1*AssingedValue.netdemIi*1/(Systemdata.Ref.Vn/sqrt(3)*1000);
        
        AssingedValue.sSvrTap(1,:)= resTT.SvrTap(iTime,:);
        AssingedValue.sSvrTap(2,:)=-AssingedValue.sSvrTap(1,:);
        AssingedValue.sLrtTap(1,:)= resTT.LrtTap(iTime,:);
        AssingedValue.sLrtTap(2,:)=-AssingedValue.sLrtTap(1,:);

        %Mapping.sEssE=struct('nRow',1,'nCol',nESS,'nPage',1);
        %Mapping.eEssE=struct('nRow',1,'nCol',nESS,'nPage',1);
        AssingedValue.sEssE=(Ess.kWhCap/2).*ones(1,nEss);%resTT.EssE(iTime,:);%これまでだと容量の半分
        AssingedValue.eEssE=(Ess.kWhCap/2).*ones(1,nEss);%これまでだと容量の半分このままだと最初の時間に放電できなくなる
        
        %外気温と配電線温度初期値
        %AssingedValue.Temp=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);%行数を720になるように配列を設定
        AssingedValue.Temp=linecap-Temp;
        AssingedValue.Anglestart=Ke*resTT.angleline(iTime,:);
        %下限制約で使う三つ
        % MappingValue.DummyIl     A_alpha*Temp+XXX*B_alpha+C_alpha
        % MappingValue.DummyIh     D_alpha*Temp+XXX*E_alpha+F_alpha 
        % MappingValue.binary      (D_beta-A_beta)*Temp+XXX*(E_beta-B_beta)+F_beta-C_beta
        % MappingValue.rhs         -(A_beta*Temp+XXX*B_beta+C_beta)
        XXX=90-Temp;
        %Mapping.DummyIl=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
        AssingedValue.DummyIl=A_alpha*Temp+XXX*B_alpha+C_alpha;
        %Mapping.DummyIh=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
        AssingedValue.DummyIh=D_alpha*Temp+XXX*E_alpha+F_alpha;
        %Mapping.binary=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
        AssingedValue.binary=(D_beta-A_beta)*Temp+XXX*(E_beta-B_beta)+F_beta-C_beta;
        %Mapping.rhs=struct('nRow',Opt.nTime,'nCol',1,'nPage',1);
        AssingedValue.rhs=-(A_beta*Temp+XXX*B_beta+C_beta);
        
        fieldNames=fieldnames(Obj);
        %目的関数は以下で自動化
        for iObj=1:length(fieldNames)
            AssingedValue.(string(fieldNames(iObj))) =10e8; %十分大きい値
        end
        %}

        solTT{iTime,:}=iniSolTT{:,:};
        fvalTT{iTime,:}=iniFvalTT{:,:};

        P(:,1)=sum(netdemTT.Pr(TimeInfo.timeRange,:),2);
        P(:,2)=sum(netdemTT.Pk(TimeInfo.timeRange,:),2);
        P(:,3)=sum(netdemTT.Pb(TimeInfo.timeRange,:),2);
        Q(:,1)=sum(netdemTT.Qr(TimeInfo.timeRange,:),2);
        Q(:,2)=sum(netdemTT.Qk(TimeInfo.timeRange,:),2);
        Q(:,3)=sum(netdemTT.Qb(TimeInfo.timeRange,:),2);
        
        tmp_TT=timetable(TimeInfo.time,P,Q,'VariableNames',{'有効電力','無効電力'});

        x0=[];
        for iObj=1:length(fieldNames)
% 最適化変数へ代入

            problem=MyProgram.OptFunction.problemMappingSet(OptimizationStruct(iObj),AssingedValue);
            problem.x0=x0;
            problem.qc=qc;%qcを設定した場合
% 配電線最大温度制約（上限制約）

%1次%aはベクトル
%xmapの段階では行列と見なされる。ベクトル表記のため1を書く
% 2次近似による上限制約

%任意の1相を指定するor別の変数を作ってIやθが最大となる相を選択
opt_Phaseno=1;
for opt_Brno=1
tt_inc=Opt.nTime*(opt_Brno-1);%opt_numが2のとき、tt_incはsys_sch_tt_max
for sTime=(tt_inc+Opt.nTime):-1:(tt_inc+1)
problem.qc(sTime).a(xVar.Dummy_Il(sTime-tt_inc,opt_Brno,opt_Phaseno),1)=(1-Ke)*(A_alpha*Temp(sTime-tt_inc,1)+C_alpha);
problem.qc(sTime).a(xVar.Dummy_Ih(sTime-tt_inc,opt_Brno,opt_Phaseno),1)=(1-Ke)*(D_alpha*Temp(sTime-tt_inc,1)+F_alpha);
problem.qc(sTime).a(xVar.Dummy_anglel(sTime-tt_inc,opt_Brno,opt_Phaseno),1)=(1-Ke)*B_beta;
problem.qc(sTime).a(xVar.Dummy_angleh(sTime-tt_inc,opt_Brno,opt_Phaseno),1)=(1-Ke)*E_beta;
problem.qc(sTime).a(xVar.B_linecap(sTime-tt_inc,opt_Brno,opt_Phaseno),1)=(1-Ke)*((D_beta-A_beta)*Temp(sTime-tt_inc,1)+(F_beta-C_beta));
%2次%
problem.qc(sTime).Q(xVar.angleline(max(sTime-tt_inc-1,1),opt_Brno,opt_Phaseno) , xVar.Dummy_Il(sTime-tt_inc,opt_Brno,opt_Phaseno))=B_alpha*(1-Ke);
problem.qc(sTime).Q(xVar.angleline(max(sTime-tt_inc-1,1),opt_Brno,opt_Phaseno) , xVar.Dummy_Ih(sTime-tt_inc,opt_Brno,opt_Phaseno))=E_alpha*(1-Ke);
%定数項
problem.qc(sTime).rhs(1,1)=linecap-Temp(sTime-tt_inc,1)-(1-Ke)*(A_beta*Temp(sTime-tt_inc,1)+C_beta);
end
end
%----------ソルバーベースの設定はここまで---------------
% 最適化計算

            
            problem.options.timelimit =40000;   %10分なら600秒         
            problem.options.display ='on'; %不要ならoff
            [x0,fval,exitflag,output] = cplexmiqp (problem)
             if isempty(x0)==0 %エラーが出るとisempty==1
%                 qcproblem.x0=[x0;x0(xVar.CgsP(:)).^2];
%                 [qcx0,qcfval,exitflag,output] = cplexmiqcp (qcproblem);
%                 if isempty(qcx0)==0
%                     AssingedValue.(string(fieldNames(iObj))) =qcfval;
%                     fvalTT{iTime,iObj} =qcfval;
%                     [solTT{iTime,iObj},tmp_TT] = MyProgram.OptFunction.sol2resTT(x0,OptimizationCell(:,iObj),tmp_TT);
%                 else
                    AssingedValue.(string(fieldNames(iObj))) =fval;
                    fvalTT{iTime,iObj} =fval;
                    [solTT{iTime,iObj},tmp_TT] = MyProgram.OptFunction.sol2resTT(x0,OptimizationStruct(iObj),tmp_TT);
                    
                    SVRTAP(:,1)=repelem(x0(xVar.SvrTap(1:144),1),2,1);%x0の8740～8787番目がSvr1、8788～8835番目がSvr2
                    SVRTAP(:,2)=repelem(x0(xVar.SvrTap(145:288),1),2,1);
                    tmp_TT.SvrTap=SVRTAP;
                    tmp_TT.LrtTap=repelem(x0(xVar.LrtTap(1:144),1),2,1);
            % end
            else
                disp(exitflag)%エラーが起きた時の処理　exitflag=〇でcplex参照            
            end
            
            %{
                problem.options.Display ='on';
                problem.options.MaxTime =120;    
                [x0,fval,exitflag,output] = intlinprog_gurobi(problem.f,problem.intcon,problem.Aineq,problem.bineq,problem.Aeq,problem.beq,problem.lb,problem.ub,problem.x0,problem.options);
            %}
            %[x0,fval,sol,exitflag] = OptFunc.solvePythonCplex(problem);
        end

% 結果の格納

        if isempty(x0)==0
            AssingedValue.sSvrTap(2,:)=[];
            AssingedValue.sLrtTap(2,:)=[];
            nameCell={'EssE','sEssE';'SvrTap','sSvrTap';'LrtTap','sLrtTap';'angleline','Anglestart'};
            %nameCell={'EssE','sEssE';'SvrTap','sSvrTap';'LrtTap','sLrtTap';'angleline','Anglestart'};
            %↑最初のθ=45は出てこなかった。そのような変数を指定↑　名前が違うから、変数を結びつけている
            %721個で出てくる。（最初のθは45が出てくる）
            addTT=iniResTT;
            %addTT.LrtTap
            addTT.Time=iTime;
            tmp_TT = MyProgram.Function.TTshift(tmp_TT,addTT,nameCell,AssingedValue,'next');
    
            resTT(TimeInfo.timeRange,:)=[];
    
            resTT = MyProgram.Function.TTvertcat(resTT,tmp_TT);
        end
        %save(fullfile(Main.FolderName.output,'OptResult.mat'),'resTT','fvalTT','solTT');
    end

%resTT(end,:)=[];
%% 計算結果の処理・格納（不要なものは削除）

Time=resTT.Time;
nodeV =reshape( resTT.nodeV_Re,[length(Time),nNode,Opt.nPhase]);
brI =reshape( sqrt(resTT.brI_Re.^2+resTT.brI_Im.^2),[length(Time),nBr,Opt.nPhase]);
Vol =reshape( sqrt(resTT.nodeV_Re.^2+resTT.nodeV_Im.^2),[length(Time),nNode,Opt.nPhase]);
Vol = (Vol*sqrt(3))/6600;
resTT.brI =sqrt(resTT.brI_Re.^2+resTT.brI_Im.^2);
resTT.Vol =sqrt(resTT.nodeV_Re.^2+resTT.nodeV_Im.^2);
%resSumaryTT=resTT(:,["有効電力","無効電力","SvrTap","LrtTap","EssE","charQInj"]);
resSumaryTT=resTT(:,["有効電力","無効電力","EssE","brI_Abs","angleline","anglemax","brI","Vol","SvrTap","LrtTap"]);

%resSumaryTT.Ploss=sum(sum(Systemdata.Grid.Edges.R'.*ones(length(Time),nBr,Opt.nPhase).*resTT.brI.^2, 2),3);
resSumaryTT.P =resTT.charPCh -resTT.charPDch;%+-を入れ替えて正を充電側、負を放電側にした。
resSumaryTT.Q =resTT.charQInj;
resSumaryTT.S_kVA =sqrt(resSumaryTT.P.^2+resSumaryTT.Q.^2);
needE_kWh =max(resSumaryTT.EssE)-min(resSumaryTT.EssE);
needE_kVA =max(resSumaryTT.S_kVA);
ESSObj=needE_kWh+needE_kVA;
%save('result_0201_DR.mat','resTT','resSumaryTT','fvalTT','solTT','needE_kWh','needE_kVA');
save('Result_0722_pv(11,13)_Br1(1.1!)DR.mat','resTT','resSumaryTT','fvalTT','solTT','needE_kWh','needE_kVA');
%nodeVTT=timetable(Time,nodeV(:,:,1),nodeV(:,:,2),nodeV(:,:,3));
%brITT=timetable(Time,brI(:,:,1),brI(:,:,2),brI(:,:,3));

%dayTT=retime([resSumaryTT(:,["有効電力","無効電力","Ploss"]),resTT(:,["charQAbs"])],'daily','sum');
%dayTT{:,:}=dayTT{:,:}*Opt.hourDT*1e-6; % M換算

%tapNumTT=retime(resTT(:,["SvrTapC","LrtTapC"]),'daily','sum');
%dayTT=[dayTT,tapNumTT];
%{
EssEDay=[];
for iDay=Time(1):days(1):Time(end)
    cellA=solTT.minLoss(iDay);
    EssEDay=[EssEDay;cellA{1}.EssE(end,:)];
end
dayTT.EssE=EssEDay;
%}
%save(fullfile(Main.FolderName.output,'OptResultSummary.mat'),'resSumaryTT','dayTT');


% Result(iLambda)=struct('lambda',lambda,...
%     'Ploss',dayTT.Ploss,'charQAbs',dayTT.charQAbs,'EssE',dayTT.EssE,...
%     'resTT',resTT,'resSumaryTT',resSumaryTT,'dayTT',dayTT,'solTT',solTT,'fvalTT',fvalTT,'nodeVTT',nodeVTT,'brITT',brITT);

%save(fullfile(Main.FolderName.output,'Result.mat'),'Result');
%end