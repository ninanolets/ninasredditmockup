from django.db import models
from datetime import datetime

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    contact_date = models.DateField(default=datetime.now, blank=True)
    user_id = models.IntegerField()

    def __str__(self):
        return self.name
    
    def custom_message(self):
        if len(self.message) > 20:
            return self.message[:20] + "..."
        elif len(self.message) == 0:
            return 'You sent an empty message'
        return self.message