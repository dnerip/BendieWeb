from django.db import models

class Room(models.Model):
	name = models.CharField(max_length=20, null=False, unique=True)

	def __str__(self):
		"""
		String que representa al objeto Room
		"""
		return self.name


class Light(models.Model):
	room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=20, null=False, unique=True)

	def __str__(self):
		"""
		String que representa al objeto Room
		"""
		return self.name


class Blind(models.Model):
	room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=20, null=False, unique=True)

	def __str__(self):
		"""
		String que representa al objeto Room
		"""
		return self.name

class Sensor(models.Model):
	room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=20, null=False, unique=True)

	def __str__(self):
		"""
		String que representa al objeto Room
		"""
		return self.name

class Door(models.Model):
	room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=20, null=False, unique=True)

	def __str__(self):
		"""
		String que representa al objeto Room
		"""
		return self.name