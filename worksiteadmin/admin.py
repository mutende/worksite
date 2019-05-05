from django.contrib import admin
from authentication.models import User, Client, Freelancer

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Freelancer)

admin.site.site_header= 'Worksite Admin'