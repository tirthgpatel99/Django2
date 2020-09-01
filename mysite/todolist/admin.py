from django.contrib import admin
from .models import Task
from django.contrib import admin

# Register your models here.

admin.site.register(Task)

admin.site.site_header = 'Ruchik Project'                    # default: "Django Administration"
admin.site.index_title = 'Ancient Anitquity'                 # default: "Site administration"
admin.site.site_title = 'Database'                           # default: "Django site admin"
