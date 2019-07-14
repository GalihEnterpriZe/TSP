#YA ALLAH SEMOGA YANG RECODE MATI AMINN:v
#RECODE NGGA BISA BIKIN JADI MASTAH YA TOD:v
from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;96m =========================================================')
           print(' ||  +-----------------------------------------------+  ||')
           print(' ||  | Creator   : Galih Prastiyo                    |  ||')
           print(' ||  +-----------------------------------------------+  ||')
           print(' ||  | github    : https://github.com/GalihEntepriZe |  ||')
           print(' ||  | WhatsApp  : +62 858 4123 8512                 |  ||')
           print(' ||  +-----------------------------------------------+  ||')
           print(' =========================================================')
           print("")
           try:
                x = str(input('\033[1;92m [?] Username \033[1;93m: '))
                print("")
                e = getpass('\033[1;92m [?] Password \033[1;93m: ')
                print ("")
#silahkan ganti username+passwordnya gan
                if x=="Username lu" and e=="Password lu":
#jangan edit yg lain kalo gak mau eror
                   print('Login Sukses ...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + x + ' | lolcat')
                   print('\033[1;92m ─────────────────────────────|by Galih ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     [!] Username/Password Salah")
                      time.sleep(2)
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     [!] Username/Password Salah")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     [!] Username/Password Salah")
                      time.sleep(2)
menu()
