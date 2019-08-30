from application import app, db
from flask import redirect, url_for, render_template, request
from flask_paginate import Pagination, get_page_parameter
from application import login_required
from application.views import string_check
from application.match.models import Match
from application.match.forms import TimeMatchForm, ListMatchForm
from application.team.models import Team
from sqlalchemy.sql import func

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
    if request.method == 'GET':
        page = request.args.get(get_page_parameter(), type=int, default=1)
        matchs = Match.query.filter(Match.date==None).all()
        rows = list(matchs)
        total = len(rows)
        offset = (page-1)*10+1
        limit = page*10
        if limit > total:
           limit = total
        pagination = Pagination(page=page,total=total, css_framework='bootstrap4')
        return render_template("match/timeMatch.html", total=total, offset=offset, limit=limit, matchs =matchs[offset-1:limit], pagination = pagination, form = TimeMatchForm())
    form = TimeMatchForm(request.form)
    if not form.validate():
        return render_template("match/timeMatch.html", form = form)

    if  Team.check_teams(form.hometeam.data, form.visitteam.data): 
        return render_template("match/timeMatch.html", form = form,
	                                    error =  "jompaa kumpaa joukkuetta ei ole")

    row_changed = Match.query.filter_by(hometeamid=form.hometeam.data, visitorteamid=form.visitteam.data, idseason=form.season.data).update(dict(date=form.gamedate.data))
    db.session().commit()

    return redirect(url_for("match_list_tocome"))

