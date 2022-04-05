## 1. Feladat

# Írjuk ki a feladat sorszámát
print("1. feladat")

# Olvassuk be a fájl tartalmát és mentsük változóba
f = open("melyseg.txt", "r")  # megnyitjuk a fájlt
tartalom = f.read()               # beolvassuk a tartalmát és mentjük
f.close()                     # bezárjuk a fájlt

# A fájl soronként egy adatot tartalmaz, alakítsuk listává
adat = tartalom.split('\n')
#print(adat[-3:])                # nézzük meg az utolsó három elemet, majd kommenteljük ki
adat.pop()                       # távolítsuk el az utolsó, üres elemet

# Írjuk ki a fájl adatainak számát:
hossz = len(adat)                           # nézzük meg az adatlista hosszát
print(f"A fájl adatainak száma: {hossz}")   # írjuk ki a példának megfelelően


## 2. Feladat

# Írjuk ki a feladat sorszámát
print("2. feladat")

# Kérjük be az adatot
tav = input("Adjon meg egy távolságértéket! ")

# Keressük ki a hozzá tartozó mélységet
idx = int(tav)-1      # a keresett hely a bekért érték - 1 lesz
melyseg = adat[idx]   # keressük vissza az adott indexhez tartozó értéket

# Írjuk ki az eredményt a példának megfelelően:
print(f"Ezen a helyen a felszín {melyseg} méter mélyen van.")


## 3. Feladat

# Írjuk ki a feladat sorszámát
print("3. feladat")

# Az lesz érintetlen felület, ahol a számérték nulla
erintetlen = 0        # ez adja a keresett területek számát

for item in adat:     # haladjuk végig a lista elemein
  if item == "0":     # ha az adott elem "0", akkor
    erintetlen += 1   # az érintetlen területek arányát növeljük eggyel

# Az arányhoz szükség lesz az első feladatban meghatározott összes adat mennyiségére (hossz)
arany = erintetlen / hossz                            # az érintetlen és az összes terület hányadosa adja a keresett arányt
szazalek = round(arany * 100, 2)                      # alakítsuk %-os formába és kerekítsük
print(f"Az érintetlen terület aránya {szazalek}%.")   # írjuk ki az eredményt a példának megfelelően



## 4. Feladat

# Hozzunk létre egy listát, ame tartalmazza a gödröket
oszlop = ""                 # Ez lesz az aktuális gödör
godrok = []                 # Ez lesz a gödröket tartalmazó lista

for item in adat:           # Menjünk végig az adatlista elemein
  if item != "0":             # Ha az adott elem nem nulla, akkor
    oszlop += item              # adjuk az adott mélységet a gödörhöz
  else:                       # Különben (ha az adott elem nulla),
    if oszlop != "":            # Ha az oszlop változó nem üres
      godrok.append(oszlop)       # rendeljük a listához az adott gödröt
      oszlop = ""                 # ürítsük ki a gödröt


# Hozzuk létre a fájlt, írásra
f = open("godrok.txt", "w")

# Írjuk fájlba az eredményeket
for i in range(len(godrok)):    # Menjünk végig a gödrök listáján
  if i == 0:                      # Az első elem esetében
    f.write(godrok[i])                # Írjuk a fájlba a gödröket
  else:                           # A többinél pedig
    f.write("\n")                     # Írjunk egy sortörést,
    f.write(godrok[i])                # majd a gödröket
# Zárjuk be a fájlt
f.close()


## 5. Feladat

# Írjuk ki a feladat sorszámát
print("5. feladat")

# Az előző feladatban létrehozott godrok lista hosszát határozzuk meg
godrok_szama = len(godrok)

# Írjuk ki az eredményt a példának megfelelően
print(f"A gödrök száma: {godrok_szama}")


## 6. feladat

# Írjuk ki a feladat sorszámát
print("6. feladat")

# a) feladat
print("a)")

# A 2. feladatban az idx változó tartalmazza a megadott helyet
# Az indexekel haladjunk előre és vissza, hogy megtaláljuk a kezdő és végpontot

i = idx
while adat[i] != "0":
  i +=1

j = idx
while adat[j] != "0":
  j -=1

# Írjuk ki az eredményt a példának megfelelően
print(f"A gödör kezdete: {j+2} méter, a gödör vége: {i} méter.")

# b) feladat
print("b)")

# Számoljuk ki a mélyülést
melyules = ['']                           # Ebbe fogjuk menteni a mélyüléseket, kezdetben tartalmazzon egy üres stringet (hogy indexelhető legyen az első ciklusban is)

for k in range(j,i+1):                    # Haladjunk végig a gödör kezdeti, illetve a végső - 1 indexei között
  if adat[k+1] > adat[k]:                   # Ha a következő mélység negyobb, mint az aktuális, és                
    if melyules[-1] != "mélyül":              # A mélyülés lista utolsó eleme nem a mélyül, akkor
      melyules.append("mélyül")                 # Rendeljük hozzá a listához a mélyülést
  elif adat[k+1] < adat[k]:                 # Viszont, ha a következő mélység kisebb, mint az aktuális, és
    if melyules[-1] != "emelkedik":           # A mélyülés lista utolsó eleme nem az emelkedik, akkor
      melyules.append("emelkedik")              # Rendeljük hozzá a listához az emelkedést

if len(melyules) == 3:                  # Ha folyamatosan mélyül, akkor tartalmazza az üres stringet, a mélyülést és az emelkedést, azaz 3 elemet
  print("Folyamatosan mélyül.")           # Ekkor írjuk ki az eredményt a példának megfelelően
else:                                   # Ha több eleme van, akkor 
  print("Nem mélyül folyamatosan.")       #Írjuk ki az eredményt a példának megfelelően
  
# c) feladat
print("c)")

# Menjünk végig a gödör mélységein, és mentsük ki a legnagyobb értéket
max_melyseg = "0"               # kiindulási állapot

for k in range(j, i):           # menjünk végig a j indextől az i-ig
  if adat[k] > max_melyseg:       # ha az aktuélis mélység nagyobb, mint a max_melyseg, akkor
    max_melyseg = adat[k]           # az adott mélység legyen a max_melyseg értéke

# Írjuk ki az eredményt a feladatnak megfelelően
print(f"A legnagyobb mélysége {max_melyseg} méter.")

# d) feladat
print("d)")

# Szedjük listába a mélységeket
melysegek = []                  # Ebbe mentjük a mélységeket

for k in range(j+1, i):         # Menjünk végig a kiindulási+1 indextől a végsőig
  melyseg = int(adat[k])          # Az aktuális mélységeket konvertáljuk egész számmá
  melysegek.append(melyseg)       # majd rendeljük hozzá a listához

# Számoljuk ki a keresztmetszet területét
A = sum(melysegek)    # mivel a hossz 1, ígg elegendő összegezni a mélységeket

# Számoljuk ki a térfogatot
V = A * 10

# Írjuk ki az eredményt
print(f"A térfogata {V} m^3.")

# e) feladat
print("e)")

# Számoljuk ki a gödrökben a maximális vízszintet
vizszintek = []
for melyseg in melysegek:
  vizszint = melyseg - 1
  vizszintek.append(vizszint)

# Számoljuk ki a keresztmetszet területét
A = sum(vizszintek)    # mivel a hossz 1, ígg elegendő összegezni a mélységeket

# Számoljuk ki a térfogatot
V = A * 10

# Írjuk ki az eredményt
print(f"A vízmennyiség {V} m^3.")