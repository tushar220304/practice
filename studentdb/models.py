from django.db import models

class Students(models.Model):
	Name = models.CharField(max_length=250)
	Age = models.IntegerField(default=0)

	class Meta:
		verbose_name = 'Students'
		verbose_name_plural = 'Students'

	def __str__(self):
		return self.Name