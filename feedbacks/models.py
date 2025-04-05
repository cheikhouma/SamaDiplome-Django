from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    """ This represents a feedback from a user """
    company = models.CharField(max_length=100)
    message = models.CharField(max_length=5000)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

# {
#     "company": "Matar",
#     "message": "The biggest is coming!"
# }

# {
#     "company": "Faly",
#     "message": "Grant me access"
# }
