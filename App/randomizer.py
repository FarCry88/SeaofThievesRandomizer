from flask import Flask
import random

app = Flask(__name__)

events = [
    "Skeleton Fleet"
    "Ghost Fleet"
    "Skeleton Fort"
    "Fort of the Damned"
    "Burning Blade"
    "Ashen Winds"
    "Megalodon"
    "Kraken"
]

@app.route("/")

def index():
    return "<h1>Sea of Thieves Event Randomizer</h1><a href='/random'>Pick Event</a>"

@app.route("/random")

def random_event():
    event = random.choice(events)
    return f"<h2>Your Event: {event}</h2><a href='/random'>Try Again</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
