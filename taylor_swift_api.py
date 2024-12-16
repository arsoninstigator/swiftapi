from flask import Flask, jsonify

app = Flask(__name__)

data = {
    "albums": [
        {"name": "Taylor Swift", "release_date": "2006-10-24", "songs": ["Tim McGraw", "Teardrops on My Guitar", "Our Song"]},
        {"name": "Fearless", "release_date": "2008-11-11", "songs": ["Love Story", "You Belong with Me", "White Horse"]},
        {"name": "Fearless (Taylor's Version)", "release_date": "2021-04-09", "songs": ["Love Story (Taylor's Version)", "You Belong with Me (Taylor's Version)", "Mr. Perfectly Fine"]},
        {"name": "Speak Now", "release_date": "2010-10-25", "songs": ["Mine", "Back to December", "Mean"]},
        {"name": "Speak Now (Taylor's Version)", "release_date": "2023-07-07", "songs": ["Enchanted (Taylor's Version)", "Better Than Revenge (Taylor's Version)", "Castles Crumbling"]},
        {"name": "Red", "release_date": "2012-10-22", "songs": ["Red", "We Are Never Ever Getting Back Together", "22"]},
        {"name": "Red (Taylor's Version)", "release_date": "2021-11-12", "songs": ["All Too Well (10 Minute Version)", "I Knew You Were Trouble", "State of Grace"]},
        {"name": "1989", "release_date": "2014-10-27", "songs": ["Blank Space", "Style", "Shake It Off"]},
        {"name": "1989 (Taylor's Version)", "release_date": "2023-10-27", "songs": ["Wildest Dreams (Taylor's Version)", "Out of the Woods (Taylor's Version)", "Slut!"]},
        {"name": "Reputation", "release_date": "2017-11-10", "songs": ["Look What You Made Me Do", "Delicate", "End Game"]},
        {"name": "Lover", "release_date": "2019-08-23", "songs": ["Lover", "You Need to Calm Down", "The Archer"]},
        {"name": "Folklore", "release_date": "2020-07-24", "songs": ["Cardigan", "Exile", "The Last Great American Dynasty"]},
        {"name": "Evermore", "release_date": "2020-12-11", "songs": ["Willow", "Champagne Problems", "No Body, No Crime"]},
        {"name": "Midnights", "release_date": "2022-10-21", "songs": ["Anti-Hero", "Lavender Haze", "Karma"]},
    ],
    "bio": {
        "name": "Taylor Swift",
        "birth_date": "1989-12-13",
        "genres": ["Pop", "Country", "Folk"],
        "description": "Taylor Swift is a singer-songwriter known for her storytelling and evolving musical style.",
    },
}



@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Taylor Swift API!"})


@app.route("/bio", methods=["GET"])
def get_bio():
    return jsonify(data["bio"])


@app.route("/albums", methods=["GET"])
def get_albums():
    return jsonify(data["albums"])


@app.route("/albums/<album_name>", methods=["GET"])
def get_album_details(album_name):
    album = next((a for a in data["albums"] if a["name"].lower() == album_name.lower()), None)
    if album:
        return jsonify(album)
    return jsonify({"error": "Album not found"}), 404


@app.route("/albums/<album_name>/songs", methods=["GET"])
def get_album_songs(album_name):
    album = next((a for a in data["albums"] if a["name"].lower() == album_name.lower()), None)
    if album:
        return jsonify(album["songs"])
    return jsonify({"error": "Album not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
