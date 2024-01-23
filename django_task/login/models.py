from django.db import models

# Create your models here.
class Register(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_phone = models.CharField(max_length=50)
    user_dob = models.DateField(max_length=100)

    def __str__(self):
        return str(self.user_id)