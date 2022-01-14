import random as rd
import pyttsx3 as ptx

engine = ptx.init()
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0")
engine.setProperty('rate', engine.getProperty('rate') - 50)

def hablar(txt):
    engine.say(txt)
    engine.runAndWait()

def balt(lst):
    return rd.randint(0,len(lst)-1)

def aLista(narch):
    f = open(narch,"r")
    lst = f.readlines()
    tmp = lst[0]
    lst = tmp.split(";")
    f.close()
    return lst

sal = aLista("saludos.csv")
desp = aLista("despedida.csv")
afi = aLista("afirm.csv")
preg = aLista("preguntas.csv")
resp = aLista("respuestas.csv")


hablar("Bienvenido al chat!")
var = input ("Bienvenido al Chat!!!")
var = var.lower()

for pal in sal:
    if (var == pal):
        aleat = balt(sal)
        hablar(sal[aleat])
        print (sal[aleat])
        break

for pal in desp:
    if (var == pal):
        aleat = balt(sal)
        hablar(desp[aleat])
        print (desp[aleat])
        break

hablar("Cual es tu nombre?")
nombre= input("Cual es tu nombre? : ")
aleat = balt(sal)
hablar(sal[aleat] + ", " + nombre)
print(sal[aleat] + ", " + nombre)
hablar("En que te puedo ayudar?")
var = input("En que te puedo ayudar? : ")

boolSalida = False
bandera = False
while (boolSalida==False):

    var = var.lower()
    bandera = False
    if var.find("?") > -1:
        for quest in preg:
            if var.find(quest) > -1:
                numerito = preg.index(quest)
                hablar(resp[numerito])
                var = input(resp[numerito] + " : ")
                bandera = True
                break
        if (bandera == False):
            hablar("Lo siento, no entiendo tu pregunta, me la puedes repetir?")
            var = input("Lo siento, no entiendo tu pregunta, me la puedes repetir?: " )
    else:
        aleat = balt(afi)
        hablar(afi[aleat])
        var = input(afi[aleat] + " : ")

    for pal in desp:
        if (var == pal):
            aleat = balt(sal)
            hablar(desp[aleat] + " " + nombre)
            print (desp[aleat] + " " + nombre)
            boolSalida = True
            break