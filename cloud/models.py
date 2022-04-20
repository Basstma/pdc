from django.db import models
from django.contrib.auth.models import User


class EmbededObject(models.Model):

    CONTENT_TYPE = (
        ('xlsx', 'Excel'),
        ('pptx', 'Powerpoint'),
        ('else', 'Sonstiges')
    )

    id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=120)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    content_type = models.TextField(max_length=5, null=False, default='file', choices=CONTENT_TYPE)
    content = models.TextField()

    def get_absolute_url(self):
        return f"/cloud/showembedded/{self.id}"

    def get_delete_url(self):
        return f"/cloud/deleteembedded/{self.id}"


class FileObject(models.Model):
    CONTENT_TYPE = (
        ('pdf', 'pdf'),
        ('video', 'Video'),
        ('img', 'Bild'),
        ('file', 'Andere Datei')
    )
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    filename = models.CharField(max_length=120)
    file = models.FileField()
    content_type = models.TextField(max_length=5, null=False, default='file', choices=CONTENT_TYPE)

    def get_absolute_url(self):
        return f'/cloud/showcontent/{self.id}'

    def get_download_url(self):
        return f'/cloud/download/{self.id}'

    def get_delete_url(self):
        return f"/cloud/deletefile/{self.id}"

