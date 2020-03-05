def create_df(df_sales, df_res, df_parcel):
    '''
    <function description>
    '''
    
    # Create 'MajorMinor' columns in df_sales
    df_sales['Major'] = df_sales['Major'].astype(str)
    df_sales['Minor'] = df_sales['Minor'].astype(str)
    df_sales['MajorMinor'] = df_sales['Major'] + '-' + df_sales['Minor']

    # Create'MajorMinor' columns in df_res

    df_res['Major'] = df_res['Major'].astype(str)
    df_res['Minor'] = df_res['Minor'].astype(str)
    df_res['MajorMinor'] = df_res['Major'] + '-' + df_res['Minor']

    # Create'MajorMinor' columns in df_parcel

    df_parcel['Major'] = df_parcel['Major'].astype(str)
    df_parcel['Minor'] = df_parcel['Minor'].astype(str)
    df_parcel['MajorMinor'] = df_parcel['Major'] + '-' + df_parcel['Minor']

    # filter for 2019 sales
    df_sales_19 = df_sales[df_sales['year']==2019]
    
    # Filter for PropertyType and SalePrice 
    q1 = ("""
            SELECT * FROM df_sales_19
            WHERE (PropertyType = 11 or PropertyType = 12 or PropertyType = 13 or PropertyType = 14) and SalePrice > 0
            """)
    df_sales_19 = ps.sqldf(q1)

    # Merge Sales and Parcel 
    new_df = pd.merge(df_sales_19, df_parcel, how = 'left',on =['MajorMinor'])

    # Merge the merged DF with Res 
    final_df = pd.merge(new_df, df_res, how = 'left',on =['MajorMinor'])

    return final_df