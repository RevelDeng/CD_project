from django.db import models
from django.db.models.fields import EmailField
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2 or postData['first_name'].isalpha() == False:
            errors['first_name'] = "First name must be only letters and must be at least 2 characters."
        if len(postData['last_name']) < 2 or postData['last_name'].isalpha() == False:
            errors['last_name'] = "Last name must be only letters and must be at least 2 characters."
        if not re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$').match(postData['email']):
            errors['email'] = "Invalid email address."
        for user in User.objects.all():
            if postData['email'] == user.email:
                errors['unique_email'] = "A user with this email has already been registered."
        if len(postData['password']) < 8 or postData['password'] != postData['confirm_pw']:
            errors['password'] = "Password must be at least 8 characters and must match the password confirmation."
        return errors
    def login_validator(self, postData):
        errors = {}
        if not re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$').match(postData['email_login']):
            errors['email_login'] = "Invalid email address."
        if len(postData['pw_login']) < 8:
            errors['pw_login'] = "Password must be at least 8 characters."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self) -> str:
        return f"<User object: {self.first_name} {self.email} ({self.id})>"

class AdminManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2 or postData['first_name'].isalpha() == False:
            errors['first_name'] = "First name must be only letters and must be at least 2 characters."
        if len(postData['last_name']) < 2 or postData['last_name'].isalpha() == False:
            errors['last_name'] = "Last name must be only letters and must be at least 2 characters."
        if not re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$').match(postData['email']):
            errors['email'] = "Invalid email address."
        for admin in Admin.objects.all():
            if postData['email'] == admin.email:
                errors['unique_email'] = "An admin with this email has already been registered."
        if len(postData['password']) < 8 or postData['password'] != postData['confirm_pw']:
            errors['password'] = "Password must be at least 8 characters and must match the password confirmation."
        return errors
    def login_validator(self, postData):
        errors = {}
        if not re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$').match(postData['email_login']):
            errors['email_login'] = "Invalid email address."
        if len(postData['pw_login']) < 8:
            errors['pw_login'] = "Password must be at least 8 characters."
        return errors

class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AdminManager()
    def __repr__(self) -> str:
        return f"<Admin object: {self.first_name} {self.email} ({self.id})>"