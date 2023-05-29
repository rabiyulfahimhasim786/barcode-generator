from django.db import models

# Create your models here.
class Barcodefile(models.Model):
    inputfile = models.FileField(upload_to='csv_files/')
    pdflink = models.TextField(blank=True)

# static method
class Barcode(models.Model):
    number = models.TextField(max_length=255)
    pdf = models.URLField(max_length=255)

    def __str__(self):
        return self.number