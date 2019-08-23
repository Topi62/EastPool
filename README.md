# EastPool

## Aihe

Biljardiliigan (East-Pool) tulospalvelu

## Heroku

[eastpool](https://eastpool.herokuapp.com)


## Käyttöohje

[Käyttö](documents/käyttöohje.md)

## Asennusohje

[Asennus](document/asennusohje.md)

## Tämän viikon tehtyjä

Viime kerran rästi, yhteenvetokysely, joka toteutuu taulukot - sarjataulukot, vielä kovakoodattu kaudelle 14 koska vain siellä 
pelattuja pelejä tietokannassa.

Pieniä korjauksia aiempiin tekemisiin.

Autorisointi, joskin rooleja käytössä vain Admin ja ANY. Tulossa pelaajien syöttö, joka vaatii roolia Captain. Player rooli 
joukkueen sisäiselle pistepörssille, jos ehdin sen toteuttaa. Visitor rooli jäänee tulevaisuuteen, jotta voidaan 
rekisteröidä mahdolliset kannustukset liveseurannassa.

Käytettävyyttä ja saavutettavuutta on ajateltu.

Käyttöohjetta on aloitettu, tätä tiedostoa on muokattu kovasti.

## Toteuttamatta

Tulospalvelu, liveseuranta, pelaajien lisäys puuttuu vielä. 

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

1. Team joukkueet, sarjataulukko näyttää paremmuusjärjestyksen
1. Player pelaajat, kuuluvat johonkin joukkueeseen, pistepörssi
1. Season kausi, syyskuusta toukokuulle vuosittain pelataan sarja, jonka parhaat palkitaan
1. Match ottelu, joukkueet kohtaavat kauden aikana sekä kotiottelussa, että vierasottelussa
1. Game pelit, pelaajat kohtaavat kolme x kolme henkisin joukkuein, pelientulos ratkaisee ottelun
1. Frame erät, pelin tulos ratkeaa erissä, East-Poolissa pelataan kolmeen voittoon

[tietokantakaavio](documents/EastPoolTK.pdf)

[Taulujen luonti](documents/CreateTables.md)

## User Storyt

[user storyt](documents/UserStories.pdf)

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

 
