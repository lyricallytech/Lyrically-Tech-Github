# HOW TO: Achieve both 6 and 7 figures through sales formulas


# NOTES: Tabulate module installed and used to create charts  
from tabulate import tabulate
from multiprocessing.sharedctypes import Value

# NOTES: Class creation to contain both 6-figure and 7-figure strategies
class Range:
    def __init__(self):
        pass

    def Six_Figure_Formulas(self):
        print("\n")
        print("$100K in One-Time Sales: ")
        main_table = [["Method #1: ", "Sell a $100 product to 1,000 customers"], ["Method #2: ", "Sell a $250 product to 400 customers"], ["Method #3: ", "Sell a $500 product to 200 customers"], ["Method #4: ", "Sell a $750 product to 135 customers"]]
        main_headers = ["List", "Formula"]
        print("\n",tabulate(main_table, main_headers, tablefmt="simple"))
        print("\n")

        print("$100K in Subscription Sales: ")
        main_table = [["Method #1: ", "Sell a $50 monthly subscription to 167 customers for a full year"], ["Method #2: ", "Sell a $100 monthly subscription to 83 customers for a full year"], ["Method #3: ", "Sell a $200 monthly subscription to 42 customers for a full year"], ["Method #4: ", "Sell a $300 monthly subscription to 28 customers for a full year"]]
        main_headers = ["List", "Formula"]
        print("\n",tabulate(main_table, main_headers, tablefmt="simple"))
        print("\n")

    def Seven_Figure_Formulas(self):
        print("$1M in One-Time Sales: ")
        main_table = [["Method #1: ", "Sell a $200 product to 5,000 customers"], ["Method #2: ", "Sell a $500 product to 2,000 customers"], ["Method #3: ", "Sell a $1,000 product to 1,000 customers"], ["Method #4: ", "Sell a $2,000 product to 500 customers"]]
        main_headers = ["List", "Formula"]
        print("\n",tabulate(main_table, main_headers, tablefmt="simple"))
        print("\n")


# NOTES: Here is my Class and Object declaration    
Range = Range()

# NOTES: Here is my Method declaration 
Range.Six_Figure_Formulas()
Range.Seven_Figure_Formulas()

