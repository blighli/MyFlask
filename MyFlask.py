from flask import Flask, redirect, url_for, render_template, request


from flask.ext.wtf import Form
from wtforms import HiddenField, StringField, SelectMultipleField
from wtforms.validators import DataRequired, Length

from math import ceil


from flask_sqlalchemy import SQLAlchemy
import os

PRIVILEGES = {
    "admin": "后台管理",
    "admin.role": "角色管理",
    "admin.role.new": "添加角色",
    "admin.user": "用户管理",
    "admin.user.new": "添加用户",
    "b": "Name of b",
    "b.1": "Name of b.1",
    "b.2": "Name of b.2",
    "b.3": "Name of b.3",
    "b.4": "Name of b.4",
    "b.5": "Name of b.5"
}


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "1234567890"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    desc = db.Column(db.String(64), default="无")
    privileges = db.Column(db.String(1024), default="")
    def __repr__(self):
        return '<Role %r>' % self.name


class RoleForm(Form):
    class Meta:
        locales = ["zh_CN"]
    name = StringField("角色")
    desc = StringField("描述")
    privileges = SelectMultipleField("权限", choices=sorted([(k,v) for k,v in PRIVILEGES.items()]))


db.drop_all()
db.create_all()

admin_role = Role(name='管理员')
user_role = Role(name='普通用户')

db.session.add(admin_role)
db.session.add(user_role)

db.session.commit()

@app.route('/')
def index():
    return redirect(url_for("admin_role_list"))

@app.route('/admin/roles/')
def admin_role_list():
    items = Role.query.all()
    return render_template("admin_list_role.html", items=items)

@app.route('/admin/roles/new')
def admin_role_new():
    form = RoleForm()
    return render_template("admin_edit_role.html", form=form)

@app.route('/admin/roles/', methods=['POST'])
def admin_role_add():
    print("admin_role_add")
    return redirect(url_for("admin_role_list"))

@app.route('/admin/roles/', methods=['DELETE'])
def admin_role_del():
    print("admin_role_del")
    print(request.form.getlist("ids[]"))
    return "ok", 200

@app.route('/admin/roles/<roleId>', methods=['GET', 'POST'])
def admin_edit_role(roleId):
    role = Role.query.get(roleId)
    form = RoleForm()
    if form.validate_on_submit():
        role.name = form.name.data
        role.desc = form.desc.data
        role.privileges = ",".join(form.privileges.data)
        db.session.add(role)
        db.session.commit()
        return redirect(url_for("admin_role_list"))
    form.name.data = role.name
    form.desc.data = role.desc
    form.privileges.data = role.privileges.split(",")
    return render_template("admin_edit_role.html", form=form, roleId=roleId)

if __name__ == '__main__':
    app.run(debug=True)
