from random import *
from time import *

carte = ["coins", "clubs", "swords", "cups"]
valori = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
a = ""
banco = 0
giocatore = 0
crediti = 200

print("Welcome to seven and an half!")

while crediti > 0:

    input("Press enter to start ")
    numeri = list(range(40))
    shuffle(numeri)
    c = numeri.pop()
    carta = c // 10
    valore = c % 10
    valoreAssoluto = valore + 1
    s = 0
    x = 0
    puntata = 1000000000000000
    sleep(0.5)
    while puntata > crediti:
        print("You have", crediti, "credits")
        sleep(0.5)
        puntata = int(input("How much do you want to bid? "))
        if puntata > crediti:
            print("You can't bid more credits than the ones you have")
    
    
    
        
    print("Shuffle the deck...")
    sleep(2)

    print("Your card:", valori[valore], "of", carte[carta])
    if valoreAssoluto > 7 and c != 9:
        x = 0.5
    elif c == 9:
        s = 7
        print("You drawn the jolly!")
    elif valoreAssoluto <= 7 and c != 9:
        x = valoreAssoluto
    b = x
        
    sleep(0.5)

    con = input("Keep or card? (keep/card) ")
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
            sleep(0.5)
            print("You drawn the jolly")
        else:
            x = valoreAssoluto
            b = b + x
        
        if s == 7 and b < 7.5:
            if b % 1 == 0 and b != 7:
                z = 7
            elif b % 1 != 0 or b == 7:
                z = 7.5
        sleep(0.5)
        if s == 0 or b > 7.5:
            print("You have", b)
        elif s == 7 and b <= 7.5:
            print("You have", z)
    
        sleep(0.5)
        
        if b > 7.5 :
            print("You busted")
            crediti = crediti - puntata
            break
        elif b == 7.5:
            con = "keep"
        if b <= 7.5:
            con = input("Keep or card? (keep/card) ")
    if b <= 7.5:
        print("You keep with", b)
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
            con = "keep"
        elif d < b:
            con = "card"

        
        
        while con == "card":
            sleep(1)
            print("The dealer draws another card")
            sleep(1)
            c = numeri.pop()                                                                
            carta = c // 10
            valore = c % 10
            valoreAssoluto = valore + 1
            print("Card:", valori[valore], "of", carte[carta])
            if valoreAssoluto > 7 and c != 9:
                x = 0.5
            elif c == 9:
                if d % 1 == 0:
                    m = 7 - d
                elif d % 1 != 0:
                    m = 7.5 - d
            elif valoreAssoluto <= 7:
                x = valoreAssoluto
            if m != 0:
                if d % 1 == 0:
                    m = 7 - d
                elif d % 1 != 0:
                    m = 7.5 - d
            d = d + x + m
            sleep(1)
            print("The dealer has", d)
            if d >= b:
                con = "keep"
            elif d < b:
              con = "card"
            if d > 7.5:
                sleep(1)
                print("The dealer busted")
                break
            
        sleep(1)
            
        if d >= b and d <= 7.5:
            print("The dealer won")
            banco = banco + 1
            crediti = crediti - puntata
            print("Dealer:", banco, "You:", giocatore, "Now you have", crediti, "credits")
            
        elif b > 7.5:
            print("The dealer won")
            banco = banco + 1
            crediti = crediti - puntata
            print("Banco:", banco, "Tu:", giocatore, "Now you have", crediti, "credits")
            
        elif d < b and d <= 7.5:
            print("You won!")
            giocatore = giocatore + 1
            crediti = crediti + puntata
            print("Dealer:", banco, "You:", giocatore, "Ora hai", crediti, "crediti")
            
        elif d > 7.5:
            print("You won!")
            giocatore = giocatore + 1
            crediti = crediti + puntata
            print("Dealer:", banco, "You:", giocatore, "Now you have", crediti, "credits")

        sleep(1)

print("You finished all your credits")
