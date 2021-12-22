from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime


class User(models.Model):
    first_name = models.CharField(max_length=20, default='ram')
    last_name = models.CharField(max_length=20, default='dev')
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    user_types = [
        ('guest', 'guest'),
        ('user', 'user'),
    ]
    user_type = models.CharField(
        max_length=20,
        choices=user_types,
        default='user'
    )

    super_user = models.BooleanField(default=False)
    dob = models.DateTimeField(default=timezone.now)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_age(self):
        return datetime.date.today().year - self.dob.year

    def __str__(self):
        return self.first_name + " " + self.last_name
