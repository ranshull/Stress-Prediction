# Stress-Prediction
---

## Stress Detection Web Application

This project is a web-based application for predicting stress levels based on user inputs. It uses a pre-trained machine learning model to categorize stress levels and recommends appropriate therapies (Yoga or Audio) based on the prediction.

---

## Features

- **Stress Level Prediction**: Predicts stress levels based on user-provided physiological data.
- **Therapy Recommendation**: Suggests Yoga or Audio therapy based on the predicted stress level.
- **Interactive Web Interface**: Simple and user-friendly interface for data input and results display.

---

## Technologies Used

- **Python**: Backend development  
- **Flask**: Web framework  
- **NumPy**: For numerical operations  
- **Joblib**: For loading the pre-trained machine learning model  
- **HTML/CSS**: For creating the web interface  

---

## Prerequisites

Ensure the following are installed on your system:

- Python (>=3.8)  
- pip (Python package manager)  

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**:  
   Install the required Python libraries using pip:
   ```bash
   pip install flask numpy joblib
   ```

3. **Add the Model File**:  
   - Place the pre-trained model file `2_stress_model.joblib` in the `models/` directory.  
   - Ensure the path to the model is correctly set in the code (`models/2_stress_model.joblib`).

4. **Add the Data Folder**:  
   - Include the `data/` directory in the project. This folder should contain any additional data files required for the application.

5. **Set Up Directory Structure**:  
   Ensure the following directory structure is maintained:
   ```
   project-folder/
   |-- models/
   |   |-- 2_stress_model.joblib
   |-- data/
   |   |-- [data-files]
   |-- static/
   |-- templates/
   |   |-- main.html
   |   |-- results.html
   |-- app.py
   ```

6. **Run the Application**:  
   Start the Flask server:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000/`.

---

## Usage

1. Navigate to the home page (`/`).  
2. Enter the required physiological data:  
   - Respiratory Rate (rr)  
   - Temperature (t)  
   - Light Movement (lm)  
   - Body Orientation (bo)  
   - Rapid Eye Movement (rem)  
   - Stress Response 1 (sr1)  
   - Heart Rate (hr)  
3. Submit the form to get the predicted stress level and recommended therapy.  
4. Follow the recommended therapy link for more details.

---

## Application Routes

- `/`: Displays the home page with the input form.  
- `/submit_form`: Processes the form data, predicts stress levels, and displays results.  
- `/yoga_therapy`: Displays the Yoga Therapy page.  
- `/audio_therapy`: Displays the Audio Therapy page.  

---

## Example Prediction Mapping

| Predicted Value | Stress Level         | Recommended Therapy |
|-----------------|----------------------|----------------------|
| 0               | Low/Normal          | Audio               |
| 1               | Medium Low          | Audio               |
| 2               | Medium              | Audio               |
| 3               | Medium High         | Yoga                |
| 4               | High                | Yoga                |

---

## Troubleshooting

1. **Model File Not Found**:  
   Ensure the `2_stress_model.joblib` file exists in the `models/` directory.

2. **Data Files Missing**:  
   Verify that the required data files are present in the `data/` directory.

3. **Invalid Input Error**:  
   Double-check that all inputs are numeric and within valid ranges.

4. **Route Not Found**:  
   Verify that the `yoga_therapy` and `audio_therapy` routes are implemented in `app.py`.

---

## Future Enhancements

- Integrate more sophisticated stress prediction models.  
- Add visualizations for input data and predictions.  
- Provide detailed therapy guides on respective therapy pages.  
- Deploy the application to a cloud platform (e.g., AWS, Heroku).  

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- **Machine Learning Model**: Pre-trained model developed for stress detection.  
- **Flask**: Lightweight web framework for Python.  
- **Therapy Code**: The Yoga and Audio Therapy pages' code was sourced from [Sukoon repository](https://github.com/Susmita-Dey/Sukoon/tree/main) by [Susmita Dey](https://github.com/Susmita-Dey).  
- **Contributors**: [Anshul Rawat].  

😊