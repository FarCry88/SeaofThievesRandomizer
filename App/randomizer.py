from flask import Flask
import random

app = Flask(__name__)

events = [
    "Skeleton Fleet",
    "Ghost Fleet",
    "Skeleton Fort",
    "Fort of the Damned",
    "Burning Blade",
    "Ashen Winds",
    "Megalodon",
    "Kraken",
    "Eternal Guard",
    "Fort Hop",
    "Island Hop",
    "PVP"
]

ships = [
    "Sloop",
    "Brig",
    "Galleon"
]

catches = [
    "No Ranged Weapons",
    "No Special Cannonballs",
    "Not Allowed to Bilge Water",
    "Can't Adjust Sails",
    "No Harpoons",
    "Cannot Board Enemy Ship",
    "No Anchor Use",
    "Fight in Storm"
]

@app.route("/")

def index():
    return "<h1>Sea of Thieves Event Randomizer</h1><a href='/random'>Pick Event</a>"

@app.route("/random")

def random_event():
    event = random.choice(events)
    ship = random.choice(ships)
    catch = random.choice(catches)
    return f"<h2>Your Event: {event}, On ship: {ship}. <br> Here is your catch: {catch} <br>  Yearg! Cast away matey!</h2><a href='/random'>Re-Roll</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
