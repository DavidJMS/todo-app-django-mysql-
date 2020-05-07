from apps.task import models as task_models
from apps.task import serializers as task_serializers
from django.db import transaction
from apps.task import validations as task_validations

def register_task(data:dict):
	if data.get('title') is not None:
		task_validations.validate_max_title(data.get('title'))
	else:
		raise ValueError(str("El título de la task no debe de estar vacío"))
	if data.get('description') is not None:
		task_validations.validate_max_description(data.get('description'))
	if data.get('completed') is not None:
		task_validations.validate_completed(data.get('completed'))
	with transaction.atomic():
		try:
			task = task_models.Task.objects.create(
				title = data.get('title').lower(),
				description = data.get('description').lower(),
				completed = data.get('completed'),
				)
			task.save()
		except Exception as e:
			raise ValueError(e)
	return task


def get_task(id:int):
	try:
		task = task_models.Task.objects.get(id=id)
	except task_models.Task.DoesNotExist:
		raise ValueError(str("La task no existe"))
	except Exception as e:
		raise ValueError(str("Hubo un error, vuelva a intentar"))
	return task

def delete_task(id:int):
	try:
		task = task_models.Task.objects.get(id=id)
		with transaction.atomic():
			task.delete()
	except task_models.Task.DoesNotExist:
		raise ValueError(str("La task no existe"))
	except Exception as e:
		raise ValueError(str("Hubo un error, vuelva a intentar"))
	return task

def update_task(data:dict,id:int):
	try:
		task = task_models.Task.objects.get(id=id)
		if data.get('title') is not None:
			task_validations.validate_max_title(data.get('title'))
			task.title = data.get('title')
		if data.get('description') is not None:
			task_validations.validate_max_description(data.get('description'))
			task.description = data.get('description')
		if data.get('completed') is not None:
			task_validations.validate_completed(data.get('completed'))
			task.completed = data.get('completed')
		with transaction.atomic():
			task.save()
	except task_models.Task.DoesNotExist:
		raise ValueError(str("La task no existe"))
	return task

def get_task_all(data:dict):
	print(data)
	tasks = task_models.Task.objects.all()
	title = data.get('title')
	if title is not None:
		tasks = tasks.filter(title__icontains=title)
	if tasks is None or len(tasks)==0:
		raise ValueError(str('El título no se encuentra, prueba con otro'))
	return tasks

def get_task_all_filter(data:dict):
	print(data)
	tasks = task_models.Task.objects.all()
	title = data.get('title')
	if title is not None:
		tasks = tasks.filter(title__icontains=title)
	if tasks is None or len(tasks)==0:
		raise ValueError(str('El título no se encuentra, prueba con otro'))
	return tasks

def delete_tasks_all():
	tasks = task_models.Task.objects.all()
	with transaction.atomic():
		tasks.delete()
	return True