from __future__ import division, print_function

import sys
import os
import  os.path
import glob
import  re
import numpy as np

from keras.applications.imagenet_utils import preprocess_input,decode_predictions
from keras.models import load_model
from keras.preprocessing import image
# from code_for_db import main,fetch_data
# from keras.applications.resnet50 import decode_predictions


from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from flask import redirect,url_for,request,render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer


MODEL_PATH = "dnn/mpg_model.h5"

mymodel = load_model(MODEL_PATH)
mymodel.make_predict_function()


import os
from flask import request
from flask import Flask
from flask import render_template

app = Flask(__name__,static_url_path='/static')
MODEL_PATH = "my_model"

@app.route('/',methods=["GET","POST"])



def upload_pred():
    if request.method=="POST":
        image_file = request.files["image"]
        predict="No file uploaded"
        if image_file:
          base_path = os.path.dirname(os.path.abspath(__file__))
          file_path = os.path.join(base_path,'evaluate',image_file.filename)
          image_file.save(file_path)
          predict = model_predict(file_path,image_file)
        return render_template("index.html",prediction=predict)
    return render_template("index.html",prediction="Upload Image")


def model_predict(file_path,image_file):
    MODEL_PATH = "dnn/mpg_model.h5"
    mymodel = load_model(MODEL_PATH)
    mymodel.make_predict_function()
    class_name = ["Flood","No Flood"]
    img = image.load_img(file_path,target_size=(224,224))
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    x=image.img_to_array(img)
    normalized_image_array = (x.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    predict1 = mymodel.predict(data)
    print(predict1)
    index_max = np.argmax(predict1)
    print(index_max)
    remove_image(file_path,image_file)
    
    return class_name[index_max]

def remove_image(file_path,image_file):
    os.remove(file_path)
# check if file exists or not
    if os.path.exists(file_path) is False:
        # file did not exists
        return True



if __name__ == "__main__": 
     app.run(debug=True)
    


