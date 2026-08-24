# Hybrid Image Caption Generator

A reconstructed version of the Hybrid Image Caption Generator web application.

## Features visible in the project output screens

- Dark responsive web interface
- Image upload
- BLIP-based image caption generation
- Uploaded-image preview
- English caption display
- Read caption in English
- Translate caption to:
  - Telugu
  - Hindi
  - Tamil
  - Kannada
  - Malayalam
- Browser speech output for translated text
- Bootstrap-based interface

## Model

The project report's source-code chapter uses:

`Salesforce/blip-image-captioning-base`

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open:

`http://127.0.0.1:5000`

The first run downloads the BLIP model from Hugging Face.

## Important reconstruction note

The report documents the BLIP captioning code and describes multilingual captioning/TTS as project features. The screenshots supplied with the project show the five translation buttons and translated output.

The printed source-code section in the report does not contain the translation endpoint implementation. Therefore, the translation backend in this reconstructed version is a new implementation added to reproduce the demonstrated UI behavior; it should not be treated as an exact recovery of the lost original translation code.

The browser Speech Synthesis API is used for audio playback because the supplied screens show "Read in English" and translated text output.

## Suggested Git commands

```bash
git init
git add .
git commit -m "Reconstruct hybrid image caption generator"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
