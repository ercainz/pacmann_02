import pandas as pd
import numpy as np

def read_data(PATH):
    '''
    Read data from dataset from path
   
    Parameters
    ----------
    PATH : str
        path source of training data, csv.
    
    Returns
    -------
    data : pd.DataFrame
        Data for modeling
    '''
    data = pd.read_csv(PATH, encoding='ISO-8859-1')
    
    return data

def rename_columns(df):
    cars_dict = {"dateCreated": "ad_created"
                ,"dateCrawled": "date_crawled"
                ,"fuelType": "fuel_type"
                ,"lastSeen": "last_seen"
                ,"monthOfRegistration": "registration_month"
                ,"notRepairedDamage": "unrepaired_damage"
                ,"nrOfPictures": "num_of_pictures"
                ,"offerType": "offer_type"
                ,"postalCode": "postal_code"
                ,"powerPS": "power_ps"
                ,"vehicleType": "vehicle_type"
                ,"yearOfRegistration": "registration_year"}

    df.rename(columns = cars_dict, inplace = True)

    return df


def read_and_check_data(path):
    """Read and checking data."""
    print("start import data")
    df = read_data(path)
    print("done import data")

    print("start rename columns")
    df = rename_columns(df)
    print("done rename columns")
    
    return df