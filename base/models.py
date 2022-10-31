from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Location(models.Model):
    place = models.CharField(max_length=200)

    def __str__(self):
        return self.place


class Group_Type(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    GROUP_TYPE = (
        ('Professional', 'Professional'),
        ('Community', 'Community'),
        ('Social', 'Social'),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='groups_type')
    value = models.CharField(max_length=200, choices=GROUP_TYPE)

    def __str__(self):
        return self.value


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=255, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    bio = models.TextField(max_length=500, blank=False)
    gender = models.OneToOneField('Gender', on_delete=models.CASCADE)
    identification = models.OneToOneField(
        'Identification', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)

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
    value = models.CharField(max_length=200, choices=GENDER_TYPE)

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


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Identification(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    aadhar = models.IntegerField(blank=False, null=False)
    aadhar_img = models.ImageField(blank=False, null=False,)
    phone = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=128, blank=False, null=False)
    gender = models.OneToOneField('Gender', on_delete=models.CASCADE)
    dob = models.DateField(max_length=12, blank=False)

    def __str__(self):
        return self.user.username
