from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as __

class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError (__("You must provide a valid email address."))
        
    def create_user(self,first_name,last_name,email,password,**extra_fields):
        if not first_name:
            raise ValueError(__("Users must have first a name."))
        if not last_name:
            raise ValueError(__("Users must have a last name."))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(__("Users must have an email address."))
        user = self.model(first_name=first_name, last_name=last_name,email=email,**extra_fields)
        user.set.password(password)
        
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,email,password,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(__("Superuser must have is_staff=True"))
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(__("Superuser must have  is_superuser=True"))
        
        if not password:
             raise ValueError(__("Superuser must have a password")) 
        
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(__("Superuser must have an email address")) 
        
        user = self.create_user(first_name,last_name,email,password,**extra_fields)
        user.save(using=self._db)
        return user
            
        