"""
This code defines a custom user model for a Django web application.

The User class inherits from AbstractBaseUser, which is a base class provided by Django's built-in authentication system that provides the core implementation for a user model. It includes fields such as date_joined, last_login, and is_active, as well as methods such as has_perm and has_module_perms that are used by Django's permission system.

The User class also defines several additional fields, such as first_name, last_name, username, email, phone_number, and role. The role field is a PositiveSmallIntegerField with a ROLE_CHOICE tuple of choices, which allows the user to be assigned one of two roles: RESTAURANT or CUSTOMER.

The User class also includes several Boolean fields such as is_admin, is_staff, is_active, and is_superadmin that can be used to manage user permissions and access within the application.

The User class also has a custom manager, UserManager, which is responsible for creating and managing User objects. The UserManager class defines two methods: create_user and create_superuser. The create_user method is used to create a normal user, while the create_superuser method is used to create a superuser, which is a user with all permissions.

Finally, the USERNAME_FIELD attribute is set to email, which specifies that the email field should be used as the unique identifier for a User object, and the REQUIRED_FIELDS attribute is set to a list of required fields when creating a User object.
---------------------------------------------------------------------

The line objects = UserManager() in the User class specifies that the UserManager class should be used as the manager for the User model.

In Django, a manager is an interface through which database query operations are provided to Django models. Django provides a default manager for every model, but it's also possible to define custom managers to perform specific tasks or customize the behavior of the model's queryset.

The UserManager class provides two methods for creating users: create_user and create_superuser. The create_user method is used to create a normal user, while the create_superuser method is used to create a superuser, which is a user with all permissions.

The objects attribute is an instance of the UserManager class, and it can be used to create new User objects, as well as perform other query operations on the User model. For example, you could use User.objects.all() to retrieve all User objects from the database.

---------------------------------------------------------------------
USERNAME_FIELD is an attribute of the AbstractBaseUser class that specifies which field should be used as the unique identifier for a user object. In the code you provided, USERNAME_FIELD is set to 'email', which means that the email field will be used as the unique identifier for User objects.

This is useful because it allows you to specify which field should be used as the login field for the user. For example, if you set USERNAME_FIELD to 'username', users would be required to enter their username when logging in, rather than their email address.

The value of USERNAME_FIELD should be a string that corresponds to the name of a field in the User model. In this case, 'email' is a valid field in the User model, so it can be used as the USERNAME_FIELD.

It's also possible to set USERNAME_FIELD to a combination of fields, such as 'email' and 'username', if you want to allow users to log in with either their email address or their username. However, it's important to ensure that the combination of fields is unique for each user, so that there are no conflicts when logging in.

"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.related import ForeignKey, OneToOneField


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        
        if not username: 
            raise ValueError("User must have an username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    VENDOR = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (VENDOR, 'Vendor'),
        (CUSTOMER, 'Customer'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    #required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models. BooleanField(default=False)
    is_staff = models. BooleanField(default=False)
    is_active = models. BooleanField(default=False)
    is_superadmin = models. BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name','last_name']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

"""
This code defines a UserProfile model for a Django web application.

The UserProfile model has a OneToOneField field called user, which is a one-to-one relationship with the User model. This means that each UserProfile object is related to a single User object, and each User object is related to a single UserProfile object. The on_delete parameter is set to models.CASCADE, which means that if the related User object is deleted, the associated UserProfile object will also be deleted.

The UserProfile model also has several other fields, such as profile_picture, cover_photo, and address_line_1, which store additional information about the user. The profile_picture and cover_photo fields are both ImageField fields, which means they are used to store image files. The upload_to parameter specifies a directory where the images should be uploaded.

The UserProfile model also has several CharField fields for storing text data, such as the address_line_1 and address_line_2 fields for storing the user's address, as well as the country, state, city, and pin_code fields for storing the user's location. The latitude and longitude fields are used to store the user's GPS coordinates.

The created_at and modified_at fields are DateTimeField fields that store the creation and modification dates for the UserProfile object.

The __str__ method is used to define a string representation of the UserProfile object. In this case, the string representation is the email of the related User object. This is useful for debugging and for working with the Django admin site.

"""
    
class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photo',blank=True, null=True)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return self.user.email 




