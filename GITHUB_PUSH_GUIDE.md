# 📤 GitHub Push Instructions
## Lung Cancer Detection ML Project

Follow these steps **exactly** on your Windows PC to push your project to GitHub.

---

## ✅ BEFORE YOU START — One-time Setup

### Step 1: Install Git (if not already installed)
1. Go to → https://git-scm.com/download/win
2. Download and install (keep all default settings)
3. After install, open **Command Prompt** and type:
   ```
   git --version
   ```
   You should see something like: `git version 2.x.x`

### Step 2: Configure Git with your identity (one-time only)
Open **Command Prompt** and run:
```bash
git config --global user.name "deepikag123"
git config --global user.email "your-email@example.com"
```
*(Replace with the email you used for GitHub)*

---

## 📁 STEP-BY-STEP: Push to GitHub

### Step 3: Create the GitHub Repository
1. Go to → https://github.com/new
2. Fill in:
   - **Repository name:** `Lung-Cancer-Detection-ML-Project`
   - **Description:** `Lung cancer detection using Deep Learning and Flask`
   - Set to **Public**
   - ✅ Do NOT check "Add README" (we already have one)
3. Click **"Create repository"**

---

### Step 4: Open Command Prompt in Your Project Folder

Your project is saved at:
```
E:\Cancer Detection\
```

**Option A — Easy way:**
1. Open **File Explorer**
2. Navigate to `E:\Cancer Detection\`
3. Click the address bar, type `cmd`, press **Enter**

**Option B — Manual:**
```bash
cd /d E:\Cancer Detection
```

---

### Step 5: Copy All Project Files into Your Folder

Make sure your `E:\Cancer Detection\` folder contains:
```
E:\Cancer Detection\
├── app.py
├── code.py
├── keras_model.h5
├── labels.txt
├── requirements.txt
├── README.md
├── .gitignore
├── templates\
│   └── index.html
└── static\
    └── uploads\
        └── .gitkeep
```

---

### Step 6: Initialize Git and Push

Run these commands **one by one** in Command Prompt:

```bash
git init
```
*(Initializes a new Git repository)*

```bash
git add .
```
*(Stages all files — the dot means "everything")*

```bash
git commit -m "Initial commit: Lung Cancer Detection ML Project"
```
*(Saves a snapshot with a message)*

```bash
git branch -M main
```
*(Renames default branch to main)*

```bash
git remote add origin https://github.com/deepikag123/Lung-Cancer-Detection-ML-Project.git
```
*(Links your local folder to GitHub)*

```bash
git push -u origin main
```
*(Uploads everything to GitHub)*

---

### Step 7: Authenticate with GitHub

When pushing, GitHub will ask you to log in:
- A browser window may open → sign in to GitHub
- OR enter your **GitHub username** and **Personal Access Token** (PAT)

#### 🔑 How to Create a Personal Access Token (PAT):
1. GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
2. Click **"Generate new token (classic)"**
3. Check ✅ **repo** scope
4. Click **Generate token**
5. Copy it — use it as your **password** when Git asks

---

## 🌐 STEP 8: Verify on GitHub

Go to:
```
https://github.com/deepikag123/Lung-Cancer-Detection-ML-Project
```
You should see all your files uploaded! ✅

---

## ▶️ STEP 9: Run the Project

In Command Prompt inside `E:\Cancer Detection\`:

```bash
pip install -r requirements.txt
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000
```

Upload a lung scan image and see the result! 🎉

---

## ⚠️ COMMON ERRORS & FIXES

| Error | Fix |
|-------|-----|
| `'git' is not recognized` | Install Git from git-scm.com |
| `Authentication failed` | Use a Personal Access Token (PAT) as password |
| `remote origin already exists` | Run: `git remote remove origin` then add again |
| `large file error` (model .h5) | Run: `git lfs install` → `git lfs track "*.h5"` → add & commit again |
| Port 5000 in use | Change `app.run(port=5001)` in app.py |

---

## 📞 Need Help?

- GitHub Docs: https://docs.github.com
- Git LFS (for large .h5 file): https://git-lfs.github.com
