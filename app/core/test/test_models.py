from django.test import TestCase #importando la clase de caso de prueba
from django.contrib.auth import get_user_model #importando la funcion auxiliar para obtener el modelo de usuario de Django

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = 'P1234'
        user = get_user_model().objects.create_user(
			email=email,
			password=password
		)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
       """Test the email for a new user is normalized"""
       email = 'test@TEST.com'
       user = get_user_model().objects.create_user(email, 'test123')
       
       self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
            """Test creating user with no email raises error"""
            with self.assertRaises(ValueError):
                get_user_model().objects.create_user(None, 'test123')
    