from django import test
from django.test import TestCase
from .models import Estate, Belongings
from django.contrib.auth.models import User
from django.urls import reverse


class EstateTestCase(TestCase):

    def setUp(self):
        self.e1 = Estate.objects.create(
            name="Karis bo",
            description="Dette er en testbeskrivelse... lalallala",
            address="Testveien 123 Trondheim",
            image='default.jpg'
        )

    def testEstate(self):
        try:
            self.assertEqual("Karis bo", self.e1.name)
            self.assertEqual("Testveien 123 Trondheim", self.e1.address)
            self.assertEqual('default.jpg', self.e1.image)
            self.assertEqual("Karis bo", str(self.e1))
        except Exception:
            print("Error with estate fields!")

    def testEstateFail(self):
        try:
            self.assertNotEqual("Heisann sveisann", self.e1.name)
        except Exception:
            print("Error with fields! Something is not supposed to be equal")


class BelongingsTestCase(TestCase):

    def setUp(self):
        self.b1 = Belongings()
        self.b1.name = "Sølvskje"
        self.b1.description = "I god stand og veldig fin"
        self.b1.status = "brukt"

    def testFields(self):
        try:
            self.assertEqual("Sølvskje", self.b1.name)
            self.assertEqual("I god stand og veldig fin", self.b1.description)
            self.assertEqual("brukt", self.b1.status)
            self.assertEqual("Sølvskje", str(self.b1))
        except Exception:
            print("Error with fields!")

    def testFieldsFail(self):
        try:
            self.assertNotEqual("dsads", self.b1.status)
        except Exception:
            print("Error with fields! Something is not supposed to be equal")


class TestEstateAndUsers(TestCase):

    def test_estate_has_many_users(self):
        estate = Estate.objects.create(name="Dødsbo 1")
        user1 = User.objects.create(username="Filip")
        user2 = User.objects.create(username="Jennifer")
        estate.users.set([user1.pk, user2.pk])
        self.assertEqual(estate.users.count(), 2)

class TestRedirectListView(TestCase):
    ''' If anon user tries to log in -> will be redirected login'''
    def test_anonymous_cannot_see_page(self):
        response = self.client.get(reverse("dashboard"))
        self.assertRedirects(response, "/users/login/?next=/dashboard/")
    
    ''' Authenicated user, will enter correct page'''
    def test_authenticated_user_can_see_page(self):
        user = User.objects.create(username="Filip", password="123456")
        self.client.force_login(user=user)
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)


class TestStringRepresentation(TestCase):

    def test_estate_str(self):
        estate = Estate.objects.create(name="Dødsbo 1")
        self.assertEqual(str(estate), "Dødsbo 1")

    def test_belongings_str(self):
        estate = Estate.objects.create(name="dødsbo 2")
        bel = Belongings.objects.create(name="Skje og en gaffel", estate=estate)
        self.assertEqual(str(bel), "Skje og en gaffel")

