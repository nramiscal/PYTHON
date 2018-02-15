from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
  def add(self, first_name, last_name, email, age):
    errors = []

    if len(first_name) < 1:
      errors.append("First name must be one letter or more")

    if len(last_name) < 1:
      errors.append("Last name must be one letter or more")

    if len(email) < 1:
      errors.append("Email is required")
    elif not EMAIL_REGEX.match(email):
      errors.append("Invalid email")

    if age < 0:
      errors.append('No timetravel allowed')
    elif age > 150:
      errors.append("No Methuselah's allowed")

    if len(errors) > 0:
      return (False, errors)
    else:
      user = User.userManager.create(first_name = first_name, last_name=last_name, email=email, age=age)
      return (True, student)


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # userManager = UserManager()
    def __repr__(self):
        return "<User object: {} {} {} {}>".format(self.first_name, self.last_name, self.email_address, self.age)
