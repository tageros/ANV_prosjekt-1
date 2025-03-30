# ANV_prosjekt-1
Mappe del 1

# Oppgave 2:

### 1.	Hvilke åpne datakilder er identifisert som relevante for miljødata, og hva er kriteriene (f.eks. kildeautoritet, datakvalitet, tilgjengelighet, brukervennlighet osv.) for å vurdere.
    Vi har benyttet oss av miljødata fra Yr og SeKlima, som begge drives av meteorologisk institutt. Denne kilden har god kildeautoritet, da meteorologisk institutt er en norsk statlig organisasjon med ansvar for værvarsling og forskningsvirksomhet innenfor meteorologi. Værdataen er derfor også kvalitetssikret data som vi kan stole på at stemmer overens med virkeligheten. Alt av miljødata som vi har brukt finner vi gratis på internett med god tilgjengelighet for alle. Yr er enkel nettside som hovedsakelig viser informasjon om været, mens SeKlima viser mer detaljert data som passer vår bruk.

### 2. Hvilke teknikker (f.eks. håndtering av CSV-filer, JSON-data) er valgt å bruke for å lese inn dataene, og hvordan påvirker disse valgene datakvaliteten og prosessen videre?
    Vi har valgt å bruke Pandas sin funksjonalitet i form av pandas.read_csv(). Denne er 	effektiv for å behandle CSV-filer i Python. Gjennom å bruke dette merket vi at pandas 	tolket informasjonen godt, og ga oss de svarene vi var ute etter. 

### 3.	Dersom det er brukt API-er, hvilke spesifikke API-er er valgt å bruke, og hva er de viktigste dataene som kan hentes fra disse kildene?
    Vi har valgt å ikke brukt APIer fordi vi benytter oss av historiske data fra 2024 som vi har hentet fra SeKlima. API er effektiv til data som kan oppdateres underveis, men siden vi bruker historiske data er ikke det nødvendig for oss å bruke API.

# Oppgave 3:

### 1.	Hvilke metoder vil du bruke for å identifisere og håndtere manglende verdier i datasettet?
    For å identifisere og håndtere manglende verdier i datasettet bruker vi Pandas.isnull(). Dette er en funksjon som sjekker etter manglende verdier i et datasett. Vi benyttet oss av denne da den gir oss en klar oversikt over hvor det er manglende data. 

### 2.	Kan du gi et eksempel på hvordan du vil bruke list comprehensions for å manipulere dataene?
    Vi har brukt list comprehensions for å bytte komma med punktum i datasettet, slik at tallene tolkes som desimaltall. Vi har også brukt list comprehensions til å endre tiden i datasettet fra norsk normaltid til Python sitt datetime-format.

### 3.	Hvordan kan Pandas SQL (sqldf) forbedre datamanipuleringen sammenlignet med tradisjonelle Pandas-operasjoner?
    Med Pandas SQL kan man bruke SQL-syntaks Pandas data som gjør det enklere å forstå informasjonen fra dataen. Sqldf kan gi kortere og mer oversiktlig kode som gjør det lettere å analysere og forstå store datasett. 

### 4.	Hvilke spesifikke uregelmessigheter i dataene forventer du å møte, og hvordan planlegger du å håndtere dem?
    Vanlige problemer som vi forventer å møte kan være verdier som mangler og datatyper som er feil. Disse uregelmessighetene kan løses ved hjelp av list comprehensions og pandas-funksjoner som Pandas.isnull(). 
