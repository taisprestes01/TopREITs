import fundamentus as FundamentusAPI
import logging

def get_filtered_result(dy_min, dy_max, pvp_min, pvp_max, liquidity_min, price_min):
    """
    Filters data from Fundamentus based on the given criteria.

    Args:
        dy_min (float): Minimum Dividend Yield.
        dy_max (float): Maximum Dividend Yield.
        pvp_min (float): Minimum Price-to-Book ratio (PVP).
        pvp_max (float): Maximum Price-to-Book ratio (PVP).
        liquidity_min (float): Minimum liquidity over the past 2 months.
        price_min (float): Minimum stock price.

    Returns:
        pandas.DataFrame: A DataFrame containing stocks that meet the criteria.

    Raises:
        ValueError: If no stocks meet the criteria (resulting DataFrame is empty).
    
    Use example: get_filtered_result(0.05, 0.1, 0, 1, 1000000, 10)
    """
    df = FundamentusAPI.get_resultado()

    filtered_df = df[
        (df['dy'] >= dy_min) & (df['dy'] <= dy_max) &
        (df['pvp'] >= pvp_min) & (df['pvp'] <= pvp_max) &
        (df['liq2m'] >= liquidity_min) &
        (df['cotacao'] >= price_min)
    ]

    if filtered_df.empty:
        raise ValueError("No stocks match the given criteria.")

    return filtered_df

def get_papel(param):
    """
    Get detailed data from Fundamentus based on a given stock symbol or a list of symbols.

    URL:
        http://fundamentus.com.br/detalhes.php?papel=WEGE3

    Input:
        - param (str or list): The stock symbol as a string or a list of stock symbols.

    Returns:
        pandas.DataFrame: DataFrame containing detailed information about the specified stock(s).

    Raises:
        ValueError: If there is an issue with the input type or data retrieval.

    Use example: get_papel('WEGE3')
    """
    _type = str(type(param))
    logging.debug('[param] is of type [{}]'.format(_type))

    try:
        if _type == "<class 'list'>":
            logging.info('detalhes: call: get..._list()')
            return FundamentusAPI.get_detalhes_list(param)
        else:
            logging.info('detalhes: call: get..._papel()')
            return FundamentusAPI.get_detalhes_papel(param)

    except Exception as e:
        raise ValueError(f"Error fetching or processing the data for the given symbol(s): {str(e)}")
    

    

