function gitpush()
% GITPUSH この関数の概要をここに記述
%   詳細説明をここに記述
% 現在の警告状態を保存
warning('off', 'all');
% ステージング
system('git add .');

% コミットメッセージの取得
commitMessage = input('Enter commit message: ', 's');
pushBranch = input('Enter branch name: ', 's');

% コミット（メッセージにスペースが含まれる場合に対応するため、シングルクォートで囲む）
system(['git commit -m "' commitMessage '"']);

% プッシュ
system(['git push origin "' pushBranch '"']); 
fprintf('origin/%s に全ての変更をpushしました\n',pushBranch);
end