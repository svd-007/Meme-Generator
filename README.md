# Meme-Generator

This is a multi-media application built to dynamically generate memes,
including an image with an overlaid quote.

The following are the features of this application:
- Interacts with and loads quotes from a variety of complex filetypes.
- Load, manipulate and save images.
- Accept dynamic user input through a command-line tool and a web service.

All required dependencies are listed in the root `requirements.txt`.

Instructions:

    CLI:
        1) clone the repository: git clone
           https://github.com/svd-007/Meme-Generator
        2) Create a virtual environement (as wanted): python3 -m venv .
        3) Activate the venv: source ./bin/activate
        4) Install the dependencies: pip install -r requirements.txt
        5) Run meme.py script with the arguments required:
           python3 meme.py --path --body --author

    Flask server:
        1) Clone the repository: git clone
           https://github.com/svd-007/Meme-Generator
        2) Create a virtual environement (as wanted): python3 -m venv .
        3) Activate the venv: source ./bin/activate
        4) Install the dependencies: pip install -r requirements.txt
        5) Run app.py script: python3 app.py
        6) Navigate to your localhost as served by flask
           (http://127.0.0.1:5000/ by default)


Program organization:
- app.py: Runs the Flask server.
- meme.py: Runs the CLI.
- _data: Used for storage and retrival of the data (quotes or images).
- MemeEngine: Module responsible for manipulating and drawing text onto the
  images.
- QuoteEngine: Module responsible for ingesting many types of files that
  contain quotes.
- tmp: Default folder to save the output meme.