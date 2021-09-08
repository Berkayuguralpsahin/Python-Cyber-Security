import requests
dosya=open("fuzzing.txt","r")
icerik=dosya.read()
dosya.close()
header={"Cookie":"security=low: PHPSESSID=a8b29e43b154e8cf261c3686bdd94"}
for i in icerik.split("\n"):
    print(i)
    url="http://10.10.10.10"+str(i)
    sonuc=requests.get(url=url,headers=header)
    if "200" in str(sonuc.status_code):
        print("Dosya veya dizin var:",i)
    else:
        print("Dosya veya dizin yok:",i)















