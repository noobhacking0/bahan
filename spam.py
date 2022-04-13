import os
import sys
import time 
 
def clear():
    os.system("clear")
    os.system("\tfiglet INSTALLER")

def menu():
    clear()
    print ("\ttolls By exogen")
    print ("\t1.install bahasa pemrogaman\n")
    print ("\t2.install bahan bahan\n")
    pil = raw_input("pilih: ")
    if pil =="1":
        os.system("apt install python2")
        os.system("apt install php")
        os.system("apt install python3")
    elif pil =="2":
        os.system("apt install git")
        os.system("apt install figlet")
        os.system("apt install lolcat")
        os.system("apt install wget")
    else:
        print ("masukan dengan benar")

menu()