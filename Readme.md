NCDscraper
====

NCDから自分の経験症例を抽出するためのスクリプトです。基本的には一般外科医 (消化器外科・小児外科・心臓血管外科・呼吸器外科・乳腺外科) のためのものですが、少し改良すればNCDのシステムを採用している循環器内科医・泌尿器科にも応用できるかもしれません。

# 開発経緯
今までの自分の経験症例数を算出する必要があったのですが、一般外科医であれば、自分の登録症例はすべてNCDに登録されていると思います。[NCD検索システム](https://user.ncd.or.jp/member/memberLogin.html)にアクセスすればいいのですが、ここで大きな問題が。手術症例数の件数表示は、施設別、術式別、術者別に一覧表示できるのですが、

* 施設・術者・術式の複数を組み合わせたフィルタリングができない
* 手術は20件ずつ表示されて、それ以上の設定はできない
* もちろん`.csv`での一括ダウンロードなんてもっての他

という仕様になっていました。さすがに手間がかかりすぎるので、Sleniumでscrapingすることにしました。Seleniumとは一言で言ってしまえば、自動でブラウザを操作する為のライブラリということです。

# Requirement
* macOS Mojave+: 他のOSには対応できていません
* Python 3.6+
* Google Chrome
* Selenium
* ChromeDriver

セットアップについては拙ブログ[ (Note of Pediatric Surgey) ](https://www.pediatricsurgery.site/)の[SeleniumとPythonでスクレイピングをやるために必要な準備](https://www.pediatricsurgery.site/entry/2019/12/15/143053)という記事にまとめてあります。

# Usage
1. `Markshee/PDF_Input`のフォルダにスキャンしたPDFファイルを移動させておく (複数のPDFファイルでもOK)
2. `ターミナル`を起動
3. `clone`もしくはダウンロードしたこのレポジトリがあるディレクトリに移る

```bash
cd "ディレクトリ名"/Marksheet
```

4. `Marksheet.py`を実行する (Python 2.7)
```
python Marksheet.py
```

5. CSV_OutputにCSVファイルが生成されていることを確認する

# Licence
以下の条件を満たす限り、自由な複製・配布・修正を無制限に許可します。
* 上記の著作権表示と本許諾書を、ソフトウェアの複製または重要な部分に記載する
* 本ソフトウェアは無保証である。自己責任で使用する。

詳しくは`License.md`を参照ください。

# Recommendation
Python初心者の方で、インストールやプログラムの内容などの理解が足りない方は下記のブログ記事が役に立つかもしれません。
* [PythonとOpenCVで簡易OMR（マークシートリーダ）を作る](https://qiita.com/sbtseiji/items/6438ec2bf970d63817b8)
* [Python初心者がnumpyとOpenCVをインストールするためにしたこと](https://www.pediatricsurgery.site/entry/2018/12/24/130442)
* [【PythonとOpenCVで簡易OMR(マークシートリーダ)を作る】を初心者が理解するために①](https://www.pediatricsurgery.site/entry/2018/12/24/154519)
* [【PythonとOpenCVで簡易OMR(マークシートリーダ)を作る】を初心者が理解するために②
Python](https://www.pediatricsurgery.site/entry/2018/12/25/231014)
* [【PythonとOpenCVで簡易OMR(マークシートリーダ)を作る】を初心者が理解するために③](https://www.pediatricsurgery.site/entry/2018/12/29/195859)

# Acknowledgments
[PythonとOpenCVで簡易OMR（マークシートリーダ）を作る](https://qiita.com/sbtseiji/items/6438ec2bf970d63817b8)  
基本的にはこのマークシートは[@sbtseiji](https://qiita.com/sbtseiji)さんの記事を参考にして作らせていただきました。本当にありがとうございます。

# Update
* Python 3系への移行
* ERRORをcsvに加えられるようにする
* DateとIDそれぞれで
* Area_sumが閾値以下しかない->unmarked
* Area_sumが大きいものが2つ->max*0.9->duplication?