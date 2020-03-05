def update_columns(final_df):
    '''
    <function description>
    '''
    
    # Create 'Year' column
    final_df['year'] = pd.DatetimeIndex(final_df['DocumentDate']).year

    # Create a lot proportion column
    final_df['SqFtProp'] = final_df['SqFtTotLiving']/final_df['SqFtLot']

    # Create a cost per square foot column
    final_df['CostSqFt'] = final_df['SalePrice']/final_df['SqFtTotLiving']

    # create a boolean waterfront location column
    qwater = ("""
                SELECT SalePrice,
                CASE
                    WHEN WfntLocation > 0 THEN 1
                    ELSE 0
                END as has_waterfront
                FROM final_df
                """)
    final_df['has_waterfront'] = ps.sqldf(qwater)

    # create a boolean porch column
    qporch = ("""
                SELECT SalePrice,
                CASE
                    WHEN SqFtOpenPorch > 0 OR SqFtEnclosedPorch > 0 OR SqFtDeck > 0 THEN 1
                    ELSE 0
                END AS has_porch
                FROM final_df
                """)
    final_df['has_porch'] = ps.sqldf(qporch)

    # create a boolean nuisance column
    qn = ("""
                SELECT SalePrice,
                CASE
                    WHEN Other_Nuisance > 0 OR PowerLines > 0 OR Traffic > 0 THEN 1
                    ELSE 0
                END AS has_nuisance
                FROM final_df
                """)
    final_df['has_nuisance'] = ps.sqldf(qn)

    # drop unnecessary columns?
    #########################
    
    return analysis_df