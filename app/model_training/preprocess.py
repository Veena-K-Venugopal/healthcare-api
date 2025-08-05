import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess(path="app/model_training/heart_disease_uci.csv"):
    # Load the dataset
    df = pd.read_csv(path)
    
    # 1. Drop unnecessary columns
    df.drop(['id', 'dataset'], axis=1, inplace=True)

    # 2. Handle missing values 
    df.fillna(df.median(numeric_only=True), inplace=True)

    # 3. Convert target to binary
    df['num'] = (df['num'] > 0).astype(int)

    # 4. Encode categorical columns
    df['sex'] = df['sex'].map({'Male': 1, 'Female': 0})
    df['fbs'] = df['fbs'].map({'True': 1, 'False': 0})
    df['exang'] = df['exang'].map({'True': 1, 'False':0})

    df = pd.get_dummies(df, columns=['cp', 'restecg', 'slope', 'thal'])

    # 5. Split features and target
    X = df.drop('num', axis=1)
    y = df['num']

    # 6. Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 7. Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, scaler