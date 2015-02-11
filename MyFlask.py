from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("admin_list_user.html")

@app.route('/admin_edit_user.html')
def edit_html():
    return render_template("admin_edit_user.html")

@app.route('/admin_list_user.html')
def admin_html():
    items = range(1,100)
    return render_template("admin_list_user.html", items=items)


if __name__ == '__main__':
    app.run(debug=True)
