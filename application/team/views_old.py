from application import app, db
from flask import render_template, request
from application.schedule.models import Team

@app.route("/teams", methods=["GET"])
def team_index():
    return render_template("team/listTeam.html", teams = Team.query.all())

    return redirect(url_for("team_index"))

