Source: https://docs.slack.dev/ja-jp

# 日本語のドキュメント

日本の開発者の皆さん、こんにちは！こちらのページでは、日本語のドキュメントをカテゴリー別にご紹介します。まだ日本語で提供されていないページも多いのですが、こちらでお探しの情報が見つかれば幸いです。

### Qiita {#qiita}

日本語での最新情報の提供やチュートリアルなどは、主に Qiita で公開しています。

### Bolt は Slack アプリ開発のための公式フレームワークです。 {#bolt-は-slack-アプリ開発のための公式フレームワークです}

*   [JavaScript (Node.js)](/tools/bolt-js/ja-jp/getting-started)
*   [Python](/tools/bolt-python/ja-jp/getting-started)
*   [Java](/tools/java-slack-sdk/ja-jp/)

## 最新情報 {#latest_news}

[**非 Marketplace アプリのレート制限の変更**](/ja-jp/2025-05-terms-rate-limit-update-and-faq)

## チュートリアル {#tutorials}

リンク

[**新機能、アプリのホーム・ヴューを活用しよう🏡**](https://qiita.com/tomomi_slack/items/fae66bcc2ec3ccf25db6)。 大事な情報を付箋に書いて App Home に貼り付けるアプリの紹介です。

[**Slack メッセージ・ショートカット API を使ってディスカバラブルなアプリを作ろう**](https://qiita.com/tomomi_slack/items/21fedcc6ce07aa44a670) - ショートカットを活用して、メッセージを保存するアプリを作ってみませんか？

[**Block Kit を使ってより情報的なレストラン検索コマンドを作ろう**](https://qiita.com/tomomi_slack/items/2254183edf9277455c51)。 アプリが送信する情報を Block Kit の利用でもっと綺麗かつ清楚なメッセージの作り方を学びましょう。

[**Bolt フレームワークを使って Slack Bot を作ろう**](/tools/bolt-js/ja-jp/getting-started/)。 Bolt を使って Hello, world! のアプリを作りましょう！

## 権限 (スコープ) {#permissions}

Slack プラットフォームを利用するために必要となる権限（スコープ）と、アプリをその権限が付与された様々なトークンの概要や利用方法について解説する記事です。トークンの発行方法、権限の管理方法を理解することが Slack アプリ開発の最初のステップです。

リンク

[**Slack API のトークンローテーション完全ガイド**](https://qiita.com/seratch/items/610c14208772d49ac9e4)。ボットトークン、ユーザートークンでサポートされている refresh token はデフォルトでは有効になっていません。有効にする場合は、英語の公式ドキュメントに加えて、こちらの日本語での詳細なガイドも参考にしてみてください。

[**トークンの種類 (英語)**](/authentication/tokens)。アプリの一番ふさわしいトークンを見つけましょう。

[**スコープ一覧 (英語)**](/reference/scopes)。プラットフォームを利用するために必要となる権限（スコープ）の一覧です。それぞれのスコープの権限が付与されるトークンの種別が異なることにご注意ください。

## API {#api}

リンク

[**Slack アプリでのモーダルの使い方完全ガイド**](https://qiita.com/seratch/items/0b1790697281d4cf6ab3)。 Slack アプリでエンドユーザーからの情報送信を受け付けたり、インタラクティブなインタフェースを提供するために利用できる「モーダル」の完全ガイドです。

[**Slack ソケットモードの最も簡単な始め方**](https://qiita.com/seratch/items/1a460c08c3e245b56441)。 公式の Bolt フレームワークを使ってソケットモードを利用するためのチュートリアルです。JavaScript (Node.js)、Python、Java、Kotlin での利用法をコード例とともに解説しています。

[**Slack ソケットモードの最も簡単な始め方 (Go 編)**](https://qiita.com/seratch/items/c7d9aeb60ead5c126c01)。 コミュニティで開発されている Go の Slack SDK を使ってソケットモードを利用する方法の解説です。

[**Web API メソッド一覧 (英語)**](/reference/methods)。公開されている Web API の一覧です。パラメーターや応答例などの詳細はリンク先の詳細ページを参考にしてください。

[**Events API の概要 (英語)**](/apis/events-api/)。あらかじめ指定しておいたイベントが Slack 内で発生したときにあなたの Slack アプリに通知してくれる API です。

[**Events API のイベント一覧 (英語)**](/reference/events)。Events API で利用できるイベントの一覧です。イベントのペイロードの詳細などはリンク先の詳細ページを参考にしてください。

[**ソケットモード (英語)**](/apis/events-api/using-socket-mode)。公開された URL ではなく、アプリ側からの WebSocket での接続で Slack プラットフォームと双方向通信するための方式です。

## SDK とツール {#sdk_tools}

リンク

[**Bolt 入門ガイド (JavaScript)**](/tools/bolt-js/ja-jp/getting-started)。三つの対応言語のうち、最初にリリースされた Slack アプリ開発フレームワークであり、最も広く利用されています。

[**Bolt 入門ガイド (Python)**](/tools/bolt-python/ja-jp/getting-started)。Python 開発者向け向けの Slack アプリ開発フレームワークです。Bolt for JS のデザインを踏襲しながらも、Python らしくデコレーターを用いてリスナーを定義できるようになっています。また、全ての主要な Web フレームワークや asyncio への対応も備えています。

[**Bolt 入門ガイド (Java)**](/tools/java-slack-sdk/ja-jp/)。Java や Kotlin などの JVM で動作する言語の開発向けの Slack アプリ開発フレームワークです。Java を多く利用する企業や組織を中心に利用されています。Kotlin では[簡単に Block Kit のデータを定義できる DSL](/tools/java-slack-sdk/ja-jp/guides/composing-messages#block-kit-kotlin-dsl) も提供しています。

[**Python Slack SDK**](https://qiita.com/seratch/items/8f93fd0bf815b0b1d557)。全ての機能（Web API、Incoming Webhooks、リクエスト署名、ソケットモード、Audit Logs API、SCIM API、OAuth フロー、RTM）をサポートしている Python SDK です。

[**Slack が提供する GitHub Action "slack-send" を使って GitHub から Slack に通知する**](https://qiita.com/seratch/items/28d09eacada09134c96c)。 GitHub Action である "slack-send" の使い方を日本語で提供しています。

[**Block Kit Builder を使ってインタラクティブな Slack アプリをプロトタイピングしよう**](https://qiita.com/seratch/items/628751be65de9eb23a80)。 Block Kit Builder の操作の仕方を説明する記事です。

## App ディレクトリ {#app_directory}

どんなワークスペースでもすぐに試せる公開 Slack アプリを 2,500 以上集めた [App ディレクトリ](https://slack.com/marketplace) には、Slack が定める基準を満たせば、誰でもアプリを公開することができます。その提出に必要なものや注意点については以下の記事を参考にしてください。

リンク

[**Slack App ディレクトリにアプリを提出しよう**](/ja-jp/submitting-apps-to-the-directory)。ディレクトリ審査チームが公開したガイドの日本語翻訳です。まずこちらをお読みください。

[**App ディレクトリのチェックリスト・最新版**](/ja-jp/directory-submission-checklist)。App ディレクトリに提出時に確認する必要があるチェックリストの日本語翻訳です。アプリ開発の企画時の検討内容にも含めるようにしてください。

* * *

## アーカイブ {#archive}

ここに掲載されている記事は、新しい機能の利用が推奨されていたり、廃止された機能に関する内容を含むものです。旧来の機能について知る必要がある場合のみ参考にするようにしてください。

リンク

[必要な Slack API はどれ？ - Slack アプリの作成のためのヒント](https://qiita.com/shaydewael/items/f8fdebf22e39410c50d0)

[スケーラブルな Slack アプリ開発: API レート制限の処理](https://qiita.com/shaydewael/items/b273398f4459098dc446)