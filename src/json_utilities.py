import json
import pwd
import os
from datetime import datetime

class JsonUtilities():
    data:dict = {}
    next_id = 1

    def _get_str_month(self, month) -> str:
        match(month):
            case 1:
                return 'January'
            case 2:
                return 'February'
            case 3:
                return 'March'
            case 4:
                return 'April'
            case 5:
                return 'May'
            case 6:
                return 'June'
            case 7:
                return 'July'
            case 8:
                return 'August'
            case 9:
                return 'September'
            case 10:
                return 'October'
            case 11:
                return 'November'
            case 12:
                return 'December'

    def _read_file(self):
        with open(self.file_path, 'r') as f:
            read = f.read()
            if read:
                self.data = json.loads(read)
            f.close()
    
    def _get_next_id(self):
        list_items = list(self.data.keys())
        if len(list_items) == 0:
            self.next_id = 1
        else:
            self.next_id = int(list_items[-1]) + 1

    def save(self):
        with open(self.file_path, 'w') as f:
            f.write(json.dumps(self.data))
            f.close()

    def add_expense(self, description, amount):
        if description and amount:
            date = datetime.now()
            d = {
                'id': self.next_id,
                'description': description,
                'amount': amount,
                'date': f'{date.year}-{date.month}-{date.day}',
            }
            try:
                self.data[self.next_id] = d
                self.save()
                print(f'Expense added successfully (ID: {self.next_id})')
            except Exception as e:
                print(f'Error {e}')
        else:
            raise Exception('You have to introduce the description and the amount of the expense.')

    def list_expenses(self) -> None:
        print('ID  Date       Description  Amount')
        for v in self.data.values():
            print(f'{v['id']}   {v['date']}  {v['description']}  {v['amount']}')

    def update_expense(self, id, amount:int = None, description:str = None):
        expense = self.data.get(str(id), None)
        print(expense)
        if expense:
            if amount:
                expense['amount'] = amount
            if description:
                expense['description'] = description
            self.data[str(id)] = expense
            self.save()
            print(f'Expense updated successfully (ID: {id})')
        else:
            raise Exception(f'There is not expense with the id {id}')

    def delete_expense(self, id):
        try:
            del self.data[str(id)]
            self.save()
            print('Expense deleted successfully')
        except Exception as e:
            print(e)
    
    def show_summary(self, month):
        if month:
            # ! Get two digits number
            m = str(month) 
            # ? Convert the month to a legitimate two digits month
            # ! Get the current year
            current = datetime.now().year
            list_values = list(self.data.values())
            total = 0
            for v in list_values:
                if f'{current}-{m}' in v['date']:
                    total = total + v['amount']
            print(f'Total expenses for {self._get_str_month(month)}: ${total}')
        else:
            total = 0
            list_values = list(self.data.values())
            for v in list_values:
                total = total + v['amount']
            print(f'Total expenses: ${total}')

    def __init__(self, test=False) -> None:
        if test:
            self.file_path = '/Users/kael/Documents/Harry/Projects/Python/ExpenseTracker/src/testjson.json'
        else:
            self.file_path = '/Users/kael/Documents/Harry/Projects/Python/ExpenseTracker/data.json'
        self._read_file()
        self._get_next_id()
