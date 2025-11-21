import mlflow
import mlflow.pyfunc
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import uvicorn

MODEL_PATH = r"C:\Windows\system32\StudentsPerformance_RF\mlruns\783668357793525180\06c224ac8ae64fce93ec56ed4722c053\artifacts\best_model"

print("Loading MLflow model...")
model = mlflow.pyfunc.load_model(MODEL_PATH)

COLUMNS_ORDER = [
    "math score","reading score","writing score","average_score","gender_male",
    "race/ethnicity_group B","race/ethnicity_group C","race/ethnicity_group D","race/ethnicity_group E",
    "parental level of education_bachelor's degree","parental level of education_high school","parental level of education_master's degree",
    "parental level of education_some college","parental level of education_some high school",
    "lunch_standard","test preparation course_none"
]

app = FastAPI(title="Students Performance Model API")

@app.get("/")
def root():
    return {"message": "API is running"}

class InputData(BaseModel):
    gender: str
    ethnicity: str
    lunch: str
    test_prep: str
    parental_education: str
    math_score: int
    reading_score: int
    writing_score: int

def preprocess_input(data: InputData):
    avg = (data.math_score + data.reading_score + data.writing_score) / 3

    input_dict = {
        "math score": data.math_score,
        "reading score": data.reading_score,
        "writing score": data.writing_score,
        "average_score": avg,
        "gender_male": 1 if data.gender.lower() == "male" else 0,
        "race/ethnicity_group B": 1 if data.ethnicity == "group B" else 0,
        "race/ethnicity_group C": 1 if data.ethnicity == "group C" else 0,
        "race/ethnicity_group D": 1 if data.ethnicity == "group D" else 0,
        "race/ethnicity_group E": 1 if data.ethnicity == "group E" else 0,
        "parental level of education_bachelor's degree": 1 if data.parental_education == "bachelor's degree" else 0,
        "parental level of education_high school": 1 if data.parental_education == "high school" else 0,
        "parental level of education_master's degree": 1 if data.parental_education == "master's degree" else 0,
        "parental level of education_some college": 1 if data.parental_education == "some college" else 0,
        "parental level of education_some high school": 1 if data.parental_education == "some high school" else 0,
        "lunch_standard": 1 if data.lunch == "standard" else 0,
        "test preparation course_none": 1 if data.test_prep == "none" else 0
    }

    df = pd.DataFrame([input_dict])

    df = df[COLUMNS_ORDER]

    return df

@app.post("/predict")
def predict(data: InputData):
    try:
        input_df = preprocess_input(data)

        prediction = model.predict(input_df)
        return {"prediction": str(prediction[0])}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("serve_model:app", host="127.0.0.1", port=5000, reload=True)

