import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# --- Page Configuration ---
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# --- Dark Mode Theme ---
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #1a1a1a;
        color: #f0f0f0;
    }
    [data-testid="stHeader"] {
        background-color: #1a1a1a;
    }
    [data-testid="stSidebar"] {
        background-color: #262626;
        color: #f0f0f0;
    }
    .st-bb { /* Selectbox background */
        background-color: #333333;
        color: #f0f0f0;
    }
    .st-bb div div p { /* Selectbox text */
        color: #f0f0f0;
    }
    .st-c7 { /* Number input background */
        background-color: #333333;
        color: #f0f0f0;
    }
    .st-c7 input { /* Number input text */
        color: #f0f0f0;
    }
    .st-d6 { /* Text input background */
        background-color: #333333;
        color: #f0f0f0;
    }
    .st-d6 input { /* Text input text */
        color: #f0f0f0;
    }
    button {
        color: #f0f0f0 !important;
        background-color: #007bff !important;
        border-color: #007bff !important;
    }
    button:hover {
        background-color: #0056b3 !important;
        border-color: #0056b3 !important;
    }
    .stSuccess {
        color: #28a745 !important;
        background-color: #386842 !important;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Hiding Streamlit Add-ons ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- Load the Saved Models ---
models = {
    'diabetes': pickle.load(open('C:\\Users\\aadhi\\Desktop\\Medical diagnosis using AI\\Models\\diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('C:\\Users\\aadhi\\Desktop\\Medical diagnosis using AI\\Models\\heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('C:\\Users\\aadhi\\Desktop\\Medical diagnosis using AI\\Models\\parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('C:\\Users\\aadhi\\Desktop\\Medical diagnosis using AI\\Models\\lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('C:\\Users\\aadhi\\Desktop\\Medical diagnosis using AI\\Models\\Thyroid_model.sav', 'rb'))
}

# --- Sidebar Menu ---
with st.sidebar:
    selected = option_menu(
        "Disease Prediction",
        ["Diabetes", "Heart Disease", "Parkinsons", "Lung Cancer", "Hypo-Thyroid"],
        icons=['activity', 'heart-fill', 'person-fill', 'lungs-fill', 'bandaid-fill'],
        menu_icon="hospital-fill",
        default_index=0,
        styles={
            "container": {"padding": "10px !important", "background-color": "#262626"},
            "icon": {"color": "#f0f0f0", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#404040",
            },
            "nav-link-selected": {"background-color": "#007bff"},
        }
    )

def display_input(label, tooltip, key, col, type="text"):
    with col:
        if type == "text":
            return st.text_input(label, key=key, help=tooltip)
        elif type == "number":
            return st.number_input(label, key=key, help=tooltip, step=1)

# --- Prediction Pages ---

if selected == 'Diabetes':
    st.title('Diabetes Prediction')
    st.markdown("<p style='color:#a9a9a9;'>Enter the following details to predict diabetes:</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    Pregnancies = display_input('Pregnancies', 'Number of times pregnant', 'Pregnancies', col1, 'number')
    Glucose = display_input('Glucose Level', 'Plasma glucose concentration a 2 hours in an oral glucose tolerance test', 'Glucose', col2, 'number')
    BloodPressure = display_input('Blood Pressure', 'Diastolic blood pressure (mm Hg)', 'BloodPressure', col1, 'number')
    SkinThickness = display_input('Skin Thickness', 'Triceps skin fold thickness (mm)', 'SkinThickness', col2, 'number')
    Insulin = display_input('Insulin Level', '2-Hour serum insulin (mu U/ml)', 'Insulin', col1, 'number')
    BMI = display_input('BMI', 'Body mass index (weight in kg/(height in m)^2)', 'BMI', col2, 'number')
    DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function', 'Diabetes pedigree function', 'DiabetesPedigreeFunction', col1, 'number')
    Age = display_input('Age', 'Age (years)', 'Age', col2, 'number')

    diab_diagnosis = ''
    if st.button('Predict Diabetes'):
        diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_diagnosis = 'The person is likely to have diabetes' if diab_prediction[0] == 1 else 'The person is unlikely to have diabetes'
        st.success(diab_diagnosis)

elif selected == 'Heart Disease':
    st.title('Heart Disease Prediction')
    st.markdown("<p style='color:#a9a9a9;'>Enter the following details to predict heart disease:</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    age = display_input('Age', 'Age of the person', 'age', col1, 'number')
    sex = display_input('Sex (1=Male, 0=Female)', 'Sex of the person', 'sex', col2, 'number')
    cp = display_input('Chest Pain Type', 'Chest pain type (0-3)', 'cp', col1, 'number')
    trestbps = display_input('Resting Blood Pressure', 'Resting blood pressure (in mm Hg on admission to the hospital)', 'trestbps', col2, 'number')
    chol = display_input('Serum Cholesterol', 'Serum cholesterol in mg/dl', 'chol', col1, 'number')
    fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)', 'Fasting blood sugar > 120 mg/dl', 'fbs', col2, 'number')
    restecg = display_input('Resting ECG', 'Resting electrocardiographic results (0-2)', 'restecg', col1, 'number')
    thalach = display_input('Max Heart Rate', 'Maximum heart rate achieved', 'thalach', col2, 'number')
    exang = display_input('Exercise Induced Angina (1=Yes, 0=No)', 'Exercise induced angina', 'exang', col1, 'number')
    oldpeak = display_input('ST Depression', 'ST depression induced by exercise relative to rest', 'oldpeak', col2, 'number')
    slope = display_input('Slope of Peak Exercise ST Segment', 'The slope of the peak exercise ST segment', 'slope', col1, 'number')
    ca = display_input('Major Vessels Colored by Fluoroscopy (0-3)', 'Number of major vessels (0-3) colored by fluoroscopy', 'ca', col2, 'number')
    thal = display_input('Thal (0-3)', 'Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect', 'thal', col1, 'number')

    heart_diagnosis = ''
    if st.button('Predict Heart Disease'):
        heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person is likely to have heart disease' if heart_prediction[0] == 1 else 'The person is unlikely to have heart disease'
        st.success(heart_diagnosis)

elif selected == "Parkinsons":
    st.title("Parkinson's Disease Prediction")
    st.markdown("<p style='color:#a9a9a9;'>Enter the following details to predict Parkinson's disease:</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    fo = display_input('MDVP:Fo(Hz)', 'Average vocal fundamental frequency', 'fo', col1, 'number')
    fhi = display_input('MDVP:Fhi(Hz)', 'Maximum vocal fundamental frequency', 'fhi', col2, 'number')
    flo = display_input('MDVP:Flo(Hz)', 'Minimum vocal fundamental frequency', 'flo', col1, 'number')
    Jitter_percent = display_input('MDVP:Jitter(%)', 'Jitter (percentage)', 'Jitter_percent', col2, 'number')
    Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Jitter (absolute)', 'Jitter_Abs', col1, 'number')
    RAP = display_input('MDVP:RAP', 'Mel-frequency cepstral coefficients', 'RAP', col2, 'number')
    PPQ = display_input('MDVP:PPQ', 'Mel-frequency cepstral coefficients', 'PPQ', col1, 'number')
    DDP = display_input('Jitter:DDP', 'Mel-frequency cepstral coefficients', 'DDP', col2, 'number')
    Shimmer = display_input('MDVP:Shimmer', 'Amplitude perturbation quotient', 'Shimmer', col1, 'number')
    Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Amplitude perturbation quotient', 'Shimmer_dB', col2, 'number')
    APQ3 = display_input('Shimmer:APQ3', 'Amplitude perturbation quotient', 'APQ3', col1, 'number')
    APQ5 = display_input('Shimmer:APQ5', 'Amplitude perturbation quotient', 'APQ5', col2, 'number')
    APQ = display_input('MDVP:APQ', 'Amplitude perturbation quotient', 'APQ', col1, 'number')
    DDA = display_input('Shimmer:DDA', 'Amplitude perturbation quotient', 'DDA', col2, 'number')
    NHR = display_input('NHR', 'Noise to harmonic ratio', 'NHR', col1, 'number')
    HNR = display_input('HNR', 'Harmonic to noise ratio', 'HNR', col2, 'number')
    RPDE = display_input('RPDE', 'Recurrence period density entropy', 'RPDE', col1, 'number')
    DFA = display_input('DFA', 'Detrended fluctuation analysis', 'DFA', col2, 'number')
    spread1 = display_input('Spread1', 'Measures of fundamental frequency variation', 'spread1', col1, 'number')
    spread2 = display_input('Spread2', 'Measures of fundamental frequency variation', 'spread2', col2, 'number')
    D2 = display_input('D2', 'Non-linear dynamical complexity measure', 'D2', col1, 'number')
    PPE = display_input('PPE', 'Pitch period entropy', 'PPE', col2, 'number')

    parkinsons_diagnosis = ''
    if st.button("Predict Parkinsons"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person is likely to have Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person is unlikely to have Parkinson's disease"
        st.success(parkinsons_diagnosis)

elif selected == "Lung Cancer":
    st.title("Lung Cancer Prediction")
    st.markdown("<p style='color:#a9a9a9;'>Enter the following details to predict lung cancer:</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    GENDER = display_input('Gender (1=Male, 0=Female)', 'Gender of the person', 'GENDER', col1, 'number')
    AGE = display_input('Age', 'Age of the person', 'AGE', col2, 'number')
    SMOKING = display_input('Smoking (1=Yes, 0=No)', 'Does the person smoke?', 'SMOKING', col1, 'number')
    YELLOW_FINGERS = display_input('Yellow Fingers (1=Yes, 0=No)', 'Does the person have yellow fingers?', 'YELLOW_FINGERS', col2, 'number')
    ANXIETY = display_input('Anxiety (1=Yes, 0=No)', 'Does the person have anxiety?', 'ANXIETY', col1, 'number')
    PEER_PRESSURE = display_input('Peer Pressure (1=Yes, 0=No)', 'Is the person under peer pressure?', 'PEER_PRESSURE', col2, 'number')
    CHRONIC_DISEASE = display_input('Chronic Disease (1=Yes, 0=No)', 'Does the person have a chronic disease?', 'CHRONIC_DISEASE', col1, 'number')
    FATIGUE = display_input('Fatigue (1=Yes, 0=No)', 'Does the person experience fatigue?', 'FATIGUE', col2, 'number')
    ALLERGY = display_input('Allergy (1=Yes, 0=No)', 'Does the person have allergies?', 'ALLERGY', col1, 'number')
    WHEEZING = display_input('Wheezing (1=Yes, 0=No)', 'Does the person experience wheezing?', 'WHEEZING', col2, 'number')
    ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1=Yes, 0=No)', 'Does the person consume alcohol?', 'ALCOHOL_CONSUMING', col1, 'number')
    COUGHING = display_input('Coughing (1=Yes, 0=No)', 'Does the person experience coughing?', 'COUGHING', col2, 'number')
    SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1=Yes, 0=No)', 'Does the person experience shortness of breath?', 'SHORTNESS_OF_BREATH', col1, 'number')
    SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1=Yes, 0=No)', 'Does the person have difficulty swallowing?', 'SWALLOWING_DIFFICULTY', col2, 'number')
    CHEST_PAIN = display_input('Chest Pain (1=Yes, 0=No)', 'Does the person experience chest pain?', 'CHEST_PAIN', col1, 'number')

    lungs_diagnosis = ''
    if st.button("Predict Lung Cancer"):
        lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        lungs_diagnosis = "The person is likely to have lung cancer" if lungs_prediction[0] == 1 else "The person is unlikely to have lung cancer"
        st.success(lungs_diagnosis)

elif selected == "Hypo-Thyroid":
    st.title("Hypo-Thyroid Prediction")
    st.markdown("<p style='color:#a9a9a9;'>Enter the following details to predict hypo-thyroid disease:</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    age = display_input('Age', 'Age of the person', 'age', col1, 'number')
    sex = display_input('Sex (1=Male, 0=Female)', 'Sex of the person', 'sex', col2, 'number')
    on_thyroxine = display_input('On Thyroxine (1=Yes, 0=No)', 'Is the person on thyroxine?', 'on_thyroxine', col1, 'number')
    tsh = display_input('TSH Level', 'Thyroid Stimulating Hormone level', 'tsh', col2, 'number')
    t3_measured = display_input('T3 Measured (1=Yes, 0=No)', 'Was T3 level measured?', 't3_measured', col1, 'number')
    t3 = display_input('T3 Level', 'Triiodothyronine level', 't3', col2, 'number')
    tt4 = display_input('TT4 Level', 'Thyroxine level', 'tt4', col1, 'number')

    thyroid_diagnosis = ''
    if st.button("Predict Hypo-Thyroid"):
        thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        thyroid_diagnosis = "The person is likely to have Hypo-Thyroid disease" if thyroid_prediction[0] == 1 else "The person is unlikely to have Hypo-Thyroid disease"
        st.success(thyroid_diagnosis)