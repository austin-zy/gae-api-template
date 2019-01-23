from flask import Flask, request
from flasgger import Swagger

from config.swagger import swagger_template, swagger_config
from controllers import example_controller

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'YOUR TITLE HERE',
    'uiversion': 3
}

swagger = Swagger(app, template=swagger_template, config=swagger_config)

action_options = {
    "testing": example_controller.example_do_something,
}


@app.route('/')
def hello_world():
    '''
    file: documentations/example.yml
    '''
    return example_controller.example_do_something()


# This is specifically for chatbot
@app.route('/chatbot_entrypoint', methods=['POST'])
def chatbot_entrypoint():
    '''
    file: documentations/chatbot_entrypoint.yml
    '''
    req = request.get_json(silent=True)
    query = request.get_json(silent=True)['queryResult']
    action = query['action']
    return action_options[action](query, req)


if __name__ == '__main__':
    app.run()
