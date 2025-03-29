from django.db import models

# Create your models here.

class Feedback(models.Model):
    """ This represents a feedback from a user """
    company = models.CharField(max_length=100)
    message = models.CharField(max_length=5000)

# {
#     "company": "Matar",
#     "message": "The biggest is coming!"
# }

# {
#     "company": "Faly",
#     "message": "Grant me access"
# }
