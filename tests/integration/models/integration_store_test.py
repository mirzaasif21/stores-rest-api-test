from models.store import StoreModel
from tests.base_test import BaseTest
from models.item import ItemModel


class IntegrationTestStore(BaseTest):
    def test_ceate_store_items_empty(self):
        store = StoreModel('test')

        self.assertListEqual(store.items.all(), [])

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')

            self.assertIsNone(store.find_by_name('test'))

            store.save_to_db()

            self.assertIsNotNone(store.find_by_name('test'))

            store.delete_from_db()

            self.assertIsNone(store.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('Test_store')
            item = ItemModel('Test_item', 21.50, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'Test_store')

    def test_store_json(self):
        with self.app_context():
            store = StoreModel('test')
            expected = {'id': None, 'name': 'test', 'items': []}

            self.assertDictEqual(store.json(), expected)

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 21.50, 1)
            store.save_to_db()
            item.save_to_db()
            expected = {'id': 1, 'name': 'test', 'items': [{'name': 'test_item', 'price': 21.50}]}

            self.assertDictEqual(store.json(), expected)
