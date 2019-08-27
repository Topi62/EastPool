# Käyttökuvaukset

## Ilmoittautuminen

1. Joukkueen ilmoittautuminen liigaan. "Kapteenina voin ilmoittaa joukkueen liigaan." 

   Valikosta Kapteeneille - Joukkueen lisäys

   Jos lomake läpäisee validoinnin ja kysely "SELECT * FROM team WHERE shortname = 'Joukkueen lyhenne'" ei palauta joukkuetta,

   luodaan uusi joukkue kyselyllä "INSERT INTO team(shortname, longname) VALUES ('Joukkueen lyhenne', 'Joukkueen nimi') 

## Rekisteröityminen

2. Käyttäjä voi rekisteröityä. "Kapteeni saa tunnuksen."

   Valikosta Käyttäjä - Rekisteröidy

   Jos salasana on syötetty kaksi kertaa samoin ja lomake läpäisee validoinnit ja kysely  "SELECT * FROM account WHERE name = 'Nimi'
   AND team = 'Joukkue' ei palauta käyttäjää

   luodaan uusi käyttäjä kyselyllä "INSERT INTO account(name, team, password) VALUES ('Nimi', 'Joukkue', 'Salasana') 

