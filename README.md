# 🫁 Lung Cancer Detection — ML Project

A deep learning–powered web application that classifies lung scan images into:
- ✅ **Normal** — No disease detected
- 🟡 **Benign** — Non-cancerous growth detected
- 🔴 **Malignant** — Cancerous growth detected
- ⚠️ **Irrelevant** — Image is not a valid lung scan

Built with **TensorFlow/Keras**, **Flask**, and a custom-trained CNN model.

---

## 📁 Project Structure

```
Lung-Cancer-Detection-ML-Project/
│
├── app.py                  # Flask web application
├── code.py                 # Standalone prediction script
├── keras_model.h5          # Trained Keras model
├── labels.txt              # Class labels
├── requirements.txt        # Python dependencies
│
├── templates/
│   └── index.html          # Web UI template
│
└── static/
    └── uploads/            # Uploaded images stored here
```

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/deepikag123/Lung-Cancer-Detection-ML-Project.git
cd Lung-Cancer-Detection-ML-Project
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask App
```bash
python app.py
```

### 5. Open in Browser
```
http://127.0.0.1:5000
```

---

## 🖼️ How to Use

1. Open the web app in your browser
2. Click **"Upload Image"** and select a lung scan image (JPG/PNG)
3. Click **"Analyse Image"**
4. View the **prediction**, **confidence score**, and **recommendation**

---

## 📸 Screenshots

### Home Page
<img width="1920" height="1080" alt="imageuploaded" src="https://github.com/user-attachments/assets/865415b4-1777-47bd-9116-b6b24978e7f0" />


### Result Page
<img width="1920" height="1080" alt="results" src="https://github.com/user-attachments/assets/b89cdb75-d9c2-4401-abcd-0a5c94029274" />


---

## 🧠 Model Details

| Property        | Value              |
|-----------------|--------------------|
| Framework       | TensorFlow / Keras |
| Input Size      | 224 × 224 × 3      |
| Normalization   | `(pixel / 127.5) - 1` |
| Output Classes  | 4                  |
| Model File      | `keras_model.h5`   |

### Classes
| Label            | Description                        |
|------------------|------------------------------------|
| `Normal_case`    | Healthy lung — no abnormality      |
| `Bengin_case`    | Benign (non-cancerous) nodule      |
| `Malignant_case` | Malignant (cancerous) growth       |
| `Irrelevant_image` | Not a valid medical scan         |

---

## 📦 Requirements

```
tensorflow==2.15.0
keras
numpy
pandas
matplotlib
scikit-learn
flask
pillow
```

---

## ⚠️ Disclaimer

> This tool is intended for **educational and research purposes only**.  
> It is **not** a substitute for professional medical diagnosis.  
> Always consult a qualified medical professional for clinical decisions.

---

## 👩‍💻 Author

**Deepika G**  
GitHub: [@deepikag123](https://github.com/deepikag123)
