from application import app, db
from flask import redirect, url_for, render_template, request
from application.schedule.models import Team

@app.route("/team/listTeam/")
def team_list():
    return render_template("team/listTeam.html", teams =  Team.query.all())
    return redirect(url_for("team_list"))

@app.route("/schedule/newTeam/")
def team_form():
    return render_template("schedule/newTeam.html")

@app.route("/schedule/", methods=["POST"])
def team_create():
    s = Team(request.form.get('shortName'))
   
    db.session().add(s)
    db.session().commit()

    return redirect(url_for("team_list"))

