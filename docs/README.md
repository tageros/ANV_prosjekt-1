# DEL 1

## Oppgave 1:

Utviklingsmiljøet ble satt opp og testet med "test.ipynb" filen. Her testet vi også at vi kan importere de bibliotekene vi vil

## Oppgave 2:

### 1.	Hvilke åpne datakilder er identifisert som relevante for miljødata, og hva er kriteriene (f.eks. kildeautoritet, datakvalitet, tilgjengelighet, brukervennlighet osv.) for å vurdere.
Vi har benyttet oss av miljødata fra Yr og SeKlima, som begge drives av meteorologisk institutt. Denne kilden har god kildeautoritet, da meteorologisk institutt er en norsk statlig organisasjon med ansvar for værvarsling og forskningsvirksomhet innenfor meteorologi. Værdataen er derfor også kvalitetssikret data som vi kan stole på at den stemmer overens med virkeligheten. Alt av miljødata som vi har brukt finner vi gratis på internett med god tilgjengelighet for alle. Yr er enkel nettside som hovedsakelig viser informasjon om været, mens SeKlima viser mer detaljert data som passer vår bruk. 
Dataen vi har hentet er en csv-fil lastet ned fra Norsk Klimaservicesenter. Denne ble hentet ved å spsifisere hvilke tidsoppløsning, værelementer, tidsrom og for hvilke stasjon. Vi valgte henoldsvis timer, høyeste vindkast og Lufttempratur, 01.01.2024-01.01.2025, Slettnes Fyr. 

### 2. Hvilke teknikker (f.eks. håndtering av CSV-filer, JSON-data) er valgt å bruke for å lese inn dataene, og hvordan påvirker disse valgene datakvaliteten og prosessen videre?
Vi har valgt å bruke Pandas sin funksjonalitet i form av pandas.read_csv(). Denne er effektiv for å behandle CSV-filer i Python. Gjennom å bruke dette merket vi at pandas 	tolket informasjonen godt, og ga oss de svarene vi var ute etter. 

### 3.	Dersom det er brukt API-er, hvilke spesifikke API-er er valgt å bruke, og hva er de viktigste dataene som kan hentes fra disse kildene?
Vi har valgt å ikke brukt APIer fordi vi benytter oss av historiske data fra 2024 som vi har hentet fra SeKlima. API er effektiv til data som kan oppdateres underveis, men siden vi bruker historiske data er ikke det nødvendig for oss å bruke API. Samtidig prøvde vi å samle samme data ved bruk av frost API for å vise hvordan dette kunne gjøres, men det viste seg at data for høyeste vindkast per time ikke fantes ved Slettnes fyr.

## Oppgave 3:

### 1.	Hvilke metoder vil du bruke for å identifisere og håndtere manglende verdier i datasettet?
For å identifisere og håndtere manglende verdier i datasettet bruker vi Pandas.isnull(). Dette er en funksjon som sjekker etter manglende verdier i et datasett. Vi benyttet oss av denne da den gir oss en klar oversikt over hvor det er manglende data. Dersom vi hadde oppdaget manglende verdier i datasettet kunne vi brukt bevegelig gjennommsnitt (moving average) eller eksponensiell glatting (Exponential smoothing) for å glatte ut datasettet og bli kvitt uteliggere.

### 2.	Kan du gi et eksempel på hvordan du vil bruke list comprehensions for å manipulere dataene?
Vi har brukt list comprehensions for å bytte komma med punktum i datasettet, slik at tallene tolkes som desimaltall. Vi har også brukt list comprehensions til å endre tiden i datasettet fra norsk normaltid til Python sitt datetime-format. Ellers kan list comprehensions brukes for behandling av de ulike kolonnene i datasettet.

