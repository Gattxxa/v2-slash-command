# v2-slash-command
[![](https://img.shields.io/badge/discord.py-v2.0.0α-informational?logo=python&logoColor=1da1f2)](https://www.python.org/)  
discord.py-v2 を使用したスラッシュコマンドの実装  
- ギルドコマンド
- グローバルコマンド
- サブコマンドを使用したコマンド
- オプション(引数)を使用したコマンド

discord.py v2.0に関する知見は[ここ](https://scrapbox.io/a-lot-of-cafsan/discord.py)に書いてます。  


## 📝 Requirements
開発バージョンである `v2.0.0a` を使用します。  
正式リリースされた後は、最新版のものを使用することを推奨します。
```
$ git clone https://github.com/Rapptz/discord.py
$ cd discord.py
$ python3 -m pip install -U .[voice]
```
https://github.com/Rapptz/discord.py#installing


## 🔧 Expand / Customize
拡張する場合、引数`ctx`に渡される型が[Interaction](https://discordpy.readthedocs.io/ja/latest/interactions/api.html#interaction)であることに注意してください。
そのほか、単純に`v2.0`移行時にいくつかの変更が行われています。
https://discordpy.readthedocs.io/ja/latest/migrating.html
