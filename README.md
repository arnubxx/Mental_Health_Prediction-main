
# 🧠 Mental Health Prediction

A machine learning-based Python project that predicts mental health status based on survey data. The project includes data preprocessing, model training, model serialization, and local deployment using Python scripts.

## 📂 Project Structure

```

Mental\_Health\_Prediction/
├── app.py                      # Main script for running predictions
├── mental\_health.py            # Data preprocessing and model training
├── project.ipynb               # Jupyter notebook for exploration and development
├── survey.csv                  # Dataset containing mental health survey responses
├── KNN.sav                     # Serialized K-Nearest Neighbors model
├── Randomf.sav                 # Serialized Random Forest model
├── logisticRegression.sav      # Serialized Logistic Regression model
├── Staking.sav                 # Serialized Stacking ensemble model
├── mental\_health\_model.sav     # Final trained model used in predictions

````

## 📦 Requirements

Install required Python packages using:

```bash
pip install -r requirements.txt
````

Typical dependencies include:

* `pandas`
* `numpy`
* `scikit-learn`
* `joblib`
* `psutil`
* `matplotlib` (if plotting is used)
* `seaborn` (optional for visualization)

> Create a `requirements.txt` with:
> `pip freeze > requirements.txt`

## 📊 Dataset

* **Source**: The `survey.csv` file contains survey responses about mental health in the workplace.
* **Attributes** include: Age, Gender, Work Environment, Mental Health History, Family Background, etc.

## 🧠 Machine Learning Models

Trained and evaluated several ML algorithms:

* Logistic Regression
* K-Nearest Neighbors
* Random Forest
* Stacking Classifier

Models are saved (`.sav` format) using `joblib` for efficient reuse.

## 🚀 How to Run

To make a prediction:

```bash
python app.py
```

The script will:

1. Load the trained model.
2. Use `psutil` to optionally monitor system resources.
3. Predict outcomes based on sample or user-provided input.

## ⚙️ psutil Usage

The project uses `psutil` to monitor system performance (CPU/memory usage) during model loading or prediction, useful for profiling or system-aware deployment.

## 📈 Model Performance

Include metrics (manually or in your notebook) like:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

## 🧪 Notebook

You can explore and modify the model pipeline using:

```bash
project.ipynb
```

It includes EDA, preprocessing steps, training procedures, and model evaluation.

## 🤝 Contributions

Suggestions, bug reports, or improvements are welcome! Feel free to fork this repository and submit a pull request.

## 📄 License

Licensed under the [MIT License](LICENSE).

```

---

Would you like me to generate the `requirements.txt` for you based on your code files?
```
