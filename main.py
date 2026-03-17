import translator as tr
t = tr.Translator()


while(True):

    print("--------------------------")
    print("Translator Alien-Italian")
    print("--------------------------")
    print()
    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input("Inserire un numero: ")
    if not(txtIn.isdigit()):
        print("Errore: inserisci un numero valido.")
        continue

    # Add input control here!

    if int(txtIn) == 1:
        print("Quale parola vuoi aggiungere? ")
        nuova_traduzione = input().lower()
        t.handleAdd(nuova_traduzione)

    if int(txtIn) == 2:
        print("Quale parola vuoi tradurre? ")
        txtIn = input().lower()
        t.handleTranslate(txtIn)

    if int(txtIn) == 3:
        pass


    if int(txtIn) == 4:
        break