# Function to filter a pandas dataframe by list, return a dataframe

def filter_by_list (list_in, df_to_filter, column_name):
    """
    Arguments: list, dataframe, column name:
        list_in: list of keywords for filtering
        df_to_filter: dataframe
        column_name: string (e.g., 'Column 1')
    Returns: Filtered dataframe
    """
    df_to_filter = df_to_filter[df_to_filter[column_name].isin(list_in)]
    return(df_to_filter)