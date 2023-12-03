# model_training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import mutual_info_classif

def train_models(df):
    # Load your dataset
    df = pd.read_csv('C:\\Users\\Personal\\Downloads\\TrainingTBdata.csv')

    # Preprocess the dataset by cleaning and coercing data types like date and objects
    df['TBRegisterNo.'] = df['TBRegisterNo.'].astype(str)

    # Drop some columns
    df = df.dropna(axis=1)

    # Identify object data types and encode them
    object_columns = df.iloc[:, 1:].select_dtypes(include=['object']).columns
    label_encoder = LabelEncoder()
    df[object_columns] = df[object_columns].apply(label_encoder.fit_transform)

    # Drop some columns
    df = df.drop(object_columns, axis=1)
    df = df.drop('TBRegisterNo.', axis=1)

    # Assuming X and y are your features and target variable
    X = df.drop('MDR-TBIncidence', axis=1)  # Replace 'target_column' with your actual target column
    y = df['MDR-TBIncidence']

    # Split into features and target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100, test_size=0.3)

    # Using p-values for feature selection
    f_p_values = chi2(X_train, y_train)
    p_values = pd.Series(f_p_values[1])
    p_values.index = X_train.columns
    p_values = p_values.sort_index(ascending=False)

    # Determine the mutual information
    mutual_info = mutual_info_classif(X_train, y_train)
    mutual_info = pd.Series(mutual_info)
    mutual_info.index = X_train.columns
    mutual_info.sort_values(ascending=False)

    # Now we will select the top 15 important features
    sel_five_cols = SelectKBest(mutual_info_classif, k=15)
    sel_five_cols.fit(X_train, y_train)
    selected_features = X_train.columns[sel_five_cols.get_support()]

    # Print selected features
    print("Selected Features:", selected_features)

    # Train Logistic Regression
    lr_model = LogisticRegression()
    lr_model.fit(X_train[selected_features], y_train)

    # Train Support Vector Machine (SVM)
    svm_model = SVC(probability=True)  # Set probability to True for soft voting
    svm_model.fit(X_train[selected_features], y_train)

    # Train Artificial Neural Network (ANN)
    ann_model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000)  # You can adjust the parameters
    ann_model.fit(X_train[selected_features], y_train)

    # Create an ensemble of models using VotingClassifier
    ensemble_model = VotingClassifier(
        estimators=[
            ('logistic_regression', lr_model),
            ('svm', svm_model),
            ('ann', ann_model)
        ],
        voting='soft'  # 'soft' for soft voting (probability-based), 'hard' for hard voting (majority-based)
    )

    # Fit the ensemble model on the training data
    ensemble_model.fit(X_train[selected_features], y_train)

    return lr_model, svm_model, ann_model, ensemble_model, selected_features
