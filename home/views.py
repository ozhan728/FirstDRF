from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person , Question
from .serializers import PersonSerializer , QuestionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from permissions import IsOwnerOrReadOnly
# from rest_framework.throttling import UserRateThrottle , AnonRateThrottle

# Create your views here.
class Home(APIView):

    permission_classes = [IsAuthenticated,]
    def get(self,request):
        # name = request.GET['name']
        # name = request.query_params['name']
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons,many=True)
        return Response(data=ser_data.data)

    # def post(self,request):
    #     name = request.data['name']
    #     return Response({'name':name})


class QuestionListView(APIView):

    # throttle_classes = [UserRateThrottle,AnonRateThrottle] implemented on entire api
    def get(self,request):
        question = Question.objects.all()
        srz_data = QuestionSerializer(instance=question, many=True).data
        return Response(srz_data,status=status.HTTP_200_OK)

class QuestionCreateView(APIView):

    permission_classes = [IsAuthenticated,]
    def post(self,request):
        srz_data = QuestionSerializer(data=request.POST) # request.data
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_201_CREATED)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):

    permission_classes = [IsOwnerOrReadOnly,]
    def put(self,request,pk):
        question = Question.objects.get(id=pk)
        self.check_object_permissions(request,question)
        srz_data = QuestionSerializer(instance=question,data=request.data,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):

    permission_classes = [IsOwnerOrReadOnly,]

    def delete(self,request,pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message':'question deleted'},status=status.HTTP_200_OK)