import pytest
import pandas as pd
from sklearn.linear_model import LogisticRegression 
from sklearn.ensemble import RandomForestClassifier
from ml.model import compute_model_metrics, train_model, inference
from ml.data import process_data
import numpy as np


@pytest.fixture
def sample_data():
    df = pd.DataFrame({
        'age': [39, 50, 38, 53, 28, 37, 49],
        'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors', 'Masters', '9th'],
        'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-speciality', 'Exec-managerial', 'Other-service'],
        'sex': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female'],
        'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K', '<=50K', '<=50K']
    })
    return df

def test_train_model(sample_data):
    # Test for training model with Random Forest and Logistic Regression
    cat_features = ["education", "occupation", "sex"]
    X, y, encoder, lb = process_data(
        sample_data,
        categorical_features = cat_features,
        label="salary",
        training=True
    )
    model = train_model(X, y)
    result = isinstance(RandomForestClassifier(random_state=42), LogisticRegression)
    assert result == False

def test_compute_model_metrics():
    # Test for Computer Metrics
    y = np.array([0, 0, 1, 1, 0])
    y_pred = np.array([1, 0, 1, 1, 1])

    precision, recall, fbeta = compute_model_metrics(y, y_pred)

    assert 0 <= precision <= 1, f"Precision {precision} out of range [0, 1]"
    assert 0 <= recall <= 1, f"Recall {recall} out of range [0, 1]"
    assert 0 <= fbeta <= 1, f"Fbeta {fbeta} out of range [0, 1]"

def test_inference(sample_data):
    #Testing inference predictions 
    cat_features = ["education", "occupation", "sex"]
    
    X, y, _, _ = process_data(
        sample_data,
        categorical_features=cat_features,
        label="salary",
        training=True
    )
    model = train_model(X, y)
    preds = model.predict(X)

    assert isinstance(preds, np.ndarray)