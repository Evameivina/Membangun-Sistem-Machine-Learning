import requests

url = "http://127.0.0.1:5000/predict"

payload = {
    "gender": "female",
    "ethnicity": "group B",
    "lunch": "standard",
    "test_prep": "none",
    "parental_education": "bachelor's degree",
    "math_score": 70,
    "reading_score": 72,
    "writing_score": 74
}

response = requests.post(url, json=payload)
print(response.json())
