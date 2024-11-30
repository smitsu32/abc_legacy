function  addpath()
%ADDPAH この関数の概要をここに記述
%   詳細説明をここに記述
    currentFolder=pwd;
    addpath(genpath(currentFolder));
    fprintf('%s をパスに追加しました\n', currentFolder);

end