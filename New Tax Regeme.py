import pyttsx3 as r
from num2words import num2words
import os 
import threading
import time
y=r.init()
y.setProperty("rate",150)
def speak(set):
    y.say(set)
    y.runAndWait()
speak(" This is a progarm to calculate new tax regeme")
def c(f):
    o=threading.Thread(target=f)
    o.start()
class tax:
    def __init__(self,x):
        self.gross=x
        net_nettaxable=self.gross-75000#Standard deduction
        def cess(x):
            return 4/100*x 
            
        if net_nettaxable<=300000:
            c(speak("Nil.you don't have to pay tax"))
            c(print("Nil.you don't have to pay tax"))
        elif 300000<net_nettaxable<=700000:
                c(print(f"No tax charge under section 87 A rebate "))
                c(speak("No tax charge under section 87 A rebate "))
        elif 700000<net_nettaxable<=1000000:
            hero=400000*5/100
            hero1=(net_nettaxable-700000)*10/100
            c(print(cess(hero1+hero)+hero+hero1))
            op=cess(hero1+hero)+hero+hero1
            c(speak(f"You have to pay{num2words(op)} "))
        elif 1000000<net_nettaxable<=1200000:
            hero=400000*5/100
            new=300000*10/100
            hero2=(net_nettaxable-1000000)*15/100
            c(print(cess(hero+new+hero2)+hero+new+hero2))
            c(speak(f"You have to give{num2words(cess(hero+new+hero2)+hero+new+hero2)}"))
        elif 1200000<net_nettaxable<=1500000:
            hero=400000*5/100
            new=300000*10/100
            hero4=200000*15/100
            hero5=(net_nettaxable-1200000)*20/100
            c(print(cess(hero+new+hero4+hero5)+hero+new+hero4+hero5))
            c(speak(f"You have to give{cess(hero+new+hero4+hero5)+hero+new+hero4+hero5}"))
        else :
            hero=400000*5/100 
            new=300000*10/100
            hero4=200000*15/100
            hero5=300000*20/100
            hero6=(net_nettaxable-1500000)*30/100
            b=hero+hero4+hero5+hero6+new
            print(b)
            
            if 5000000<net_nettaxable<=10000000:
                b=b*10/100
            elif 10000000<net_nettaxable<=20000000:
                b=b*15/100
            elif 20000000<net_nettaxable<=50000000:
                b=b*25/100
            elif 50000000<net_nettaxable:
                b=b*37/100
            print(cess(hero+new+hero4+hero5+hero6+b),"is the cess")
            print(b)
            c(print(cess(hero+new+hero4+hero5+hero6+b)+hero+new+hero4+hero5+hero6+b))
            c(speak(f"You have to give{cess(hero+new+hero4+hero5+hero6)+hero+new+hero4+hero5+hero6+b}"))
c(speak("Enter your gross income (including other income if you have)"))            
p=int(input("Enter your gross income(including other income if you have):"))


q=input("Do you have any deductions? write'y' for yes and 'n' for no:")
#These are for all the deductions 
if q.lower()=="y":

    o2=int(input(""))
    o3=int(input("Employee's contribution to NPS - 80CCD(2) [Maximum 14 per cent  of the salary you can deduct]"))
    o6=int(input("Interest on Educational Loan - 80E "))

    o5=int(input("Medical Insurance - 80D "))

    if o3<=14/100*p:
        t=o2+o3+o5+o6
    else:
        print("Write again")
        o3=int(input("Employee's contribution to NPS - 80CCD "))
        t=o2+o3+o5+o6
    
    rt=p-t
    pol=tax(rt)
elif q.lower()=="n":
    pol=tax(p)

