from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_crate_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="marcos", email="marcos@email.com", password="testpass123"
        )
        self.assertEqual(user.username, "marcos")
        self.assertEqual(user.email, "marcos@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="marcos_admin", email="marcos_admin@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, "marcos_admin")
        self.assertEqual(admin_user.email, "marcos_admin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
