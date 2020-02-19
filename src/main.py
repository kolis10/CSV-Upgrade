"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import io
import csv
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
from datetime import datetime, timedelta
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200

@app.route('/tournaments/upload', methods=['POST','GET'])
def upload_tournaments():
    
    if 'csv' not in request.files:
        raise APIException('"csv" property should be in file, Issac')

    f = request.files['csv']                        #} gets csv from files

    f_read = io.StringIO(f.read().decode())         #}  csv reader
    files_row = csv.reader(f_read, delimiter = ',') #}

    headers = []
    for x in files_row:
        # headers.append(files_row[0])
        return jsonify(x)

@app.route('/tournament_list', methods=['POST', 'GET'])
def tournament_list():
    
    if 'csv' not in request.files:
        raise APIException('"csv" property should be in file, Issac')

    f = request.files['csv']                        #} gets csv from files

    f_read = io.StringIO(f.read().decode())         #}  csv reader
    files_row = csv.reader(f_read, delimiter = ',') #}

    json = request.get_json()

    lst = [x for x in files_row]
    headers = lst[0]
    lst = lst[1:]

    date = []
    for x in lst:
        date.append(x[0])
    
    day = []
    for x in lst:
        day.append(x[1])

    time = []
    for x in lst:
        time.append(x[2])
    
    casino = []
    for x in lst:
        casino.append(x[3])
    
    name = []
    for x in lst:
        name.append(x[4])
    
    buy_in = []
    for x in lst:
        buy_in.append(x[5])
    
    starting_stack = []
    for x in lst:
        starting_stack.append(x[6])
    
    blinds = []
    for x in lst:
        blinds.append(x[7])
    
    structure_link = []
    for x in lst:
        structure_link.append(x[8])
    
    notes = []
    for x in lst:
        notes.append(x[12])
    
    results_link = []
    for x in lst:
        results_link.append(x[13])
    
    dict_list = []
    for i, word in enumerate(lst):
        # date = datetime.utcnow()
        if day[i] == '' or date[i] == '' or time[i] == '':
            continue

        dt_object0 = day[i] + ' ' + date[i] + ' ' + time[i]
        dt_object2 = datetime.strptime(dt_object0, '%a %d-%b-%y %H:%M %p')

        tournament_dict = {}
        tournament_dict["casino"] = casino[i]
        tournament_dict["name"] = name[i]
        tournament_dict["buy_in"] = buy_in[i]
        tournament_dict["blinds"] = blinds[i]
        tournament_dict["starting_stack"] = starting_stack[i]
        tournament_dict["results_link"] = results_link[i]
        tournament_dict["structure_link"] = structure_link[i]
        tournament_dict["start_at"] = dt_object2
        tournament_dict["notes"] = notes[i]
        # tournament_dict["created_at"] = date
        # tournament_dict["updated_at"] = updated_at[i]
        dict_list.append( tournament_dict )
        
        
    return jsonify( dict_list )
    


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
