from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_scrape_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    complete_mars_dict = mongo.db.complete_mars_dict.find_one()
    return render_template("index.html", listings=complete_mars_dict)


@app.route("/scrape")
def scraper():
    complete_mars_dict = mongo.db.complete_mars_dict
    mars_data = scrape_mars.scrape()
    complete_mars_dict.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)