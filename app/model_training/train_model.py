from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
from app.model_training.preprocess import load_and_preprocess

def train_and_save():
    # Load data
    X_train, X_test, y_train, y_test, scaler = load_and_preprocess()

    # Train model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    #Save model and scaler
    joblib.dump(model, "app/model/heart_model.pkl")
    joblib.dump(scaler, "app/model/scaler.pkl")
    print("Model and scaler saved successfully.")

if __name__ == "__main__":
    train_and_save()