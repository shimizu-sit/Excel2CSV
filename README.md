# Excel2CSV
このリポジトリは，自分が使っている成績管理用Excelから大学の成績システムに成績入力をするためのCSVを生成するプログラムです．

なので，とても個人的なものであって，一般的には使えません．

## プログラムの内容

成績システムに成績を登録する方法は，手入力による登録とCSVファイルによる登録があります．
手入力は時間がかかるうえ，ミスを招き大きな問題になる可能性がある基本使わないです．
なので，CSVファイルによる登録をすることになります．

成績システムが要求するCSVファイルのフォーマットは `学籍番号, 成績` となっていて全体的には以下のようになります．
（もしかすると，他のフォーマットもあるのかもしれない）

```CSV
学籍番号, 成績
xxAxxxx, xx
xxAxxxx, xx
xxAxxxx, xx
：
xxAxxxx, xx
```

1行目は必要ない（あってもシステムは無視します）ですが，個人的にあった方がいいのでつけてます．

Excelファイルの中身はいかのようになっています．
プログラムは，Excelファイルの「Result」シートの2列目（B列）の「学籍番号」と13列目（M列）の「最終評価」の値をコピーしてCSVファイルに書き出すというものになります．

![Excel](/images/Excel.png)
