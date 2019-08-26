# Asennusohje

Eastpool tietokantasovellus on toteutettu Pyhtonn Flask kirjastollalla, tietokantana on 
paikallisasennuksessa Sqlite, Herokussa Postgresql.

Sovelluskehitystä ja versionhallintaa varten on tämä Github-repositio.

## Paikallisasennus

Koneessa tulee olla Python 3.6.8+ ja [Git](https://git-scm.com) asennettuna. 

### Sovelluksen lataaminen Githubista

Lataa sovellus Githubista kansioon komennolla

```~/kansio git clone https://github.com/Topi62/Eastpool.git```

### Virtuaaliympäristö

Paikallisasennuksessa tarvitaan Pythonin virtuaaliympäristö venv. Asennus linuxissa 'kansio'
nimiseen hakemistoon, johon luodaan virtuaaliympäristölle hakemisto 'polku':

```~/kansio$ python3 -m venv polku```

windowsssa:

```c:\Path to Python\python3 -m venv c:\kansio\polku```

Jatkossa asennuksen esimerkkikoodi ovat linuxissa, mutta komennot ovat
samat windowsissakin.

Luotu virtuaaliympäristö on aktivoitava. Tämä tapahtuu komennolla:

```~/kansio$ source polku/bin/activate```

Komentokehotteen eteen tullut (polku) kertoo, että ympäristö on aktiivinen.


### Riippuvuudet

Sovelluksen tarvitsemat riippuvuudet on tiedostossa requiments.txt. Ne asennetaan komennolla:

```(polku) ~/kansio$ pip install -r requiments.txt```

Asennuksen palaute kertoo, jos uudempi versio pip asennuspakettiin  on saatavilla,
tämä on hyvä päivittää

```(polku) ~/kansio$ pip install --upgrade pip```

### Käynnistäminen

Kun virtuaaliympäristö on aktiivinen ja riippuvuudet asennettu, käynnistä sovellus komennolla:

```(polku) ~/kansio python3 run.py```

Sovellus on nyt käytettävissä selaimella osoitteessa http://127.0.0.1:5000

Katso käytöstä [ohjeesta](käyttöohje.md).

## Asentaminen Herokuun

Oletuksena on, että käytössä on [Heroku tili](https://signup.heroku.com/signup/dc), Heroku CLI, [Git](https://git-scm.com) ja Python 3 asennettuna paikallisesti.

### Lataa sovellus paikalliseen kansioon

``` git clone https://github.com/Topi62/Eastpool.git```

### Luo Heroku sovellus

Luodessasi sovelluksen Herokuun, voit antaa sovellukselle nimen, jonka täytyy olla yksilöllinen. Jos et keksi nimeä, voit jättää
nimen pois, jolloin Heroku luo nimen automaattisesti

``` heroku create [nimi]```

### Kopioi sovellus Herokuun

Koodin kopiointi Herokuun komennolla:

```git push heroku master```

### Sovelluksen käyttö

Nyt sovellus on käytettävissä selaimella osoitteessa 'nimi.herokuapp.com'
