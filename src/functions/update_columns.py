def update_columns(final_df):
    '''
    This function takes in the merged dataframe of the King Country datasets, adds
    some additional analytical columns, drops all unnecessary columns and returns 
    the updated dataframe for analysis purposes.
    '''
    
    import pandas as pd
    import pandasql as ps
    pd.set_option('max_colwidth', 80)

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
    final_df['has_waterfront'] = ps.sqldf(qwater)['has_waterfront']

    # create a boolean porch column
    qporch = ("""
                SELECT SalePrice,
                CASE
                    WHEN SqFtOpenPorch > 0 OR SqFtEnclosedPorch > 0 OR SqFtDeck > 0 THEN 1
                    ELSE 0
                END AS has_porch
                FROM final_df
                """)
    final_df['has_porch'] = ps.sqldf(qporch)['has_porch']

    # create a boolean nuisance column
    qn = ("""
                SELECT SalePrice,
                CASE
                    WHEN OtherNuisances > 0 OR PowerLines > 0 OR TrafficNoise > 0 THEN 1
                    ELSE 0
                END AS has_nuisance
                FROM final_df
                """)
    final_df['has_nuisance'] = ps.sqldf(qn)['has_nuisance']

    # drop unnecessary columns
    analysis_df = final_df[['SalePrice', 'MajorMinor', 'SqFtProp', 'CostSqFt', 'has_waterfront', \
                            'has_porch', 'has_nuisance', 'ZipCode', 'year', 'BldgGrade', \
                            'Condition', 'PropertyType']]
    
    return analysis_df