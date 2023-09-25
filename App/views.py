
from rest_framework.response import Response
from .models import Invoice,InvoiceDetail
from .serializers import InvoiceSerializer,InvoiceDetailSerializer
from .models import InvoiceDetail,Invoice
from rest_framework.views import APIView
from rest_framework import status

class InvoiceAPI(APIView):

    def get(self, request):
        objs = Invoice.objects.all()
        serializer = InvoiceSerializer(objs,many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        try:
            data = request.data
            obj = Invoice.objects.get(id=data['id'])
                    
            serializer = InvoiceSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response({
                    'data': {},
                    'message': 'invalid request . ! '
                }, status=status.HTTP_400_BAD_REQUEST)


class InvoiceDetailAPI(APIView):

    def get(self, request):
        objs = InvoiceDetail.objects.all()
        serializer = InvoiceDetailSerializer(objs,many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = InvoiceDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        try:
            data = request.data
            obj = InvoiceDetail.objects.get(id=data['id'])
                    
            serializer = InvoiceDetailSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response({
                    'data': {},
                    'message': 'invalid request . ! '
                }, status=status.HTTP_400_BAD_REQUEST)
