from django.db import models
import string
import random

# Helper function to generate a unique 5-character key
def generate_unique_key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

class Session(models.Model):
    key = models.CharField(max_length=5, unique=True, default=generate_unique_key)

class File(models.Model):
    session = models.ForeignKey(Session, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
