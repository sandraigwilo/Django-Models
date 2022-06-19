from django.contrib import admin

from models import Title,Text,Author,Created_date,Published_date

# Register your models here.

admin.site.register(Title)
admin.site.register(Text)
admin.site.register(Author)
admin.site.register(Created_date)
admin.site.register(Published_date)

