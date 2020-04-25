from django.contrib import admin
from .models import Post

#レコード表示機能
class PostAdmin(admin.ModelAdmin):
    list_display = ('task','created_date',)
    list_display_links = ('task','created_date',)

admin.site.register(Post,PostAdmin)