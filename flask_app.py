# flask_app.py

from flask import Flask, render_template, request
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from model_training import train_models
import plotly.express as px
import pandas as pd
from plotly.offline import plot

app = Flask(__name__)

# Load models and selected features
lr_model, svm_model, ann_model, ensemble_model, selected_features = train_models('C:\\Users\\Personal\\Downloads\\TrainingTBdata.csv')

# Assuming X and y are your features and target variable
df = pd.read_csv('C:\\Users\\Personal\\Downloads\\TrainingTBdata.csv')
X = df.drop('MDR-TBIncidence', axis=1)
y = df['MDR-TBIncidence']

# Split into features and target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100, test_size=0.3)

@app.route('/')
def home():
    return render_template('index.html', selected_features=selected_features)

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    user_input = {}
    for feature in selected_features:
        value = float(request.form[feature])
        user_input[feature] = [value]

    # Create a DataFrame from user input
    user_input_df = pd.DataFrame(user_input)

    # Make predictions using the ensemble model
    user_input_selected = user_input_df[selected_features]
    ensemble_predictions = ensemble_model.predict(user_input_selected)

    # Map predicted class to a string
    class_mapping = {0: "not likely to develop MDR_TB", 1: "likely to develop MDR_TB"}
    ensemble_predicted_class = class_mapping.get(ensemble_predictions[0], "Unknown")

    # Get probabilities from the ensemble model for each class
    ensemble_probs = ensemble_model.predict_proba(user_input_selected)[0]

    # Plot performance charts
    plot_accuracy_chart()
    plot_probabilities_chart(ensemble_probs)

    return render_template('result.html', predicted_class=ensemble_predicted_class)

def plot_accuracy_chart():
    # Create an accuracy chart
    models = ['Logistic Regression', 'SVM', 'ANN', 'Ensemble']
    accuracies = [accuracy_score(y_test, lr_model.predict(X_test[selected_features])),
                  accuracy_score(y_test, svm_model.predict(X_test[selected_features])),
                  accuracy_score(y_test, ann_model.predict(X_test[selected_features])),
                  accuracy_score(y_test, ensemble_model.predict(X_test[selected_features]))]

    fig = px.bar(x=models, y=accuracies, labels={'y': 'Accuracy', 'x': 'Model'}, title='Model Accuracy Comparison')
    plot(fig, filename='templates/accuracy_chart.html', auto_open=False)

def plot_probabilities_chart(ensemble_probs):
    # Create a bar chart for class probabilities
    classes = ['Not likely', 'Likely']
    fig = px.bar(x=classes, y=ensemble_probs, labels={'y': 'Probability', 'x': 'Class'}, title='Class Probabilities')
    plot(fig, filename='templates/probabilities_chart.html', auto_open=False)


def plot_confusion_matrices():
    # Create confusion matrices for each model
    models = ['Logistic Regression', 'SVM', 'ANN', 'Ensemble']
    matrices = []

    for model, name in zip([lr_model, svm_model, ann_model, ensemble_model], models):
        predictions = model.predict(X_test[selected_features])
        matrix = confusion_matrix(y_test, predictions)
        matrices.append({'model': name, 'matrix': matrix})

        # Plot confusion matrices using Seaborn
    for model_info in matrices:
        plt.figure(figsize=(6, 4))
        sns.heatmap(model_info['matrix'], annot=True, fmt='d', cmap='Blues', xticklabels=['Not likely', 'Likely'],
                    yticklabels=['Not likely', 'Likely'])
        plt.title(f"Confusion Matrix - {model_info['model']}")
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.savefig(f'templates/confusion_matrix_{model_info["model"]}.png')
        plt.close()
@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = app.root_path
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(debug=True)
