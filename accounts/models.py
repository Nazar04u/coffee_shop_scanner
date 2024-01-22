from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.apps import apps

User = apps.get_registered_model('custom_user', "User")


class User_Unauthorized_Contact_Model(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = RichTextUploadingField()


class User_Contact_Model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = RichTextUploadingField()
