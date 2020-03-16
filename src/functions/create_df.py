def create_df(df_sales, df_res, df_parcel):
    '''
    This function takes in the three dataset files from the King County assessor website, 
    merges them on the combination of the Major-Minor columns, and returns the merged
    dataframe.
    '''
    
    import pandas as pd
    
    ## Clean up df_sales
    # Create 'MajorMinor' and 'year' columns
    df_sales['year'] = pd.DatetimeIndex(df_sales['DocumentDate']).year
    df_sales['Major'] = df_sales['Major'].astype(str)
    df_sales['Minor'] = df_sales['Minor'].astype(str)
    df_sales['MajorMinor'] = df_sales['Major'] + '-' + df_sales['Minor']
    
    # filter for 2019 sales, sale price and property type
    df_sales_19 = df_sales[df_sales['year']==2019]
    df_sales_19 = df_sales_19[df_sales_19['PropertyType'] == 11]
    df_sales_19 = df_sales_19[df_sales_19['SalePrice'] > 50000]
    df_sales_19 = df_sales_19[df_sales_19['SalePrice'] < 10000000]
    
    
    ## Clean up df_res
    # Create'MajorMinor' columns
    df_res['Major'] = df_res['Major'].astype(str)
    df_res['Minor'] = df_res['Minor'].astype(str)
    df_res['MajorMinor'] = df_res['Major'] + '-' + df_res['Minor']

    # remove null addresses (needs to happen before zipcode cleanup)
    df_res = df_res.dropna(subset=['Address'])

    # filter for living square feet
    df_res = df_res[df_res['SqFtTotLiving'] < 8000]

    # clean up zip codes
    df_res['ZipCode'] = df_res['ZipCode'].str[:5]
    df_res.loc[10523, 'ZipCode'] = 98115
    df_res.loc[14903, 'ZipCode'] = 98115

    ## Clean up df_parcel
    # Create'MajorMinor' columns in df_parcel
    df_parcel['Major'] = df_parcel['Major'].astype(str)
    df_parcel['Minor'] = df_parcel['Minor'].astype(str)
    df_parcel['MajorMinor'] = df_parcel['Major'] + '-' + df_parcel['Minor']

    
    ## Merges
    # Merge Sales and Parcel 
    new_df = pd.merge(df_sales_19, df_parcel, how = 'left',on =['MajorMinor'])

    # Merge the merged DF with Res 
    final_df = pd.merge(new_df, df_res, how = 'left',on =['MajorMinor'])

#     # Cleaning ZipCode column so that all zip codes are formatted the same
#     final_df['ZipCode'] = final_df['ZipCode'].str.split('-').str[0],
#     final_df['ZipCode'] = final_df['ZipCode'].astype(float),
#     final_df['ZipCode'] = final_df['ZipCode'].astype(str),
#     final_df['ZipCode'] = final_df['ZipCode'].str.split('.').str[0]
    
    return final_df