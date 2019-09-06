# Käyttöohje

## Aloitus

Sovelluksen auetessa tullaan index sivulle, jossa kerrotaan lyhyesti East-Poolin pitämästä biljardiliigasta. Käyttäjä voi aina
palata tälle sivulle navigaatiosta "Aloita"

## Käyttäjäroolit

Admin eli ylläpitäjä

Captain eli joukkueen kapteeni. Roolin antaa ylläpitäjä. Tämä voi tapahtua kahdella tapaa. Ylläpitäjä antaa jo joukkueeseen
kirjautuneelle käyttäjälle tai uusi käyttäjä rekisteröityy ensin olemassa olevaan joukkueeseen. Toinen vaihtoehto on, että uusi käyttäjä 
luo ensin uuden joukkueen, ja rekisteröi itsensä sitten sille joukkuetunnukselle. Ylläpitäjä sitten antaa roolin.

Player eli pelaaja, ei toimintoja tässä vaiheessa, mutta tulevaisuudessa joukkueen sisäiset palvelut.

Visitor eli vierailija. Ei toteuteta tässä vaiheessa, mutta tulevaisuudessa kirjautunut käyttäjä, joka voi kannustaa seuraamansa 
ottelun osapuolia.

## Rekisteröityminen

Rekistöityminen tapahtuu navigaatiosta "Käyttäjä" - "Rekisteröidy"

Kuka tahansa voi luoda itselleen tunnuksen olemassa olevalle joukkueelle. Mikäli joukkuetta ei vielä ole, on se luotava ensin. 
Ylläpitäjän lisää pyynnöstä kapteenin roolin käyttäjätunnukseen ja näin valvoo ettei kapteenille kuuluvia toimintoja voi tehdä 
ulkopuoliset. 

## Kirjautuminen

Kirjautuminen tapahtuu navigaatiosta "Käyttäjä" - "Kirjaudu"

Kirjautuminen tapahtuu 'Käyttäjä' valikosta valitsemalla 'Kirjaudu' ja antamalla luotu tunnus, joka sisältää Nimen ja Joukkueen,
 ja niihin liittyvän salasanan. Tämän jälkeen sivun navigointipalkin alla näkyy käyttäjän nimi, joukkue ja roolit.

### Tunnuksen vaatimukset

Tunnuksen nimessä saa olla vain kirjaimia ja välilyöntejä, sen tulee alkaa isolla kirjaimella, maksimipituus on 14 merkkiä.
Joukkueen lyhenne on kaksi isoa kirjainta ja numero.
Salasana saa sisältää vain kirjaimia tai numeroita ja maksimipituus on 8 merkkiä.

### Salasanan vaihto

Navigaatiosta "Käyttäjä" - "Vaihda salasana", näkyy vain kun käyttäjä on kirjautunut.

Kirjautunut käyttäjä voi vaihtaa salasanansa valikossa Käyttäjä.

### Tunnuksen poisto

Navigaatiosta "Käyttäjä" - "Poista tunnus", näkyy vain jos käyttäjällä on Admin-rooli

Ylläpitäjä voi poistaa käyttäjätunnuksen käytöstä.

## Ylläpitäjän tehtävät

Luo kauden, sen ottelut ja aikatauluttaa ottelut. Antaa ja poistaa rooleja muilta käyttäjiltä ja voi poistaa
muita käyttäjiä,

Navigaatiosta "Käyttäjä" - "Roolin lisäys"

Ylläpitäjä voi antaa roolin valitsemalleen käyttäjälle, hänen tulee tietää käyttäjän nimi ja joukkue.

Navigaatiosta "Käyttäjä" - "Roolin poisto"

Ylläpitäjä voi poistaa roolin valitsemaltaan käyttäjältä, hänen tulee tietää käyttäjän nimi ja joukkue.

Navigaatio "Ylläpito" näkyy vain, jos käyttäjällä on Admin-rooli

Navigaatiosta "Ylläpito" - "Joukkueet"

Ylläpitäjä näkee kaikki mukana olevat joukkueet.


