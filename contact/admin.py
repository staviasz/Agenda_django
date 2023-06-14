from django.contrib import admin

from contact import models

# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'phone')
  ordering = '-id',
  list_filter = 'created_at',
  list_per_page = 10
  list_max_show_all = 200


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = 'name',
  ordering = '-id',