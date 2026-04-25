# Smart-library-system
Smart Library Management System with reservation and notification features (OOP coursework project)

# 1. ĮVADAS.

## Kas yra ši programa?

„Smart Library Management System“ yra Python kalba sukurta objektinio programavimo sistema, skirta bibliotekos veiklai valdyti. Programa leidžia tvarkyti knygas, vartotojus, knygų skolinimą, grąžinimą, rezervacijas bei pranešimus.

## Kaip programą paleisti?

1. Atsidarykite projektą su Visual Studio Code ar kitu Python IDE.
2. Įsitikinkite, kad turite įdiegtą Python.
3. Paleiskite programą: terminale įrašydami python main.py

## Kaip naudotis programa?
Programa leidžia:
- pridėti knygas
- pridėti vartotojus
- skolinti knygas
- grąžinti knygas
- rezervuoti knygas
- gauti pranešimus apie atsiradusią galimybę pasiimti rezervuotą knygą
- išsaugoti ir nuskaityti duomenis iš CSV failų


# 2. PROGRAMOS ANALIZĖ

## Funkcinių reikalavimų įgyvendinimas

Sistema susideda iš šių pagrindinių komponentų:
- `Book` klasė – saugo knygos informaciją ir jos prieinamumą
- `User`, `Student`, `Librarian` klasės – vartotojų valdymas
- `Reservation` klasė – rezervacijų saugojimas
- `Library` klasė – pagrindinė sistemos logika (skolinimas, grąžinimas, rezervavimas)
- `Notification` klasės – pranešimų siuntimas
- `FileHandler` klasė – duomenų saugojimas ir nuskaitymas iš CSV failų

## Objektinio programavimo principai

# Encapsulation 
Klasėse naudojami privatūs atributai (pvz. `_book_id`, `_title`, `_author`, `_is_available`), o prieiga prie jų vykdoma per metodus (`get_id()`, `get_title()` ir kt.). Tai apsaugo duomenis nuo neteisingo naudojimo.

# Inheritance 
Klasės `Student` ir `Librarian` paveldi `User` klasę. Tai leidžia išvengti pasikartojančio kodo ir sukurti aiškią klasės struktūrą.

# Polymorphism 
Skirtingos klasės (`EmailNotification` ir `SMSNotification`) turi tą patį metodą `send()`, tačiau jo veikimas skiriasi priklausomai nuo klasės.

# Abstraction 
Naudojama abstrakti klasė `Notification`, kuri apibrėžia bendrą metodą `send()`, tačiau jo realizacija paliekama konkrečioms klasėms.


## Dizaino šablonas 

Programoje naudojamas **Factory Method** dizaino šablonas.

Jis realizuotas `NotificationFactory` klasėje, kuri atsakinga už pranešimų objektų kūrimą.

Šis šablonas pasirinktas todėl, kad sistema gali turėti skirtingų tipų pranešimus (pvz. el. pašto ar SMS), o Factory leidžia:
- centralizuoti objektų kūrimą
- lengvai pridėti naujus pranešimų tipus
- sumažinti kodo priklausomybę

## Kompozicija 

`Library` klasė naudoja kompoziciją, nes ji „turi“:
- knygų sąrašą
- vartotojų sąrašą
- rezervacijų sąrašą

Tai reiškia, kad `Library` valdo kitus objektus kaip savo sudedamąsias dalis.

## Darbas su failais 

Sistema leidžia išsaugoti ir nuskaityti duomenis naudojant CSV formatą:
- `books.csv` – knygų duomenys
- `users.csv` – vartotojų duomenys

Tai įgyvendinta naudojant `FileHandler` klasę.


## Testavimas

Programos funkcionalumas testuojamas naudojant `unittest` modulį.

Testuojamos šios funkcijos:
- knygos skolinimas
- knygos grąžinimas
- knygos rezervavimas
- `NotificationFactory` veikimas
- klaidų atvejai (neteisingas pranešimo tipas)


# 3. Rezultatai

- Sukurta veikianti bibliotekos valdymo sistema naudojant Python ir OOP principus.
- Sėkmingai panaudoti visi keturi objektinio programavimo principai.
- Įgyvendintas Factory Method dizaino šablonas pranešimų kūrimui.
- Realizuotas duomenų saugojimas ir nuskaitymas iš CSV failų.
- Sukurti vienetiniai testai, patvirtinantys sistemos funkcionalumą.


# 4. Išvados

Šio darbo metu buvo sukurta pilnai veikianti bibliotekos valdymo sistema su rezervacijų ir pranešimų funkcionalumu.  
Programa demonstruoja objektinio programavimo principų taikymą, dizaino šablonų naudojimą bei tvarkingą kodo struktūrą.

Ateityje sistema galėtų būti išplėsta:
- sukuriant grafinę vartotojo sąsają
- naudojant duomenų bazę vietoje CSV failų
- pridedant terminų (due date) ir baudų sistemą
- išplečiant pranešimų tipus



# 5. Naudoti šaltiniai

- Python dokumentacija
- unittest dokumentacija
- PEP8 gairės
- Markdown dokumentacija
- GitHub dokumentacija






