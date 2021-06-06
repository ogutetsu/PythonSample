import gspread

# Google APIの取得が必要
# ダウンロードした鍵(JSON)は、ユーザー名/AppData/Roaming/gspread/service_account.json
# で保存する

gc = gspread.service_account()
sh = gc.open("test")

print(sh.sheet1.get('A1'))

