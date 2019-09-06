# Käyttökuvaukset

## Ilmoittautuminen

1. Joukkueen ilmoittautuminen liigaan. "Kapteenina voin ilmoittaa joukkueen liigaan." 

   Valikosta Kapteeneille - Joukkueen lisäys

   Jos lomake läpäisee validoinnin ja kysely
´´´sql
   SELECT * FROM team WHERE shortname = 'Joukkueen lyhenne'";
´´´
   ei palauta joukkuetta,

   luodaan uusi joukkue kyselyllä "INSERT INTO team(shortname, longname) VALUES ('Joukkueen lyhenne', 'Joukkueen nimi') 

## Rekisteröityminen

2. Käyttäjä voi rekisteröityä. "Käyttäjä voi määritellä tunnuksen ja salasanan itselleen."

   Valikosta Käyttäjä - Rekisteröidy

   Jos salasana on syötetty kaksi kertaa samoin ja lomake läpäisee validoinnit ja kysely 
´´´sql
   SELECT * FROM account WHERE name = 'Nimi' AND team = 'Joukkue';
´´´
   ei palauta käyttäjää

   luodaan uusi käyttäjä kyselyllä 
´´´sql
   INSERT INTO account(id, date_created, date_modified, name, team, password) VALUES (max(id)+1,
   CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Nimi', 'Joukkue', 'Salasana');
´´´ 

### Kirjautuminen

   Käyttäjä voi kirjautua.

   Valikosta Käyttäjä - Kirjaudu

   Jos lomake läpäisee validoinnin ja kysely 
´´´sql
   SELECT * FROM account WHERE name = 'Nimi', team = 'Joukkue' ja password ='Salasana';
´´´
   palauttaa käyttäjän, kirjataan kyseinen käyttäjä sisäään.

### Salasanan vaihto

   Käyttäjä voi vaihtaa salasanansa, kun on kirjautuneena.

   Jos lomake läpäisee validoinnin, sovellus hakee käyttäjän tiedot tietokannasta current_user.name ja current_user.team tiedoilla ja
   päivittää salasaan kyselyllä 
'''sql
   UPDATE account SET date_modified = CURRENT_TIMESTAMP, password = 'Salasana' WHERE id = ?
´´´ 

## Ottelukalenteri

3. Kaikki voivat nähdä ottelukalenterin.

   Valikosta Ottelut - Tulevat ottelut

   Näyttää kyselyn 
´´´sql
   SELECT to_char(date, 'DD.MM. HH24:MI') AS gamedate, hometeamid, visitorteamid FROM match where date > :today
   ORDER BY date ASC;
´´´
    palauttamat tiedot taulusta match.

### Pelatut ottelut

   Valikosta Ottelut - Pelatut ottelut

   Näyttää kyselyn 
´´´sql
   SELECT to_char(date, 'DD.MM.') AS gamedate, hometeamid, visitorteamid, homegamenumwins, visitorgamenumwins
   FROM match where status <> 'T' ORDER BY date DESC
´´´
    palauttamat tiedot taulusta match.
    
## Tulospalvelu

   Valikosta Ottelut - Tulospalvelu

   Tulospalveluun sisältyy lukuisia select, count, update kyselyitä tietokantaan. Liitoksista esimerkki, joka on toteutetu sqlalchemyllä :

´´´python
´´´games = db.session.query(Game.idmatch, Game.idgame, Game.homeframewins, Game.visitorframewins, H.name.label('homePlayerName'), V.name.label('visitPlayerName')).\\
´´´        join(H,(Game.homeplayerid == H.idplayer)).\\
´´´        join(V, (Game.visitorplayerid == V.idplayer)).\\
´´´        filter(Game.idmatch==idmatch).\\
´´´        order_by(asc(Game.idgame))
´´´

## Liveseuranta

   Ei toteutettu vielä

## Sarjataulukko

5 Sarjataulukko per kausi. 

   Valikosta Taulukot - Sarjataulukko

   Kysely = SELECT team.longname,
            (SELECT count(idmatch) FROM match WHERE idseason= :season AND homegamenumwins>4 AND hometeamid = team.shortname)
             + (SELECT count(idmatch) FROM match  WHERE idseason= :season AND visitgamenumwins>4 AND visitorteamid = team.shortname)
             AS voitot, 
            (SELECT count(idmatch) FROM match WHERE idseason= :season AND visitgamenumwins>4 AND hometeamid = team.shortname) 
             + (SELECT count(idmatch) FROM match  WHERE idseason= :season AND homegamenumwins>4 AND visitorteamid = team.shortname)
             AS tappiot,          
            (SELECT COALESCE(sum(homegamenumwins),0) FROM match WHERE idseason= :season AND hometeamid = team.shortname) 
             + (SELECT COALESCE(sum(visitgamenumwins), 0) FROM match  WHERE idseason= :season AND visitorteamid = team.shortname)
             AS pelivoitot,
            (SELECT COALESCE(sum(visitgamenumwins),0) FROM match WHERE idseason= :season AND hometeamid = team.shortname)
             + (SELECT COALESCE(sum(homegamenumwins),0) FROM match  WHERE idseason= :season AND visitorteamid = team.shortname)
             AS pelitappiot,
            (SELECT COALESCE(sum(homeframewins),0) FROM game JOIN match ON game.idmatch = match.idmatch WHERE idseason= :season AND
             hometeamid = team.shortname) + (SELECT COALESCE(sum(visitorframewins), 0) FROM game JOIN match ON game.idmatch = 
	     match.idmatch WHERE idseason= :season AND visitorteamid = team.shortname) AS erävoitot,
            (SELECT COALESCE(sum(visitorframewins),0) FROM game JOIN match ON game.idmatch = match.idmatch WHERE idseason= :season
             AND hometeamid = team.shortname) + (SELECT COALESCE(sum(homeframewins),0) FROM game JOIN match ON game.idmatch =
             match.idmatch WHERE idseason= :season AND visitorteamid = team.shortname) AS erätappiot
            FROM team GROUP BY team.shortname, team.longname ORDER BY voitot DESC, pelivoitot  DESC, erävoitot  DESC "


   Alikyselyt suoritetaan kerran kullekin joukkueelle eli vaativuus 12*joukkuemäärä

   Kauden valintaa ei ole vielä toteutettu.

## Pelaajapörssi

6. Pelaajat per kausi

   Ei toteutettu vielä.

### Pelaajapörssi per joukkue

   Ei Toteutettu vielä

