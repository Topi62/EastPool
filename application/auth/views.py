import re
from flask import render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegUserForm, ChangePw, DelUser

def string_check(string, pnum):
    pattern = {
       1: '[ÅÄÖA-Z][åäöa-z]{0,13}$',
       2: '[ÅÄÖA-Z][ÅÄÖA-Z][1-9]',
       3: '[ÅÄÖA-Zåäöa-z0-9]{1,8}$'
       }
    syntax =  re.compile(pattern.get(pnum), flags=0)
    return re.match(syntax, string)


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    #validoinnit

    if not  string_check(form.name.data, 1):
        return render_template("auth/loginform.html", form = form,
                               error = "tunnuksessa saa olla vain kirjaimia, joista ensimmäinen iso")

    if not string_check(form.shortname.data, 2):
        return render_template("auth/loginform.html", form = form,
                               error = "lyhenteessä pitää olla kaksi isoa kirjainta ja numero")

    if not string_check(form.password.data, 3):
        return render_template("auth/loginform.html", form = form, 
                               error = "salasanassa saa olla vain kirjaimia ja numeroita")

    user = User.query.filter_by(name=form.name.data, team=form.shortname.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "tarkista tunnus ja salasana")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_reg():
    if request.method == "GET":
         return render_template("auth/regform.html", form = RegUserForm())

    form = RegUserForm(request.form)

    if form.password.data != form.confirm.data:
         form.password.data = ""
         form.confirm.data = ""
         return render_template("auth/regform.html", form = form, 
                                 error = "Salasanat eroavat")

    # validoinnit
    if not string_check(form.name.data, 1):
        return render_template("auth/regform.html", form = form,
                               error = "tunnuksessa saa olla vain kirjaimia, joista ensimmäinen iso")
    if not string_check(form.shortname.data, 2):
        return render_template("auth/regform.html", form = form,
                               error = "lyhenteessä pitää olla kaksi isoa kirjainta ja numero")
    if not string_check(form.password.data, 3):
        return render_template("auth/regform.html", form = form, 
                               error = "salasanassa saa olla vain kirjaimia ja numeroita")

    user = User.query.filter_by(name=form.name.data, team=form.shortname.data).first()
    if user:
         return render_template("auth/regform.html", form = form,
                                 error = "tunnus on jo olemassa, keksi toinen")
    n = form.name.data
    t = form.shortname.data
    p = form.password.data
    u = User(n, t, p)
    db.session.add(u)
    db.session.commit()
    return render_template("auth/loginform.html", form = LoginForm())

@app.route("/auth/changePw", methods= ["GET", "POST"])
@login_required
def auth_changepw():
    if request.method == "GET":
         return render_template("auth/changepw.html", form = ChangePw())

    form = ChangePw(request.form)
    if form.password.data != form.confirm.data:
         form.password.data = ""
         form.confirm.data = ""
         return render_template("auth/changepw.html", form = form, 
                                 error = "Salasanat eroavat")
 
    if not string_check(form.password.data, 3):
        return render_template("auth/changepw.html", form = form, 
                               error = "salasanassa saa olla vain kirjaimia ja numeroita")
    user = User.query.filter_by(name=current_user.name, team=current_user.team).first()
    user.password = form.password.data
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/auth/deluser", methods= ["GET", "POST"])
@login_required
def auth_deluser():
    if request.method == "GET":
         return render_template("auth/deluser.html", form = DelUser())

    form = DelUser(request.form)
    if (string_check(form.name.data, 1) and string_check(form.team.data, 2)): 
        user = User.query.filter_by(name=form.name.data, team=form.team.data).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for("index"))
    return render_template("auth/deluser.html", form = form, 
                                 error = "Tunnusta ei ole")

