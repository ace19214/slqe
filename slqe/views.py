from django.shortcuts import render

from django.http.response import *
from rest_framework.parsers import *
from rest_framework_files.viewsets import *
from rest_framework import *
from rest_framework.views import *

from slqe.models import *
from slqe.serializers import *
from rest_framework.decorators import api_view
from ninja import *
from ninja.files import *
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
# Create your views here.
# ------- User view -------------------

class SLQE_API(APIView):
    parser_classes = (MultiPartParser, FormParser, )
    @api_view(['GET', 'POST'])
    def user_list(request):
        if request.method == 'GET':
            users = User.objects.all()
            user_serializer = UserSerializer(users, many=True)
            return JsonResponse(user_serializer.data, safe=False)
            # 'safe=False' for objects serialization
        elif request.method == 'POST':
            user_data = JSONParser().parse(request)
            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
    @api_view(['GET', 'PUT', 'DELETE'])
    def user_detail(request, id):
        try: 
            user = User.objects.get(id=id)
            user_serializer = UserSerializer(user, many=True)
        except User.DoesNotExist: 
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            return JsonResponse(user_serializer.data, safe=False)
        elif request.method == 'PUT':
            user_data = JSONParser().parse(request)
            user_serializer = UserSerializer(user, data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data, status=status.HTTP_204_NO_CONTENT)
            else:
                return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            user.delete()
            return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# ------- Image view -------------------

    @api_view(['POST'])
    def get_image(request, format=None):
        file_obj = request.FILES['file']
        print(file_obj)
        # print(open(file_obj, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True))
        # do some stuff with uploaded 
        # Read Images 
        # img = mpimg.imread(file_obj) 
        # print(img)
        # Output Images 
        # print(plt.imshow(img))
        return Response(status=204)



        