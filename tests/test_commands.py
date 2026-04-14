
import unittest
from use_cases.commands import DataStore, AddCommand
from domain.entities import Item
from domain.interfaces import DataPersistencePort

class DummyPersistence(DataPersistencePort):
	def __init__(self):
		self.saved = []
		self.loaded = []
	def save(self, items):
		self.saved = list(items)
	def load(self):
		return list(self.loaded)

class TestDataStore(unittest.TestCase):
	def test_add_and_save(self):
		persistence = DummyPersistence()
		store = DataStore(persistence)
		cmd = AddCommand()
		cmd.execute(store, "test value")
		self.assertEqual(len(store._items), 1)
		self.assertEqual(store._items[0].val, "test value")
		store.save()
		self.assertEqual(len(persistence.saved), 1)

if __name__ == "__main__":
	unittest.main()
