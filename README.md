# Online Boutiqueへの負荷試験とグラフ作成の自動化
## 概要
Google-CloudPlatformがデモアプリケーションとして公開しているOnline Boutiqueの各マイクロサービスに対するシェルスクリプトを用いたコマンド．負荷試験を行い，そこから得たデータから最大応答時間と毎秒あたりのリクエスト量の関係を表すグラフを作成する．
## 使用方法
```
$ bash lgra
```

## 出力結果
左の縦軸が最大応答時間，右の縦軸が毎秒あたりのリクエスト量を表し，横軸はタイムスタンプである．
![product_graph_data](https://user-images.githubusercontent.com/68373166/212017736-58099a1c-6dfa-4de4-bda4-c3b06e0bf9bf.png)
