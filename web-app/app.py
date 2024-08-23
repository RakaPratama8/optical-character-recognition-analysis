from flask import Flask, render_template, request
from model import RecognizeText
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def predict():
    imagefile = request.files["imagefile"]
    image_path = os.path.join(os.getcwd(), "images", imagefile.filename)
    if not os.path.exists(os.path.dirname(image_path)):
        os.makedirs(os.path.dirname(image_path))
    imagefile.save(image_path)
    
    results = RecognizeText(image_path)
    
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(port=5000, debug=True)