from application import app
from flask import request, redirect, url_for, render_template
from application.team.models import Team

@app.route("/serietables/teamTable/")
def team_table():
    season = request.args.get('season')
    if season:
        return render_template("serietables/serieTable.html", scores =  Team.serie_tables(season))
    return redirect(url_for("team_table"))


