from lib.globals import *  # this imports global INT_ FLOAT_ STRING_ replacement constants

# DAS Scripts vars for testing
Bid = 37.00
Ask = 37.10
StopPrice = 36.95  # Stop price


# INTEGER CONSTANTS: Use format INT_ or FLOAT_ or STRING_ and the Print util will convert to the value
INT_DOLLAR_RISK = 200
INT_DISPLAY_SHARE = 100
FLOAT_SLIPPAGE = 0.05
STRING_TIF = "DAY+"
STRING_HANDINST = "ANY"


def das_script():
    '''
    DAS Script methods
    Will ignore the following
      triple single quote comments and hash comments
      print statements
      global vars
      will remove double quotes and whitespace
    '''

    global StopPrice
    global Bid
    global Ask

    '''
    Buy Limit on the Bid with $200 risk and stop equal to the price field
    '''
    print("Bid=%.2f" % Bid)
    print("Ask=%.2f" % Ask)

    ROUTE = STRING_STOP
    SShare = INT_DISPLAY_SHARE
    TIF = STRING_TIF
    HANDINST = STRING_HANDINST

    # Get the risk in price
    StopType = STRING_TRAILING  # set to trailing temporarily to access the TrailPrice field
    TrailPrice = Ask + FLOAT_SLIPPAGE - StopPrice
    print("PriceRisk=%.2f" % TrailPrice)
    """ TrailPrice = STRING_ROUND2 """  # Here is a way to prevent python execution but include in DAS
    Price = TrailPrice  # need to use price field to access in next step

    # Number of shares
    Share = INT_DOLLAR_RISK / Price
    print("Share=%.2f" % Share)
    Share = STRING_ROUND

    # Set the price to the Mid
    Price = Ask + FLOAT_SLIPPAGE
    print("EntryPrice=%.2f" % Price)
    Price = STRING_ROUND2

    ROUTE = STRING_LIMIT
    """ BUY """

    # Here is the stop order
    ROUTE = STRING_STOP
    StopType = STRING_MARKET
    print("StopPrice=%s" % StopPrice)
    """ SELL """
