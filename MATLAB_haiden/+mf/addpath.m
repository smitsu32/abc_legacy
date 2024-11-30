function  addpath()
%ADDPAH この関数の概要をここに記述
%   詳細説明をここに記述
[currentFolder, ~, ~] = fileparts(mfilename('fullpath');
addpath(currentFolder);
fprintf('%s をパスに追加しました\n', pwd);
end