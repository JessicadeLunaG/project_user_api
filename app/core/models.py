from django.db import models
from django.conf import settings


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
    
    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    adress = models.CharField(max_length=255)
    user_description = models.CharField(max_length=255)
    date_birth = models.DateTimeField(blank=True, null=True)
    #user_projects = models.ManyToManyField('Project')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) #se ocupa para el admin
    objects = UserManager() #use default usermanager

    USERNAME_FIELD = 'email'

    def __str__(self):
        """Return string representation of user"""
        return self.email

class Project(models.Model):
    """Ingredient to be used in a recipe"""
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    schedule = models.CharField(max_length=11)#check with tags
    project_description = models.CharField(max_length=255)
    creation_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    project_type = models.CharField(max_length=50) #check for tags
    project_status = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name
