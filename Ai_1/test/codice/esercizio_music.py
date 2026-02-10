import pandas as pd

## Esercizio 1: Carica il CSV in un DataFrame
## Task: Leggi i dati del file CSV fornito in un Pandas DataFrame e visualizza le prime 3 righe  
## Soluzione:
print("***ESERCIZIO 1***")
csv_path="../dati/SomeMusicAlbums(1).csv"
df=pd.read_csv(csv_path)
print(df.head(3)) #leggi le prime 3 righe con head(di base proietta i primi 5 elem)
print("*****************"+"\n")    
 
### Esercizio 2: Mostra informazioni di base sul DataFrame 
### Task: Mostra il numero di righe, colonne e tipi di dati per ogni colonna 
### Soluzione:
print("***ESERCIZIO 2***")
df2=pd.read_csv(csv_path)
print(df.shape)
print(df.dtypes)

print("*****************"+"\n")
 

### Esercizio 3: Filtra gli album per genere
### Task: Crea un nuovo DataFrame contenente solo gli album con "rock" nella colonna 'Genre'
### Soluzione:
print("***ESERCIZIO 3***")
df3=pd.read_csv(csv_path)
rock=df3[df3["Genre"].str.contains("rock",case=False)]
print(rock)

print("*****************"+"\n")

## Esercizio 4: Trova gli album pubblicati dopo il 1980
## Task: Filtra gli album pubblicati dopo il 1980 e visualizza solo le colonne 'Artist', 'Album' e 'Released'
## Soluzione:
print("***ESERCIZIO 4***")

df4=pd.read_csv(csv_path)
cond=df4["Released"]>1980
print(df4[cond][["Artist","Album","Released"]])

print("*****************"+"\n")


### Esercizio 5: Calcola la media delle valutazioni
### Task: Calcola la media della colonna 'Rating' per tutti gli album
### Soluzione:
print("***ESERCIZIO 5***")
df5=pd.read_csv(csv_path)
media=df5["Rating"].mean()
print(media)


print("*****************"+"\n")

### Esercizio 6: Trova l'album più lungo e il più breve
### Task: Identifica l'album con la durata massima e minima nella colonna 'Length' e visualizza i suoi dettagli
### Soluzione:
print("***ESERCIZIO 6***")
df6 = pd.read_csv(csv_path)
massimo = df6["Length"].max()
minimo = df6["Length"].min()

print("Durata massima:", massimo)
print("Durata minima:", minimo)
print("\nAlbum con durata massima:")
print(df6[df6["Length"] == massimo])
print("\nAlbum con durata minima:")
print(df6[df6["Length"] == minimo])
print("*****************"+"\n")
 
### NON FARE
### Esercizio 7: Elenco generi unici
### Task: Estrai e stampa tutti i generi unici nel dataset (dividendo i generi combinati come "pop, rock")
### Soluzione:
print("***ESERCIZIO 7***")
df7=pd.read_csv(csv_path)
generi=df7["Genre"].str.split(", ")

print(df7["Genre"].unique())
print("*****************"+"\n")

### Esercizio 8: Confronta le vendite con vendite dichiarate
### Task: Aggiungi una nuova colonna 'Sales_Difference' che mostri la differenza tra 'Claimed Sales' e 'Music Recording Sales'
### Soluzione:
print("***ESERCIZIO 8***")
df8 = pd.read_csv(csv_path)
# Calcolo differenza corretta
df8["Sales_Difference"] = df8["Claimed Sales (millions)"] - df8["Music Recording Sales (millions)"]
print("Sales Difference:")
print(df8["Sales_Difference"])

  
### Esercizio 9: Trova gli album colonna sonora
### Task: Elenca tutti gli album contrassegnati come 'Soundtrack' (dove la colonna è "Y")
### Soluzione:
print("***ESERCIZIO 9***")
df9=pd.read_csv(csv_path)
cond=df9[df9["Soundtrack"]=="Y"]
print(cond[["Album","Artist"]])
print("*****************"+"\n")

### Esercizio 10: Salva i dati filtrati in un file CSV
### Task: Salva tutti gli album con una valutazione (Rating) ≥ 9 in un nuovo file CSV
### Soluzione:
print("***ESERCIZIO 10***")
df10=pd.read_csv(csv_path)
reting=df10[df10["Rating"]>=9]
reting.to_csv("rating.csv")
print(reting[["Album","Artist","Rating"]])

print("******************"+"\n")

### NON FARE  
### Esercizio 11: Conta gli album per genere
### Task:Conta quanti album appartengono a ogni genere unico (dividendo generi combinati come "pop, rock")
### Soluzione:  
print("***ESERCIZIO 11***")
df11=pd.read_csv(csv_path)
generi_divisi=df11["Genre"].str.split(",")
generi_divisi = df11["Genre"].str.split(",").explode().str.strip().str.lower()
print( generi_divisi.value_counts())
print("******************"+"\n")

### Esercizio 12: Trova l'album con la maggior differenza tra vendite e vendite dichiarate
### Task: Identifica l'album con la maggiore differenza tra 'Claimed Sales' e 'Music Recording Sales' e visualizza i suoi dettagli
### Soluzione:  
print("***ESERCIZIO 12***")
df12=pd.read_csv(csv_path)
df12["differenza_prezzo"]=(df12["Claimed Sales (millions)"]-df12["Music Recording Sales (millions)"])
max_diff=df12["differenza_prezzo"].max()
album=df12[df12["differenza_prezzo"]==max_diff] 

print("differenza massima:",max_diff)
print("Album con la maggior differenza:")
print(album[["Artist","Album","differenza_prezzo"]])
print("******************"+"\n")
  
### Esercizio 13: Filtra gli album per generi multipli
### Task: Crea un nuovo DataFrame contenente gli album che includono entrambi "rock" e "pop" nella colonna 'Genre'
### Soluzione:**  
print("***ESERCIZIO 13***")
df13=pd.read_csv(csv_path)
condizione=df13["Genre"].str.contains("pop") & df13["Genre"].str.contains("rock")
print(df13[condizione])
print("******************"+"\n")

### NON FARE    
### Esercizio 14: Calcola la durata media per genere
### Task: Calcola la media della durata (in minuti) degli album per ogni genere (dividendo generi combinati)
### Soluzione:  
print("***ESERCIZIO 14***")

df14 = pd.read_csv(csv_path)
# 1. Split dei generi
df14["Genre"] = df14["Genre"].str.split(",")
# 2. Esplosione delle righe
df14_new = df14.explode("Genre")
# 3. Rimuovi spazi
df14_new["Genre"] = df14_new["Genre"].str.strip()
# 4. Conversione della durata
df14_new["Length"] = pd.to_numeric(df14_new["Length"], errors="coerce")

# 5. Calcolo della media
media= df14_new["Length"].mean()
print(media)


print("******************"+"\n")

### Esercizio 15: Trova l'album più venduto che non è una colonna sonora
### Task: Identifica l'album con le maggiori 'Music Recording Sales' che non è una colonna sonora
### Soluzione:  
print("***ESERCIZIO 15***")

print("******************"+"\n")