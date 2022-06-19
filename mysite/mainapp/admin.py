from django.contrib import admin
from .models import Kandydat, Raport, Wyborca, Wybory

admin.site.register(Kandydat)
admin.site.register(Wybory)
admin.site.register(Wyborca)
admin.site.register(Raport)
