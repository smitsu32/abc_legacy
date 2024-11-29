function  addpath()
%ADDPAH この関数の概要をここに記述
%   詳細説明をここに記述
nowDir = genpath(pwd);
addpath(nowDir);
fprintf('addpath: %s\n', pwd);
end