import requests
import subprocess
import datetime
import sqllite3
cikti=subprocess.check_output('dir',shell=True)
if not "port.db" in str(cikti):
    conn = sqllite3.connect('port.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE portlar(port text, p text, zaman text)''')
    c.close()
header={"X-ApiKeys": "accessKey=4e8b198bff5fbcffeceb4724787bca36ff1759a35ba73ba4e84bdc31345cce35; secretKey=85a22a8376d2dd6e5d798"}
url="https://127.0.0.1:8834/scans"
sonuc=requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()['scans']:
    scan_id=i['id']
    url="https://127.0.0.1:8834/scans/"+str(scan_id)
    sonuc=requests.get(url=url,headers=header,verify=False)
    for j in tarama.json()['hosts']:
        try:
            host_id=j['host_id']
            #14272 açık portları gösteriyor
            url = "https://127.0.0.1:8834/scans/"+str(scan_id)+"/host/"+str(host_id)+"/plugins/11219"
            IP=requests.get(urk=url,headers=header,verify=False)
            for k in IP.json()['outputs']:
                port=list(k['ports'].keys())[0]
                IP=j['hostname']
                conn = sqllite3.connect("port.db")
                c=conn.cursor()
                cikti=c.execute('select * from portlar where port=? and ip=?',(port,IP))
                port_sayisi=len(cikti.fetchall())
                conn.close()
                if port_sayisi<1:
                    print("Yeni port:",port"IP:",IP)
                    conn=sqllite3.connect("port.db")
                    c=conn.cursor()
                    conn.commit()
                    conn.close()
        except:
            pass