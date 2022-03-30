### 4. Céges autók

## 1. feladat

# Első lépésben nyissuk meg a fájlt:
file = open("autok.txt", 'r') # TextIOWrapper

# Olvassuk be az adatokat:
data = file.read()
file.close()
#print(data)  # ellenőrzésképpen írassuk ki, de aztán kommenteljük ki

# az adott sorokat szedjük listába:
data_list = data.split('\n')
#print(data_list)  # ellenőrzésképpen írassuk ki, de aztán kommenteljük ki

# A kapott elemeket bontsuk allistára

tablazat = [] # ebbe mentjük a sorok listáját

for i in range(len(data_list)):  # végighaladunk a data_list elemein
  sor = data_list[i].split(' ')  # az adott elemet szóköz mentén felbontjuk
  tablazat.append(sor)           # az adott sor listáját rendeljük a táblázathoz

#print(tablazat[-3:])            # ellenőrizzük le a táblázat végét, hogy tartalmaz-e üres listát (majd kommenteljük ki)

tablazat.pop()      # az utolsó elemet, ami egy üres stringet tartalmazó lista, távolítsuk el



## 2. feladat

# Írjuk ki a feladat sorszámát:
print('2. feladat')

# A feladatban meg kell keresnünk a legutolsó 0 értéket az utolsó oszlopban
#    ha megvan ennek az indexe akkor az adott sor többi oszlopából lehívhatjuk a kívánt értékeket

for i in range(len(tablazat)):    # menjünk végig a táblázat sorain
  if int(tablazat[i][-1]) == 0:   # ha a táblázat adott sorának utolsó eleme (egész számmá konvertálva) megegyezik a 0-val, akkor
    sor = i                       # a sor változónk legyen az adott sor indexe, ami az utolsó kihajtás sora

nap = tablazat[sor][0]            # a keresett nap a táblázat adott sorának 0. eleme
rendszam = tablazat[sor][2]         # a keresett rendszám a táblázat adott sorának 2. eleme


## 3. feladat

# Írjuk ki a feladat sorszámát:
print('3. feladat')

nap = input("Nap: ")                    # Kérjük be a nap sorszámát
print(f"Forgalom a(z) {nap}. napon:")   # Írjuk is ki

for i in range(len(tablazat)):        # menjünk végig a táblázat sorain
  if tablazat[i][0] == nap:           # ha az adott sorban szereplő nap sorszáma megegyezik a kívánttal, akkor
    ido = tablazat[i][1]              # az idő legyen az adott sorban szereplő
    rendszam = tablazat[i][2]         # a rendszám legyen az adott sorban szereplő
    szemely = tablazat[i][3]          # a személy legyen az adott sorban szereplő
    
    if int(tablazat[i][-1]) == 0:     # ha az adott sor utolsó eleme (egész számmá konvertálva) 0, akkor
      kibe = 'ki'                     # kihajtás történt,
    else:                             # különben
      kibe = 'be'                     # behajtás

    
    print(f"{ido} {rendszam} {szemely} {kibe}")   # Írjuk ki ezeket az értékeket a példának megfelelően
	
	

## 4. feladat

# Írjuk ki a feladat sorszámát
print("4. feladat")

# Számoljuk meg hogy hány alkalommal vittek el, illetve hoztak vissza autókat!

el = 0        # Ebben gyűjtjük az elvitelek számát
vissza = 0    # Ebben gyűjtjük a visszahozatalok számát

for i in range(len(tablazat)):  # menjünk végig a táblázat sorain
  if tablazat[i][-1] == "0":    # ha az utolsó oszlop értéke 0, akkor
    el += 1                     # növeljük eggyel az elvitelek számát
  else:                         # különben
    vissza += 1                 # növeljük a visszahozatalok számát

tavol = el - vissza             # ha az elvitelek számából levonjuk a visszahozatalokét, akkor megkapjuk, hogy hány autó van távol a hónap végén

print(f"A hónap végén {tavol} autót nem hoztak vissza.")  # Írassuk ki az eredményt a példának megfelelően



## 5. feladat

# Írjuk ki a feladat sorszámát
print("5. feladat")

# Készítsünk el a rendszámok listáját
rendszamok = []                           # Ebbe az üres listába gyűjtjük a rendszámokat

for i in range(len(tablazat)):            # Menjünk végig a táblázat sorain
  if tablazat[i][2] not in rendszamok:    # ha az aktuális rendszám még nincs a listában, akkor
    rendszamok.append(tablazat[i][2])     # rendeljük azt hozzá

rendszamok.sort()                         # végezetül rendezzük növekvő sorrendbe a rendszámokat
# print(rendszamok)                       # ellenőrzésképp írassuk ki, majd kommenteljük

# A következő lépésben minden egyes rendszám esetén meg kell keresnünk a legkisebb, illetve a legnagyobb kilométeróra-állást, majd eze különbsége adja a megtett utat

