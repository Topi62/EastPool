# Eastpool tietokannan taulujen luonnit

## Account

```
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(14),
        idteam VARCHAR(3) NOT NULL,
        password VARCHAR(8),
        PRIMARY KEY (id),
        FOREIGN KEY (idteam) REFERENCES team (shortname)
)
```


## Roles

```
CREATE TABLE roles (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(14),
        idteam VARCHAR(3) NOT NULL,
        role VARCHAR(7),
        PRIMARY KEY (id),
        FOREIGN KEY (idteam) REFERENCES team (shortname)
)
```


## Team

```
CREATE TABLE team (
        shortname VARCHAR(3) NOT NULL,
        longname VARCHAR(15),
        PRIMARY KEY (shortname)
)
```

## Player

```
CREATE TABLE player (
        idplayer INTEGER NOT NULL,
        idteam VARCHAR(3) NOT NULL,
        name VARCHAR(12),
        nromember INTEGER,
        PRIMARY KEY (idplayer),
        FOREIGN KEY (idteam) REFERENCES team (shortname)
)
```


## Match

```
CREATE TABLE match (
        idmatch INTEGER NOT NULL,
        idseason INTEGER,
        type, INTEGER,
        date DATETIME,
        hometeamid VARCHAR(3),
        visitorteamid VARCHAR(3),
        homegamenumwins INTEGER,
        visitorgamenumwins INTEGER,
        status VARCHAR(1),
        PRIMARY KEY (idmatch),
        FOREIGN KEY(idseason) REFERENCES season (idseason),
        FOREIGN KEY(hometeamid) REFERENCES team (shortname),
        FOREIGN KEY(visitorteamid) REFERENCES team (shortname)
)
```


## Season

```
CREATE TABLE season (
        idseason INTEGER NOT NULL,
        period VARCHAR(9),
        PRIMARY KEY (idseason)
)
```

## Game

```
CREATE TABLE game (
	idgame INTEGER NOT NULL, 
	idmatch INTEGER,
        homeplayerid INTEGER,
        visitorplayerid INTEGER, 
	starttime DATETIME, 
	endtime DATETIME, 
	homeframewins INTEGER, 
	visitorframewins INTEGER, 
	PRIMARY KEY (idgame), 
	FOREIGN KEY(idmatch) REFERENCES match (idmatch),
	FOREIGN KEY(homeplayerid) REFERENCES player (idplayer),
	FOREIGN KEY(visitorplayerid) REFERENCES player (idplayer)
)
```

## Frame

```
CREATE TABLE frame (
	idframe INTEGER NOT NULL, 
	idgame INTEGER, 
	starttime DATETIME, 
	endtime DATETIME, 
	vinner INTEGER, 
	vintype INTEGER, 
	PRIMARY KEY (idframe), 
	FOREIGN KEY(idgame) REFERENCES game (idgame)
)
```
