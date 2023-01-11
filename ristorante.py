'''
Si deve realizzare un sistema per un ristorante per gestire i clienti e i tavoli con il relativo numero di posti , le prenotazioni 
(effettuate dai clienti per un certo giorno e ora,e per un certo numero di persone).

Alle prenotazioni vengono assegnati uno o più tavoli (divisi in fumatori/non fumatori) , i camerieri che servono i clienti al tavolo e il conto, 
composto dalle singole portate ordinate.

Dei clienti interessano il nome e numero di telefono , mentre dei camerieri interessano
il nome e gli anni di servizio. Ogni portata ha un costo unitario previsto dal listino 
e al cliente viene presentato il conto dove vengono indicate le singole portate con il nome, il prezzo unitario e la quantità ordinata c
he permette di calcolare il totale per portate e il conto totale per gruppo.
'''
numero_tavoli = input("di quanti coperti dispone il ristorante?")
print("Perfetto, ristorante creato!"
numero_clienti = input("Quanti clienti abbiamo questa sera?")
if numero_clienti > n_tavoli:
    print("non possiamo, non abbiamo tutti quei posti!")
else:
    print("perfetto, siamo felici di accogliervi!")

numero_prenotazioni = input("Quante prenotazioni abbiamo?")
l_prenotazioni = []
l_orari = []
l_pers_tavolo = []

i=1
for i in range(numero_prenotazioni):
    print("Ordine numero "+ i +"/n")
    l_orari_dato = input("A che ora hanno ordinato il tavolo? ")
    l_orari.append(l_orari_dato)
    l_pers_tavolo_dato = input("Quante coperti hanno prenotato? ")
    l_pers_tavolo.append(l_pers_tavolo_dato)
    i+=1
