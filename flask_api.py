# Import flask and datetime module for showing date and time
from flask import Flask
from flask_cors import CORS

import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
CORS(app)



# Route for seeing a data
@app.route('/')
def get_time():
    # Returning an api for showing in reactjs
    return {
        'Name': "geek",
        "Age": "22",
        "Date": x,
        "programming": "python"
    }

# @app.route('/video')
# def add_user(u):



# Running app
if __name__ == '__main__':
    from waitress import serve
    print(5)
    serve(app, host="0.0.0.0", port=8080)
    # app.run(debug=True)