### 3.	Hvordan kan Pandas SQL (sqldf) forbedre datamanipuleringen sammenlignet med tradisjonelle Pandas-operasjoner?
Med Pandas SQL kan man bruke SQL-syntaks Pandas data som gjør det enklere å forstå informasjonen fra dataen. Sqldf kan gi kortere og mer oversiktlig kode som gjør det lettere å analysere og forstå store datasett. I dette prosjektet har vi brukt det for å kunne kun printe ut de to øverste linjene i csv filen for å analysere hvordan det er bygd opp slik at vi kunne håndtere datasettet.

### 4.	Hvilke spesifikke uregelmessigheter i dataene forventer du å møte, og hvordan planlegger du å håndtere dem?
Vanlige problemer som vi forventer å møte kan være verdier som mangler og datatyper som er feil. I tillegg kan det være at verdiene i datasettet har feil format. Disse uregelmessighetene kan løses ved hjelp av list comprehensions og innebygde funksjoner i python, numpy og pandas 



# DEL 2

## Oppgave 4

### 1. Hvordan kan du bruke NumPy og Pandas til å beregne gjennomsnitt, median og standardavvik for de innsamlede dataene, og hvorfor er disse statistiske målene viktige?
NumPy og Pandas gir raske og effektive måter å oppsummere store datasett på. Gjennomsnitt gir en generell verdi for datasettet, for eksempel gjennomsnittlig temperatur eller vindkast over perioden. Median brukes for å forstå den sentrale verdien, og er spesielt nyttig dersom datasettet har uteliggere eller skjevheter. Standardavvik forteller hvor mye verdiene sprer seg rundt gjennomsnittet, og gir innsikt i hvor stabile eller varierende forholdene er.
Disse målene er viktige fordi de gir en grunnleggende statistisk forståelse av datasettet ditt og hjelper deg å identifisere mønstre, avvik eller behov for videre analyse.

### 2. Kan du gi et eksempel på hvordan du vil implementere en enkel statistisk analyse for å undersøke sammenhengen mellom to variabler i datasettet?
En enkel måte å undersøke sammenhengen mellom to variabler – for eksempel vindkast og lufttemperatur – er å beregne korrelasjonskoeffisienten. Den gir en verdi mellom -1 og 1 som forteller hvor sterkt og i hvilken retning to variabler er relatert. En verdi som går mot 0 betyr at det er lite eller ingen sammenheng. Verdier som går mot 1 eller -1 tyder på sterk korrelasjon.

Ved vår beregning av korrelasjon får vi en verdi på -0.18. Dette viser at det er en liten sammenheng, men at det fortsatt har betydning. Den negative korrelasjonen tyder på at høyere verdier av vind henger sammen med lavere temperaturer.

### 3. Hvordan planlegger du å håndtere eventuelle skjevheter i dataene under analysen, og hvilke metoder vil du bruke for å sikre at analysen er pålitelig?
Skjevheter i data kan oppstå av mange grunner – uteliggere, målefeil, eller skjev fordeling. For å håndtere det har vi
fjerne eller vurdere uteliggere med visualiseringer som boxplots og sikret at dataen vi har samlet er standardisert. Under utførelse av korrelasjonsanalysen brukte vi flere metoder (Pearson, Spearman, kendall) for å sjekke om resultatene er konsistente. Ved å bruke hele datasettet og tydelig dokumentasjon av fremgangsmåten kan vi styrke påliteligheten 


### 4. Hvilke visualiseringer vil du lage for å støtte analysen din, og hvordan vil disse visualiseringene hjelpe deg med å formidle funnene dine?
For å videre støtte analysen samt utføre analysen har vi laget vanlige tidsseriegrafer for å vise utviklingen av vindkast og temperatur over tid, spredningsdiagram (scatterplot) som viser mulig sammenheng (korrelasjon) mellom vind og temperatur.
Ellers har vi laget et boxplot for å visualisere spredning og uteliggere, histogram for å vise fordelingen av hver variabel og heatmap for å se hvordan temperaturen er fordelt.
Disse visualiseringene gjør det enklere å formidle funnene visuelt, oppdage trender, mønstre og avvik, og gjør det lettere for andre å forstå.


## Oppgave 5

