from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
import uuid
from django.utils.translation import ugettext as _


class BaseModel (models.Model):
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    
class EmailList (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=CASCADE)
    email = models.EmailField(max_length=254)
    is_subscribed = models.BooleanField(default=True)

class UserDetails (models.Model):
    class Meta:
        verbose_name_plural = "User Details"
    class Type(models.TextChoices):
        FEMALE = 'F', _('FEMALE')
        MALE = 'M', _('MALE')
        PNTS = 'P', _('PREFER NOT TO SAY')
        # Test
        OTHER = models.TextField (max_length=10), _('OTHER')
    user = models.ForeignKey(User, null=False, on_delete=CASCADE)
    age = models.IntegerField()
    gender  = models.CharField (max_length=40, choices=Type.choices, default=None)

    def __str__(self):
        return f"User: {self.user}, Age: {self.age},  Gender: {self.gender}"