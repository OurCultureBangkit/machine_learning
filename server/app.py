from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from keras.models import load_model
from keras.preprocessing import image
import os
import numpy as np


app = Flask(__name__)
app.config["ALLOWED_EXTENSIONS"] = set(['jpg', 'png', 'jpeg'])
app.config["UPLOAD_FOLDER"] = "static/uploads"

def allowed_file(filename):
    return "." in filename and filename.split(".", 1)[1] in app.config["ALLOWED_EXTENSIONS"]

model = load_model("model.h5", compile=False)

with open("labels.txt", "r") as file:
    labels = file.read().splitlines()

with open("labelInformation.txt", "r") as file:
    information = file.read().splitlines()


@app.route("/")
def index():
    return jsonify({
        "status":{
            "code": 200,
            "message": "Success fetching the API",
        },
        "data": None
    }), 200

@app.route("/ml/vision", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        img = request.files["gambar"]
        if img and allowed_file(img.filename):
            # save input image
            filename = secure_filename(img.filename)
            img.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            
            # pre-processing input image
            img = image.load_img(image_path, target_size=(150,150))
            img = image.img_to_array(img) / 255.0
            img = np.expand_dims(img, axis=0)
            
            # predicting 
            predict = model.predict(img)
            best_index = np.argmax(predict)
            class_name = labels[best_index]

            return jsonify({
                "status": {
                    "code": 200,
                    "message": "Register Success"
                },
                "data": {
                    "title": class_name
                }
            }), 200
        else:
            return jsonify({
                "status": {
                    "code": 400,
                    "message": "Client side error"
                },
                "data": None
            }), 400
    else: 
        return jsonify({
            "status": {
                "code": 405,
                "message": "Method not allowed"
            }, 
            "data": None
        }), 405


if __name__ == "__main__":
    app.run()
