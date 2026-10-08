from django.contrib import admin
from .models import Pessoa
from .models import Contato
    # Register your models here.
admin.site.register(Pessoa)

admin.site.register(Contato)