### Kauden luonti

Navigaatiosta "Ylläpito" - "Kauden luonti"

Kautta luodessa näytetään jo olemassa olevat kaudet, Kaudelle annetaan sekä id-numero, että teksti. Eastpoolissa kausien id-numero
on sen järjestysnumero ja tekstinä vuosiluvut väliviivalla erotettuna. Esimerkiksi ensimmäinen kausi oli 1 2005-2006.

Luodessaan kauden ylläpitäjä voi valita boolean kentän otteluiden luonti, jolloin sovellus luo kaksin kertaisen sarjan ottelut 
luotavalle kaudelle. Ottelupäivämäärät jäävät tyhjiksi ja ylläpitäjä käyttäjälle avautuu sivu, jossa ottelut voi ajoittaa kalenterista, myös kellonaika on annettava.

### Pelien ajoitus

Navigaatiosta "Ylläpito" - "Pelien ajoitus", näkyy vain jos käyttäjällä on Admin-rooli

Sivulla näkyy ne ottelut, joille ei ole määritelty pelipäivää. Ylläpitäjä syöttää kenttiin ottelun osapuolet, päivämäärän kellonaikoineen ottelulle
ja kauden id:n. Tämän jälkeen kyseinen ottelu poistuu listalta.

Listalla näkyy kerrallaan maksimissaan 10 ottelua, kaikkia ajoittamattomia otteluita voi selata listan yläpuolisista linkeistä.
 
## Joukkueen kapteenin tehtävät

Lisää joukkueensa, lisää pelaajat joukkueeseensa ja tulospalvelussa kirjaa pelitapahtumat.

### Joukkueen lisäys

<a name="add team"></a>Joukkueen lisäys tapahtuu navigaatiosta "Kapteeneille" - "Joukkueen lisäys"

Kuka tahansa voi luoda joukkueen. Kun joukkue on luotu, voi käyttäjä rekisteröityä se tunnuksensa joukkueosana.

Joukkueelle on annettava tunnus, joka on kaksi isoa kirjainta ja numero. Sen on oltava uniikki, eli ei voi olla jo käytössä.

Joukkueen nimessä voi oll kirjaimia, numeroita ja välilyöntejä. Minimipituus 1 merkki maksimipituus on 15 merkkiä.

### Pelaajien lisäys

Navigaatiosta "Kapteeneille" - "Lisää pelaaja", näkyy vain jos käyttäjällä on Captain-rooli

Joukkueen kapteeni voi lisätä pelaajia joukkueeseen. Pelaajasta on annettava nimi, maksimi 14 merkkiä, sekä jäsennumero. 
Eastpoolissa kaikkien pelaajien on oltava yhdistyksen jäseniä. Tässä vaiheessa jäsennumeron oikeellisuutta ei tarkisteta, vain 
validointi, että kyseessä on maksimissaan kolme numeroa pitkä kokonaisluku.

### Tulospalvelu

Navigaatiosta "Ottelut" - "Tulospalvelu", näkyy vain jos käyttäjällä on Captain-rooli

Aluksi käyttäjä valitsee pudotusvalikosta ottelun. Valikossa näkyy ne ottelut, joiden pelipäivä on tänään tai aiemmin ja joissa
käyttäjällä on kapteeni rooli, eli hän on joko koti tai vierasjoukkueeseen rekisteröity kapteeniksi.

Seuraavaksi käyttäjä valitsee otteluun  pudotusvalikoista joukkueiden pelaajat. Valikoissa näkyvät joukkueeseen lisättyjen pelaajien
nimet ja jos pelaajaa ei vielä ole, pitää se käydä lisäämässä kapteenit - pelaajan lisäys  ja lisäystä varten kyseisen joukkueen kapteenin pitää kirjautua. Et siis voi lisätä pelaajaa kuin omaan joukkueeseesi.

Valikossa näkyy myös aina vaihtoehto "Ei Pelaajaa". Sallittua on pelata ottelu kahdella pelaajalla. Jos joukkue jättää tulematta, kirjaa 
paikalle saapunut kapteeni ottelutuloksen valitsemalla omat pelaajat ja vastustajalle jokaiseen kohtaan "Ei Pelaajaa". 

