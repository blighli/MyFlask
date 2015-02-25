from flask import Flask, redirect, url_for, render_template


from flask.ext.wtf import Form
from wtforms import StringField, SelectMultipleField
from wtforms.validators import DataRequired, Length

from math import ceil


funcs = {
    "a": "Name of a",
    "a.1": "Name of a.1",
    "a.2": "Name of a.2",
    "a.3": "Name of a.3",
    "a.4": "Name of a.4",
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
    name = StringField("角色",validators=[DataRequired()])
    desc = StringField("描述",validators=[DataRequired()])
    funcs = SelectMultipleField("权限", choices=sorted([(k,v) for k,v in funcs.items()]))


app = Flask(__name__)
app.config['SECRET_KEY'] = "1234567890"


@app.route('/')
def index():
    return redirect(url_for("admin_list_role"))


@app.route('/admin/roles/<roleId>',methods=['GET', 'POST'])
def admin_edit_role(roleId):
    form = RoleForm()
    if form.validate_on_submit():
        print(form.name.data)
        print(form.desc.data)
        print(form.funcs.data)
        return redirect(url_for("admin_list_role"))
    return render_template("admin_edit_role.html", form=form, roleId=roleId)

class NoteItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author


@app.route('/admin/roles/')
def admin_list_role():
    items = range(0,1000)
    return render_template("admin_list_role.html", items=items)


if __name__ == '__main__':
    app.run(debug=True)
