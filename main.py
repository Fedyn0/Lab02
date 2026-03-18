import translator as tr
from dictionary import Dictionary
t = tr.Translator()

t.loadDictionary("dictionary.txt")

while(True):

    print()
    print("--------------------------")
    print("Translator Alien-Italian")
    print("--------------------------")
    print()
    t.printMenu()



    txtIn = input("Scegli cosa vuoi fare inserendo il numero corrispondente. Inserire un numero: ")
    if not(txtIn.isdigit()):
        print("Errore: inserisci un numero valido.")
        continue
    if int(txtIn) <1 or int(txtIn) >5:
        print("Errore: inserisci un numero valido.")
        continue

    # Add input control here!

    if int(txtIn) == 1:
        print("Per aggiungere una nuova parola, devi inserire la parola aliena"
              "e la traduzione italiana separate da uno spazio. \n"
              "Inserisci qui la coppia <parola> <traduzione>")
        nuova_traduzione = input().lower()
        t.handleAdd(nuova_traduzione)

    if int(txtIn) == 2:
        print("Quale parola vuoi tradurre? ")
        parola_da_tradurre = input().lower()
        t.handleTranslate(parola_da_tradurre)

    if int(txtIn) == 3:
        print("Quale parola vuoi cercare con WildCard?")
        parola_da_trovare = input().lower()
        t.handleWildCard(parola_da_trovare)


    if int(txtIn) == 4:
        dizionario = t.dizionario.traduzioni
        print("\n --- Contenuto del Dizionario ---")
        for parola_aliena, parola_italiana in dizionario.items():
            print(parola_aliena, parola_italiana)

    if int(txtIn) == 5:

        while True:

            print("Sei sicuro di voler uscire? Digita 'SI' se vuoi uscire, 'NO' altrimenti.")
            risposta = input().strip().upper()

            if risposta == "SI" or risposta == "NO":
                break

            print("Errore: risposta non valida. Devi digitare esattamente 'SI' oppure 'NO'.\n")

        if risposta == "SI":
            print("Arrivederci!")
            break

        if risposta == "NO":
            print("Uscita annullata. Torno al menu principale...\n")
            continue