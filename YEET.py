# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:15:37 2020

@author: William
"""

from time import sleep
from subprocess import check_output, CalledProcessError
from sys import exit
#from easygui import enterbox
from platform import system
import os
x=-3
y=-30
os.environ["SDL_VIDEO_WINDOW_POS"]="%d,%d" % (x,y)
import pgzrun
from pygame import K_ESCAPE, K_q
from urllib.request import urlopen

TITLE="Pingtest by WG"
WIDTH = 481
HEIGHT = 320
sizei=150
dt=1
couleur=""
serv = "jeuxvideo.com"
offset=0
port=8000
couleurHTTP=""
rayon=8

def http():
    global couleurHTTP
    try:
        urlopen(f"http://localhost:{port}").read()
        couleurHTTP="green"
    except:
        couleurHTTP="red"
    return couleurHTTP

def ping():
    global system
    systeme=system()
    if systeme == "Windows":
        ping = check_output(['ping', serv, "-n", '1']).decode('cp850', errors="backslashreplace").split(' ')[15].split("=")[1]
    elif systeme == "Linux":
        ping = check_output(['ping', serv, "-c", '1']).decode('cp850', errors="backslashreplace").split(' ')[13].split("=")[1].split(".")[0] 
    elif systeme == "MacOS":
        pass #ntm
    return ping
        
def update(dt):
    
   global pin
   global pingd
   global chttp
   try:
       pin = ping()
       pingd = pin+" ms"
       
   except CalledProcessError:      
       pingd = "CRASH"   
       
   finally:
       if len(pin)>3:
           size=0.75*sizei
       else:
           size=sizei           
       if pingd=="CRASH" or int(pin)>=150:
           couleur="red"
       elif int(pin) in range(80,150):
           couleur="orange"
       else:
           couleur="green"
       chttp=http()
       screen.clear()
       screen.draw.text(pingd,center=(WIDTH/2,(HEIGHT/2)-offset),fontsize=size,color=couleur)
       screen.draw.text(serv,center=(WIDTH/2,(3*HEIGHT/4)-offset),fontsize=size/5,color="lightblue")
       screen.draw.filled_circle((17,20),rayon,color=chttp)
       screen.draw.text(f"Serveur HTTP (port: {port})", centery=20,left=30,fontsize=size/7,color="lightblue")
       screen.draw.filled_circle((WIDTH-20,20),rayon,color="yellow")
       screen.draw.text("VPN",centery=20,left=WIDTH-60,fontsize=size/7,color="lightblue")
       sleep(1)
       
       
def on_key_down(key):
    if key == K_ESCAPE:
        exit() 
    elif key == K_q:
        global serv
       # serv=enterbox(msg="Choisissez le nouveau serveur Ã  ping",title="Choix serveur")
        serv=input("Nouveau serveur:")
    
if __name__=="__main__":
        pgzrun.go()
