from flask import render_template, request, redirect, url_for, flash
from flask_login import  current_user
from application import app, db, login_required
from application.views import string_check
from application.roles.models import Role
from application.roles.forms import RoleForm


@app.route("/roles/update", methods = ["GET", "POST"])
@login_required("Admin")
def role_update():
    if request.method == "GET":
        return render_template("roles/roleaddform.html", form = RoleForm())

    form = RoleForm(request.form)

    if not form.validate():
        return render_template("roles/roleaddform.html", form=form) 
    r = Role.query.filter_by(name=form.name.data, team=form.team.data, role=form.role.data).first()
    if not r:
        u = Role(form.name.data, form.team.data, form.role.data)
        db.session.add(u)
        db.session.commit()
        flash('Rooli lisätty')
        return redirect(url_for("index"))
    else:
        flash('Käyttäjällä jo kyseinen rooli')
        return redirect(url_for("index"))

@app.route("/roles/delete", methods = ["GET", "POST"])
@login_required(role="Admin")
def role_delete():
    if request.method == "GET":
        return render_template("roles/roleremoveform.html", form = RoleForm())

    form = RoleForm(request.form)

    if not form.validate():
        return render_template("roles/roleremoveform.html", form=form) 
    u = Role.query.filter_by(name=form.name.data, team=form.team.data, role=form.role.data).one_or_none()
    if u != None:
       db.session.delete(u)
       db.session.commit()
       flash('Rooli poistettu')
       return redirect(url_for("index"))
    else:
       flash('Roolia ei ollut')
       return redirect(url_for("index"))

