from dictionary import Dictionary

class Translator:

    def __init__(self):
        self.dizionario = Dictionary()
        self.nomefile = None

    def printMenu(self):
        print("1. Aggiungi nuova parola\n"
              "2. Cerca una traduzione\n"
              "3. Cerca con wildcard\n"
              "4. Stampa tutto il Dizionario\n"
              "5. Exit")
        pass

    def loadDictionary(self, dict):

        self.nomefile = dict
        try:
            with open(self.nomefile, "r", encoding="utf-8") as file:
                for r in file:
                    parti = r.strip().split(" ",1)

                    if len(parti) == 2:
                        parola_aliena = parti[0]
                        traduzione = parti[1]
                        self.dizionario.addWord(parola_aliena, traduzione)

        except FileNotFoundError:
            print(f"Errore: Il file {self.nomefile} non è stato trovato!")

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

        if not entry.replace(" ","").isalpha():
            print("Errore: sono ammesse solo lettere alfabetiche")
            return

        elementi = entry.strip().split(" ",1)

        if len(elementi) < 2:
            print("Errore: devi inserire sia la parola aliena che la traduzione, separate da uno spazio")
            return

        self.dizionario.addWord(elementi[0], elementi[1])

        try:
            with open(self.nomefile, "a", encoding="utf-8") as file:
                file.write(f"\n{elementi[0]} {elementi[1]}")
            print("Parola aggiunta")
        except FileNotFoundError:
            print("Il file non è stato trovato!")


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        parola_da_tradurre = query
        traduzioni = self.dizionario.translate(query)

        if traduzioni is None:
            print(f"Errore: la parola '{parola_da_tradurre}' non è presente nel dizionario")
            return

        else:
            if len(traduzioni) > 1:
                print(f"'{parola_da_tradurre}' ha diverse traduzioni, ovvero: ")
                for i in traduzioni: print(f"'{i}'")

            else:
                print(f"La traduzione di '{parola_da_tradurre}' è '{traduzioni[0]}'")


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass