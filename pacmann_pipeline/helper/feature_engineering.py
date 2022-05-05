
import pandas as pd
from helper.preprocessing import feature_normalize, categorical_converter

def feature_engineering(df):
    df_transformed = df.copy()

    # transform into datetime
    df_transformed['ad_created'] = pd.to_datetime(df_transformed['ad_created'])
    df_transformed['date_crawled'] = pd.to_datetime(df_transformed['date_crawled'])
    df_transformed['last_seen'] = pd.to_datetime(df_transformed['last_seen'])

    # transform into int
    df_transformed['price'] = df_transformed['price'].str.replace(',|\$','',regex=True)
    df_transformed['odometer'] = df_transformed['odometer'].str.replace(',|km','',regex=True)
    df_transformed['price'] = pd.to_numeric(df_transformed['price'])
    df_transformed['odometer'] = pd.to_numeric(df_transformed['odometer'])

    # drop unecesssary columns
    drop_cols = ['seller','offer_type','num_of_pictures','name','postal_code']
    df_transformed.drop(columns=drop_cols, axis=1, inplace=True)

    # handling outliers
    df_transformed = df_transformed[(df_transformed['price'] <= 40000) & (df_transformed['price'] >= 500)].copy()

    # handling NaN value
    type_object_with_nan = ['vehicle_type','gearbox','model','fuel_type','unrepaired_damage']
    for i_type_object in (type_object_with_nan):
        mode = df_transformed[i_type_object].mode().values[0]
        df_transformed[i_type_object] = df_transformed[i_type_object].fillna(mode)

    # normalization
    normalize_cols = ['registration_year','power_ps','odometer','registration_month']
    df_transformed = feature_normalize(df_transformed, cols=normalize_cols)

    # categorizing
    cat_cols = ['abtest','vehicle_type','gearbox','model','fuel_type','brand','unrepaired_damage']
    df_transformed = categorical_converter(df_transformed, cols=cat_cols)

    return df_transformed