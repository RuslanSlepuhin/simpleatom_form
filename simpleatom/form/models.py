from django.db import models

class FormAnswerModel(models.Model):
    data = models.JSONField(blank=True, null=True)
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return str(self.email)

