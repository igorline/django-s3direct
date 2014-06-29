from django.db import models


class Kitten(models.Model):
    file = models.FileField(upload_to='path/foo')

    def __unicode__(self):
        return str(self.file)