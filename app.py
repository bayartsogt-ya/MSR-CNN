
import os
from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource
from flask_cors import CORS

from label_wav import label_wav
from split_on_silence import get_chunk
import time
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['UPLOAD_FOLDER'] = 'uploads/original'

api = Api(app, prefix="/api/to_back_end")
PATH = os.path.dirname(os.path.abspath(__file__))

timestamp = time.time()
class Predictor(Resource):

    def get(self):

        content = request.json
        return make_response(jsonify(
            content
        ), 200)

    def post(self):

        audio_webm = request.files['blob']
        audio_webm.save(os.path.join(app.config['UPLOAD_FOLDER'], str(timestamp)+".webm"))

        try:
            if(get_chunk(str(timestamp)+".webm")=="silence"):
                raise FileExistsError
            else:
                top = label_wav("uploads/chunk0.wav", "sp_train/conv_labels.txt", "model/my_frozen_graph.pb", "wav_data:0", "labels_softmax:0", 4)
                print(top)
                return make_response(jsonify(
                    top
                ), 200)
        except FileExistsError:
            return make_response(jsonify(
                "silence"
            ), 200)

api.add_resource(Predictor, '/predict')

if __name__ == '__main__':
    app.run(debug=True)
