import requests
import json
import time
from datetime import datetime, date
from dateutil.relativedelta import relativedelta, WE, FR
#Import built libraries
import piket_minggu
import piket_randomizer
import isi_pesan

#WhatsApp Sender API
api = ''
sender = 0
target = 0
url = ''
days_use = [2,4,6]

def wasender(msg):
    data = {
        'api_key' : api,
        'sender' : sender,
        'number' : target,
        'message' : msg,
     }
    headers = {'Content-Type' : 'application/json'}
    response = requests.post(url,data=json.dumps(data),headers=headers)

nama_rabu = {}
nama_jumat = {}
with open('daftar_nama/nama_jumatOri.txt','r') as r_nama:
    for lines in r_nama:
        line = lines.strip("\n").split(":")
        nama_jumat[line[0]] = line[1]
with open('daftar_nama/nama_rabuOri.txt','r') as r_nama:
    for lines in r_nama:
        line = lines.strip("\n").split(":")
        nama_rabu[line[0]] = line[1]

today_WE,nextweek_WE = 0,0
today_FR,nextweek_FR = 0,0
# 2 4
# def denda(names):
#     nama,denda,tanggal = names,[],[]
#     data = {
#         "nama" : nama,
#         "denda" : [],
#         "tanggal" : []
#     }

def is_nextweek(day=None):
    if day == days_use[0]:
        today_WE = date.today()
        nextweek_WE = today_WE + relativedelta(weekday=WE(2))
        return "wed"
    elif day == days_use[1]:
        today_FR = date.today()
        nextweek_FR = today_FR + relativedelta(weekday=FR(2))
        return "fri"

print("Program is running...")
while True:
    today_date = datetime.now().weekday()
    if is_nextweek(today_date) == "wed" and datetime.today().second == 1:
        from daftar_nama.name_splitter import r_rabu
        acak_rabu = piket_randomizer.acak(r_rabu)
        wasender(isi_pesan.isi_pesan(is_nextweek(today_date),list(acak_rabu.values()),nama_rabu))
        time.sleep(5)
    elif is_nextweek(today_date) == "fri" and datetime.today().second == 1:
        from daftar_nama.name_splitter import r_jumat
        acak_jumat = piket_randomizer.acak(r_jumat)
        wasender(isi_pesan.isi_pesan(is_nextweek(today_date),list(acak_jumat.values()),nama_jumat))
        time.sleep(5)
    if today_date == 6:
        if piket_minggu.piket_minggu() == True:
            wasender("Saatnya Piket Rutin Minggu!")
