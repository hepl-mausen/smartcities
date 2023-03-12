#File : Music
#making The Imperial Marche - STAR WARS with the buzzer
#loic.mausen@student.hepl.be


from machine import Pin, PWM, ADC            #import functions from libraries
from time import sleep_ms

buzzer = PWM(Pin(27))                        #setting the pin 27 as an pwm output
vol = 1000                                   #setting variable volume to 1000

def do(time):                                #define the do note function 
    buzzer.freq(1046)                        #setting the sound frequency to match the note
    buzzer.duty_u16(vol)                     #setting the note volume to 1000
    sleep_ms(time)                           #the program stops during the time set between the parentheses of the function
    
def sol(time):                               #define the sol note function 
    buzzer.freq(1568)                        #setting the sound frequency to match the note
    buzzer.duty_u16(vol)                     #setting the note volume to 1000
    sleep_ms(time)                           #the program stops during the time set between the parentheses of the function
    
def mib(time):                               #...
    buzzer.freq(1244)
    buzzer.duty_u16(vol)
    sleep_ms(time)
    
def sib(time):
    buzzer.freq(1864)
    buzzer.duty_u16(vol)
    sleep_ms(time)
    
def rep(time):
    buzzer.freq(2349)
    buzzer.duty_u16(vol)
    sleep_ms(time)
    
def mibp(time):
    buzzer.freq(2489)
    buzzer.duty_u16(vol)
    sleep_ms(time)
    
def fad(time):
    buzzer.freq(1480)
    buzzer.duty_u16(vol)
    sleep_ms(time)

def solp(time):
    buzzer.freq(3136)
    buzzer.duty_u16(vol)
    sleep_ms(time)
    
def fadp(time):
    buzzer.freq(2960)
    buzzer.duty_u16(vol)
    sleep_ms(time)

def fap(time):
    buzzer.freq(2793)
    buzzer.duty_u16(vol)
    sleep_ms(time)
    

def mip(time):
    buzzer.freq(2637)
    buzzer.duty_u16(vol)
    sleep_ms(time)
    
def redp(time):
    buzzer.freq(2489)
    buzzer.duty_u16(vol)
    sleep_ms(time)

def sold(time):
    buzzer.freq(1661)
    buzzer.duty_u16(vol)
    sleep_ms(time)
    
def dodp(time):
    buzzer.freq(2217)
    buzzer.duty_u16(vol)
    sleep_ms(time)
    
def dop(time):
    buzzer.freq(2093)
    buzzer.duty_u16(vol)
    sleep_ms(time)
    
def si(time):
    buzzer.freq(1975)
    buzzer.duty_u16(vol)
    sleep_ms(time)
    
def la(time):
    buzzer.freq(1760)
    buzzer.duty_u16(vol)
    sleep_ms(time)
    
def fad(time):
    buzzer.freq(1480)
    buzzer.duty_u16(vol)
    sleep_ms(time)

def n(time):                          #define the n fucntion
    buzzer.duty_u16(0)                #set the volume to 0
    sleep_ms(time)                    #the program stops during the time set between the parentheses of the function
   
while True:                           #starting the while loop
    n(1000)                           #calling n fucntion during 1000 ms
    sol(600)                          #calling sol fucntion during 600 ms
    n(20)                             #...
    sol(600)
    n(20)
    sol(600)
    mib(400)
    sib(200)
    sol(600)
    mib(400)
    sib(200)
    sol(700)
    n(600)
    
    rep(600)
    n(20)
    rep(600)
    n(20)
    rep(600)
    n(20)
    mibp(400)
    sib(200)
    fad(600)
    mib(400)
    sib(200)
    sol(700)
    n(600)
    
    solp(600)
    sol(400)
    n(20)
    sol(100)
    solp(600)
    fadp(600)
    fap(150)
    mip(150)
    redp(150)
    mip(500)
    n(20)
    
    mip(100)
    sold(500)
    dodp(500)
    dop(500)
    si(150)
    sib(150)
    la(150)
    sib(500)
    n(50)
    
    sib(200)
    mib(400)
    fad(600)
    mib(400)
    fad(200)
    sib(400)
    sol(400)
    sib(200)
    rep(600)
    n(600)
    
    solp(600)
    sol(400)
    n(20)
    sol(100)
    solp(600)
    fadp(600)
    fap(150)
    mip(150)
    redp(150)
    mip(500)
    n(50)
    
    mip(100)
    sold(500)
    dodp(500)
    dop(500)
    si(150)
    sib(150)
    la(150)
    sib(500)
    n(50)
    
    mib(400)
    fad(600)
    mib(400)
    sib(200)
    sol(600)
    mib(400)
    sib(200)
    sol(600)


    
    n(3000)