from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.dashboard_url = reverse('dashboard')
        self.user_credentials = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Testpass123!',
            'password2': 'Testpass123!'
        }
        self.user = User.objects.create_user(username='existinguser', password='Testpass123!')

    def test_register_get(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_post_success(self):
        response = self.client.post(self.register_url, self.user_credentials)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.dashboard_url)
        user_exists = User.objects.filter(username='testuser').exists()
        self.assertTrue(user_exists)

    def test_register_post_password_mismatch(self):
        data = self.user_credentials.copy()
        data['password2'] = 'Mismatch123!'
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        # Check error message in response context since assertFormError expects a form instance
        self.assertContains(response, "The two password fields didn’t match.")

    def test_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_post_success(self):
        login_data = {'username': 'existinguser', 'password': 'Testpass123!'}
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.dashboard_url)

    def test_login_post_invalid(self):
        login_data = {'username': 'existinguser', 'password': 'WrongPass!'}
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid username or password.")

    def test_logout(self):
        self.client.login(username='existinguser', password='Testpass123!')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)

    def test_dashboard_access_authenticated(self):
        self.client.login(username='existinguser', password='Testpass123!')
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_dashboard_access_unauthenticated(self):
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{self.login_url}?next={self.dashboard_url}")
