from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LibraryUser, ReadingList, BookReview
# Register your models here.
admin.site.register(LibraryUser, UserAdmin)
admin.site.register(ReadingList)
admin.site.register(BookReview)