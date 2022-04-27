from django.db import models
from django.contrib.auth.models import User


class EmbededObject(models.Model):
    CONTENT_TYPE = (
        ('xlsx', 'Excel'),
        ('pptx', 'Powerpoint'),
        ('else', 'Sonstiges')
    )

    id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=120, verbose_name='Dateiname')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True,
                              verbose_name='Besitzer')
    content_type = models.TextField(max_length=5, null=False, default='file', choices=CONTENT_TYPE,
                                    verbose_name='Dateityp')
    content = models.TextField(verbose_name='Inhalt')

    def get_absolute_url(self):
        return f"/cloud/showembedded/{self.id}"

    def get_content(self):
        return self.content

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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True,
                              verbose_name='Besitzer')
    filename = models.CharField(max_length=120, verbose_name='Dateiname')
    file = models.FileField(verbose_name='Datei')
    content_type = models.TextField(max_length=5, null=False, default='file', choices=CONTENT_TYPE,
                                    verbose_name='Dateityp')

    def get_absolute_url(self):
        return f'/cloud/showfile/{self.id}'

    def get_download_url(self):
        return f'/cloud/download/{self.id}'

    def get_delete_url(self):
        return f"/cloud/deletefile/{self.id}"
