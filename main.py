from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

images = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        file = request.files["file"]

        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        images.append(path)

        return redirect("/")

    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)
