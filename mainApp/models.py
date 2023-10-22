from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    course = models.PositiveSmallIntegerField()
    number_of_book = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


gender = [('Male', 'Male'), ('Female', 'Female')]


class Author(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(choices=gender, max_length=6)
    date_of_birth = models.DateField(verbose_name="Date of birth: ")
    number_of_book = models.PositiveSmallIntegerField()
    alive = models.BooleanField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    page = models.PositiveSmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


times = (
    ("06:00 dan 12:00 gacha", "06:00 dan 12:00 gacha"),
    ("12:00 dan 18:00 gacha", "12:00 dan 18:00 gacha"),
    ("18:00 dan 23:59 gacha", "18:00 dan 23:59 gacha")
)


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    working_time = models.CharField(max_length=255, choices=times)

    def __str__(self):
        return self.name


class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    date_of_recieved = models.DateField()
    isreturned = models.BooleanField(default=False)
    date_of_returned = models.DateField()

    def __str__(self):
        return f"{self.student}- {self.book}"
