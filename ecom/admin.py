from django.contrib import admin

# Register your models here.
from .models import Category,Sub_Category,Product,Contact_us,Order
# for image show in admin
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.image.url))
    list_display =['image_tag', 'name', 'price', 'date']


class ContactAdimn(admin.ModelAdmin):
    list_display =['name', 'email', 'subject']


class OrderAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.image.url))
    list_display =['image_tag', 'user', 'product','quantity', 'total','phone', 'date']

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact_us, ContactAdimn)
