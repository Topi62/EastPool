from application import app, db, login_required
from flask import redirect, url_for, render_template, request
from flask_login import current_user
from application.views import string_check
from application.player.models import Player
from application.player.forms import PlayerForm

@app.route("/player/listTeam/")
@login_required("Captain")
def list_team_players():
    return render_template("player/listTeam.html", players =  Player.query.filter_by(idteam=current_user.team).all())
    return redirect(url_for("list_team"))

@app.route("/player/newPlayer/")
def player_form():
    #  Kapteeneille - pelaajan lisäys
    form= PlayerForm()
    return render_template("player/newPlayer.html", form = form)

@app.route("/player/newPlayer", methods=["GET", "POST"])
def player_create():
    form = PlayerForm(request.form)
    if not form.validate():
        return render_template("player/newPlayer.html", form = form)
    player = Player.query.filter_by(name= form.name.data).first()
    if  player: 
        form.name.data = ""
        return render_template("player/newPlayer.html", form = form,
	                                    error =  "Joukkueessa on jo {} niminen pelaaja!".format(player.name))
    p = Player(current_user.team, form.name.data,  form.member.data)
    db.session().add(p)
    db.session().commit()

    return redirect(url_for("list_team_players"))

