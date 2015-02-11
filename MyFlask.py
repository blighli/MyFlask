from flask import Flask, redirect, url_for, render_template


from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length


funcs = {
    "a": "Name of a",
    "a.b": "Name of a.b",
    "b": "Name of b",
    "b.c": "Name of b.c"
}


class RoleForm(Form):
    class Meta:
        locales = ["zh_CN"]
    name = StringField("Name",validators=[DataRequired(), Length(min=6,max=10)])
    desc = StringField("Desc",validators=[DataRequired()])


app = Flask(__name__)
app.config['SECRET_KEY'] = "1234567890"


@app.route('/')
def index():
    return redirect(url_for("admin_list_role"))


@app.route('/admin/roles/<roleId>',methods=['GET', 'POST'])
def admin_edit_role(roleId):
    form = RoleForm()
    if form.validate_on_submit():
        return redirect(url_for("admin_list_role"))
    return render_template("admin_edit_role.html", form=form, roleId=roleId)


@app.route('/admin/roles/')
def admin_list_role():
    items = range(1,5)
    return render_template("admin_list_role.html", items=items)


if __name__ == '__main__':
    app.run(debug=True)
