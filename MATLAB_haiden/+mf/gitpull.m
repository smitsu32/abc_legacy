function gitpull()
%GITFETCH この関数の概要をここに記述
%   詳細説明をここに記述
system('git fetch')
system('git pull')
fprintf('全ての変更をプルしました\n')
end

