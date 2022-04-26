## 1. Feladat

# Írjuk ki a feladat sorszámát
print("1. feladat")

# Kérjük be a fájl nevét
fajl = input("Adja meg a bemeneti fájl nevét! ")

# Kérjük be a sor számát
n_sor = int(input("Adja meg egy sor számát! ")) - 1

# Kérjük be az oszlop számát
n_oszlop = int(input("Adja meg egy oszlop számát! ")) - 1


## 2. Feladat

# Nyissuk meg a fájlt
f = open(fajl)
adat = f.read()

# Bontsuk fel az adatot sortörésenként
adat_lista = adat.split("\n")
# print(adat_lista) # ellenőrizzük

# Bontsuk fel a táblára és a lépésekre
tabla_nyers = adat_lista[:9] # az első 9 sor lesz a tálba
lepesek_nyers = adat_lista[9:-1] # a továbbiak a lépések (az utolsót kihagyjuk, mert az egy üres string)

# Bontsuk tovább a táblát
tabla = []

for i in range(len(tabla_nyers)):
  sor = tabla_nyers[i].split()
  tabla.append(sor)

#print(tabla[-3:])

# Bontsuk fel a lépéseket is
lepesek = []

for i in range(len(lepesek_nyers)):
  sor = lepesek_nyers[i].split()
  lepesek.append(sor)

#print(lepesek)


## 3. Feladat

# Írjuk ki a feladat sorszámát
print("3. feladat")

### 1. alfeladat ###
szam = tabla[n_sor][n_oszlop]
print(f"Az adott helyen szereplő szám: {szam}")

### 2. alfeladat ###
# Számoljuk ki, hogy melyik résztáblába tartoik
resztabla = n_sor // 3 * 3  + n_oszlop // 3 + 1

# Majd írjuk ki
print(f"A hely a(z) {resztabla} résztáblázathoz tartozik.")



## 4. Feladat

# Írjuk ki a feladat sorszámát
print("4. feladat")

# Ebbe a változóba mentjük az üres helek számát
ures = 0

# Menjünk végig a táblázat sorain, majd a sorok elemein
for i in range(9):
  for j in range(9):
    if tabla[i][j] == '0':  # Ha az adott elem '0', akkor
      ures += 1             # Növeljük az üres helyek számát eggyel

osszes = 9 * 9                        # Az összes mező száma 9 x 9
arany = round(ures / osszes *100, 1)  # Számoljuk ki az arányt

print(f"Az üres helyek aránya: {arany}% ")  # Írjuk ki az eredményt


## 5. Feladat

for lepes in lepesek:           # Menjünk végig a lépéseket tartalmazó sorokon
  szam = lepes[0]                 # Az első elem a szám
  sor = int(lepes[1]) - 1         # a második a sor --> ebből számoljuk az indexet
  oszlop = int(lepes[2]) - 1      # a harmadik az oszlop --> ebből számoljuk az indexet

  print(f"A kiválasztott sor: {sor + 1} oszlop: {oszlop + 1} a szám: {szam} ")  #Írjuk ki a feladatnak megfelelően a lépést

  #Vegyük sorra a lehetséges eseteket:
  eset = 0

  # A helyet már kitöltötték:
  if tabla[sor][oszlop] != '0': # Ha az adott sor, adott oszlopában a szám nem nulla, akkor
    eset = 1                      # A helyet kitöltötték --> 1. eset

  # Az adott sorban szerepel a szám:    
  if eset == 0 and szam in tabla[sor]:  # Ha az előző eset nem következett be, illetve az adott szám eleme a sor listájának
    eset = 2                                # Az adott sorban szerepel a szám --> 2. eset

  # Az adott oszlopban szerepel a szám:
  for i in range(len(tabla)):                     # Menjünk végig az oszlopokon
    if eset == 0 and tabla[i][oszlop] == szam:     # Ha a korábbi esetek nem következtek be, illetve az adott oszlop bármelyik sorában megtalálható a szám, akkor
      eset = 3                                        # Az adott oszlopban szerepel a szám -->3. eset

  # Az adott résztáblázatban szerepel a szám:
  resztabla = (sor // 3 ) * 3  + oszlop // 3 + 1    # Nézzük meg, hogy melyik résztáblába szeretne beírni

  for i in range(len(tabla)):                       # Menjünk végig minden soron, azon belül
    for j in range(len(tabla)):                       # Minden oszlopon
      if resztabla == (i // 3 ) * 3  + j // 3 + 1:      # Ha elérkezünk a kívánt résztáblához, és azon belül
        if tabla[i][j] == szam  and eset == 0:            # A korábbi esetek nem következtek be, illetve itt található a szám, akkor
          eset = 4                                          #Az adott résztáblában szerepel a szám --> 4. eset

  # Esetek következményei - írjuk ki a feladatban leírtak szerint:
  if eset == 1:
    print("A helyet már kitöltötték.")
  elif eset == 2:
    print("Az adott sorban már szerepel a szám.")
  elif eset == 3:
    print("Az adott oszlopban már szerepel a szám.")
  elif eset == 4:
    print("Az adott résztáblázatban már szerepel a szám.")
  else:
    print("A lépés megtehető.")