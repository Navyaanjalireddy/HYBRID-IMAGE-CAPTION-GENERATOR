import os

from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Translation is used for the multilingual buttons shown in the project UI.
# The original report documents multilingual captioning, but its printed
# source-code section does not include the translation implementation.
try:
    from deep_translator import GoogleTranslator
except ImportError:
    GoogleTranslator = None

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}

# BLIP model documented in the project report.
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs)
    return processor.decode(output[0], skip_special_tokens=True)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return redirect(url_for("index"))

    file = request.files["image"]

    if file.filename == "" or not allowed_file(file.filename):
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    caption = generate_caption(filepath)

    return render_template(
        "index.html",
        filename=filename,
        caption=caption
    )


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()
    language = data.get("language", "").strip().lower()

    language_codes = {
        "telugu": "te",
        "hindi": "hi",
        "tamil": "ta",
        "kannada": "kn",
        "malayalam": "ml",
    }

    if not text or language not in language_codes:
        return jsonify({"error": "Invalid translation request."}), 400

    if GoogleTranslator is None:
        return jsonify({
            "error": "Translation dependency is not installed. "
                     "Run: pip install deep-translator"
        }), 500

    try:
        translated = GoogleTranslator(
            source="en",
            target=language_codes[language]
        ).translate(text)

        return jsonify({"translation": translated})
    except Exception as exc:
        return jsonify({
            "error": f"Translation failed: {exc}"
        }), 500


if __name__ == "__main__":
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    app.run(debug=True)
