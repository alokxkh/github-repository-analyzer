from flask import Flask, render_template, request
from analyzer import analyze_repo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        repo = (
            request.form["repo"]
            .strip()
            .replace("https://github.com/", "")
            .rstrip("/")
        )

        if repo.endswith(".git"):
            repo = repo[:-4]

        result = analyze_repo(repo)

        if result is None:
            error = "Repository not found!"

    return render_template(
        "index.html",
        result=result,
        error=error
    )

if __name__ == "__main__":
    app.run()