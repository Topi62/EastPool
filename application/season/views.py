from application import app, db
from flask import redirect, url_for, render_template, request
from flask_login import login_required
from application.views import string_check
from application.season.models import Season
from application.season.forms import SeasonForm
from application.match.models import Match

@app.route("/season/newSeason/", methods=['GET', 'POST'])
@login_required
def season_form():
    if request.method == 'GET':
       return render_template("season/createSeason.html", form = SeasonForm(), seasons = Season.query.all())
       return redirect(url_for("season_form"))

    form = SeasonForm(request.form)
    if not form.validate():
        return render_template("season/createSeason.html", form = form, seasons = seasons)
    
    #lisaa tarkistus id jo olemassa
    season = Season.query.filter_by(period= form.period.data).first()
    if  season:
                                        error = "Kausi nimeltä {} on jo olemassa".format(form.period.data)
    s = Season(form.seasonid.data, form.period.data)
    db.session().add(s)
    db.session().commit()
    if form.games.data:
        Match.create_matches(form.seasonid.data)
        return redirect(url_for("match_list"))
    return redirect(url_for("index"))

