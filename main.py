from flask import Flask, request, jsonify
from flasgger import Swagger
import pandas as pd
import pymysql
from config.swagger import swagger_template, swagger_config
from controllers import example_controller

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': '',
    'uiversion': 3
}

swagger = Swagger(app, template=swagger_template, config=swagger_config)

@app.route('/name')
def name():
    return jsonify({"name":"gzy"})

@app.route('/hello_world')
def hello_world():
    '''
    file: documentations/example.yml
    '''
    sql = """
    SELECT * FROM `bigquery-public-data.samples.gsod` LIMIT 100
    """
    df = pd.read_gbq(sql, project_id='radiant-micron-790',  dialect='standard')
    records = df.to_dict(orient='records')
    return jsonify({"results": records})

@app.route('/call_query')
def call_query():
    '''
    file: documentations/example.yml
    '''
    sql = """
    SELECT * FROM `bigquery-public-data.samples.gsod` LIMIT 100
    """
    conn = pymysql.connect(host='35.186.156.137',
                             user='viewer',
                             password='password123',
                             db='datadict',
                             cursorclass=pymysql.cursors.DictCursor)
    df = pd.read_sql('SELECT * FROM datadict.systems',con=conn)
    records = df.to_dict(orient='records')
    return jsonify({"results": records})

if __name__ == '__main__':
    app.run(debug=True)
