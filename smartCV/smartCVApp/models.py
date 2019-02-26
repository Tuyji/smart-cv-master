from django.db import models

class AccessToken(models.Model):
	oauth_token= models.CharField(max_length=200)
	oauth_token_secret= models.CharField(max_length=200)
	a_oauth_token= models.CharField(max_length=200,null=True)
	a_oauth_token_secret= models.CharField(max_length=200,null=True)
	created_date= models.DateTimeField('date published')
	oauth_verifier=models.CharField(max_length=200,null=True)
	token_status=models.IntegerField()

# Create your models here.
