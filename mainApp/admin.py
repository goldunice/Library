from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "course", "number_of_book"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "date_of_birth", "alive", "number_of_book"]
    list_display_links = ["name", "id"]
    list_editable = ["number_of_book", "alive"]
    search_fields = ["name"]
    search_help_text = "Look for by these fields: ID, Name, Date_of_birth "
    list_filter = ["alive"]
    # date_hierarchy = "date_of_birth"
    list_per_page = 10


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "page", "genre", "author"]
    search_fields = ["id", "name", "author__name"]
    list_filter = ["genre", "author"]
    list_editable = ["page"]
    autocomplete_fields = ["author"]


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "working_time"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]
    search_help_text = ["Look for by their names"]
    list_filter = ["working_time"]


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ["id", "student", "book", "librarian", "date_of_recieved", "isreturned",
                    "date_of_returned"]
    search_fields = ["student__name", "book__name", "librarian__name"]
    autocomplete_fields = ["student", "book", "librarian"]
    list_display_links = ["id", "student"]
