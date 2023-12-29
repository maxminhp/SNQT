import os
import pandas as pd


def Chg_sample(file_txt, file_xlsx,dump=0):
    filename = file_txt
    filename2 = file_xlsx
    file_out = os.path.splitext(filename)[0] + "_out" + os.path.splitext(filename)[1]
    ext_name = os.path.splitext(filename)[1]
    df = pd.read_csv(filename, encoding="gbk", names=["SampleNo", "Name", "Val", "Sr"])
    df_exam = pd.read_excel(
        filename2, engine="openpyxl", usecols=[4, 5, 6, 7, 9], index_col=0
    )
    df_exam_idx = df_exam.groupby(df_exam.index).first()
    for val in df_exam_idx.index:
        row = df_exam.loc[val]
        bar_code = row.iloc[0]
        df["SampleNo"].replace(val, bar_code, inplace=True)
    if dump == 1:
      try:
         df.to_csv(file_out, index=False, header=False,encoding="utf-8-sig")
         df_result= file_out +'文件生成！'
      except PermissionError:
         df_result='导出文件被占用,请先关闭该文件!'
      except Exception as e:
          df_result='出现错误！错误信息：' + e
      return df_result
    elif dump == 0:
        return df

if __name__ == "__main__":
    Chg_sample()