for rendszam in rendszamok:                     # menjünk végig a rendszámok litájának elemein
  oraallasok = []                               # hozzuk létre / ürtsük ki az óraállások listáját
  for i in range(len(tablazat)):                # a cikluson belül menjünk végig a táblázat sorain
    if tablazat[i][2] == rendszam:              # ha az adott sor rendszáma megegyezik az aktuálissal, akkor
      oraallasok.append(int(tablazat[i][4]))    # az egész számmá konvertált óraállást rendeljük hozzá a listához

  elso = oraallasok[0]                          # Ha a lista elkészült, mentsük ki az első és az 
  utolso = oraallasok[-1]                       # utolsó elemet
  ut = utolso - elso                            # a megtett út e kettőnek a különbsége lesz

  print(f"{rendszam} {ut} km")                  # a külső for cikluson belül írassuk ki a rendszámot és a hozzá tartozó megtett utat
  
  
  
  ## 6. feladat
  
  from IPython.core.display import Javascript
# Írjuk ki a feladat sorszámát:
print("6. feladat")

# Készítsük el a személyek listáját
szemelyek = []                          # Ebbe a listába mentjük a személyeket

for i in range(len(tablazat)):          # Menjünk végig a táblázat sorain
  if tablazat[i][3] not in szemelyek:   # ha az aktuális személy még nincs a személyek listájában, akkor 
    szemelyek.append(tablazat[i][3])    # rendeljük hozzá

szemelyek.sort()                        # végezetül rendezzük névsorba a listát

# Keressük meg a személyek által megtett leghosszabb utakat:
max_utak = []                             # Ebbe a listába mentjük a személyenként megtett leghosszabb utakat

for szemely in szemelyek:                 # menjünk végig a személyek listáján
  utak = []                               # ebbe a listába mentjük az egyes személyek megtett útjait

  for j in range(len(tablazat)):          # a cikluson belül haladjunk végig a táblázat sorain
    if tablazat[j][3] == szemely:         # ha az adott sorban szereplő személy megegyezik az adott személlyel, akkor
      if tablazat[j][-1] == '0':          # ha a sor utolsó eleme 0, azaz kihagyjottak a parkolóból, akkor
        indulas = int(tablazat[j][4])     # az indulás legyen az adott sorban szereplő óraállással
      else:                               # különben (tehát ha visszahozta az adott személy a kocsit)
        erkezes = int(tablazat[j][4])     # az adott sor óraállása legyen a visszatérési állás
        ut = erkezes - indulas            # a megtett út az érkezési és az indulási óraállás különbségével
        utak.append(ut)                   # az aktuálisan megtett utat rendeljük hozzá a személyenkénti utak listájába
  
  if utak != []:                          # ha az utak listája nem üres, akkor
    max_utak.append(max(utak))            # a személyhez tartozó leghosszabb utat rendeljük hozzá a max_utak listához
  else:                                   # különben (tehát ha üres) a személy nem hozta vissza az autót, ezért
    max_utak.append(0)                    # hozzá rendeljük a nulla értéket

# Keressük meg a leghosszabb utat a személyenkénti leghosszabb utak listájából
max_ut = max(max_utak)                # a leghosszabb út a lista legnagyobb eleme lesz
max_index = max_utak.index(max_ut)    # keressük meg hogy ez hányadik eleme a listának
max_szemely = szemelyek[max_index]    # keressük meg a leghosszabb úthoz tartozó személyt az előző index segítségével

print(f"Leghosszabb út: {max_ut} km, személy: {max_szemely}") # írjuk ki az eredményt a példának megfelelően



## 7. feladat

# Írjuk ki a feladat sorszámát
print("7. feladat")

# Kérjük be a rendszámot
rendszam = input("Rendszám: ")

# Hozzuk létre (írásra) a fájlt
f = open(rendszam + ".txt", "w")

for i in range(len(tablazat)):                                # Haladjunk végig a táblázat sorain
  if tablazat[i][2] == rendszam:                              # ha a sorban szereplő rendszám megegyezik a bekérttelel, akkor
    if tablazat[i][-1] == '0':                                # ha a sor utolsó eleme 0, azaz kihajtás történt, akkor
      szemely = tablazat[i][3]                                # a személyt,
      nap = tablazat[i][0]                                    # a napot,
      ido = tablazat[i][1]                                    # az időpontot és
      oraallas = tablazat [i][4]                              # az óraállást mentsük ki, majd
      f.write(f"{szemely}\t{nap}.\t{ido}\t{oraallas} km\t")   # tabulátorokkal elválasztva írjuk a fájlba ezeket a példának megfelelően (!a sor vége is tabulátorral végződjön)
    else:                                                     # különben (ha visszaérkezés történt)
      nap = tablazat[i][0]                                    # a napot,              
      ido = tablazat[i][1]                                    # az időpontot és
      oraallas = tablazat [i][4]                              # az óraállást mentsük ki, majd
      f.write(f"{nap}.\t{ido}\t{oraallas} km\n")              # (folytatva a sort) tabulátorokkal elválasztva írjuk a fájlba ezeket a példának megfelelően (! a sort sortöréssel zárjuk)

f.close()                       # zárjuk be a fájlt
print("Menetlevél kész.")       # írjuk ki, hogy a menetlevél kész

print(f"{nap}. nap rendszám: {rendszam}")    # Írjuk ki ezeket a példának megfelelően
