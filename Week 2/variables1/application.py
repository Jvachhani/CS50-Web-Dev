import random
from flask iport Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    headline = random.choice(["Hello, world!", "Hi there!", "Good morning!"])
    return render_template("index.html", headline=headline