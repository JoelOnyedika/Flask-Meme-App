import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    url = 'https://meme-api.com/gimme/50'
    response = requests.get(url)
    memes = response.json()['memes']

    return render_template('home.html', memes=memes)

@app.route('/image/<path:image_url>')
def show_image(image_url):
    return render_template('image.html', image_url=image_url)


if __name__ == '__main__':
    app.run(debug=True)
