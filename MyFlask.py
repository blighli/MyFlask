from flask import Flask, redirect, url_for, render_template, request


from flask.ext.wtf import Form
from wtforms import StringField, SelectMultipleField
from wtforms.validators import DataRequired, Length

from math import ceil


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

class RoleForm(Form):
    class Meta:
        locales = ["zh_CN"]
    name = StringField("角色")
    desc = StringField("描述")
    funcs = SelectMultipleField("权限", choices=sorted([(k,v) for k,v in PRIVILEGES.items()]))


app = Flask(__name__)
app.config['SECRET_KEY'] = "1234567890"


@app.route('/')
def index():
    return redirect(url_for("admin_role_list"))

@app.route('/admin/roles/')
def admin_role_list():
    items = range(0,1000)
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
    form = RoleForm()
    if form.validate_on_submit():
        print(form.name.data)
        print(form.desc.data)
        print(form.funcs.data)
        return redirect(url_for("admin_role_list"))
    return render_template("admin_edit_role.html", form=form, roleId=roleId)

if __name__ == '__main__':
    app.run(debug=True)
