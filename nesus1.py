import requests
import subprocess
header={"X-ApiKeys": "accessKey=4e8b198bff5fbcffeceb4724787bca36ff1759a35ba73ba4e84bdc31345cce35; secretKey=85a22a8376d2dd6e5d798"}
url="https://127.0.0.1:8834/scans"
sonuc=requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()["scans"]:
    print(i["id"])  #scan_id=i["id"]
    url="https://127.0.0.1:8834/scans/"+str(i[id])
    sonuc=requests.get(url=url,headers=header,verify=False)
    for i in sonuc.json()["hosts"]:
        try:
            IP=i["hostname"]
            host_id=["host_id"]
            print(IP)
            print(host_id)
            print("============")
            url="https://127.0.0.1:8034/scans/"+str(scan_id)+"/hosts/"+str(host_id)+"/plugins/11936"
            zafiyet=requests.get(url=url,headers=header,verify=False)
            plugin_output=zafiyet.json()['outputs'][0]['plugin_output']
            print(plugin_output)
            if "Windows" in plugin_output:
                dizin=subprocess.check_output("dir",shell=True)
                print(dizin)
                if not "windows.txt" in str(dizin):
                    veri=str(IP)+"\n"
                    dosya=open("windows.txt","w")
                    dosya.write(veri)
                    dosya.close()
                dosya=open("windows.txt","r")
                IP_kontrol=dosya.read()
                dosya.close()
                if not str(IP) in IP_kontrol:
                    veri=str(IP)+"\n"
                    dosya=open("windows.txt","a")
                    dosya.write(veri)
                    dosya.close()
        except:
            pass