Valinnan jälkeen sovellus luo pelit (Game) tauluun yhdeksän peliä ja avaa ottelupöytäkirjan.

![tulospalvelu](https://user-images.githubusercontent.com/15327338/64434991-6b14b080-d0ca-11e9-8865-7cea6391d2b0.png)

Yllä olevassa kuvass  kuudes peli on alkanut ja Topi johtaa 1-0, alhaalta painikkeista voi valita kumpi Topi vai Hudde voittaa
seuraavan erän ja millä tavoin. 

Kun ottelupöytäkirja näkyy vain luettelo ottelun peleistä ja ruudukko. Kun pelin valitsee ja painaa "Valitse ja Aloita", sovellus tallentaa 
erälle aloitusajan ja lisää ottelupöytäkirjaan nuo eräpainikkeet ja peruutapainikkeen, jota ei vielä ole toteutettu. Tulevaisuudessa 
keskeneräisestä pelistä voi peruuttaa edellisen erän. Peli päättyy kun jompi kumpi pelaajista voittaa kolmannen erän.

Ottelun aluksi ja siis jokaisen pelin jälkeen tulee valita seuraavaksi pelattava peli. Listan järjestys on suositus, sillä se takaa
mahdollisimman tasaisen pelirytmin kaikille pelaajille.

Jos käyttäjä poistuu ottelupöytäkirjalta tai yhteys katkeaa, voidaan palata sinne Ottelut - Tulospalvelu ja  valitsemalla ottelu valikosta. Sovellus ohittaa pelaajien
valinnan, sillä tietokannassa on jo pelit. Vielä on korjaamatta se, ettei keskenjääneeseen peliin voi palata, vaan nyt joutuu valitsemaan
seuraavaksi pelattavan pelin, mutta tämä tullaan toki korjaamaan jatkossa.  

Jokainen erän voittopainikkeen painallus tallentaa tietokantaan erän päättymisajan ja tavan, erävoiton käynnissä olevaan peliin valitulle pelaajalle
ja mikäli kyseessä on kolmas erävoitto, kirjautuu pelivoitto kyseiselle joukkueelle ja mikäli pelivoitto on ottelun viides, kirjautuu otteluvoitto sarjataulukkoon.

## Kaikille avoinna

Katso kohta [joukkueen lisäys](#add team)

Ottelut Liveseuranta. Ei toteutettu vielä. Täältä tulevaisuudessa voi seurata menossa olevia pelejä reaaliajassa. Käyttäjä valitsee päivän otteluista haluamansa ja 
tämän jälkeen sivu päivittyy minuutin välein. 

Navigaatiosta "Ottelut" - "Tulevat ottelut"

Täältä näkee aikataulutetut tulevat ottelut. Sivu listaa tulevat ottelut aikajärjestyksessä.

Navigaatiosta "Ottelut" - "Pelatut ottelut"

Täältä näkee ottelutulokset pelatuista otteluista. Sivu listaa pelatut ottelut viimeksi pelattu ylimpänä 
eli käänteisessä aikajärjestyksessä.

Navigaatiosta "Taulukot" - "Sarjataulukko"

Sarjataulukko. Täältä näkee voimassa olevan joukkueiden sarjataulukon. Sivu näyttää viimeisimmän kauden joukkueiden 
sarjataulukon, nyt selaimen komentoriviltä voi vaihtaa kauden editoimalla viimeiset numerot ja painamalla siirry (Enter), mutta tulevaisuudessa sivulla on mahdollisuus valita kausi tai valita jonkin joukkueen tiedot eri kausilta.

Taulukot Pelaajapörssi. Ei toteutettu vielä. Täältä tulee näkemään voimassa olevan pelaajien pistepörssin. Sivu näyttää viimeisimmän kauden pelaajien pistepörssin, 
mutta  kausi on mahdollisuus valita tai on mahdollista valita jonkin pelaajan tiedot eri kausilta.
