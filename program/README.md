# IoT
# 1．このスクリプトファイルについて

pythonによるgmail送信を可能とするファイルです．
主に，異常検知をした際のアラーム機能としての利用を目的として編集しました．
その他にも使えるかと思いますので，利活用してください．

# 2．使用方法について

メインファイルに対して
'''bash
import mail
'''
を記載する．

次に，メールを送信したい箇所に
'''bash
mail.mail(宛先メールアドレス,送信するgmailアカウント,件名,本文,ファイルパス)
'''
を記載する．

メインファイルを実行するとメールが送信される．

# 3．説明例

1行目

```bash
print("Hello World")
```

Hello Worldを変更すると出力される内容が変更される

# Note

注意点など

# 参考文献

各スクリプトの説明文に記載

# Author

作成情報を列挙する

* 作成者
* 所属
* E-mail

# License
ライセンスを明示する

"hoge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

社内向けなら社外秘であることを明示してる

"hoge" is Confidential.
