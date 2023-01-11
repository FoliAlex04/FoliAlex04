
int main()
{
    int input;
    prenotazioni *lista = NULL;
    sale *lista2 = NULL;
    calendario *lista3 = NULL;

    do{

        printf("MENU\n");
        printf("-Inserisci 1 per inizializzare le lista delle prenotazioni\n -Inserisci 2 per inizializzare la lista delle aperture\n -Inserisci 3 per fare una prenotazione\n -Inserisci 4 per fare una prenotazione da file\n -Inserisci 5 per visualizzare i tavoli disponibili\n");
        scanf("%d",input);

            switch(input){

                case 1{

                    lista=inizializza("prenotazioni.txt", lista);

                }

                case 2{

                    lista3=inizializza_c("aperture.txt", lista3);

                }

                case 3{

                    lista=inserisci_prenotazione(lista);

                }

                case 4{

                    lista=inserisci_da_file("richieste.txt", lista);

                }

                case 5{

                    lista2=disponibili(lista2,lista3);

                }

            }

        }

    }
