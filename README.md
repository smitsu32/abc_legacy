# abc_legacy
ABCでの自分の過去回答を管理するリポジトリ


## VSCodeとGitHubの紐づけがうまくいかないときは
1. gitインストール（portableじゃない方）、Git Bashにて
   ` git config --global user.name , user.email `
   で初期設定する
1. Git Bashで
   `where git`
   を実行し、結果をコピー
1. Win10/11の環境設定でPathの"編集"→2.を"新規"
1. GitHubでリモートリポジトリ作成（右上＋）
1. VSCodeでローカルリポジトリ作成 (ソース管理->リポジトリの初期化)
1. VSCodeで
   `git remote add origin (url)`
   と入力することで

   VSCode変更  -> ローカルへ<br>
   プッシュ -> ローカルからリモートへ

## .gitignoreが認識されないとき
1. BashかPowershellに以下のコードを入力してキャッシュを削除
   `git rm --cashed file.name`
