#server1.py
from flask import Flask, request #import main Flask class and request object
import json

app = Flask(__name__) #create the Flask app

#http://694d334b.ngrok.io -> http://localhost:8888
@app.route('/', methods=['GET'])
def hello_world():
    return "hello"



#http://3e014fff.ngrok.io/zap-sent -> http://localhost:8888/zap-sent
@app.route('/zap-sent', methods=['POST','GET'])
def zap_sent():
    #return "test"
    
    req_data = request.get_json()
    print(json.dumps(req_data))

    language = req_data ['language']
    framework = req_data ['framework']
    python_version = req_data ['version_info']['python']
    examples = req_data ['examples'][0]
    boolean_test = req_data ['boolean_test']


    return '''<h1>
        The language value is {}.
        The framework value is {}.
        The Python version is {}.
        The example at 0 index is{}.
        The boolean value is {}.
        </h1>'''.format(language, framework, python_version, examples, boolean_test)

if __name__ == '__main_':
    app.run(port=8888) #run app on port 8888