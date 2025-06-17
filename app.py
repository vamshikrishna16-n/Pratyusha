from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, template_folder='templates')
CORS(app)

# Route to serve the main page
@app.route('/')
def home():
    return render_template('index.html')

# Route to serve static files (like CSS, JS, or favicon)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# Optional: API endpoint for love messages
@app.route('/api/love_message', methods=['GET'])
def love_message():
    return {
        'message': 'Pratyusha, you make my heart skip a beat!',
        'author': 'Your Secret Admirer',
        'special': True
    }

if __name__ == '__main__':
    # Create necessary folders if they don't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    if not os.path.exists('static'):
        os.makedirs('static')
    
    app.run(debug=True, port=5000)