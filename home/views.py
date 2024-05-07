from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person , Question , Answer
from .serializers import PersonSerializer , QuestionSerializer , AnswerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

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


class QuestionView(APIView):
    def get(self,request):
        question = Question.objects.all()
        srz_data = QuestionSerializer(instance=question, many=True).data
        return Response(srz_data,status=status.HTTP_200_OK)

    def post(self,request):
        pass

    def put(self,request,pk):
        pass

    def delete(self,request,pk):
        pass