from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=255, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    gender = models.OneToOneField('Gender', on_delete=models.CASCADE)
    dob = models.DateField(max_length=12, blank=False)
    aadhar = models.IntegerField(blank=False, null=False)
    phone = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=128, blank=False, null=False)

    def __str__(self):
        return self.username


class Gender(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    GENDER_TYPE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='genders')
    value = models.CharField(max_length=55, choices=GENDER_TYPE)

    def __str__(self):
        return self.value


class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    username = models.CharField(max_length=255, blank=False, null=False)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
