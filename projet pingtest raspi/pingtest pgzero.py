# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:15:37 2020

@author: William
"""

import pgzrun
from pygame import K_ESCAPE,K_q
from time import sleep
from subprocess import check_output, CalledProcessError
from sys import exit
from easygui import enterbox
from platform import system
 

TITLE="Pingtest by WG (press Q to change server)"
WIDTH = 480
HEIGHT = 320
sizei=150
dt=1
couleur=""
serv = "jeuxvideo.com"


def ping():
    global system
    systeme=system()
    if systeme == "Windows":
        ping = check_output(['ping', serv, "-n", '1']).decode('cp850', errors="backslashreplace").split(' ')[15].split("=")[1]
    elif systeme == "Linux":
        ping = check_output(['ping', serv, "-c", '1']).decode('cp850', errors="backslashreplace").split(' ')[7].split("=")[1] 
    elif systeme == "MacOS":
        pass #ntm
    return ping
        
def update(dt):
    
   global pin
   global pingd

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
           
       screen.clear()
       screen.draw.text(pingd,center=(WIDTH/2,HEIGHT/2),fontsize=size,color=couleur)
       screen.draw.text(serv,center=(WIDTH/2,3*HEIGHT/4),fontsize=size/5,color="lightblue")
       sleep(1)
       
       
def on_key_down(key):
    if key == K_ESCAPE:
        exit() 
    elif key == K_q:
        global serv
        serv=enterbox(msg="Choisissez le nouveau serveur à ping",title="Choix serveur")
    
    
if __name__=="__main__":
        pgzrun.go()