from django.db import models
import re
from datetime import datetime

# Create your models here.
class UserManager(models.Manager):
  def validate(self, form_data):
    errors = {}
    if len(form_data['first']) < 2:
      errors['first'] = 'First name should be at least 2 letters'
    if len(form_data['last']) < 2:
      errors['last'] = 'Last name should be at least 2 letters'
  
    if not form_data['first'].isalpha() and form_data['first'] != '':
      errors['first'] = "First name must contain only letters"

    if not form_data['last'].isalpha() and form_data['last'] != '':
        errors['last'] = "Last name must contain only letters"
    
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(form_data['email']):    # test whether a field matches the pattern            
        errors['email'] = ("Invalid email address!")

    exist_email = self.filter(email=form_data['email'])
    if exist_email:
      errors['email'] = 'Email in use already, choose another one'

    if len(form_data['birthday']) < 1:
      errors['birthday'] = "Field required, please provide date"
    
    #checking if user is under 13 years old
    
    today = datetime.today()
    converted_birthday = datetime.strptime(form_data['birthday'], '%Y-%m-%d')
    age = (today - converted_birthday).days
    age = round(age/365)

    if age < 13:
      errors['birthday'] = "You are too young to sign up this site."
    
    #checking if user put valid past birth date
    convert = datetime.strptime(form_data['birthday'], '%Y-%m-%d')
    if convert > datetime.now():
      errors['r_date'] = "You can't choose future date "

    if len(form_data['password']) < 4:
      errors['password'] = "Password must be at least 3 Charactors."
    
    if form_data['cpassword'] != form_data['password']:
      errors['cpassword'] = "Password did not match. "
    return errors




class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  birth_date = models.DateTimeField()
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()