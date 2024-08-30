import random
import pyttsx3#first you have write in the terminal(pip install pyttsx3)
from num2words import num2words as n#first you have write in the terminal(pip install num2words)
import webbrowser as o
import threading
def u(p):
    o=threading.Thread(target=p)
    o.start()
poi=pyttsx3.init()
poi.setProperty("rate",147)
def s(x):
    poi.say(x)
    poi.runAndWait()
rt="https:\\www.chess.com"
p=random.randint(3000,3019)
lo=-1
ot=0
s(f"Guess the secret code between {n(3001)} and {n(3020)}")
while lo!=p:
    ot+=1
    k=int(input("Guess the secret code"))
    if k>p:
        u(print("Lesser than the number"))
        u(s("Lesser than the number"))
    elif k<p:
        u(print("Higher than the number"))
        u(s("Higher than the number"))
    else:
        u(o.open(rt))
        u(s("Successfully opened"))
        break
u(print(f"You have done it in {ot} attempts"))
u(s(f"You have done it in {ot} attemets"))


