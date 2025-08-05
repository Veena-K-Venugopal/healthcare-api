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

    # 3. Fill categorical NaNs with 'Unknown'
    categorical_cols = ['cp', 'restecg', 'slope', 'thal']
    for col in categorical_cols:
        if col in df.columns:
            df.loc[:, col] = df[col].fillna('Unknown')

    # 4. Convert target to binary
    df['num'] = (df['num'] > 0).astype(int)

    # 5. Encode binary categorical columns
    df['sex'] = df['sex'].map({'Male': 1, 'Female': 0})
    df['fbs'] = df['fbs'].map({'True': 1, 'False': 0})
    df['exang'] = df['exang'].map({'True': 1, 'False':0})

    # 6. One-hot encode for multi-class categories
    df = pd.get_dummies(df, columns=['cp', 'restecg', 'slope', 'thal'])

    # Final safeguard: replace any remaining NaNs with the 0
    df.fillna(0, inplace=True)

    # 7. Split features and target
    X = df.drop('num', axis=1)
    y = df['num']

    print("Any NaNs left before scaling? ", df.isnull().any().any())

    # 8. Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 9. Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, scaler