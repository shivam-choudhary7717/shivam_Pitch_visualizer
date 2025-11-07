# shivam_Pitch_visualizer

The Pitch Visualizer

The Pitch Visualizer is an AI-powered Flask web app that transforms a short story or paragraph into a visual storyboard.
It automatically splits the text into logical scenes, creates descriptive prompts for each, and generates scene-by-scene illustrations using Hugging Face’s Stable Diffusion model.

Features

Accepts a short paragraph (3–5 sentences)

Automatically breaks it into scenes

Enhances each sentence into a more visual AI prompt

Generates an AI image for each scene using Hugging Face

Displays all generated visuals in a storyboard layout on a webpage

Tech Stack

Python 3.8 or higher

Flask (backend web framework)

NLTK (for text segmentation)

Requests (for API calls)

HTML and CSS with Jinja2 (for the user interface)

Installation and Setup

Clone the repository:
git clone https://github.com/shivam-choudhary7717/shivam_Pitch_visualizer.git

cd pitch-visualizer

Create a virtual environment:
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS/Linux)

Install dependencies:
pip install dotenv , os , nltk , requests , flask , openAI

Create a file named path_visualizer.env in the main folder and add your tokens:
HUGGINGFACE_TOKEN=hf_your_token_here
OPENAI_API_KEY=optional_if_you_use_openai

Running the App

Run this command:
python app.py

Then open your browser and go to:
http://127.0.0.1:5000/
