class Modello3d():
    def __init__(self, nome_mod, descriz, dipart_az):
        self.nome_mod = nome_mod
        self.descriz = descriz
        self.dipart_az = dipart_az
    def modifica(self, nome_mod, descriz, dipart_az):
        self.nome_mod = nome_mod
        self.descriz = descriz
        self.dipart_az = dipart_az
    def info_mod(self):
        print("il modello3d %s e' stato creato dal dipartimento %s" % (self.nome_mod, self.dipart_az))
        print("e Questa e' la sua descrizione:\n%s " % (self.descriz))

class Catalogo3d():
    def __init__(self, dipart_az):
        self.dipart_az = dipart_az
        self.modelli3d = []
    def inserimento(self, modello3d):
        self.modelli3d.append(modello3d)
        print("modello3d denominato %s  - aggiunto con successo" % (modello3d.nome_mod))
    def modifica(self, dipart_az):
        self.dipart_az = dipart_az
    def cancella(self, nome):
        for el in self.modelli3d:
            if el.nome_mod == nome:
                indice = self.modelli3d.index(el)
        self.modelli3d.pop(indice)
    def ricerca(self, nome):
        for el in self.modelli3d:
            if el.nome_mod == nome:
                el.info_mod()
    def stampa(self):
        print("\t Il Catalogo3d %s contiene:" % (self.dipart_az))
        for modello in self.modelli3d:
            print(modello.nome_mod)
        print("---"*4)

modello1 = Modello3d("chiaveInglese", "Chiave del 13", "AA33")
modello2 = Modello3d("dado", "dado del 13", "AA33")
modello1.info_mod()
catalogoAA33= Catalogo3d("AA33")

catalogoAA33.inserimento(modello1)
catalogoAA33.inserimento(modello2)

catalogoAA33.stampa()
catalogoAA33.cancella("dado")
catalogoAA33.stampa()

catalogoAA33.ricerca("chiaveInglese")
