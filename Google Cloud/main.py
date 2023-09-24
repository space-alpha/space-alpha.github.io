from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# NASA APOD API URL
apod_url = 'https://api.nasa.gov/planetary/apod'

# Replace 'YOUR_API_KEY' with your actual NASA API key
api_key = 'T4AdBg7CZyG3HgtCkkO5MHjJoubYt6D0HIcCf8OJ'

# Function to retrieve APOD image URL
def get_apod_image_url(date=None):
    params = {'api_key': api_key}
    if date:
        params['date'] = date

    response = requests.get(apod_url, params=params)

    if response.status_code == 200:
        apod_info = response.json()
        return apod_info.get('url', '')
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_apod', methods=['POST'])
def get_apod():
    date = request.form.get('date')
    apod_image_url = get_apod_image_url(date)
    return render_template('index.html', apod_image_url=apod_image_url)

if __name__ == '__main__':
    app.run(debug=True)
