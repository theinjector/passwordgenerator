import random

up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low="abcdefghijklmnopqrstuvwxyz"
num="0123456789"
symbols="@#&()§!*$£+:,;/={}[]-_%.≠÷~◊‹›√¿ŸΩ∑∆¢Ø„"
all= up+low+num+symbols
#length of password
length=int(input("\033[32m Please enter a valid length:" "\033[31m"))
password="".join(random.sample(all,length))
print("\033[32mYour password generated is:""\033[31m",password)
