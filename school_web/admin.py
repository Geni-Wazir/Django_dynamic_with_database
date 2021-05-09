from django.contrib import admin
from .models import achiever, event, thought, announcement,quiz

# Register your models here.

admin.site.register(achiever)
admin.site.register(event)
admin.site.register(thought)
admin.site.register(announcement)
admin.site.register(quiz)
