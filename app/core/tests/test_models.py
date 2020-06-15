from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with email is success"""
        email = 'test@test.com'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test if the email for new user is normalized"""
        email = "test@LONDONAPP.COM"
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email.lower(), email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_super_user_created(self):
        """tests if create superuser success"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
