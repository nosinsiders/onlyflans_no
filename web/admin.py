from django.contrib import admin
from .models import Flan, ContactForm
	
# Register your models here.
@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
	list_display = ('flan_uuid', 'name', 'description', 'image_url', 'slug', 'is_private')
	search_fields = ('name', 'description')
	list_filter = ('name', 'is_private')

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('contact_form_uuid', 'customer_email','customer_name','message')
    search_fields = ('customer_email','customer_name')