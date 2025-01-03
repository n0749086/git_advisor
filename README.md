# git_advisor
## これなに
[こちらの記事](https://recruit.gmo.jp/engineer/jisedai/blog/ai-gitcommit-message-codereview/)の内容を元に、機能修正したもの

## 開発環境
* **OS:** Windows 11
* **Python:** 3.11以上 (推奨: 3.13.1)
* **必要なライブラリ:**  `requirements.txt`を参照してください。

## インストール手順
1.  `git clone <repository_url>` でリポジトリをクローンします。
2.  `pip install -r requirements.txt` で必要なライブラリをインストールします。
3.  .envファイルを作成して下さい。

### .envファイル
以下の２項目について記載して下さい。
- LLM: 使用するLLM(GPTもしくはGemni)
- API_KEY: LLMのAPIキー
- ENDPOINT: APIのエンドポイント(**AzureOPenAIのみ**)

```
LLM=GPT
API_KEY=test
ENDPOINT=hogehoge
```

## 使い方
```bash
python git_advisor.py <オプション>
```
オプションは、以下から選択可能です。
- commit: diffの内容を元に、コミットメッセージの作成を行います
- review: diffの内容を元に、コードレビューを行います
