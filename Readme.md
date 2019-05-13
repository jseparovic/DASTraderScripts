# DASTraderScripts
Python approach to implementing DAS Trader scripts.
This tool allows the user to create a DAS script (in a line by line format within a python method) and then provides Test and Print utilities for development and debugging prior to testing it in DAS Trader Pro.

#### Layout
```
/lib - common utils
/scripts - das python style scripts
dasscript.py - main entry point
```


### Guide
1) Create a new script file in `scripts` directory
2) Declare any global variables to be used in the script like `Bid`, `Ask`, etc
3) Add a method definition for the script called `das_script`
4) Declare the global variables within the das_script method
5) Add any print statements that make sense for debugging the test output
6) Add comments. Either `'''comment'''` or `#comment`
7) To prevent python executing code that you want to run in DAS, use triple quote comments `""" Price = STRING_ROUND2 """`

Example:
```
Bid = 10.00
Ask = 10.10

def das_script():
    """
    This script sets the Price field to the current Bid
    """
    global Bid
    global Ask
    print("Test DAS Script")
    Price = Bid
```

For a full example check out `buy_mid_with_risk_on_stop.py` in the scripts directory. 

Checkout the DAS Hotkey Command List pdf for info on the variables you can use in your script. It takes a some trial an error as not all the variables can be accessed all the time. 
Also some variables won't accept some operations

http://dastrader.com/documents/HotkeyCommandList.pdf

To do complex math may need to break it down into simpler instructions. DAS only allows +-*/ and processed operations from left to right regardless of operation type.

Eg: 1 + 1 / 2 = 1 (not 1.5 as you might expect)

Check the scripts dir for working examples

For more detail on the way variables work in DAS check out this post:

https://forums.bearbulltraders.com/topic/716-das-dynamically-calculate-shares-on-risk-or-risk-hot-key-configuration-updated-1213-v146/



#### User defined constants
Within a script you can define constants that will be replaced in the DAS Script Print utility.
They need to be in the format:
- INT_
- FLOAT_
- STRING_

Checkout the examples in the scripts directory for more details


#### Globally defined constants
There is also support for Globally defined constants and must be placed in `lib/globals.py`
These will also be replaced by the print utility

Just note that the replacement method does not replace recursively so constants can only be defined at one level. Assigning a constant to another constant is not supported and won't be replaced by the Print utility


#### Prevent python execution
You can use triple quote comments in the python script to prevent execution in the python test. These lines will however be run in the DAS script.
Again, check the examples
Hash and Triple single quote comments will not be executed in DAS


#### Usage
```
usage: dasscript.py [-h] -s SCRIPT [-p] [-t]

DAS Scripts

optional arguments:
  -h, --help            show this help message and exit
  -s SCRIPT, --script SCRIPT
                        Python DAS Script name without py extension
  -p, --print           Print DAS Format
  -t, --test            Print DAS Format

```

#### Examples
Test your script
```
# python dasscript.py -s sell_mid_with_risk_on_stop -t

Bid=37.00
Ask=37.10
PriceRisk=55.60
Share=-10.84
EntryPrice=55.60
StopPrice=37.15

```

Example: Print the DAS format
```
# venv/Scripts/python dasscript.py -s sell_mid_with_risk_on_stop -p

ROUTE = STOP; SShare = 100; StopType = Trailing; TrailPrice = Ask + Bid / 2; Price = StopPrice - TrailPrice; Share = 200 / Price; Share = ROUND; Price = Ask + Bid / 2; Price = ROUND2; ROUTE = Limit; SELL = Send; ROUTE = STOP; StopType = Market; TIF = DAY+; HANDINST = ANY; BUY = Send; ROUTE = Market;
```


Big Thanks to KyleK29 from forums.bearbulltraders.com for the inspiration behind this tool:

https://forums.bearbulltraders.com/topic/716-das-dynamically-calculate-shares-on-risk-or-risk-hot-key-configuration-updated-1213-v146/


#### TODOs:
Implement a way to reuse a block of code within a script

