function gitpush(commitMessage)
%GITPUSH この関数の概要をここに記述
%   詳細説明をここに記述
% コミットメッセージを生成
% commitMessage = sprintf('コミットメッセージを入力: "%s"', commitMessage);
% pushRepository = sprintf('ブランチ名(main:1,branch:2):"%s"', pushRepository);

% ステージング
system('git add .');

% コミット
system(['git commit -m ' commitMessage]);

% プッシュ
system('git push origin main') % ブランチ名がmainの場合、適宜変更してください
end