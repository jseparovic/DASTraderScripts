from lib.globals import *  # this imports global INT_ FLOAT_ STRING_ replacement constants

# INTEGER CONSTANTS: Use format INT_ or FLOAT_ or STRING_ and the Print util will convert to the value
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
    Close Full long at Bid
    '''

    """ CXL ALLSYMB """
    ROUTE = STRING_LIMIT
    SShare = INT_DISPLAY_SHARE
    Share = STRING_POS
    Price = Bid
    TIF = STRING_TIF
    HANDINST = STRING_HANDINST
    """ BUY """
