# EXPENSE TRACKER

## DESCRIPTION

Python command line project for getting and saving you expenses information.

## SETUP AND CONFIGURATION

To setup the command line project you have to add the alias of the python file 'expense-tracker.py' in your enviroment variables. Example: `alias expense-tracker="<file_path>"`

## USAGE

* `expense-tracker add --description <description> --amount <amount>` Create a new expense with the description and amount.
* `expense-tracker update --id <id> --description <description> --amount <amount>` Update an expense already created with the description or amount you provide, both description and amount are optional but you must provide one of them.
* `expense-tracker summary --month <int_month>` Summarize the expenses, if you provide the number of a month, the app will show the expenses of that month in the current year.
* `expense-tracker delete --id <id>` Delete the expense you want to delete based in the id you provide.