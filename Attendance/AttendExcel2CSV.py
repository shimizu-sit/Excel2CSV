import os
import pandas as pd

# 作業フォルダへのパスを設定
path = '/content/drive/MyDrive/01_LectureNotes/2024-1st-SCfCL/Attendance/'

# Excelファイルの読み込み
excel_file = 'jbxl_download_20240513104524.xlsx'  # 読み込み対象のExcelファイル名を指定

# データフレームとしてExcelファイルの内容を読み込む
df = pd.read_excel(path + excel_file)

# L列に「出」と書かれている行をフィルタリング
filtered_df = df[df[11] == '出']

# フィルタリングされた行のC列の値を取得
c_values = filtered_df['C']

# CSVファイルに書き出し
c_values.to_csv('output.csv', index=False, header=False)
