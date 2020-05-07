from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from apps.task import services as task_services
from apps.task import serializers as task_serializers

class Task(APIView):

	def post(self,request):
		try:
			new_task = task_services.register_task(request.data)
		except ValueError as e:
			return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = task_serializers.TaskSerializer(new_task,many=False).data
		serializer['detail'] = str("Has guardado correctamente la task")
		return Response(serializer, status=status.HTTP_201_CREATED)

	def get(self,request,id):
		try:
			task = task_services.get_task(id)
		except ValueError as e:
			return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = task_serializers.TaskSerializer(task,many=False).data
		serializer['detail'] = str("Has obtenido la task correctamente")
		return Response(serializer, status=status.HTTP_200_OK)

	def delete(self,request,id):
		try:
			task_deleted = task_services.delete_task(id)
		except ValueError as e:
			return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		message = str("Has eliminado la task")
		return Response(message,status=status.HTTP_200_OK)

	def put(self,request,id):
		try:
			task_updated = task_services.update_task(request.data,id)
		except ValueError as e:
			return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = task_serializers.TaskSerializer(task_updated,many=False).data
		serializer['detail'] = str("Has editado la task exitosamente")
		return Response(serializer, status=status.HTTP_200_OK)

class TaskList(APIView):

	def post(self,request):
		try:
			print(request.data)
			task = task_services.get_task_all_filter(request.data)
		except ValueError as e:
			return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = task_serializers.TaskSerializer(task,many=True).data
		return Response(serializer, status=status.HTTP_200_OK)

	def get(self,request):
		try:
			task = task_services.get_task_all(request.data)
		except ValueError as e:
			return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = task_serializers.TaskSerializer(task,many=True).data
		return Response(serializer, status=status.HTTP_200_OK)

	def delete(self,request):
		try:
			task_services.delete_tasks_all()
		except ValueError as e:
			return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		message = str("Has eliminado las tasks")
		return Response(message,status=status.HTTP_200_OK)