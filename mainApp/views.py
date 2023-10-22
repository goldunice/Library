from django.shortcuts import render, redirect
from .models import *


def homepage(request):
    return render(request, 'homepage.html')


def students(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST.get("name"),
            course=request.POST.get("course"),
            number_of_book=request.POST.get("number_of_book")
        )
        return redirect("/students/")

    word = request.GET.get("search")
    result = Student.objects.all()
    if word:
        result = result.filter(name__contains=word)
    content = {
        "students": result
    }
    return render(request, 'students.html', content)


def delete_student(request, num):
    Student.objects.get(id=num).delete()
    return redirect("/students/")


def update_student(request, num):
    if request.method == 'POST':
        Student.objects.filter(id=num).update(
            name=request.POST.get("name"),
            course=request.POST.get("course"),
            number_of_book=request.POST.get("number_of_book")
        )
        return redirect("/students/")
    content = {
        "student": Student.objects.get(id=num)
    }
    return render(request, 'update_student.html', content)


def authors(request):
    if request.method == 'POST':
        Author.objects.create(
            name=request.POST.get("name"),
            gender=request.POST.get("gender"),
            date_of_birth=request.POST.get("date_of_birth"),
            number_of_book=request.POST.get("number_of_book"),
            alive=request.POST.get("alive") == "on"
        )
        return redirect("/authors/")
    word = request.GET.get("search")
    result = Author.objects.all()
    if word:
        result = result.filter(name__contains=word)
    content = {
        "authors": result
    }
    return render(request, 'authors.html', content)


def delete_author(request, num):
    Author.objects.get(id=num).delete()
    return redirect("/authors/")


def update_author(request, num):
    if request.method == 'POST':
        Author.objects.filter(id=num).update(
            name=request.POST.get("name"),
            gender=request.POST.get("gender"),
            date_of_birth=request.POST.get("date_of_birth"),
            number_of_book=request.POST.get("number_of_book"),
            alive=request.POST.get("alive") == "on"
        )
        return redirect("/authors/")
    content = {
        "author": Author.objects.get(id=num)
    }
    return render(request, 'update_author.html', content)


def books(request):
    if request.method == 'POST':
        Book.objects.create(
            name=request.POST.get("name"),
            genre=request.POST.get("genre"),
            page=request.POST.get("page"),
            author=Author.objects.get(id=request.POST.get("author"))
        )
        return redirect("/books/")
    word = request.GET.get("search")
    result = Book.objects.all()
    if word:
        result = result.filter(name__contains=word)
    content = {
        "books": result,
        "authors": Author.objects.all()
    }
    return render(request, 'books.html', content)


def delete_book(request, num):
    Book.objects.get(id=num).delete()
    return redirect("/books/")


def update_book(request, num):
    if request.method == 'POST':
        Book.objects.filter(id=num).update(
            name=request.POST.get("name"),
            genre=request.POST.get("genre"),
            page=request.POST.get("page"),
            author=Author.objects.get(id=request.POST.get("author")),
        )
        return redirect("/books/")
    content = {
        "book": Book.objects.get(id=num),
        "authors": Author.objects.all()
    }
    return render(request, 'update_book.html', content)


def records(request):
    if request.method == 'POST':
        Record.objects.create(
            student=Student.objects.get(id=request.POST.get("student")),
            book=Book.objects.get(id=request.POST.get("book")),
            librarian=Librarian.objects.get(id=request.POST.get("librarian")),
            date_of_recieved=request.POST.get("date_of_recieved"),
            isreturned=request.POST.get("isreturned") == "on",
            date_of_returned=request.POST.get("date_of_returned")
        )
        return redirect("/records/")
    word = request.GET.get("search")
    result = Record.objects.all()
    if word:
        result = result.filter(student__name__contains=word)
    content = {
        "records": result,
        "students": Student.objects.all(),
        "books": Book.objects.all(),
        "librarians": Librarian.objects.all()
    }
    return render(request, 'records.html', content)


def delete_record(request, num):
    Record.objects.get(id=num).delete()
    return redirect("/records/")


def update_record(request, num):
    if request.method == 'POST':
        Record.objects.filter(id=num).update(
            student=Student.objects.get(id=request.POST.get("student")),
            book=Book.objects.get(id=request.POST.get("book")),
            librarian=Librarian.objects.get(id=request.POST.get("librarian")),
            date_of_recieved=request.POST.get("date_of_recieved"),
            isreturned=request.POST.get("alive") == "on",
            date_of_returned=request.POST.get("date_of_returned")
        )
        return redirect("/records/")
    content = {
        "record": Record.objects.get(id=num),
        "students": Student.objects.all(),
        "books": Book.objects.all(),
        "librarians": Librarian.objects.all()
    }
    return render(request, 'update_record.html', content)
