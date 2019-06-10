from tests.unit.unit_base_test import UnitBaseTest
from models.user import UserModel


class TestUser(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test', "User name is not equal to expected.")
        self.assertEqual(user.password, 'abcd', "Password is not equal to expected.")

