# prova_pratica
Prova Pratica N.3 14-06-2021 Corso IFTS Grosseto
Valerio Tognozzi

Una azienda manifatturiera si e' dotata di una stampante 3D per la realizzazione di prototipi. Per ottimizzare le attivita' legate alla stampante 3D ha deciso di dotarsi di un software per la gestione e la catalogazione dei modelli utilizzabili nella stampante stessa. I modelli dovranno essere catalogati in base al dipartimento azinedale che li ha prodotti.
L'azienda ha inoltre manifestato l'esigenza di volere anche una manutenzione successiva di detto software.
Il candidato dovra' pertanto:

1. Progettare e ralizzare in python, mediante tecniche di programmazione orientste agli oggetti, tale programma. Il programma dovra' in particolare poter gestire (inserimento, modifica e cancellazione) i modelli 3D prodotti con tutti i ddttagli necessari (nome del modello e descrizione) nei diversi dipartimenti, consentire una ricerca per nome e una stampa a video di tutti i modelli presenti per i diversi dipartimenti.

2. estendere il software aggioungendo la possibilita' di salvare i dati in maniera permanente sul disco rigido, utilizzando un metodo a propria scelta ( pickle, sqlite, ORM...)

3. Creare un repository su github ed utilizzarlo per tutte le fasi di lavorazione del software, creando almeno un commit distinto per ogni punto di cui sopra.

----------------------------------------

Definizione delle scelte iniziali di composizione del software:

Creero' una classe Modello3d che avra' le caratteristiche : 
	nome_mod
	descriz
	dipart_az
la classe avra' i seguenti modulii
	modifica
	info_mod

Ceero' un classe Catalogo3d che avra' le seguenti caratteristiche:
	dipart_az
	modelli
la classe avra' i seguenti moduli:
	inserimento 
	modifica
	cancellazione
	stampa_catalogo
	ricerca

----------
per il secondo punto della prova ho deciso di utilizzare l' ORM peewee 

In questo caso utilizzero' solamente una classe la classe Catalogo3d che conterra' tutte le informazioni del modello3d e, essendo basata su database sqlite, avro' tutte le "comodita'" di accesso ai dati in un DB, utilizzando le varie query necessarie per i requisiti della prova.






	
