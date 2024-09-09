import unittest
from src.json_utilities import JsonUtilities

class TestJsonUtitilies(unittest.TestCase):
    def setUp(self) -> None:
        self.json_utitilities = JsonUtilities(test=True)
        return super().setUp()

    def test_add_expense(self):
        description = 'Hola'
        amount = 10
        self.json_utitilities.add_expense(description, amount)
        self.json_utitilities.__init__(True)
        self.assertEqual(self.json_utitilities.next_id, 2)
        self.assertEqual(description, self.json_utitilities.data['1']['description'])
    
    def test_update_and_delete_expense(self):
        description = 'Klk'
        self.json_utitilities.update_expense(1, None, description)
        self.json_utitilities.__init__(True)
        self.assertEqual(self.json_utitilities.next_id, 2)
        self.assertEqual(description, self.json_utitilities.data['1']['description'])
        # Delete
        self.json_utitilities.delete_expense(1)
        self.json_utitilities.__init__(True)
        self.assertEqual(self.json_utitilities.next_id, 1)
        self.assertEqual(0, len(self.json_utitilities.data.values()))

if __name__ == '__main__':
    unittest.main()