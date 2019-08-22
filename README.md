# EastPool

## Aihe

Biljardiliigan (East-Pool) tulospalvelu

## Heroku

[eastpool](https://eastpool.herokuapp.com)

Sivusto käyttää Bootstrapia jo osittain. Omaa css tiedostoa ei lue paikallisesti, joten oma style layout.html:ssä.

Tässä vaiheessa toteutettuja:
  1. Käyttäjän rekisteröinti ja poisto
  2. Käyttäjän kirjautumine sisään ja ulos, salasanan vaihto, käyttäjän poisto
  3. Joukkuiden listaus ja joukkueen lisääminen tietokantaan
  4. Navigointipalkki, ihan kaikki ei vielä ole toteutettu
  5. Ylläpito kohdassa voi luoda uuden kauden ja ohjelmallisesti luoda kaksinkertaisen sarjan otteluiden pohjan olemassa oleville joukkueille
  6. Luoduille otteluille voi antaa pelipäivät yksitellen
  7. Tulevat ottelut ja pelatut ottelut voi listata
  8. Sarjataulukko toteuttaa yhteenvetokyselyn

Tässä vaiheessa pelattuja otteluita on vain muutama, jotta toiminnot voi tarkistella, samoin tulevia

  1. autorisoinnin täydennys
  2. asennusohje
  3. käyttöohje 

Tietokantana  on sqlite paikallisesti ja postgresql herokussa. 

Lomakkeet validoivat syötteen.

Tietotaulut tietokantakaavion mukaisesti, pieniä viilauksia ei ole päivitetty tietokantakaavioon.

Testaajaa varten on herokun kannassa käyttäjä 'Testaaja', joukkue 'TST' ja salasana 'Testi'
Kirjautuneen käyttäjän nimen näkymisen toteutus on vielä huono, pitäisi näkyä kentästä username, ei name + " " + team..
Myös oman tunnuksen ja salasanan luonti on mahdollista.

## Taustaa 

East-Pool ravintolabiljardiliigaa on pelattu vuodeta 2005 lähtien Itä-Helsingin ravintoloissa. Nykyinen (kaudet 2009-2010…2018-2019) tulospalvelu tapahtuu ilmoittamalla tulos jälkikäteen php:lla ja mySql:llä
 toteuttamillani nettilomakkeilla ja tietokannalla.

Kurssin harjoitustyönä teen uuden tulospalvelun East-Poolille.

## Tietotauluja

1. Team joukkueet, sarjataulukko näyttää paremmuusjärjestyksen
1. Player pelaajat, kuuluvat johonkin joukkueeseen, pistepörssi
1. Season kausi, syyskuusta toukokuulle vuosittain
1. Match ottelut, joukkueet kohtaavat
1. Game pelit, pelaajat kohtaavat, pelitulos ratkaisee ottelun
1. Frame erät, pelin tulos ratkeaa erissä

[tietokantakaavio](documents/EastPoolTK.pdf)

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

 
