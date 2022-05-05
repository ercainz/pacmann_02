import pickle
import pandas as pd

from helper.data_check_preparation import read_and_check_data
from helper.feature_engineering import feature_engineering
from helper.constant import TARGET, PATH
from helper.preprocessing import standard_scaler

from sklearn.model_selection import train_test_split


def train_model():
    # pembacaan dan pengecekan data
    df = read_and_check_data(PATH)
    
    # feature engineering
    df_transformed = feature_engineering(df)
    print("Start Saving Result Feature Engineering!")
    df_transformed.to_csv("artifacts/df_transformed.csv")
    
    # siapkan fitur data dan target data 
    X = df_transformed.drop([TARGET], axis =1)
    y = df_transformed[TARGET]

    # ????????? Terpaksa convert karena error saat melakukan standard_scaler
    X['date_crawled'] = pd.to_numeric(X['date_crawled'])
    X['ad_created'] = pd.to_numeric(X['ad_created'])
    X['last_seen'] = pd.to_numeric(X['last_seen'])
    
    # data splitting
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)
    
    # scaler
    train_scaler, X_train_scaled = standard_scaler(X_train)
    pickle.dump(train_scaler, open("artifacts/train_scaler.pkl", "wb"))
    X_test_scaled = train_scaler.transform(X_test)
    
    print("Start Saving Result Standard Scaler!")
    X_train_scaled.to_csv("artifacts/X_train_scaled.csv")


if __name__ == "__main__":
    print("START RUNNING PIPELINE!")
    train_model()
    print("FINISH RUNNING PIPELINE!")