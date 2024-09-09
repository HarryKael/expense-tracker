#! /usr/local/bin/python3

import argparse
import sys
from src.json_utilities import JsonUtilities

def main():
    print('Expense Tracker')
    # ! Get the arguments
    parser = argparse.ArgumentParser('expense-tracker')
    arguments = sys.argv
    # ? Know if the arguments has enough length
    if len(arguments) > 1:
        method = arguments[1]
        json_utilities = JsonUtilities()
        match(method):
            case 'add':
                # ! Getting the arguments
                parser.add_argument('add')
                parser.add_argument('--description', type=str, metavar='str', required=True)
                parser.add_argument('--amount', type=int, metavar='int', required=True)
                # ! Parse arguments
                args = parser.parse_args()
                # Add
                json_utilities.add_expense(args.description, args.amount)
            case 'update':
                # ! Getting the arguments
                parser.add_argument('update')
                parser.add_argument('--id', type=str, metavar='str', required=True)
                parser.add_argument('--description', type=str, metavar='str', required=False)
                parser.add_argument('--amount', type=int, metavar='int', required=False)
                # ! Parse arguments
                args = parser.parse_args()
                # Update
                json_utilities.update_expense(args.id, args.amount, args.description)
            case 'list':
                # ! Getting the arguments
                parser.add_argument('list')
                # List
                json_utilities.list_expenses()
            case 'summary':
                # ! Getting the arguments
                parser.add_argument('summary')
                parser.add_argument('--month', type=int, metavar='int', required=False)
                # ! Parse arguments
                args = parser.parse_args()
                # Summary
                json_utilities.show_summary(args.month)
            case 'delete':
                # ! Getting the arguments
                parser.add_argument('delete')
                parser.add_argument('--id', type=int, metavar='int', required=True)
                # ! Parse arguments
                args = parser.parse_args()
                # Delete
                json_utilities.delete_expense(args.id)

if __name__ == '__main__':
    main()