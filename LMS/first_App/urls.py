from django.urls import path
from .views import Libary_user_view,Libary_user_Detail,Book_view,Book_ID_view,Book_Detail_Info_view,BorrowedBooks_list_view,BorrowedBooks_return_update_view,BorrowedBooks_user_view


urlpatterns = [
    path("Libary_user/",Libary_user_view.as_view()),
    path("Libary_user_detail/<int:pk>",Libary_user_Detail.as_view()),
    path('Book/',Book_view.as_view()),
    path('Book_detail/<int:pk>',Book_ID_view.as_view()),
    path('Book_info',Book_Detail_Info_view.as_view()),
    path('Book_borrow/',BorrowedBooks_user_view.as_view()),
    path('Book_return/',BorrowedBooks_return_update_view.as_view()),
    path('Book_Borrow_list/',BorrowedBooks_list_view.as_view()),
    
]
