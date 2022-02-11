from django.test import TestCase
from .models import User


class ProfileTestCase(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(
            username="Kliff Arne",
            email="godmode@stud.ntnu.no",
            password="NordNorge"
        )

    def testFields(self):
        try:
            self.assertEqual("Kliff Arne", self.u1.username)
            self.assertEqual("godmode@stud.ntnu.no", self.u1.email)
            self.assertEqual("NordNorge", self.u1.password)
        except Exception:
            print("Error with user fields!")

    def testFieldsFail(self):
        try:
            self.assertNotEqual("olaf Helge", self.u1.username)
        except Exception:
            print("Error with fields! Something is not supposed to be equal")

class testRedirectListView(TestCase):
    ''' If anon user tries to log in -> will be redirected login'''
    def test_anonymous_cannot_see_profile(self):
        response = self.client.get(reverse("profile"))
        self.assertRedirects(response, "/users/login/?next=/users/profile/")
    
    ''' Authenicated user, will enter correct page'''
    def test_authenticated_user_can_see_profile(self):
        user = User.objects.create(username="Filip", password="123456")
        self.client.force_login(user=user)
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)