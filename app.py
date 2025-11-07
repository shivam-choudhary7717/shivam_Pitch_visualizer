from dotenv import load_dotenv
import os
import nltk
import requests
from flask import Flask, render_template, request
from openai import OpenAI

# Load environment variables from .env
load_dotenv(dotenv_path="path_visualizer.env")

# Access API key from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)

nltk.download('punkt')

def segment_text(text):
    sentences = nltk.sent_tokenize(text)
    return sentences[:5]

def engineer_prompt(scene):
    return (
        f"crete a detailed scene :"
        f"{scene}.focus on emotions , atmosphere , visual storytelling."
    )

def generate_image_openai(prompt):
    try:
        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )
        return result.data[0].url
    except Exception as e:
        print(e)
        return None

def generate_image_huggingface(prompt):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        # Save the image locally
        image_bytes = response.content
        image_path = f"static/output_{hash(prompt)}.png"
        os.makedirs("static", exist_ok=True)
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        return image_path
    else:
        print("❌ Hugging Face error:", response.text)
        return None

def generate_image(prompt):
    image_url = generate_image_huggingface(prompt)
    if image_url:
        return image_url
    else :
        return None

@app.route('/',methods=['GET','POST'])
def index():
    storyboard = []

    if request.method == 'POST':
        text = request.form['text']
        scenes = segment_text(text)

        for scene in scenes :
            visual_prompt = engineer_prompt(scene)
            image_url = generate_image(visual_prompt)
            storyboard.append({
                "scene":scene,
                "prompt":visual_prompt,
                "image_url":image_url
            })
    
    return render_template('index.html',storyboard=storyboard)

if __name__ == '__main__':
    app.run(debug=True)


