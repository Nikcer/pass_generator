import random
import string

print("Benvenuto nel generatore di password casuali!")
print("Il numero di caratteri della password deve essere compreso tra 8 e 15.")

while True:
    len_pswd = int(input("Scegli la lunghezza della password: "))

    if len_pswd >= 8 and len_pswd <= 15:
        print("")

        break

    else:
        print("Il numero dei caratteri non soddisfa le richieste! Inserisci nuovamente.")
        continue

caratteri = string.ascii_letters
numeri = string.digits
simboli = string.punctuation
password = ""
for i in range(0, len_pswd):
    password += random.choice(caratteri + numeri + simboli)
print("La password è:", password)
print("Grazie per aver scelto il nostro servizio")
        

    

