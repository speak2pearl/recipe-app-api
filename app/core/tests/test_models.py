from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""

        email = 'bhupesh@gmail.com'
        password = 'test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test email for a new user is normalized"""
        email = "test@BHUPESH.com"
        user = get_user_model().objects.create_user(
            email,
            'test123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test email for a new user"""

        email = ""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new super user"""

        email = 'superuser@gmail.com'
        name = 'Bhupesh'
        password = 'test12345'
        user = get_user_model().objects.create_superuser(
            email=email,
            name=name,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
