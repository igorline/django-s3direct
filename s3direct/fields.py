import os
import datetime

from django.db.models import Field
from django.forms import widgets
from s3direct.widgets import S3DirectEditor
from django.conf import settings
from django.utils.encoding import force_str, force_text

import sys

class S3DirectField(Field):
    def __init__(self, *args, **kwargs):
        upload_to = kwargs.pop('upload_to', '')
        self.upload_to = upload_to
        if callable(upload_to):
            self.generate_filename = upload_to

        self.widget = S3DirectEditor(upload_to=self.get_directory_name())
        super(S3DirectField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "TextField"

    def formfield(self, **kwargs):
        defaults = {'widget': self.widget}
        defaults.update(kwargs)
        return super(S3DirectField, self).formfield(**defaults)

    def get_directory_name(self):
        return os.path.normpath(force_text(datetime.datetime.now().strftime(force_str(self.upload_to))))

    def generate_filename(self, instance, filename):
        return os.path.join(self.get_directory_name(), self.get_filename(filename))


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^s3direct\.fields\.S3DirectField"])