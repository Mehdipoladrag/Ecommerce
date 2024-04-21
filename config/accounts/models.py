from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
# Create your models here.

# what is a diffrent bettwen a AbstractBaseUser, AbstractUser ===>> https://www.mongard.ir/one_part/123/django-abstractuser-vs-abstractbaseuser/ 
class User(AbstractBaseUser) : 
  email = models.EmailField( max_length=254, unique=True)
  phone_number = models.CharField( max_length=11, unique=True)
  full_name = models.CharField(max_length=50)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'phone_number' # Validation User for Login or Register
  REQUIRED_FIELDS = ['email', 'full_name'] # just For CreateSuperuser

  def __str__(self):
    return self.email
  
  def has_perm(self, perm, obj=None):
    return True
  
  def has_module_perms(self, app_label) : 
    return True
  
  @property
  def is_staff(self) : 
    return self.is_admin
