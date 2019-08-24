# Asennusohje

Eastpool tietokantasovellus on toteutettu Pyhtonn Flask kirjastollalla,
 Sqlaclhemylla, Jinja2:lla. 
Tietokantana on paikallisasennuksessa Sqlite, Herokussa Postgresql.

Sovelluskehitystä ja versionhallintaa varten on tämä Github-repositio.

## Paikallisasennus

Koneessa tulee olla Python asennettuna. Jatkossa oletuksena on, että se
on versio 3.6.8, mutta sovellus toimii myös versiolla 2.7.15+.

### Virtuaaliympäristö

Paikallisasennuksessa tarvitaan virtuaaliympäristö venv. Asennus linuxissa kansio
nimiseen hakemistoon, johon luodaan virtuaaliympäristölle kansio polku:

```~/kansio$ python3 -m venv polku```

windowsssa:

```c:\Paht to Python\python 3 -m venv c:\kansio\polku```

Jatkossa komennot annetaan hakemistossa kansio, jos muuta ei mainita.

Luotu virtuaaliympäristö on aktivoitava. Tämä tapahtuu komennolla:

```source polku/bin/activate```
