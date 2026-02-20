from flask import Flask, render_template, request

app = Flask(__name__)

users = {}

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            if users[username] == password:
                message = "Giriş başarılı"
            else:
                message = "Şifre yanlış"
        else:
            users[username] = password
            message = "Kayıt başarılı"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run()