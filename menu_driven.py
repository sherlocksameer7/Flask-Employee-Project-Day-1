from flask import Flask, render_template

Menu = Flask(__name__)

@Menu.route("/")
def add():
    return render_template("add.html")

@Menu.route("/search")
def search():
    return render_template("search.html")

@Menu.route("/update")
def update():
    return render_template("update.html")


@Menu.route("/delete")
def delete():
    return render_template("delete.html")



if __name__ == "__main__":
    Menu.run()