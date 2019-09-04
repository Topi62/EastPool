from application import app, db
from flask import redirect, url_for, render_template, request
from flask_login import current_user
from flask_paginate import Pagination, get_page_parameter
from application import login_required
from application.views import string_check
from application.match.models import Match
from application.match.forms import TimeMatchForm, ListMatchForm, SelectMatchForm, SelectPlayersForm
from application.team.models import Team
from application.player.models import Player
from application.game.models import Game
from application.frame.models import Frame
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func, text, or_, and_
from sqlalchemy import asc, desc
from datetime import datetime, timedelta

@app.route("/match/listComingMatch/")
def match_list_tocome():
    # Näyttää tulevat ottelut
    return render_template("match/listComing.html", matchs =  Match.get_coming_match())
    return redirect(url_for("match_list_tocome"))

@app.route("/match/listPlayedMatch/")
def match_list_played():
    # Näyttää pelatut ottelut
    return render_template("match/listPlayed.html", matchs =  Match.get_played_match())
    return redirect(url_for("match_list_played"))

@app.route("/match/timeMatch/", methods=['GET', 'POST'])
@login_required("Admin")
def match_time():
    # Näyttää ottelut joita ei ole pelattu ja joille ei ole määritelty pelipäivää
    page = request.args.get(get_page_parameter(), type=int, default=1)
    matchs = Match.query.filter(Match.date==None).all()
    rows = list(matchs)
    total = len(rows)
    offset = (page-1)*10+1
    limit = page*10
    if limit > total:
        limit = total
    pagination = Pagination(page=page,total=total, css_framework='bootstrap4')
    if request.method == 'GET':    
       return render_template("match/timeMatch.html", total=total, offset=offset, limit=limit, matchs =matchs[offset-1:limit], pagination = pagination, form = TimeMatchForm())
    form = TimeMatchForm(request.form)
    if not form.validate():
        return render_template("match/timeMatch.html", total=total, offset=offset, limit=limit, matchs =matchs[offset-1:limit], pagination = pagination, form = form)

    if  Team.check_teams(form.hometeam.data, form.visitteam.data): 
        return render_template("match/timeMatch.html", total=total, offset=offset, limit=limit, matchs =matchs[offset-1:limit], pagination = pagination, form = form, error =  "jompaa kumpaa joukkuetta ei ole")

    row_changed = Match.query.filter_by(hometeamid=form.hometeam.data, visitorteamid=form.visitteam.data, idseason=form.season.data).update(dict(date=form.gamedate.data))
    db.session().commit()

    return redirect(url_for("match_time"))


@app.route("/match/selectMatch/")
@login_required("Captain")
def select_match():
    form= SelectMatchForm()
    tomorrow = datetime.today() + timedelta(days=1)

    form.match.choices=[(m.idmatch, m.hometeamid + '-' + m.visitorteamid) for m in Match.query.filter(and_(and_(or_(Match.hometeamid==current_user.team, Match.visitorteamid==current_user.team),Match.status=='T'), Match.date<tomorrow)).all()]
    return render_template("match/selectMatch.html", form=form )

@app.route("/match/selectPlayersTomatch/", methods=['POST'])
@login_required("Captain")
def select_players():
    form = SelectMatchForm(request.form)
    idmatch= form.match.data
    if idmatch == None:
        return redirect(url_for("index"))
    match = Match.query.filter(Match.idmatch==idmatch).first()
    form= SelectPlayersForm()
    form.match.data=idmatch
    homeplayers = list(Player.query.filter(Player.idteam==match.hometeamid).with_entities(Player.idplayer, Player.name))
    homeplayers.append((0, 'Ei Pelaajaa'))
    visitplayers= list(Player.query.filter(Player.idteam==match.visitorteamid).with_entities(Player.idplayer, Player.name))
    visitplayers.append((0, 'Ei Pelaajaa'))
    form.home1.choices=homeplayers
    form.home2.choices=homeplayers
    form.home3.choices=homeplayers
    form.visit1.choices=visitplayers
    form.visit2.choices=visitplayers
    form.visit3.choices=visitplayers
    return render_template("match/selectPlayers.html", match=match, form=form)

@app.route('/match/gamebook/', methods=['POST'])
@login_required("Captain")
def match_book():
    cancel = request.args.get('cancel')
    if cancel:
        return "Painettu peruuta edellinen"
    idgame = request.args.get('next_game')
    if next_game:
        return "Valittu peli : " + str(next_game)
    winner = request.args.get('vin')
    how = request.args.get('how')
    game = request.args.get('gameid')
    return "Tulossa kirjaus pelin " + game + " erän voitti " +  winner + " tavalla " + how

@app.route('/match/startmatch/', methods=['POST'])
@login_required("Captain")
def match_start():
    form = SelectPlayersForm(request.form)
    idmatch = form.match.data
    match = Match.query.filter_by(idmatch=idmatch).first()
    players=[]
    players.append(form.home1.data)
    players.append(form.home2.data)
    players.append(form.home3.data)
    players.append(form.visit1.data)
    players.append(form.visit2.data)
    players.append(form.visit3.data)
    for h in range(0,3):
       g = Game(idmatch, players[h], players[3])
       db.session.add(g)
       g = Game(idmatch, players[h], players[4])
       db.session.add(g)
       g = Game(idmatch, players[h], players[5])
       db.session.add(g)
    db.session.flush()
    H = aliased(Player)
    V = aliased(Player)
    games = db.session.query(Game.idmatch, Game.idgame, Game.homeframewins, Game.visitorframewins, H.name.label('homePlayerName'), V.name.label('visitPlayerName')).\
		join(H,(Game.homeplayerid == H.idplayer)).\
                join(V, (Game.visitorplayerid == V.idplayer)).\
                filter(Game.idmatch==idmatch).\
                order_by(asc(Game.idgame))
    db.session.commit()
    playorder=[0,4,8,1,5,6,2,3,7]
    selected=0
    return render_template("match/match.html", selected=selected, playorder=playorder, match=match, games=games)
