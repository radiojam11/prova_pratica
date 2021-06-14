import peewee

db = peewee.SqliteDatabase("modelli3d.db")
class Catalogo3d(peewee.Model):
    dipart_az = peewee.CharField()
    nome_mod = peewee.CharField()
    descrizione = peewee.CharField()

    class Meta:
        database = db
        db_table = "modelli3d"
#creo tabelle
Catalogo3d.create_table(Catalogo3d)
#creo contenuti nel db
modello1 = Catalogo3d.create(dipart_az = "AA33", nome_mod = "chiaveInglese", descrizione = "chiave del 13")
modello2 = Catalogo3d.create(dipart_az = "AA33", nome_mod = "dado", descrizione = "dado del 13")
modello1.save()
modello2.save()

#stampo il contenuto del db
modelli3d = Catalogo3d.select()
for modello in modelli3d:
    print(modello.dipart_az, modello.nome_mod, modello.descrizione)

#aggiungo modello di altro dipartimento aziendale
modello3 = Catalogo3d.create(dipart_az = "BB44", nome_mod = "staffa", descrizione = "staffa 30x20")
modello3.save()
#faccio una select solo del nuovo dipartimento
modelliBB44  = Catalogo3d.select().where(Catalogo3d.dipart_az=="BB44")
#...e la stampo a video
for el in modelliBB44:
    print(el.dipart_az, el.nome_mod, el.descrizione)


#ricerca
chiave = Catalogo3d.get(Catalogo3d.nome_mod=="chiaveInglese")

#cancellazione
chiave.delete_instance()

#stampa x riprova
modelli3d = Catalogo3d.select()
print("----"*4)
for modello in modelli3d:
    print(modello.dipart_az, modello.nome_mod, modello.descrizione)