### 1. Hvilke spesifikke typer visualiseringer planlegger du å lage for å representere endringer i luftkvalitet og temperaturdata, og hvorfor valgte du disse?
For å vise endringer i dataene mine har vi valgt å bruke vanlige tidseriegrafer av det glidende gjennomsnittet (moving average) og heatmaps. Tidseriegrafer over lengre tid blir fort rotete og upversiktlig å analysere, derfor har vi brukt glidende gjennomsnitt for å glatte ut dataene og lettere kunne identifisere trender. Ved bruk av heatmaps kan vi også lettere se trender dag for dag, men også time for time.

### 2. Hvordan kan Matplotlib og Seaborn brukes til å forbedre forståelsen av de analyserte dataene, og hvilke funksjoner i disse bibliotekene vil være mest nyttige?
Matplotlib og Seaborn er kraftige visualiseringsverktøy for å gjøre analyser mer forståelige. Matplotlib gir deg full kontroll over hvordan figurer og akser presenteres. Den er fleksibel, og nyttig for klassiske grafer som linjeplott, stolpediagram og scatterplots. Seaborn bygger på Matplotlib og er designet for statistisk visualisering. Den gjør det lett å lage elegante grafer med mindre kode, og har innebygde funksjoner for automatisk gruppering, aggregering og bruk av fargepaletter.

### 3. Hvordan vil du håndtere og visualisere manglende data i grafene dine for å sikre at de fortsatt er informative?
Vi vil bruke moving average for å kunne gi en slags midlertidig fylling og oppnå en mer kontinuerlig fremstilling.

### 4. Kan du beskrive prosessen for å lage interaktive visualiseringer med Widgets, Plotly eller Bokeh, og hvilke fordeler dette kan gi i forhold til statiske visualiseringer?
Prosessen for å lage interaktive modeller var krevende da vi ikke har gjort dette før, men fortsatt veldig lærikt å kult. VI brukte Plotly fordi den brukes for å lage responsive grafer med hover-effekter, zoom, sliders og dropdown-meny. Da vi fikk lest oss opp fant vi ut at plotly kun trengte å lage dataserien for å så oppdatere oppsettet med en "range slider". ELlers valgte vi å gjøre modellene om til html filer fordi det var mer pålitelig og oversiktlig. Fordelene med interaktive modeller er at det lar oss utforske dataene selv og dermed blir det bedre for å presentere data.

### 5. Hvordan vil du evaluere effektiviteten av visualiseringene dine i å formidle de viktigste funnene fra dataanalysen til et bredere publikum?
Med de begrensede mengdene data vi jobbet med, har vi klart å presentere dataen

## Oppgave 6

### 1. Lag minst tre forskjellige typer visualiseringer (f.eks. linjediagrammer, søylediagrammer og scatterplots) for å representere endringer i luftkvalitet og temperaturdata over tid. Forklar valget av visualiseringstype for hver graf.

### 3. Implementer visualiseringer ved hjelp av Matplotlib og Seaborn. Inkluder tilpassede akser, titler, og fargepaletter for å forbedre lesbarheten og estetikk.

### 4. Demonstrer hvordan manglende data håndteres i visualiseringene. Lag en graf som viser hvordan manglende verdier påvirker datatrender, og diskuter hvordan dette kan påvirke tolkningen av dataene.

### 5. Skriv en kort evaluering av de utviklede visualiseringene. Diskuter hvilke visualiseringer som var mest effektive for å formidle informasjon, og hvorfor. Reflekter over tilbakemeldinger fra medstudenter eller veileder.



# Evaluering

- Skulle hatt mer data og jobbe med
- skulle brukt api for å kunne hente inn data, slik kunne dataen vært hentet frem til dagens dato, da ville vi kunne skjekket egen prognose opp mot prognoser fra yr eller storm. 
- Linjer regressjon er ikke en veldig passende regresjonslinje for slik type data. Det ville passet bedre med mer sykliske regresjonslinjer som sinus, eller logistisk.
- (kanskje bedre requirements.txt filen, den er ikke ryddet enda) 
