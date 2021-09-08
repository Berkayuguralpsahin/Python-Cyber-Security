dosya=open("sayilar.txt","r")
içerik=dosya.read()
dosya.close()
for i in içerik.splitlines():
    print(i)