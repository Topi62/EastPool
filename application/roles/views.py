from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from application import app, db
from application.views import string_check
from application.roles.models import Role
from application.roles.forms import RoleForm


@app.route("/roles/update", methods = ["GET", "POST"])
@login_required
def role_update():
    if request.method == "GET":
        return render_template("roles/roleform.html", form = RoleForm())

    form = RoleForm(request.form)

    if not form.validate():
        return render_template("roles/roleform.html", form=form) 
    r = Role.query.filter_by(name=form.name.data, team=form.team.data).first()
    if not r:
        u = Role(form.name.data, form.team.data, form.role.data)
        db.session.add(u)
        db.session.commit()
        flash('Rooli luotu')
        return redirect(url_for("index"))
    else:
        r.role = form.role.data
        db.session.commit()
        flash('Rooli päivitetty')
        return redirect(url_for("index"))
