from application import app, db, login_required
from flask import redirect, url_for, render_template, request
from application.views import string_check
from application.team.models import Team
from application.team.forms import TeamForm

@app.route("/team/listTeam/")
def team_list():
    return render_template("team/listTeam.html", teams =  Team.query.all())
    return redirect(url_for("team_list"))

@app.route("/team/newTeam/")
def team_form():
    #  Kapteeneille - Joukkueen lisäys
    return render_template("team/newTeam.html", form = TeamForm())

@app.route("/team/", methods=["GET", "POST"])
def team_create():
    form = TeamForm(request.form)
    if not form.validate():
        return render_template("team/newTeam.html", form = form)
    if not (string_check(form.shortname.data, 2)):
        return render_template("team/newTeam.html", form = form,
                               error = "Joukkueen lyhenne oltava kaksi isoa kirjainta ja numero")
    team = Team.query.filter_by(shortname= form.shortname.data).first()
    if  team: 
        form.shortname.data = ""
        return render_template("team/newTeam.html", form = form,
	                                    error =  "lyhenne {} on jo varattu".format(team.shortname))
    if not (string_check(form.longname.data, 4)):
        return render_template("team/newTeam.html", form = form,
                                            error = "Joukkueen nimessä vain kirjaimia ja numeroita, maksimi pituus 15 merkkiä")
    t = Team(form.shortname.data, form.longname.data)
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("team_list"))

