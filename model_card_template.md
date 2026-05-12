# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
    This model uses RandomClassifier to develop a Machine Learning algorithm that predicts whether an individual's income exceeds $50,000 per year. The US Census Data was used to perform and develop this project. 

## Intended Use
    This Project is intended for educational purposes on how to develop machine learning practices using APIs, GitHub Actions, and pipelines. In addition, this project predicts if a person within the US Census Data earns more than $50,000 yearly, and showcases data in relation to it. It is not intended for operational use.  

## Training Data
    Training Data was provided by the US Census Bureau based on the annual income. The ratio used to perform training was 80/20, by splitting the dataset into a smaller sample for testing and evaluation. The categorical features were transformed with OneHotEncoding using the value Income as a target (<=$50,000). Some of the dataset values used for training are : age, education, ocupation, race, sex, among other attributes.

## Evaluation Data
    The evaluation dataset represents the 20% of the complete dataset that was excluded from the training phase. Before evaluation, these samples were transformed using the same fitted encoder and label binarizer applied to the training data. Using this method helps avoid data leakage and ensures that model testing closely resembles real-world prediction scenarios.

## Metrics
    Metrics used to evaluate the model:

    Precision: 0.7419
    Recall: 0.6384
    F1 Score: 0.6863

     A precision of 0.74 means that the model predicts that a person earns more than $50,000, being right 74% of the time. Recall data shows that the model actually find at least 64% of the time the correct amount of people who make more than $50,000 yearly. Lastly, F1 Score is the balanced between the two previous data, measuring its harmonic mean, presenting a 68% accuracy.
    
## Ethical Considerations
    This dataset contains demographic data not intended to be shared or misused. It is only for educational purposes regarding machine learning and data testing. Please do not apply or use any information found in this Project in real-world scenarios. Sensitive data was used, such as age, occupation, race, sex, education, country of origin, and others. I encourage respecting the privacy and sensitivity of data. 

## Caveats and Recommendations
    The data collected by the US Census Bureau in 1994 is not up to date, which is a major caveat. Since the data is from at least 3 decades ago, it might not be the most accurate to reflect the current demographic, economic conditions, or simply occupation trends. In addition, education has certainly changed over time, which might reduce the model's relevance. Among the recommendations, I would expand the dataset to take additional features such as fairness, bias detection, and regular updates to maintain data relevance.