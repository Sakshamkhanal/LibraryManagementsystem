from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Libary_user)
admin.site.register(Book)
admin.site.register(BooksDetails)
admin.site.register(BorrowedBooks)