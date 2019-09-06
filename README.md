# EastPool

## Aihe

Biljardiliigan (East-Pool) tulospalvelu

## Heroku

[eastpool](https://eastpool.herokuapp.com)


## Käyttöohje

[Käyttö ohjeet](documents/kayttoohje.md)

## Asennusohje

[Asennus ohjeet](documents/asennusohje.md)

## Tämän viikon tehtyjä

Tulospalvelua on jatkettu, nyt ottelupöytäkirjassa valitaan peli, syötetään eriä ne tallentuvat oikein. Jos poistuu
ottelupöytäkirjasta, voi siihen palata, mutta vielä ei palata aloitettuun peliin, ja se jää loplta kesken.

Autorisointi, joskin rooleja käytössä vain Admin, Captain ja ANY. Tulevia: Player rooli 
joukkueen sisäiselle pistepörssille, jota en ehtine toteuttaa. Visitor rooli jäänee tulevaisuuteen, jotta voidaan 
rekisteröidä mahdolliset kannustukset liveseurannassa, jota en myöskään ehdi kurssin aikana saada alulle.

Käytettävyyttä ja saavutettavuutta on ajateltu, muotoiltu ottelupöytäkirjaa, mutta tämä kesken.

Käyttöohjetta on tarkoitus täydentää seuraavaksi, tätä tiedostoa on muokattu.

Testaajaa varten tieto, OT2, OT1, HB2 ja JI2 joukkueissa on pelaajat. Näitä vastaan peleissä testaus mielekkäämpää. 

## Toteuttamatta

Testaamatta miten sarjataulukkoon kirjautuu, jos ottelusta puuttuu pelaajia.

Tulospalvelussa vielä pari virhettä, keskeneräiseen peliin palaaminen ominaisuus puuttuu, joutuu valitsemaan seuraavan pelin, erien syötössä väärät nimet eikä näy edelliset
erät, liveseuranta. Pelaajia valittaessa Ei pelaajaa valinta ei toimi.

Liveseuranta jäänee kurssin ulkopuolelle, samoin pelaajien pistepörssi.

Tämän harjoituksen ulkopuolella on East-Poolin taustalla yhdistys, jolla on tarve omille nettisivuille
tiedottamisen kannalta. Toisaalta järjestetään myös muita kilpailuita ja esimerkiksi osallistujamäärään ja ottelukaavioon mukautuva
kisakaavio olisi hyvä lisä. Nykymuodossa jotkin asiat, kuten joukkuiden kohtaamisten määrä, joukkueen pelaajamäärä per ottelu ja 
erämäärä per peli on kovakoodattuja, nämä voisi olla ylläpitäjän valittavissa kullekin kaudelle.

## Testaus

Testaajaa varten on herokun kannassa käyttäjä 'Testaaja', joukkue 'TS1' ja salasana 'Testi' 
Kirjautuneen käyttäjän nimen perässä näkyy hänen roolinsa. Rooleja voi lisätä tai poistaa käyttäjä, jonka rooli on 'Admin'. Myös oman tunnuksen ja salasanan luonti on mahdollista.


## Taustaa 

East-Pool ravintolabiljardiliigaa on pelattu vuodeta 2005 lähtien Itä-Helsingin ravintoloissa. Nykyinen (kaudet 2009-2010…2018-2019) tulospalvelu tapahtuu ilmoittamalla tulos jälkikäteen php:lla ja mySql:llä
 toteuttamillani nettilomakkeilla ja tietokannalla.

Kurssin harjoitustyönä teen uuden tulospalvelun East-Poolille.

## Tietokantarakenne

1. Account, käyttäjät
1. Roles, käyttäjien roolit sovelluksessa
1. Team joukkueet, sarjataulukko näyttää paremmuusjärjestyksen
1. Player pelaajat, kuuluvat johonkin joukkueeseen, pistepörssi
1. Season kausi, syyskuusta toukokuulle vuosittain pelataan sarja, jonka parhaat palkitaan
1. Match ottelu, joukkueet kohtaavat kauden aikana sekä kotiottelussa, että vierasottelussa
1. Game pelit, pelaajat kohtaavat kolme x kolme henkisin joukkuein, pelientulos ratkaisee ottelun
1. Frame erät, pelin tulos ratkeaa erissä, East-Poolissa pelataan kolmeen voittoon

[tietokantakaavio](documents/EastPoolTK.pdf)

Account ja roles taulujen yhteys on nyt ohjelmallinen. Tulevaisuudessa muutan niin, että roles tauluun lisätään kenttä idaccount,
ja tämä toimii foreignkey kenttänä. Samalla poistetaan name ja team kentät tarpeettomana roles taulusta. Tätä en todennäköisesti
 ehdi tehdä kurssin aikana.

[Taulujen luonti](documents/createtables.md)

## User Storyt

[user storyt](documents/userstory.md)

### Käyttökuvauksien taustana ollut alustava luettelo 

1. joukkueen ilmoittautuminen, tunnuksien luonti
1. ottelukalenteri
1. ottelun pelikirjanpito
   1. (reaaliajassa)
   1. vaatii tunnistautumisen
1. ottelun etäseuranta
1. sarjataulukko per kausi
1. pistepörssi
   1. pelaajat per kausi
   1. joukkueen sisäinen

 
