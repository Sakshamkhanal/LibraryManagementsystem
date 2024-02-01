from django.db import models

from django.db import models

# Create your models here.
class Libary_user(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    MembershipDate = models.DateField()
    
    def __str__(self):
            return self.Name

class Book(models.Model):
    BookID = models.IntegerField(primary_key=True)
    Book_number = models.IntegerField()
    Title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13,unique=True)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=255)

    def __str__(self):
        return str(self.BookID)
    

class BooksDetails(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    BookID = models.OneToOneField(Book,on_delete=models.CASCADE)
    NumberOfPages = models.PositiveIntegerField()
    Publisher = models.CharField(max_length=255)
    Language = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.BookID.Title} - Details"
    

class BorrowedBooks(models.Model):
    UserID = models.ForeignKey(Libary_user,on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book,on_delete=models.CASCADE)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.UserID.Name} - {self.BookID.Title}"