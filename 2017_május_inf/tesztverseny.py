## 1. Feladat

f = open("valaszok.txt")
adat = f.read()
f.close()

# Bontsuk fel sortörések mentén az adatokat
adat_lista = adat.split('\n')
#adat_lista[:3] # Nézzük meg az első három elemet

# Az első elemet válasszuk le, ez lesz a helyes válasz
megoldas = adat_lista[0]

# Majd ezt töröljük
adat_lista = adat_lista[1:]

# Bontsuk fel szóközönként az adatlistát:
tablazat = []

for i in range(len(adat_lista)):
  sor = adat_lista[i].split()
  tablazat.append(sor)

# print(tablazat[-3:]) # Nézzük meg az utolsó három elemet
tablazat.pop() # Távolítsuk el az utolsó üres elemet

# Írjuk ki a feladatot a példának megfelelően:
print("1. feladat: Az adatok beolvasása")


## 2. Feladat

# Nézzük meg hány elemet tartalmaz a táblázat lista
hossz = len(tablazat)

# Írjuk ki a példának megfelelően
print(f"2. feladat: A vetélkedőn {hossz} versenyző indult.")


## 3. Feladat

# Kérjük be az azonosítót:
id = input("3. feladat: A versenyző azonosítója = ")

# Keressük meg a versenyzőt a táblázatban, és mentsük ki a válaszát
for i in range(len(tablazat)):  # Haladjunk végig a táblázat sorain
  if tablazat[i][0] == id:      # ha az adott sorban szereplő azonosító megegyezik a bekérttel, akkor
    valasz = tablazat[i][1]       # mentsük el a válszat
    break                         # Ha megvan, akkor lépjünk ki a for ciklusból

print(f"{valasz} (a versenyző válasza)")  # Írjuk ki az eredményt



## 4. Feladat

# Írjuk ki a feladat sorszámát
print("4. feladat:")

# Írjuk ki a helyes megoldást
print(f"{megoldas} (a helyes megoldás)")

# Menjünk végig a helyes megoldás karakterein, ha megegyezik a válasz karakterável, akkor + jelet tegyünk
for i in range(len(megoldas)):  
  if megoldas[i] == valasz[i]:
    print('+', end="")
  else:
    print(end=" ")

# Végül írjuk ki a maradék szöveget
print(" (a versenyző helyes válaszai)")


## 5. Feladat

# Kérjünk be egy sorszámot
no = int(input("5. feladat: A feladat sorszáma = "))

# Menjünk végig a táblázaton, és az adott sorból, a válaszok közül keressük ki a bekért indexű elemet
db = 0
helyes_valasz = megoldas[no - 1]  # Az indexelés miatt egyet le kell vonni

for i in range(len(tablazat)):
  if tablazat[i][1][no - 1] == helyes_valasz: # 1. index a sor, a 2. az oszlop, a 3. pedig a karakterek
    db += 1

arany = round(db / hossz * 100, 2)
# Írjuk ki a megoldást:
print(f"A feladatra {db} fő, a versenyzők {arany}%-a adott helyes választ.")


## 6. feladat

# Írjuk ki a feladat sorszámát
print("6. feladat: A versenyzők pontszámának meghatározása")

# Hozzuk létre a pontok listáját
pontok = []

for i in range(len(megoldas)):
  if i < 5:
    pontok.append(3)
  elif i < 10:
    pontok.append(4)
  elif i <13:
    pontok.append(5)
  else:
    pontok.append(6)

# print(pontok) # Ellenőrizzünk

# Hozzuk létre a fájlt, amibe írni fogunk
f = open("pontok.txt", "w")

#Menjünk végig a táblázat sorain, majd minden versenyző esetén vizsgáljuk meg a válaszokat
pontszamok = []

for i in range(len(tablazat)):  # Menjünk végig a táblázat sorain
  versenyzo = tablazat[i][0]    # Mentsük ki az adott sorban lévő versenyző azonosítóját, valamint
  valasz = tablazat[i][1]       # Az adott választ
  pontszam = 0                  # a pontszámokat ebbe gyűjtjük, kiindulási értéke legyen 0

  for j in range(len(valasz)):    #Menjünk végig a válasz string karakterein
    if valasz[j] == megoldas[j]:  # Ha a válasz adott indexű karaktere megegyezik a helyes válasz adott indexű karakterével, akkor
      pontszam += pontok[j]       # Adjuk az eddigi pontokhoz az aktuális feladathoz tartozó pontszámot

  pontszamok.append(pontszam)           # Mentsük ki a pontszámokat (A következő feladathoz szükséges!)
  f.write(f"{versenyzo} {pontszam}\n")  # Írjuk a fáljba a kért adatokat

f.close()   # Zárjuk be a fájlt


## 7. feladat

# Írjuk ki a feladatot
print("7. feladat: A verseny legjobbjai:")

# Határozzuk meg az első három helyezett pontszámait
sorrend = pontszamok[:]       # Csináljunk másolatot a pontszámokból, majd
sorrend.sort(reverse=True)    # Tegyük csökkenő sorrendbe
helyezes_pontok = []          # Ebbe a listába mentjük ki a díjazottak pontszámait

for pont in sorrend:              # Menjünk végig a csökkenő sorrendű pontszámokon
  if len(helyezes_pontok) == 3:       # Ha a helyes pontszámok listájában 3 elem szerepel,
    break                               # Lépjünk ki
  elif pont not in helyezes_pontok:   # Ha viszont az aktuális pont még nincs a listában, 
    helyezes_pontok.append(pont)        # Rendeljük hozzá

#print(helyezes_pontok) # Ellenőrzés!

for i in range(len(helyezes_pontok)):                                   # Menjünk végig a helyezésekhez tartozó pontok listáján
  for j in range(len(pontszamok)):                                        # Minden pont esetében menjünk végig a pontszámokon.
    if pontszamok[j] == sorrend[i]:                                         # Ha a helyezésért járó pontszám megegyzik a versenyző összpontszámával,
      print(f"{i+1}. díj ({helyezes_pontok[i]} pont): {tablazat[j][0]}")      #  akkor írjuk ki a helyezést, a pontszámot, illetve a versenyző azonosítóját