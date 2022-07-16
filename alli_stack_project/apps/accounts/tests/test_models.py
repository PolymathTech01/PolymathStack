from django.db.utils import IntegrityError
from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserManagerTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='user@email.com', password='alll')
        # performs its equality using '=='
        self.assertEqual(user.email, 'user@email.com')
        # self.assertEquals  # performs its equality using 'is'
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

        with self.assertRaises(TypeError):
            # if all parameters are not passed in correctely, it will raise a TypeError
            User.objects.create_user()

        with self.assertRaises(TypeError):
            # if an email is supplied without password
            User.objects.create_user(email='')

        with self.assertRaises(ValueError):
            # if email is null and password is passed
            User.objects.create_user(email='', password='alll')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='superuser@email.com', password='alll')
        self.assertEqual(admin_user.email, 'superuser@email.com')
        # self.assertEquals  # performs its equality using 'is'
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class CustomUserModelTests(TestCase):
    def test_user_slug_is_unique(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='user@email.com', password='alll')
        user2 = User.objects.create_user(
            email='user2@email.com', password='alll')
        self.assertNotEqual(user.slug, user2.slug)

        with self.assertRaises(IntegrityError):
            # if a user is created with the same slug, it will raise an IntegrityError
            User.objects.create_user(
                email='user@email.com', slug='user', password='alll')
            User.objects.create_user(
                email='user@email.com', slug='user', password='alll')

    def test__str__(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='user@email.com', password='alll')
        self.assertEqual(str(user), user.email)

    def test_user_slug_is_generated_if_blank(self):
        """
        test if a slug is generated if it is blank
        """
        User = get_user_model()
        user = User.objects.create_user(
            email='user@email.com', password='alll')
        self.assertNotEqual(user.slug, '')

    def test_user_slug_is_not_overwritten(self):
        """
        test that a user inputed slug is not overwritten
        """
        User = get_user_model()
        user = User.objects.create_user(
            email='user@email.com', password='alll', slug='user')
        self.assertEqual(user.slug, 'user')
