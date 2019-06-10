from models.store import StoreModel
from tests.unit.unit_base_test import UnitBaseTest


class TestStore(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('Test_store')

        self.assertEqual(store.name, 'Test_store')
