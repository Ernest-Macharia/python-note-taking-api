from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('notes-list/', views.NoteList),
    path('notes-create/', views.NoteCreate),
    path('notes-list/<str:pk>/', views.NoteListOne),
    path('notes-update/<str:pk>/', views.NoteUpdate),
    path('notes-delete/<str:pk>/', views.NoteDelete),
]