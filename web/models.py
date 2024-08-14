import uuid
from django.db import models

# Create your models here.
class Flan(models.Model):
  flan_uuid = models.UUIDField(primary_key = True)
  name = models.CharField(max_length=64, blank = False)  #blank: dato no vacio
  description = models.TextField(blank = False)
  image_url = models.URLField(blank = False)
  slug = models.SlugField()   #URL que identifica a la pagina
  is_private = models.BooleanField(default=False)

  def __str__(self):
      return self.name    #self es una referencia actual del objeto.

class ContactForm(models.Model):
  contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
  customer_email = models.EmailField(blank = False)
  customer_name = models.CharField(max_length = 64, blank = False)
  message = models.TextField(blank = False)

  def __str__(self) -> str:
      return self.customer_name
