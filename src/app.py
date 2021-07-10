import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeEngine import MemeGenerator

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file_path in quote_files:
        parsed_quotes = Ingestor.parse(file_path)
        quotes.extend(parsed_quotes)

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dir, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form['image_url']
    response = requests.get(image_url, stream=True)
    body = request.form['body']
    author = request.form['author']

    img_temp_path = f'./tmp/{random.randint(0, 1000)}.png'
    with open(img_temp_path, 'wb') as infile:
        infile.write(response.content)

    path = meme.make_meme(img_path=img_temp_path, text=body, author=author)

    os.remove(img_temp_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
