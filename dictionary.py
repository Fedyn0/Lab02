import re

class Dictionary:
    def __init__(self):
        self.traduzioni = {}

    def addWord(self, parola_aliena: str, traduzione: str):
        if parola_aliena in self.traduzioni:
            self.traduzioni[parola_aliena].append(traduzione)
        else:
            self.traduzioni[parola_aliena] = [traduzione]

    def translate(self, parola_aliena: str):
        return self.traduzioni.get(parola_aliena, None)

    def translateWordWildCard(self, pattern: str):

        risultati_trovati = {}

        for parola_aliena, traduzioni_italiane in self.traduzioni.items():
            if re.fullmatch(pattern, parola_aliena):
                risultati_trovati[parola_aliena] = traduzioni_italiane
        return risultati_trovati

    def __repr__(self):
        return self.traduzioni.__repr__()
