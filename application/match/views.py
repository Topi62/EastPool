from application import app, db
from flask import redirect, url_for, render_template, request
from application import login_required
from application.views import string_check
from application.match.models import Match
from application.match.forms import TimeMatchForm, ListMatchForm
from application.team.models import Team
from sqlalchemy.sql import func

@app.route("/match/listComingMatch/")
def match_list_tocome():
    return render_template("match/listComing.html", matchs =  Match.get_coming_match())
    return redirect(url_for("match_list_tocome"))

@app.route("/match/listPlayedMatch/")
def match_list_played():
    return render_template("match/listPlayed.html", matchs =  Match.get_played_match())
    return redirect(url_for("match_list_played"))

@app.route("/match/timeMatch/", methods=['GET', 'POST'])
@login_required("Admin")
def match_time():
    if request.method == 'GET':
        return render_template("match/timeMatch.html", matchs = Match.query.filter(Match.date==None).all(), form = TimeMatchForm())
    form = TimeMatchForm(request.form)
    if not form.validate():
        return render_template("match/timeMatch.html", form = form)

    if  Team.check_teams(form.hometeam.data, form.visitteam.data): 
        return render_template("match/timeMatch.html", form = form,
	                                    error =  "jompaa kumpaa joukkuetta ei ole")

    row_changed = Match.query.filter_by(hometeamid=form.hometeam.data, visitorteamid=form.visitteam.data, idseason=form.season.data).update(dict(date=form.gamedate.data))
    db.session().commit()

    return redirect(url_for("match_list_tocome"))

