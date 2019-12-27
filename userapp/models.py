from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.
class UserProfileManager(BaseUserManager):
    '''user profile manager'''

    def create_user(self,email,FirstName,password,LastName=None,Institute=None,Role=None,course=None,semester=None,Roll_fac=None,discipline=None,DOB=None,mobile=None):
        '''creating user model'''
        if not email:
            raise ValueError("Email field is required")

        email=self.normalize_email(email)
        user=self.model(email=email,FirstName=FirstName,LastName=LastName,Institute=Institute,Role=Role,course=course,semester=semester,Roll_fac=Roll_fac,discipline=discipline,DOB=DOB,mobile=mobile)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,FirstName,password):
        '''creating superuser for user profile'''

        user=self.create_user(email,FirstName,password)

        user.is_staff=True
        user.is_superuser=True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    '''Database model for users in thr system'''

    email = models.EmailField(max_length=255,unique=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255,blank=True,null=True)
    Institute = models.CharField(max_length=20,blank=True,null=True)
    Role = models.CharField(max_length=10,blank=True,null=True)
    course = models.CharField(max_length=10,blank=True,null=True)
    semester = models.IntegerField(blank=True,null=True)
    Roll_fac = models.CharField(max_length=20,blank=True,null=True)
    discipline = models.CharField(max_length=50,blank=True,null=True)
    DOB = models.DateTimeField(blank=True,null=True)
    mobile = models.CharField(max_length=10,blank=True,null=True)
    password = models.CharField(max_length=20)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['FirstName']

    def get_full_name(self):
        '''Retrieve full name of user'''
        return self.FirstName

    def get_short_name(self):
        '''Retrieve short name of the user'''
        return self.FirstName

    def __str__(self):
        return self.email
#
# class UserTable(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete = models.CASCADE
#     )
