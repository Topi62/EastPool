from application import app, db
from flask import redirect, url_for, render_template, request
from flask_login import login_required
from application.views import string_check
from application.match.models import Match
from application.match.forms import TimeMatchForm, ListMatchForm
from application.team.models import Team

@app.route("/match/listMatch/")
def match_list():
    return render_template("match/listMatch.html", matchs =  Match.query.all())
    return redirect(url_for("match_list"))

@app.route("/match/timeMatch/", methods=['GET', 'POST'])
@login_required
def match_time():
    if request.method == 'GET':
        return render_template("match/timeMatch.html", matchs = Match.query.filter(Match.date==None).all(), form = TimeMatchForm())
    form = TimeMatchForm(request.form)
    if not form.validate():
        return render_template("match/timeMatch.html", form = form)

    if  Team.check_teams(form.hometeam.data, form.visitteam.data): 
        return render_template("match/timeMatch.html", form = form,
	                                    error =  "jompaa kumpaa joukkuetta ei ole")

    row_changed = Match.query.filter_by(hometeamid=form.hometeam.data, visitorteamid=form.visitteam.data).update(dict(date=form.gamedate.data))
    db.session().commit()

    return redirect(url_for("match_list"))

