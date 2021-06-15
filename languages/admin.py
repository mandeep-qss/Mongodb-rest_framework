from django.contrib import admin
from languages.models import Language, Paradigm, Programmer, Book, Author

# Register your models here.

admin.site.register(Paradigm)
admin.site.register(Language)
admin.site.register(Programmer)
admin.site.register(Book)
admin.site.register(Author)