from django.db import models


class FileObject(models.Model):
    id = models.TextField(primary_key=True, max_length=32)
