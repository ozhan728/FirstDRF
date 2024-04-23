from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Home(APIView):
    def get(self,request):
        # name = request.GET['name']
        # name = request.query_params['name']
        return Response({'age':26,'name':'ozhan'})

    def post(self,request):
        name = request.data['name']
        return Response({'name':name})