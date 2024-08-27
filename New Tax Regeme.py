import pyttsx3 as r
y=r.init()
y.setProperty("rate",150)
def speak(set):
    y.say(set)
    y.runAndWait()
#speak("This is a progarm to calculate new tax regeme")
class tax:
    def __init__(self,x):
        self.gross=x
        net_nettaxable=self.gross-75000
        def cess(x):
            return 4/100*x 
        if net_nettaxable<=300000:
            speak("Nil.you don't have to pay tax")
            print("Nil.you don't have to pay tax")
        elif 300000<net_nettaxable<=700000:
            hero=400000*5/100
            if hero<=25000:
                print("No tax cahrge under section 87 A rebate ")
            else:
                print(cess(hero))
        elif 700000<net_nettaxable<=1000000:
            hero=400000*5/100
            hero1=(net_nettaxable-700000)*10/100
            print(cess(hero1+hero)+hero+hero1)
        elif 1000000<net_nettaxable<=1200000:
            hero=400000*5/100
            new=300000*10/100
            hero2=(net_nettaxable-1000000)*15/100
            print(cess(hero+new+hero2)+hero+new+hero2)
        elif 1200000<net_nettaxable<=1500000:
            hero=400000*5/100
            new=300000*10/100
            hero4=200000*15/100
            hero5=(net_nettaxable-1200000)*20/100
            print(cess(hero+new+hero4+hero5)+hero+new+hero4+hero5)
        else :
            hero=400000*5/100
            new=300000*10/100
            hero4=200000*15/100
            hero5=300000*20/100
            hero6=(net_nettaxable-1500000)*30/100
            print(cess(hero+new+hero4+hero5+hero6)+hero+new+hero4+hero5+hero6)
            
p=int(input("Enter your gross income(if you don't donn't know just write  'n'):")) 
if p.lower()=="n":
    print("Hello")
else:
    pass
q=input("Do you have any deductions? write'y' for yes and 'n' for no:")
#These are for all the deductions 
if q.lower()=="y":
    o=int(input("Interest on Housing Loan - 80EEA :"))
    o2=int(input(""))
    o3=int(input("Employee's contribution to NPS - 80CCD(2) [I will not check whether you are central government employees or ]"))
    o6=int(input("Interest on Educational Loan - 80E "))
    o4=int(input("Basic Deductions - 80C "))
    o5=int(input("Medical Insurance - 80D "))
    o1=int(input("Donations to Charity - 80G:"))
    if o3<=14/100*p:
        t=o+o1+o2+o3+o4+o5+o6
    else:
        print("Write again")
        o3=int(input("Employee's contribution to NPS - 80CCD "))
        t=o+o1+o2+o3+o4+o5+o6
    
    rt=p-t
    pol=tax(rt)
elif q.lower()=="n":
    pol=tax(p)

