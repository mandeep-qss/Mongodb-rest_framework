from django.urls import path , include
from languages import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages',views.LanguageView)
router.register('paradigms',views.ParadigmView)
router.register('programmers',views.ProgrammerView)
router.register('authors',views.AuthorView)
router.register('books',views.BookView)

urlpatterns = [
    path('',include(router.urls))
]