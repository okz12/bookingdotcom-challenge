from zipfile import ZipFile
import pandas as pd
import great_expectations as ge

def load():
    filename = "Data/raw.zip"

    with ZipFile(filename, 'r') as zp:
        zp.extract('booking_train_set.csv', 'Data/')

    df = ge.read_csv("data/booking_train_set.csv", index_col=0)

    cats = ['user_id',
            'city_id',
            'device_class',
            'affiliate_id',
            'booker_country',
            'hotel_country',
            'utrip_id']
    dates = ['checkin', 'checkout']
    for c in cats:
        df[c] = df[c].astype('category')

    for d in dates:
        df[d] = pd.to_datetime(df[d])
    return df