from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

# Customer Login Modal
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password,  **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError('The Password field must be set')

        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        extra_fields.setdefault('is_seller',False)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_seller',True)
        return self._create_user( email, password, **extra_fields)

    def create_seller(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        extra_fields.setdefault('is_seller',True)
        return self._create_user( email, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)


class customerUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True,max_length=254)
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='user_accounts',
        related_query_name='user_account',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='user_accounts',
        related_query_name='user_account',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username','firstname','lastname']
    
    class Meta:
        verbose_name = 'customerUser'
        verbose_name_plural = 'customerUsers'


class customerData(models.Model):
    customeruser = models.ForeignKey(customerUser,on_delete=models.CASCADE , related_name='customer')
    gender = models.CharField(max_length=10)
    countrycode = models.CharField(max_length=4)
    mobileno = models.CharField(max_length=10)
    profileimg = models.ImageField(upload_to='media/seller_prof')

    def __str__(self):
        return self.customeruser
