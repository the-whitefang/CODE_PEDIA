import pandas as pd

def load_data():
    return pd.read_csv('sales_and_customer_insights 1(in).csv')

def get_seasonal_trends():
    df = load_data()
    df = df.dropna(subset=['Season', 'Average_Order_Value'])
    seasonal = df.groupby('Season')['Average_Order_Value'].agg(['sum', 'mean', 'count']).reset_index()
    return seasonal.to_dict(orient='records')

def get_regional_trends():
    df =load_data()
    df = df.dropna(subset=['Region', 'Average_Order_Value'])
    regional = df.groupby("Region")["Average_Order_Value"].agg(['sum', 'mean', 'count']).reset_index()
    return regional.to_dict(orient="records")

def get_churn_percentage():
    df = load_data()
    df["churn"] = df["Churn_Probability"].apply(lambda x: 1 if x >= 0.5 else 0)
    churn_rate = (df["churn"].sum() / len(df)) * 100
    return round(churn_rate, 2)
