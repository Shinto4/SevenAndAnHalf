from random import *
from time import *

carte = ["coins", "clubs", "swords", "cups"]
valori = ["Ace", "Two", "Tree", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
a = ""

print("Welcome to: Seven and a half!")

while a == "":

    input("Press enter to start ")
    numeri = list(range(40))
    shuffle(numeri)
    c = numeri.pop()
    carta = c // 10
    valore = c % 10
    valoreAssoluto = valore + 1
    s = 0
    x = 0
    
    
    
        
    print("Shuffle the deck...")
    sleep(2)

    print("Your card:", valori[valore], "of", carte[carta])
    if valoreAssoluto > 7 and c != 9:
        x = 0.5
    elif c == 9:
        s = 7
        print("You drew the jolly")
    elif valoreAssoluto <= 7 and c != 9:
        x = valoreAssoluto
    b = x 
        
    sleep(0.5)

    con = input("Stop or card? (stop/card) ")
    while con == "card":
        c = numeri.pop()
        carta = c // 10
        valore = c % 10
        valoreAssoluto = valore + 1
        
        print("Card:", valori[valore], "of", carte[carta])
        
        if valoreAssoluto > 7 and c != 9:
            x = 0.5
            b = b + x
        elif c == 9:
            s = 7
            print("You drew the jolly")
        else:
            x = valoreAssoluto
            b = b + x

        if s == 7 and b < 7.5:
            if b % 1 == 0 and b != 7:
                z = 7
            elif b % 1 != 0 or b == 7:
                z = 7.5
        
        if s == 0 or b > 7.5:
            print("You have", b)
        elif s == 7 and b <= 7.5:
            print("You have", z)
        
        if b > 7.5 :
            print("You busted")
            break
        elif b == 7.5:
            con = "stop"
        if b <= 7.5:
            con = input("Stop or card? (stop/card) ")
    if b <= 7.5:
        print("You stay with", b)
        sleep(0.5)
    
        c = numeri.pop()                                                                #banco
        carta = c // 10
        valore = c % 10
        valoreAssoluto = valore + 1
        print("The dealer has", valori[valore], "of", carte[carta])
        x = 0
        m = 0
        if valoreAssoluto > 7 and c != 9:
            x = 0.5
        elif c == 9:
            m = 7
        else:
            x = valoreAssoluto
        d = x + m
        if d >= b:
            con = "stop"
        elif d < b:
            con = "card"

        while con == "card":
            sleep(1)
            print("The dealer draw another card")
            sleep(0.5)
            c = numeri.pop()                                                                
            carta = c // 10
            valore = c % 10
            valoreAssoluto = valore + 1
            print("Card:", valori[valore], "of", carte[carta])
            if valoreAssoluto > 7 and c != 9:
                x = 0.5
            elif c == 9:
                if d % 1 == 0:
                    m = 7 
                elif d % 1 != 0:
                    m = 7.5 
            elif valoreAssoluto <= 7:
                x = valoreAssoluto
            
            d = d + x + m
            sleep(1)
            print("The dealer has", d)
            if d >= b:
                con = "stop"
            elif d < b:
              con = "card"
            if d > 7.5:
                print("The dealer busted")
                break
            sleep(1)
        if d >= b and d <= 7.5:
            print("The dealer won")
        elif d < b and d <= 7.5:
            print("You won!")
        elif d <= 7.5:
            print("You won!")
           
        
        
    
    
    
