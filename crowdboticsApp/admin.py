from django.contrib import admin

# Register your models here.
from crowdboticsApp.models import Dog, Cat

admin.site.register(Dog)
admin.site.register(Cat)
