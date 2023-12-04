from django.urls import path
from .views import (
    NoteListView,
    NoteCreateView,
    NoteDetailView,
    NoteUpdateView,
    NoteDeleteView,
    TopicListView,
    TopicDetailView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    login_page,
    login_view,
    logout_view,
)

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('login/view/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout'),
    path("note/", NoteListView.as_view(), name="note_list"),
    path("note/<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("note/create/", NoteCreateView.as_view(), name="note_create"),
    path("note/<int:pk>/update/", NoteUpdateView.as_view(), name="note_update"),
    path("note/<int:pk>/delete/", NoteDeleteView.as_view(), name="note_delete"),
    path("topic/", TopicListView.as_view(), name="topic_list"),
    path("topic/<int:pk>/", TopicDetailView.as_view(), name="topic_detail"),
    path("topic/create/", TopicCreateView.as_view(), name="topic_create"),
    path("topic/<int:pk>/update/", TopicUpdateView.as_view(), name="topic_update"),
    path("topic/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic_delete"),
]
