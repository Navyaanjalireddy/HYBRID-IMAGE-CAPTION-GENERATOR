# Hybrid Image Caption Generator

> 🖼️ An AI-powered web application that automatically generates meaningful and descriptive captions for uploaded images using Deep Learning and the BLIP image-captioning model.
---

 🌟 Overview

The **Hybrid Image Caption Generator** is a Flask-based web application that combines Computer Vision and Natural Language Processing to understand images and generate human-readable captions.

Users can upload an image through an interactive web interface, and the application processes the image using the **BLIP (Bootstrapping Language-Image Pre-training)** model to generate an appropriate caption.

The application also provides multilingual translation support, making generated captions more accessible to users in different languages. 🌍

---

## ✨ Features

- 🖼️ **Image Upload** – Upload images directly through the web interface.
- 🤖 **AI-Based Caption Generation** – Generate descriptive captions automatically.
- 🧠 **BLIP Model** – Uses a pre-trained BLIP image-captioning model from Hugging Face.
- 🌍 **Multilingual Translation** – Translate generated captions into multiple languages.
- 🔊 **User-Friendly Interface** – Clean and responsive web interface.
- ⚡ **Real-Time Processing** – Generate captions immediately after uploading an image.
- 📱 **Responsive Design** – Designed for convenient use across different screen sizes.
- 🔒 **Secure File Handling** – Uses Flask's secure filename handling for uploaded files.

---

## 🛠️ Technologies Used

### 💻 Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap
- Font Awesome

### ⚙️ Backend
- Python 🐍
- Flask

### 🧠 AI / Machine Learning
- Hugging Face Transformers 🤗
- BLIP Image Captioning Model
- PyTorch

### 🌐 Translation
- Deep Translator

### 🖼️ Image Processing
- Pillow (PIL)

---

## 🧩 System Workflow

```text
                ┌──────────────────┐
                │   Upload Image   │
                └────────┬─────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Image Validation   │
              └──────────┬───────────┘
                         │
                         ▼
             ┌────────────────────────┐
             │ Image Preprocessing    │
             │      using PIL         │
             └───────────┬────────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   BLIP Image Model   │
              │ Hugging Face Model   │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Caption Generation   │
              └──────────┬───────────┘
                         │
              ┌──────────┴───────────┐
              │                      │
              ▼                      ▼
     ┌─────────────────┐    ┌─────────────────┐
     │   Translation   │    │ Text-to-Speech  │
     │   🌍 Languages  │    │      🗣️         │
     └─────────────────┘    └─────────────────┘
              │                      │
              └──────────┬───────────┘
                         ▼
                ┌──────────────────┐
                │   User Output    │
                │ Generated Caption│
                └──────────────────┘

```
### 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Navyaanjalireddy/HYBRID-IMAGE-CAPTION-GENERATOR.git
```
### 2️⃣ Navigate to the Project Directory

```bash
cd HYBRID-IMAGE-CAPTION-GENERATOR
```
### 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```
### 4️⃣ Activate the Virtual Environment

Windows:
```bash
venv\Scripts\activate
```
### 5️⃣ Install Required Dependencies
```bash
pip install -r requirements.txt
```
### 6️⃣ Run the Application
```bash
python app.py
```
### 7️⃣ Open the Web Application

After running the application, open the local Flask URL displayed in the terminal:

http://127.0.0.1:5000/

### 📂 Project Structure

```text
HYBRID-IMAGE-CAPTION-GENERATOR/
│
├── 📁 hybrid_image_caption_generator_/
│   │
│   ├── 📁 static/
│   │   └── 📁 uploads/
│   │
│   ├── 📁 templates/
│   │   └── 📄 index.html
│   │
│   ├── 🐍 app.py
│   ├── 📄 requirements.txt
│   └── 📄 .gitignore
│
└── 📄 README.md
```
### 🌍 Multilingual Support

The application provides multilingual support for generated captions, making the system accessible to users from different linguistic backgrounds.

### 🗣️ Supported Languages

- 🇬🇧 English
- 🇮🇳 Telugu
- 🇮🇳 Hindi
- 🇮🇳 Tamil
- 🇮🇳 Kannada
- 🇮🇳 Malayalam

Users can generate an image caption and translate the generated caption into their preferred language using the built-in translation functionality.

---
## 🔮 Future Enhancements

The project can be further enhanced with:

- 🔐 User Login & Registration
- 👤 Personalized User Dashboard
- 🗂️ Caption History Management
- 📸 Multiple Image Upload
- ☁️ Cloud Deployment
- 📱 Improved Mobile Responsiveness
- 🎙️ Advanced Voice Interaction
- 🧠 Integration of Advanced Image Captioning Models
- 🌍 Support for Additional Languages
- ⚡ Faster Model Inference
- 📊 Caption Quality Evaluation
- 💾 Database Integration for User History

---
