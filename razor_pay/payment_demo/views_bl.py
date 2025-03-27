from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class TestAPI(APIView):
    def get(self,request):
        data = {
            "name":"Aditya Kumar",
            "designation":"Python developer",
            "emp_id":"911",
        }
        return Response({"status":status.HTTP_200_OK,"data":data,"message":"Data sent successfully!"})
