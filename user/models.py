from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils import timezone



# Create your models here.
class UserManager(BaseUserManager):
    

    def create_user(self, email, bio, username, password):
        
        user = self.model(
            email=self.normalize_email(email),
            bio=bio,
            username=username,
            date_joined = timezone.now(),
            is_superuser = 0,
            is_staff = 0,
            is_active = 1,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

def create_superuser(self, email, bio, password):
        
        user = self.create_user(email, bio, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = 1
        user.is_staff = 1
        user.save(using=self._db)

        return user

class UserModel(AbstractUser, PermissionsMixin):


    class Meta:
        db_table = "my_user"
    
    password = models.CharField(max_length=128)
    bio = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = 'email'
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    REQUIRED_FIELDS = ['bio', 'username'] # removes email from REQUIRED_FIELDS
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.email


