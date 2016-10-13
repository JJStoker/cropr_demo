from django.db import models


class Grant(models.Model):
    user = models.OneToOneField('auth.User', related_name='grant')
    grant = models.CharField(max_length=100)

class AccessToken(models.Model):
    user = models.OneToOneField('auth.User', related_name='access_token')
    access_token = models.CharField(max_length=100)
