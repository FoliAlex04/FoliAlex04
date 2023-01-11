n_tavoli = input("di quanti coperti dispone il ristorante?")
print("Perfetto, ristorante creato!")
n_clienti = input("Quanti clienti abbiamo questa serata?")
if n_clienti > n_tavoli:
    print("non possiamo, non abbiamo tutti quei posti!")
else:
    print("perfetto, siamo felici di accogliervi!")

n_prenotazioni = input("Quante prenotazioni diverse abbiamo?")
l_prenotazioni = []
l_orari = []
l_pers_tavolo = []

i=1
for i in range(n_prenotazioni):
    print("Ordine numero "+ i +"/n")
    l_orari_dato = input("A che ora hanno ordinato il tavolo? ")
    l_orari.append(l_orari_dato)
    l_pers_tavolo_dato = input("Quante coperti hanno prenotato? ")
    l_pers_tavolo.append(l_pers_tavolo_dato)
    i+=1
