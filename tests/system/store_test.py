from models.store import StoreModel
from tests.base_test import BaseTest
import json
from models.item import ItemModel


class StoreTest(BaseTest):
    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/store/test_store')

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('test_store'))
                self.assertDictEqual({'name': 'test_store', 'items': []},
                                     json.loads(response.data))

    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test_store')
                response = client.post('/store/test_store')

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': "A store with name 'test_store' already exists."},
                                     json.loads(response.data))

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                response = client.delete('/store/test')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'message': 'Store deleted'},
                                     json.loads(response.data))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                response = client.get('store/test')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'name': 'test', 'items': []},
                                     json.loads(response.data))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                response = client.get('store/no_store')

                self.assertEqual(response.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'},
                                     json.loads(response.data))

    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 21.50, 1).save_to_db()

                response = client.get('store/test')
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'name': 'test', 'items': [{'name': 'test', 'price': 21.50}]},
                                     json.loads(response.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                resp = client.get('/stores')

                self.assertDictEqual({'stores': [{'name': 'test', 'items': []}]},
                                     json.loads(resp.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 21.50, 1).save_to_db()
                resp = client.get('/stores')

                self.assertDictEqual({'stores': [{'name': 'test', 'items': [{'name': 'test', 'price': 21.50}]}]},
                                     json.loads(resp.data))
