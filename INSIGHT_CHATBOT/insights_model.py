import pandas as pd

def load_data():
    return pd.read_csv('sales_and_customer_insights 1(in).csv')

# All insight functions that can be taken from the dataset.

def get_total_sales():
    df = load_data()
    return round(df["Average_Order_Value"].sum(), 2)

def get_top_category():
    df =load_data()
    return df['Most_Frequent_Category'].value_counts().idxmax()

def get_top_region():
    df = load_data()
    return df.groupby('Region')['Average_Order_Value'].sum().idxmax()

def get_average_resolution_time():
    df = load_data()
    if "resolution_time" in df.columns:
        return round(df["resolution_time"].mean(), 2)
    else:
        return "Column 'resolution_time' not found"

def get_summary_insights():
    return {
        "total_sales": get_total_sales(),
        "top_category": get_top_category(),
        "top_region_by_sales": get_top_region()
    }

if __name__ == "__main__":
    print("Sample Insights: ")
    print(get_summary_insights())