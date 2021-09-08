import requests
import subprocess
import sqlite3
import datetime
import socket
header={"X-ApiKeys": "accessKey=4e8b198bff5fbcffeceb4724787bca36ff1759a35ba73ba4e84bdc31345cce35; secretKey=85a22a8376d2dd6e5d798"}
cikti=subprocess.check_output("dir",shell=True)
if not "host_dicovery.db" in str(cikti):
    print("veritabanı yok")
    conn = sqlite3.connect('host_discovery.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE host(ip text,zaman text''')
    c.close()
conn = sqlite3.connect('host_discovery.db')
c = conn.cursor()
c.execute('SELECT ip FROM hosts')
ipler=c.fetchall()
ipler_liste=[]
for i in ipler:
    ipler_liste.append(str(i[0]))
conn.close()
url="https://127.0.0.1:8834/scans"
sonuc=requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()['scans']:
    if "HD" in i['name'] and "completed" in i['status']:
        url="https://127.0.0.1:8834/scans/"+str(i['id'])
        sonuc.requests.get(url=url,headers=header,verfy=False)
        for j in sonuc.json()['hosts']:
            if not j['hostname'] in ipler_liste:
                print("Yeni İP",j['hostname'])
                conn=sqlite3.connect('host.discovery.db')
                c.execute(('INSERT İNTO hosts VALUES(?,?)',str(j['hostname']),str(datetime,datetime.now())))
                conn.close()
                s=socket.socket()
                s.connect(("10.10.10.10",515))
                log="yeni ip bulundu"+str(j['hostname'])
                s.sendall(str(log).encode())
                s.close()