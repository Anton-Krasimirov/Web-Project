# from django.core.validators import RegexValidator
# from django.db import models
#
#
#
# class UserProfile(models.Model):
#     phoneNumberRegex = RegexValidator(regex=r"^[+|0]\d{9,12}$")
#
#     email = models.EmailField(unique=True, null=False, blank=False, )
#
#     phone = models.CharField(validators=[phoneNumberRegex], max_length=10,  null=False, blank=False, )
#
#     region = models.CharField(max_length=30, null=False, blank=False, )
#
#     address = models.TextField(null=False, blank=False, )
#
#     USERNAME_FIELD = 'email'
