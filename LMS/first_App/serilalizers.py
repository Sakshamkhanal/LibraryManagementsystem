from .models import *
from rest_framework import serializers


class Libary_user_serializer(serializers.ModelSerializer):
    class Meta:
        model = Libary_user
        fields = '__all__'

class Book_serializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BooksDetails_serializer(serializers.ModelSerializer):
    class Meta:
        model = BooksDetails
        fields = '__all__'

class BorrowedBooks_user_serializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = ['UserID','BookID','BorrowDate']
        
class BorrowedBooks_return_update_serializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = ['UserID','BookID','ReturnDate']

class BorrowedBooks_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = ['BookID']