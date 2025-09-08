from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    profile_pic = models.ImageField(upload_to='profile_photo/', blank=True, default='profile_photo.png')
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    address = models.CharField(max_length=800)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

STATUS = (
    (0,"Unresolved"),
    (1,"Resolved")
)

STATUS_R = (
    (0,"Not Allocated"),
    (1,"Allocated")
)
STATUS_T = (
    (0,"Incompleted"),
    (1,"Completed")
)
class disaster(models.Model):
    disaster_name = models.CharField(max_length=500)
    location = models.CharField(max_length=1000)
    status = models.IntegerField(choices=STATUS, default=0)
    details = models.TextField(max_length=5000)
    resources_needed = models.TextField(max_length=5000)
    tasks = models.TextField(max_length=5000)
    updates = models.TextField(max_length=5000)
    slug = models.SlugField(default="")

    def __str__(self):
        return self.disaster_name
    
class resources(models.Model):
    resource_name = models.CharField(max_length=500)
    type = models.CharField(max_length=1000)
    allocation_status = models.IntegerField(choices=STATUS_R, default=0)
    details = models.TextField(max_length=5000)
    quantity = models.IntegerField()
    allocation_history = models.TextField(max_length=5000)
    assignment = models.TextField(max_length=5000)
    slug = models.SlugField(default="")

    def __str__(self):
        return self.resource_name
    
class tasks(models.Model):
    task_name = models.CharField(max_length=500)
    type = models.CharField(max_length=1000)
    status = models.IntegerField(choices=STATUS_T, default=0)
    description = models.TextField(max_length=5000)
    assigned_resources = models.ManyToManyField(resources)
    slug = models.SlugField(default="")
    
    updates = models.TextField(max_length=5000)

    def __str__(self):
        return self.task_name