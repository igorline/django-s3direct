from django.contrib import admin
from .models import Kitten
from .forms import KittenForm


class KittenAdmin(admin.ModelAdmin):
	form = KittenForm


admin.site.register(Kitten, KittenAdmin)
