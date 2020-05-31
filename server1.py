#server1.py
from flask import Flask, request #import main Flask class and request object
import json

app = Flask(__name__) #create the Flask app

#http://884549d31ca6.ngrok.io/zap-sent -> http://localhost:8080/zap-sent
@app.route('/zap-sent', methods=['POST','GET'])
def zap_sent():
    if request.method == 'POST':
        print(request.json)
        return '', 200
    else:
        abort(400)

if __name__ == '__main_':
    app.run(port=8000) #run app on port 8080

    #req_data = request.get_json()
    #print(json.dumps(req_data))

    #language = req_data ['language']
    #framework = req_data ['framework']
    #python_version = req_data ['version_info']['python']
    #examples = req_data ['examples'][0]
    #boolean_test = req_data ['boolean_test']


    #return '''<h1>
        #The language value is {}.
        #The framework value is {}.
        #The Python version is {}.
        #The example at 0 index is{}.
        #The boolean value is {}.
        #</h1>'''.format(language, framework, python_version, examples, boolean_test)
