from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Employee(models.Model):
    full_name = models.CharField(max_length=200, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)  # validators should be a list
    company = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    # owner = models.ForeignKey('auth.User', related_name='employee', on_delete=models.CASCADE)
    # highlighted = models.TextField()

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
