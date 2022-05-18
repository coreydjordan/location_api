import requests
from dotenv import dotenv_values
from flask import Flask, render_template, request

# Base Url for geocoding
app = Flask(__name__)


ENV = dotenv_values()
@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        address = request.form['address_field']

    #Your unique private_token should replace value of the private_token variable.
    #To know how to obtain a unique private_token please refer the README file for this script.

        data = {
            'key': ENV['PRIVATE_TOKEN'],
            'q': address,
            'format': 'json'
        }

        try:
            response = requests.get(ENV['URL'], params=data)
        except Exception as e:
            raise e

        latitude = response.json()[0]['lat']
        longitude = response.json()[0]['lon']

        res = {
            'message' : address,
            'latitude': latitude,
            'longitude': longitude
        }

        return render_template('results.html', **res)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host=ENV['HOST'], port=ENV['PORT'], debug=True)


