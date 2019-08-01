# EastPool

## Aihe

Biljardiliigan (East-Pool) tulospalvelu

## Heroku

[eastpool](https://eastpool.herokuapp.com/team/listTeam/)

Tässä vaiheessa toteutettu joukkuiden listaus ja joukkueen lisääminen tietokantaan. Näissäkin lyhenne menee nimen paikalle, 
ja lyhenne jää tyhjäksi. 

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

[user storyt](documents\UserStories.pdf)

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

 
