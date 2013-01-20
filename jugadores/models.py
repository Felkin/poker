from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jugador(models.Model):
	usuario = models.OneToOneField(User, primary_key=True)
	dni = models.CharField(max_length=12, unique=True)
	fnacim = models.DateField("fecha de nacimiento")

	def __unicode__(self):
		return User.objects.get(id=self.usuario.id).username

	def edad(self):
		e = date.today().year - self.fnacim.year
		if date.today().month < self.fnacim.month or (date.today().month == self.fnacim.month and date.today().day < date.fnacim.day):
			e -= 1
		return e

	def nombre_completo(self):
		user = User.objects.get(id=self.usuario.id)
		full_name = user.get_full_name()
		if full_name != "":
			return full_name
		else:
			return user.username
