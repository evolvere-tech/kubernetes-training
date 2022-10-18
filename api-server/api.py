from flask import render_template
from flask_cors import CORS
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the yaml file to configure the endpoints
app.add_api('schema.yaml')
CORS(app.app)

# Create a URL route in our application for "/"
@app.route('/', methods=['GET'])
def home():
    return '''<h1>DRW Demo</h1>'''

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
