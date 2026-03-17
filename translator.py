from dictionary import Dictionary

class Translator:

    def __init__(self):
        self.dizionario = Dictionary()
        self.nomefile = None

    def printMenu(self):
        print("1. Aggiungi nuova parola\n"
              "2. Cerca una traduzione\n"
              "3. Cerca con wildcard\n"
              "4. Stampa tutto il Dizionario1\n"
              "5. Exit")
        pass

    def loadDictionary(self, dict):

        self.nomefile = dict
        try:
            with open(self.nomefile, "r", encoding="utf-8") as file:
                for r in file:
                    parti = r.strip().split(" ",1)
                    parola_aliena = parti[0]
                    traduzione = parti[1]
                    self.dizionario.addWord(parola_aliena, traduzione)

        except FileNotFoundError:
            print(f"Errore: Il file {self.nomefile} non è stato trovato!")

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

        while True:
            entry = entry.lower()
        elementi = entry.strip().split(" ",1)
        print(elementi)

        if len(elementi) != 2:
            print("Errore: devi inserire la parola aliena e la traduzione italiana separate da uno spazio")
            return



    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass