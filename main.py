import livestreamer
from flask import Flask, redirect
app = Flask(__name__)


@app.route("/")
def index():
    return "No URL given"


@app.route("/<path:url>")
def streamredir(url):
    try:
        streams = livestreamer.streams(url)
        best = streams['best']
        return redirect(best.url)
    except:
        return "No stream found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=False)
