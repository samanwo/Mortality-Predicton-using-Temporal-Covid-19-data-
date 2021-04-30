# import flask
# from flask import Flask, jsonify, request
# import json
# from data_input import data_in
# import numpy as np
# import pickle
# import xgboost



# def load_models():
#     file_name = "models/model_file.p"
#     with open(file_name, 'rb') as pickled:
#         data = pickle.load(pickled)
#         model = data['model']
#     return model

# app = Flask(__name__)
# @app.route('/predict', methods=['GET'])

# def predict():
#     # stub input features
#     x = np.array(data_in).reshape(1,-1)
#     query = input('input patient data')
#     print(x)
#     # load model
#     model = load_models()
#     prediction = model.predict(x)[0]
#     response = json.dumps({'Estimated Number of Days for patient to die ': prediction})
#     return response, 200

# if __name__ == '__main__':
#     application.run(debug=True)

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Estimated number of days to die {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)