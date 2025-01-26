# from flask import Flask, render_template, request, redirect, url_for
# import joblib
# from tensorflow.keras.models import load_model
# import numpy as np
# import cv2
# import os
# from flask import Flask, render_template, request, jsonify


# app = Flask(__name__, static_folder='static')

# #------------------------------------------------------------------
# # Load the trained mode
# model_path = 'models/2_stress_model.joblib'                                         
# model = joblib.load(model_path)
# #----------------------------------------------------------------

# @app.route('/')
# def Pstress():
#     return render_template('main.html')

# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#      # Retrieve form data
#     rr = float(request.form['rr'])
#     t = float(request.form['t'])
#     lm = float(request.form['lm'])
#     bo = float(request.form['bo'])
#     rem = float(request.form['rem'])
#     sr1 = float(request.form['sr1'])
#     hr = float(request.form['hr'])
    
#    # Create an input array for the model
#     input_data = np.array([[rr, t, lm, bo, rem, sr1, hr]])

#     # Make prediction
#     prediction = model.predict(input_data)[0]  # This will be a numerical value (0-4)
    
#     # Map the prediction to a stress level
#     stress_levels = ["Low/Normal", "Medium Low", "Medium", "Medium High", "High"]
#     stress_category = stress_levels[prediction]

#        # Determine recommended therapy based on stress level
#     if prediction >= 3:  # High or Medium High Stress
#         therapy_link = url_for('yoga_therapy')  # Correctly link to yoga therapy page
#         therapy_name = "Yoga"
#     else:  # Low, Medium Low, or Medium Stress
#         therapy_link = url_for('audio_therapy')  # Correctly link to audio therapy page
#         therapy_name = "Audio"


#    # Render the results page with the prediction and therapy link
#     return render_template('results.html', prediction=prediction, stress_category=stress_category, therapy_link=therapy_link, therapy_name=therapy_name)

# #---------------
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__, static_folder='static')

# Load the trained model
model_path = 'models/2_stress_model.joblib'
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    print(f"Error: Model file not found at {model_path}")
    exit(1)

@app.route('/')
def Pstress():
    return render_template('main.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Retrieve form data
    try:
        rr = float(request.form['rr'])
        t = float(request.form['t'])
        lm = float(request.form['lm'])
        bo = float(request.form['bo'])
        rem = float(request.form['rem'])
        sr1 = float(request.form['sr1'])
        hr = float(request.form['hr'])
    except ValueError:
        return "Invalid input! Please enter numeric values only.", 400

    # Create an input array for the model
    input_data = np.array([[rr, t, lm, bo, rem, sr1, hr]])

    # Make prediction
    prediction = int(model.predict(input_data)[0])  # Cast prediction to integer
    
    # Map the prediction to a stress level
    stress_levels = ["Low/Normal", "Medium Low", "Medium", "Medium High", "High"]
    stress_category = stress_levels[prediction]

    # Determine recommended therapy based on stress level
    if prediction >= 3:  # High or Medium High Stress
        therapy_link = url_for('yoga_therapy')  # Ensure 'yoga_therapy' route exists
        therapy_name = "Yoga"
    else:  # Low, Medium Low, or Medium Stress
        therapy_link = url_for('audio_therapy')  # Ensure 'audio_therapy' route exists
        therapy_name = "Audio"

    # Render the results page with the prediction and therapy link
    return render_template('results.html', prediction=prediction, stress_category=stress_category, therapy_link=therapy_link, therapy_name=therapy_name)

# Ensure routes for therapies are defined
@app.route('/yoga_therapy')
def yoga_therapy():
    return "Yoga Therapy Page"

@app.route('/audio_therapy')
def audio_therapy():
    return "Audio Therapy Page"

if __name__ == '__main__':
    app.run(debug=True)
