# Käyttöohje

## Käyttäjäroolit

Admin eli ylläpitäjä

Captain eli joukkueen kapteeni

Player eli pelaaja, ei toimintoja tässä vaiheessa, mutta tulevaisuudessa joukkueen sisäiset palvelut.

Visitor eli vierailija. Ei toteuteta tässä vaiheessa, mutta tulevaisuudessa kirjautunut käyttäjä, joka voi kannustaa seuraamansa 
ottelun osapuolia.

## Rekisteröityminen

Kuka tahansa voi luoda itselleen tunnuksen olemassa olevalle joukkueelle. Mikäli joukkuetta ei vielä ole, on se luotava ensin. 
Ylläpitäjän lisää pyynnöstä kapteenin roolin käyttäjätunnukseen ja näin valvoo ettei kapteenille kuuluvia toimintoja voi tehdä 
ulkopuoliset. 

## Kirjautuminen

Kirjautuminen tapahtuu 'Käyttäjä' valikosta valitsemalla 'Kirjaudu' ja antamalla luotu tunnus, joka sisältää Nimen ja Joukkueen,
 ja niihin liittyvän salasanan. Tämän jälkeen sivun navigointipalkin alla näkyy käyttäjän nimi, joukkue ja roolit.

### Tunnuksen vaatimukset

Tunnuksen nimessä saa olla vain kirjaimia ja välilyöntejä, sen tulee alkaa isolla kirjaimella, maksimipituus on 14 merkkiä.
Joukkueen lyhenne on kaksi isoa kirjainta ja numero.
Salasana saa sisältää vain kirjaimia tai numeroita ja maksimipituus on 8 merkkiä.

### Salasanan vaihto

Kirjautunut käyttäjä voi vaihtaa salasanansa valikossa Käyttäjä.

### Tunnuksen poisto

Ylläpitäjä voi poistaa käyttäjätunnuksen käytöstä.

## Ylläpitäjän tehtävät

Luo kauden, sen ottelut ja aikatauluttaa ottelut. Antaa ja poistaa rooleja muilta käyttäjiltä ja voi poistaa
muita käyttäjiä,

### Kauden luonti

Kautta luodessa näytetään jo olemassa olevat kaudet, Kaudelle annetaan sekä id-numero, että teksti. Eastpoolissa kausien id-numero
on sen järjestysnumero ja tekstinä vuosiluvut väliviivalla erotettuna. Esimerkiksi ensimmäinen kausi oli 1 2005-2006.

Luodessaan kauden ylläpitäjä voi valita boolean kentän otteluiden luonti, jolloin sovellus luo kaksin kertaisen sarjan ottelut 
luotavalle kaudelle. Ottelupäivämäärät jäävät tyhjiksi ja näkyvät tämän jälkeen Pelien ajoitus sivulla.

### Pelien ajoitus

Sivulla näkyy ne ottelut, joille ei ole määritelty pelipäivää. Ylläpitäjä syöttää kenttiin ottelun osapuolet, päivämäärän ottelulle
ja kauden id:n. Tämän jälkeen kyseinen ottelu poistuu listalta.

## Joukkueen kapteenin tehtävät

Lisää joukkueensa, lisää pelaajat joukkueeseensa ja tulospalvelussa kirjaa pelitapahtumat.

### Joukkueen lisäys

Kuka tahansa voi luoda joukkueen. Kun joukkue on luotu, voi käyttäjä rekisteröityä se tunnuksensa joukkueosana.

Joukkueelle on annettava tunnus, joka on kaksi isoa kirjainta ja numero. Sen on oltava uniikki, eli ei voi olla jo käytössä.

Joukkueen nimessä voi oll kirjaimia, numeroita ja välilyöntejä. Maksimipituus on NN merkkiä.

### Pelaajien lisäys

Joukkueen kapteeni voi lisätä pelaajia joukkueeseen. Pelaajasta on annettava nimi, maksimi 14 merkkiä, sekä jäsennumero. 
Eastpoolissa kaikkien pelaajien on oltava yhdistyksen jäseniä. Tässä vaiheessa jäsennumeron oikeellisuutta ei tarkisteta, vain 
validointi, että kyseessä on maksimissaan kolme numeroa pitkä kokonaisluku.

## Kaikille avoinna

Joukkueen lisääminen.

Ottelut Liveseuranta. Täältä voi seurata menossa olevia pelejä reaaliajassa. Käyttäjä valitsee päivän otteluista haluamansa ja 
tämän jälkeen sivu päivittyy minuutin välein. 

Ottelut Tulevat ottelut. Täältä näkee aikataulutetut tulevat ottelut. Sivu listaa tulevat ottelut aikajärjestyksessä.

Ottelut Pelatut ottelut. Täältä näkee ottelutulokset pelatuista otteluista. Sivu listaa pelatut ottelut viimeksi pelattu ylimpänä 
eli käänteisessä aikajärjestyksessä.

Taulukot sarjataulukko. Täältä näkee voimassa olevan joukkueiden sarjataulukon. Sivu näyttää viimeisimmän kauden joukkueiden 
sarjataulukon, mutta tulevaisuudessa on mahdollisuus valita kausi tai valita jonkin joukkueen tiedot eri kausilta.

Tauluko pistepörssi. Täältä näkee voimassa olevan pelaajien pistepörssin. Sivu näyttää viimeisimmän kauden pelaajien pistepörssin, 
mutta tulevaisuudessa kausi on mahdollisuus valita tai on mahdollista valita jonkin pelaajan tiedot eri kausilta.
