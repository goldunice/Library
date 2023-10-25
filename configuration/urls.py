from django.contrib import admin
from django.urls import path
from mainApp.views import homepage, students, authors, books, records, delete_student, delete_author, delete_book, \
    delete_record, update_student, update_author, update_book, update_record, librarians, delete_librarian,update_librarian

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('students/', students),
    path('delete_student/<int:num>/', delete_student),
    path('update_student/<int:num>/', update_student),
    path('authors/', authors),
    path('delete_author/<int:num>/', delete_author),
    path('update_author/<int:num>/', update_author),
    path('books/', books),
    path('delete_book/<int:num>/', delete_book),
    path('update_book/<int:num>/', update_book),
    path('records/', records),
    path('delete_record/<int:num>/', delete_record),
    path('update_record/<int:num>/', update_record),
    path('librarians/', librarians),
    path('delete_librarian/<int:num>/', delete_librarian),
    path('update_librarian/<int:num>/', update_librarian),
]
