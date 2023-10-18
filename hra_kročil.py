import random
from time import sleep
print("Kdysi dávno jsi v jedné staré knize našel mapu, která vypadá, jako by na ní byla vyznačena cesta k nějakému pokladu. Rozhodl ses tedy, že se vydáš za dobrodružstvím.")
sleep(1)
print("Jsi na cestě a vypadá to, že tě mapa vede přímo do lesa, dojdeš na místo a před tebou se z ničeho nic zjeví tajuplný dům, chystáš se vejít do jeho dveří...")
sleep(1)
print("INFO:")
print("V každé místnosti jsou dveře, a také plno nástrah, které na tebe čekají. Dovedeš se s těmito věcmi vypořádat a zmocnit se pokladu? Do dveří vcházíš pomocí WASD. ")
sleep(1)
print("Po celou dobu hry máš pět životů. Ty můžeš postupně ztratit bojem s nepřáteli, nebo rovnou například spadnutím do jámy a podobnými překážkami ")
sleep(2)
print("W je nahoru")
print("A je doleva")
print("S je dolů")
print("D je doprava")
sleep(1)
print("___________________________________________________________________________________________________________________________")
cykl = True
klic = False
cyklus_mov = 0
while cykl == True:
    sleep(1)
    vchod = input("Zahaj hru vkročením do vchodových dveří : (D)\n")
    if vchod == "D":
        sleep(1)
        print("Vstoupil jsi do hlavních dveří domu... Teď se musíš ovšem rozhodnout, kudy se vydat.")
        while cyklus_mov < 1:
            sleep(2)
            movement = input("Tak, kam půjdeš? (W) (A) (S) (D)\n")
            cyklus_mov = 2
            if klic == True and movement == "W":
                print("Tam už ne, tam už jsi byl.")
                cyklus_mov = 0
            elif movement == "W":
                movement = ()
                print('Vejdeš do místnosti a před tebou se naráz objeví zombie. Všimne si tě a chystá se na tebe zaútočit! Teď bude záležet hlavně na tvém štěstí. Vylosuj si ho stiskem tlačítka "M" ' )
                sleep(2)
                print('INFO: tvé štěstí je číslo od 0 do 100, které si vylosuješ stisknutím tlačítka "M". Pokud bude hodnota tvého štěstí větší než hodnota soupeře, ubíráš mu život. Pokud bude stejné nebo nižší, soupeř ti ubírá život.')
                sleep(2)
                print("___________________________________________________________________________________________________________________________")
                sleep(1)
                print("Štěstí zombie je: 30")
                print("Životy zombie jsou: 1 ")
                zivoty = 5
                print(f"Počet tvých životů je {zivoty}")
                mira = True
                zombie = 30
                while mira == True:  
                    mira_stesti = input('Stiskni (M) :\n')
                    character = random.randint(0,100)
                    mira = False
                    if mira_stesti == "M":
                        mira_stesti = ()
                        sleep(2)
                        print(f"Tvé štěstí je : {character}")
                        mira = False 
                        if character <= zombie:
                            print("Au! Ztratil jsi život.")
                            zivoty = zivoty - 1 
                            print(f"Počet tvých životů je {zivoty}!")
                            if zivoty == 0:
                                print("Zemřel jsi! Pokus se o dobytí pokladu znovu.")  
                                exit()
                            print("Vylosuj si ho znova, třeba budeš mít větší štěstí")
                            mira = True 
                        else:
                            sleep(1)
                            print("Vyhrál jsi nad zombie! Gratuluji! Teď je načase se vydat dál, tentokrát můžeš jít pouze do dveří nahoru (W) nebo doprava (D).  ")
                            sleep(1)
                            print(f"Počet tvých životů je {zivoty}")
                            kod = False
                            cyklus = True 
                            while cyklus == True :
                                sleep(1)
                                movement = input("Tak, kam půjdeme?\n")
                                cyklus = False
                                if kod == True and movement == "W":
                                    print("Tam už jsi byl!")
                                    cyklus = True
                                elif movement == "W":
                                    movement = ()
                                    print("Rozhodneš se jít nahoru, vejdeš do místnosti a hned si všímáš, že na zemi leží dva předměty. Je to nějaké sako a starobylá váza. Napadne tě, že by ses mohl podívat, jestli v nich něco není! ")
                                    sleep(2)
                                    nahlednout = True
                                    while nahlednout == True:
                                        print('Pokud se rozhodneš nahlédnout do vázy, zmáčkni "1" , pokud prozkoumat sako, tak zmáčkni "2"')
                                        nahlednout = False 
                                        move = int(input())
                                        if move == 1:
                                            move = ()
                                            sleep(1)
                                            print("Nahlédneš do vázy a strčíš do ní ruku, to se ti ale nevyplácí, protože se v ní nachází hnízdo kousavých mravenců! Jeden z nich tě kousne a ubírá ti jeden život.")
                                            zivoty -= 1
                                            if zivoty == 0 :
                                                print(f"Počet tvých životů je {zivoty}!")
                                                sleep(1)
                                                print("Zemřel jsi! Pokus se o dobytí pokladu znovu.")  
                                                exit()
                                            move = 2 
                                        if move == 2 :
                                            movement = ()
                                            print("Rozhodneš se tedy prozkoumat sako. A máš štěstí! V poslední kapse nacházíš papírek, na kterém je napsáno:")
                                            sleep(2)
                                            print("KÓD = počet dní v přestupném roce") 
                                            sleep(1)
                                            print("Vycházíš z místnosti a teď už ti zbývá jít jen doprava: (D)")
                                            kod = True 
                                            cyklus = True
                                elif movement == "D":
                                    cyklus = False
                                    print("Vejdeš do místnosti a uvidíš ve zdi naproti sobě trezor")
                                    if kod == True:
                                        kod_heslo = 366
                                        cyklus_kod = True
                                        sleep(1)
                                        print("Přijdeš k němu, vytáhneš svůj papírek s kódem a chystáš se jej zadat do trezoru")
                                        while cyklus_kod == True:
                                            kod_uzivatel = int(input("ZADEJ KÓD: "))
                                            cyklus_kod = False                               
                                            if kod_uzivatel == kod_heslo:
                                                print("VYHODNOCOVÁNÍ")
                                                sleep(3)
                                                print("Výborně! Trezor se otevírá a ty v něm nacházíš klíč, ke kterým dveřím asi patří? Protože zde není více dveří, do kterých by se dalo jít, vracíš se zpátky ke vstupním dveřím, kterými jsi vešel do domu.")
                                                movement = ()
                                                cyklus_mov = 0
                                                klic = True                                 
                                            else:
                                                print("VYHODNOCOVÁNÍ")
                                                sleep(3)
                                                print("NESPRÁVNÉ HESLO")
                                                cyklus_kod = True
                                    elif kod == False:
                                        movement = ()
                                        sleep(2)
                                        print("Bohužel k němu ale zatím neznáš kód :(. Vracíš se do předchozí místnosti...")
                                        cyklus = True 
                                elif movement == "A":
                                    sleep(1)
                                    print("Tam je zeď!")
                                    cyklus = True   
                                elif movement == "S":
                                    sleep(1)
                                    print("Nevracej se, přece tady musíš něco najít!")
                                    cyklus = True 
                                
                                
                                else:
                                    print("INFO: Pohybuješ se pomocí WASD")
                                    cyklus = True 
                    else:
                        mira = True 



                    
            elif movement == "D":
                sleep(1)
                print("Vejdeš do místnosti, dveře za tebou náhle zmizí a podlaha pod tebou začíná praskat. Pomalu si začínáš uvědomovat, že je tohle asi tvůj konec. Do pár sekund už padáš společně se zbytky podlahy do bezedné jámy.")
                print("Zemřel jsi! Pokus se o dobytí pokladu znovu.")  
                exit()
            elif movement == "A":
                print("Těmito dveřmi jsi přišel, takže tudy cesta nepovede :D")
                cyklus_mov = 0
            elif movement == "S":
                if klic == False:
                    sleep(1)
                    print("Chytneš za kliku dveří a zjišťuješ, že jsou zamknuté. Musíš k nim nejprve najít klíč.")
                    cyklus_mov = 0
                elif klic == True:
                    sleep(1)
                    print("Chytneš za kliku dveří a zjišťuješ, že jsou zamknuté. Ty však máš klíč a odemykáš.")
                    cyklus_mov = 2 
                    movement = ()
                    sleep(1)
                    print("Naštěstí v této místnosti není nic, čeho by ses měl bát, jen opět tři dveře v každé ze zdí")
                    kod_cislo_jedna = False
                    kod_cislo_dva = False 
                    cyklus3 = True 
                    while cyklus3 == True:
                        movement = input("Kterými dveřmi se vydáš? (S) - dolů (D) - doprava (A) - doleva\n")
                        cyklus3 = False
                        if movement == "A" and  kod_cislo_jedna == True:
                            print("Tam už jsi byl.")
                            cyklus3 = True 
                        elif movement == "D" and  kod_cislo_dva == True:
                            print("Tam už jsi byl.")
                            cyklus3 = True 
                        elif movement == "S":
                            sleep(1)
                            print("Přijdeš ke dveřím a hned si všimneš, že to nejsou jen tak obyčejné dveře. místo kliky mají čtyřčíselný kód!")
                            sleep(1)
                            leave = input('Pokud zatím kód neznáš, zmáčkni libovolné písmeno, pokud se chceš pokusit o zadání správného kódu, zmáčkni "C"\n')
                            if leave == "C":
                                    zadavani = True 
                                    while zadavani == True :
                                            kod2_uzivatel = int(input("ZADEJTE KÓD: "))
                                            kod2 = 5927
                                            zadavani = False
                                            if kod2 == kod2_uzivatel:
                                                sleep(2)
                                                print("Fantastické, klika povolí, dveře se otevírají a už z dálky tě oslňuje obrovská záře zlatých mincí! Poklad je tvůj! Zmocníš se ho a rychle prcháš pryč z domu.")
                                                zadavani = False
                                                exit()
                                            else:
                                                sleep(2)
                                                print("Zadáš do dveří kód a nic se neděje.. Asi to není ten správný kód.")
                                                sleep(1)
                                                leave = input('Pokud zatím kód neznáš, zmáčkni libovolné písmeno, pokud se chceš pokusit o zadání správného kódu znovu, zmáčkni "C"\n ')
                                                if leave == "C":
                                                    zadavani = True 
                                                else:
                                                    cyklus3 = True
                            else:
                                cyklus3 = True
                        
                        elif movement == "A":
                            print("Vejdeš do místnosti, která je celá posetá pavučinami. Najednou vidíš jak se k tobě shora spouští po pavučině obří pavouk! Opět bude záležet na tvém štěstí")
                            sleep(1)
                            print("INFO: Pavouk je těžší na poražení, než zombie. Má více životů, a také větší štěstí.")
                            sleep(1)
                            print("___________________________________________________________________________________________________________________________")
                            sleep(1)
                            print("Štěstí pavouka je 40")
                            print("Počet životů pavouka je 3")
                            print(f"Počet tvých životů je {zivoty}")
                            sleep(1)
                            mira_stesti2 = input('Stiskni (M) :\n')
                            mira2 = True
                            pavouk_stesti = 40
                            pavouk_zivoty = 2
                            while mira2 == True:  
                                character = random.randint(0,100)
                                if mira_stesti2 == "M":
                                        mira_stesti2 = ()
                                        sleep(1)
                                        print(f"Tvé štěstí je : {character}")
                                        mira2 = False 
                                        if character <= pavouk_stesti:
                                                print("Au! Ztratil jsi život.")
                                                zivoty = zivoty - 1 
                                                print(f"Počet tvých životů je {zivoty}!")
                                                if zivoty == 0:
                                                        print("Zemřel jsi! Pokus se o dobytí pokladu znovu.")  
                                                        exit()
                                                mira_stesti2 = input("Vylosuj si ho znova, třeba budeš mít větší štěstí  - (M) : \n ")
                                                mira2 = True 
                                        elif pavouk_zivoty == 0:
                                            sleep(2)
                                            print("Porazil jsi pavouka! Vynikající! Jeho mrtvé tělo náhle zmizí a zanechá za sebou jen kus papíru, na kterém je napsáno:")
                                            print("59--")
                                            print("Vracíš se do předchozí místnosti...")
                                            kod_cislo_jedna = True
                                            mira2 = False 
                                            cyklus3 = True 
                                            
                                        elif character > pavouk_stesti:
                                            sleep(1)
                                            pavouk_zivoty -= 1
                                            mira_stesti2 = input(f"Paráda, ubíráš pavoukovi život! Teď už má jen {pavouk_zivoty + 1} ! Zmáčkni (M) pro další zahájení útoku :\n")
                                            mira2 = True
                        elif movement == "W" :
                            print("Zpátky nechoď :D")   
                            cyklus3 = True

                        elif movement == "D"  :
                            print("Vejdeš do dveří a naproti tobě se náhle zjeví čarodějnice a praví:")
                            pripraven = True 
                            sleep(1)
                            print('"Dám ti několik matematických příkladů, pokud odpovíš špatně, zle to s tebou dopadne!"')
                            while pripraven == True:
                                sleep(2)
                                ready = input("Jsi připraven? Jestli ano, zmáčkni : (Y)\n")
                                pripraven = False
                                if ready == "Y":
                                    print("první příklad : (8 * 5) / 2")
                                    sleep(0.5)
                                    answer = int(input("Tvá odpověď : "))     
                                    if answer == 20:
                                        answer = ()
                                        sleep(1)
                                        print("Čarodějnice se zamračí a ihned ti dává další příklad :")
                                        sleep(1)
                                        print("8 + 3 * √81 ")
                                        sleep(0.5)                                                        
                                        answer = int(input("Tvá odpověď : "))
                                        if answer == 35:
                                            answer = ()
                                            print("Čarodějnice se začína třást zlostí div nevybouchne. Přesto ti ale dává poslední příklad:")
                                            sleep(1)
                                            print("6 : 2(1 + 2)")
                                            sleep(0.5)
                                            answer = int(input("Tvá odpověď : "))
                                            if answer == 9:
                                                print("Skvěle! Čarodějnice je natolik nazlobená že naráz zmizí a po sobě zanechá svůj oblek, na kterém je napsáno:")
                                                sleep(1)
                                                kod_cislo_dva = True 
                                                print("--27")
                                                sleep(1)
                                                print("Teď se zase vracíš do předchozí místonosti.")
                                                cyklus3 = True 
                                
                                            else:
                                                print("Čarodějnice na tebe namíří svou hůl a promění tě v žábu! Tohle je tvůj konec!")
                                                exit()
                                        
                                        else:
                                            print("Čarodějnice na tebe namíří svou hůl a promění tě v žábu! Tohle je tvůj konec!")
                                            exit()
                                            
                                    else:
                                        print("Čarodějnice na tebe namíří svou hůl a promění tě v žábu! Tohle je tvůj konec!")
                                        exit()
                                        
                                


                                else:
                                    pripraven = True 
                        else:
                            print("INFO: Pohybuješ se pomocí WASD")
                            cyklus3 = True


                            





            
            
            
            
            
            else:
                print("INFO: Pohybuješ se pomocí WASD")
                cyklus_mov = 0