from django.contrib import admin
from .models import creds

class credsadmin(admin.ModelAdmin):
    fields=(('project_name','secret_key'),'database_name',('database_user','database_password'),'database_host')
    list_display=['id','project_name','date']
    list_filter=['date','project_name']
    search_fields=['project_name','database_user','database_name']

    class Meta:
        ordering:['id']


admin.site.register(creds,credsadmin)
