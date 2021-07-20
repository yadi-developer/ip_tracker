# coded by Yadi

from requests import Session, get
import json
# s = Session()

ip = input("Target ip : ")
url = f"https://www.komoot.com/api/geoip/json/{ip}"

response = get(url)

j = response.json()

def check(js):
    if js['zip_code']:
         return print(f'Kode pos ditemukan : {js["zip_code"]}')
    else:
        return print(f"Kode pos tidak ditemukan!")
    pass


title = '''
      Ip tracker By Yadi x Niko
'''
pos = check(j)
ip = f" {title}Hasil dari pelacakan ip : {j['ip']} \nTarget tinggal di negara : {j['country_name']} | {j['country_code']} \nProvinsi : {j['region_name']} | {j['region_code']} \nKota : {j['city']} \nZona waktu : {j['time_zone']} \nlatitude: {j['latitude']} | longitude {j['longitude']}"
print(ip)
print(pos)

f = open('result.txt', 'a')
f.write(ip)
f.close()
