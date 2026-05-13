from flask import Flask, request, render_template
from tf_keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load Keras model
model = load_model("keras_model.h5", compile=False)

# Load labels
class_names = [line.strip() for line in open("labels.txt", "r").readlines()]

# Prevention guidelines based on classification
disease_prevention = {
    "Normal_case": "No disease detected. Maintain a healthy lifestyle!",
    "Bengin_case": "This is a benign case. Regular checkups and a healthy diet are advised.",
    "Malignant_case": "Consult a specialist immediately for proper diagnosis and treatment.",
    "Irrelevant_image": "Please upload a valid medical image for analysis.",
}

def process_image(image_path):
    """Preprocesses the uploaded image and returns model predictions."""
    image = Image.open(image_path).convert("RGB")
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name, confidence_score

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return render_template("index.html", message="No file uploaded!")

        file = request.files["file"]
        if file.filename == "":
            return render_template("index.html", message="No file selected!")

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Process image & get prediction
        class_name, confidence_score = process_image(filepath)
        class_name = class_name[2:]  # Remove number prefix from label
        prevention = disease_prevention.get(class_name, "No prevention available.")

        return render_template(
            "index.html",
            uploaded_image=filepath,
            result=class_name,
            confidence=round(confidence_score * 100, 2),
            prevention=prevention,
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
