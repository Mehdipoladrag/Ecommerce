from django.contrib.auth.models import BaseUserManager

# What is a Managers? https://www.mongard.ir/one_part/167/django-managers/ 


class UserManager(BaseUserManager) :
  def create_user(self, phone_number, email, full_name, password) : 
    if not phone_number: 
      raise ValueError('user must have phone number')
    if not email:
      raise ValueError('user must have email')
    if not full_name:
      raise ValueError('user must have full name')
    user = self.model(phone_number=phone_number, email=self.normalize_email(email), full_name=full_name)
    user.set_password(password) # for change pass to hash 
    user.save(using=self._db)
    return user 
  
  
  def create_superuser(self, phone_number, email, full_name, password) : 
    user = self.create_user(phone_number, email, full_name, password)
    user.is_admin = True
    user.save(using=self._db)
    return user 