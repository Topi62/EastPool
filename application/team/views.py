from application import app, db
from flask import redirect, url_for, render_template, request
from flask_login import login_required
from application.team.models import Team
from application.team.forms import TeamForm

@app.route("/team/listTeam/")
def team_list():
    return render_template("team/listTeam.html", teams =  Team.query.all())
    return redirect(url_for("team_list"))

@app.route("/team/newTeam/")
@login_required
def team_form():
    return render_template("team/newTeam.html", form = TeamForm())

@app.route("/team/", methods=["POST"])
@login_required
def team_create():
    form = TeamForm(request.form)
    if not form.validate():
        return render_template("team/newTeam.html", form = form)

    team = Team.query.filter_by(shortname= form.shortname.data).first()
    if  team: 
        form.shortname.data = ""
        return render_template("team/newTeam.html", form = form,
	                                    error =  "lyhenne {} on jo varattu".format(team.shortname))
    t = Team(form.shortname.data, form.longname.data)
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("team_list"))

