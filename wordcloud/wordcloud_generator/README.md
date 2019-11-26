# 概要

wordcloudを生成するアプリ

# 使い方

1. flaskアプリを起動する
1. 入力欄に文章を入力してボタンをクリックする
1. ダウンロードフォルダに保存される画像を開いて確認する

- flaskアプリの起動は以下のコマンドを実行
	- ```python app.py```

# 設定

- 最大入力文字数は、以下で設定する
	- ```flaskr/config.py```の```MAX_CONTENT_LENGTH```
- 除外したい単語は、以下で設定する
	- ストップワード：```flaskr/config.py```の```STOP_WORDS```
	- 正規表現：```flaskr/config.py```の```RE_ALPHABET```
