from django.contrib import admin
from .models import User_Contact_Model, User_Unauthorized_Contact_Model


class User_Unauthorized_Contact_Admin(admin.ModelAdmin):
    pass


class User_Contact_Admin(admin.ModelAdmin):
    pass


admin.site.register(User_Unauthorized_Contact_Model, User_Unauthorized_Contact_Admin)
admin.site.register(User_Contact_Model, User_Contact_Admin)
