#開発環境*
* OS: windows7 32bit
* Python Version: 3.4.3

#実行方法
python *.py input_filename output_filename 繰り返し回数  
上記コマンドの引数の数を適宜変更する
#ファイル説明

* 01_File_row_counter:  
引数で指定したファイルの行数を数える

* 02_Subst_tab2blank:  
引数で指定したファイルのタブを空白に置き換える  
  
* 03_pick_up_col1_col2:  
引数で指定したファイルの1列目と2列目を別ファイルに格納する
  
* 04_join_two_col:  
2つファイルの1列目を結合し新たなファイルを作成する
  
* 05_display_top_N:  
引数で指定した数だけファイルの上からファイルに書き出す
  
 *06_display_tail_N:  
引数で指定した数だけファイルの下からファイルに書き出す
  
* 07_col_counter:  
1列目の各行の文字列の数をコンソール上に表示する
  
* 08_col2_sort:  
引数で指定したファイルの2列目をソートしたものをファイルに書き出す
  
* 09_col2_col1_sort:  
引数で指定したファイルの1列目,2列目の順にソートしたものをファイルに書き出す
  
* 10_col2_counter:  
03_pick_up_col1_col2で作成したcol2.txtの文字列の出現頻度を求め出現頻度が高い順にソートしたものをファイルに格納する
