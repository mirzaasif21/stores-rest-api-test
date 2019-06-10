from models.user import UserModel
from tests.base_test import BaseTest


class IntegrationTestUser(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('Test_user', 'abcdef')

            self.assertIsNone(UserModel.find_by_username('Test_user'))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('Test_user'))
            self.assertIsNotNone(UserModel.find_by_id(1))



