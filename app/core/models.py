from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    adress = models.CharField(max_length=255)
    user_description = models.CharField(max_length=255)
    date_birth = models.DateTimeField(blank=True, null=True)
    #user_projects = models.ManyToManyField('Project')
    is_staff = models.BooleanField(default=False)

    objects = UserManager() #use default usermanager

    USERNAME_FIELD = 'email'

    def __str__(self):
        """Return string representation of user"""
        return self.email

