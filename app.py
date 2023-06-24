from flask import Flask, render_template, request
from keras.models import load_model
import keras.utils as image
import numpy as np

app = Flask(__name__)

model = load_model("new_Model.h5")

@app.route('/' , methods = ['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/' , methods = ['POST'])
def predict():
    img = request.files['imagefile']
    img_path = "static/" + img.filename
    img.save(img_path)

    test_image = image.load_img(img_path, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)

    if result[0][0] == 1:
        prediction = 'Alia Bhatt'
    elif result[0][1] == 1:
        prediction = 'Kiara Advani'
    elif result[0][2] == 1:
        prediction = 'MS Dhoni'
    elif result[0][3] == 1:
        prediction = 'Narendra Modi'
    elif result[0][4] == 1:
        prediction = 'Shraddha Kapoor'


    return render_template('index.html', prediction_text=f' The Result is {prediction}')
# def predict_label(img_path):
#     i = image.load_img(img_path, target_size=(64, 64))
#     i = image.img_to_array(i)
#     i = np.expand_dims(i, axis=0)
#     result = model.predict(i)
#
#     return result
#
# # routes
# @app.route("/", methods=['GET', 'POST'])
# def main():
#     return render_template("index2.html")
#
# @app.route("/submit", methods = ['GET', 'POST'])
# def get_output():
#     if request.method == 'POST':
#         img = request.files['my_image']
#
#         img_path = "static/" + img.filename
#         img.save(img_path)
#
#         print(img_path)
#
#
#
#         result = predict_label(img_path)
#
#         prediction=""
#         if result[0][0] == 1:
#             prediction = 'Alia Bhatt'
#         elif result[0][1] == 1:
#             prediction = 'Justin Bieber'
#         elif result[0][2] == 1:
#             prediction = 'MS Dhoni'
#         elif result[0][3] == 1:
#             prediction = 'Narendra Modi'
#         elif result[0][4] == 1:
#             prediction = 'Shraddha Kapoor'
#
#         return render_template('index2.html' , img_path = img_path)
#
#
if __name__ =='__main__':
    app.run(debug = True)