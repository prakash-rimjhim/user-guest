import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from User.api.serializers import UserSerializer
from User.models import User

class UserTestCase(APITestCase):
    def test_user_create(self):
        user = User.objects.user_create('rimmi','nitinojha34@gmail.com','487328947','true','user','false','2021-12-22T05:53:11Z')












