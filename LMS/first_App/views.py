
from rest_framework.views import APIView
from .models import *
from .serilalizers import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class Libary_user_view(APIView):
    
    def get(self,request):
            users = Libary_user.objects.all()
            serializers = Libary_user_serializer(users,many=True)
            return Response(serializers.data)
    
    def post(self,request,format=None):
        serializers = Libary_user_serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class Libary_user_Detail(APIView):
     def get(self,request,pk):
          user = Libary_user.objects.get(pk=pk)
          serializers = Libary_user_serializer(user)
          return Response(serializers.data)

          
     
class Book_view(APIView):
    def get(self,request):
            book = Book.objects.all()
            serializers = Book_serializer(book,many=True)
            return Response(serializers.data)
    
    def post(self,request,format=None):
        serializers = Book_serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class Book_ID_view(APIView):
     def get(self,request,pk):
          book = Book.objects.get(pk=pk)
          serializers = Book_serializer(book)
          return Response(serializers.data)
     
class Book_Detail_Info_view(APIView):
     def get(self,request):
          book_details = BooksDetails.objects.all()
          serializers = BooksDetails_serializer(book_details,many=True)
          return Response(serializers.data)
     
     def post(self,request,format=None):
        serializers = BooksDetails_serializer(data=request.data)    
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class BorrowedBooks_user_view(APIView):
    def get(self,request):
            book = BorrowedBooks.objects.all()
            serializers = BorrowedBooks_user_serializer(book,many=True)
            return Response(serializers.data)
    
    def post(self,request,format=None):
        serializers = BorrowedBooks_user_serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class BorrowedBooks_return_update_view(APIView):
    def get(self,request):
            book = BorrowedBooks.objects.all()
            serializers = BorrowedBooks_return_update_serializer(book,many=True)
            return Response(serializers.data)
    
    def post(self,request,format=None):
        serializers = BorrowedBooks_return_update_serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class BorrowedBooks_list_view(APIView):
    def get(self,request):
            book = BorrowedBooks.objects.all()
            serializers = BorrowedBooks_list_serializer(book,many=True)
            return Response(serializers.data)
    
   