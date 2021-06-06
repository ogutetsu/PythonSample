import pandas as pd

url = "https://info.finance.yahoo.co.jp/ranking/?kd=45"
df = pd.read_html(url)

url2 = "https://info.finance.yahoo.co.jp/ranking/?kd=4"
df2 = pd.read_html(url2)


df[0][["順位","コード","市場","名称","平均年収（千円）","従業員数（単独）"]]
df[0].to_csv("IOFiles/ranking.csv", encoding="UTF-8")

with pd.ExcelWriter("IOFiles/ranking.xlsx") as writer:
    df[0][["順位","コード","市場","名称","平均年収（千円）","従業員数（単独）"]].to_excel(writer, encoding="UTF-8", sheet_name="平均年収ランキング")
    df2[0].to_excel(writer, encoding="UTF-8", sheet_name="時価総額ランキング")

