import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import normalize

def feature_normalize(df, cols):
    df_transformed = df.copy()
    df_transformed[cols] = normalize(X=df_transformed[cols], axis=1)

    return df_transformed


def categorical_converter(df, cols):
    df_transformed = df.copy()
    for i in cols:
        col_newname = i
        df_transformed[col_newname] = df_transformed[i].astype('category').values.codes

    return df_transformed


def standard_scaler(df: pd.DataFrame):
    """Scaling standard scaler transform."""
    index_cols = df.index
    scaler = preprocessing.StandardScaler()
    np_scaler = scaler.fit_transform(df)

    df_transformed = pd.DataFrame(
        np_scaler, index=index_cols, columns=df.columns
    )
    
    return scaler, df_transformed