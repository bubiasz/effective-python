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
)

urlpatterns = [
    path("note/", NoteListView.as_view(), name="note_list"),
    path("note/<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("note/create/", NoteCreateView.as_view(), name="note_create"),
    path("note/<int:pk>/update/", NoteUpdateView.as_view(), name="note_update"),
    path("note/<int:pk>/delete/", NoteDeleteView.as_view(), name="note_delete"),
    path("", TopicListView.as_view(), name="topic_list"),
    path("<int:pk>/", TopicDetailView.as_view(), name="topic_detail"),
    path("create/", TopicCreateView.as_view(), name="topic_create"),
    path("<int:pk>/update/", TopicUpdateView.as_view(), name="topic_update"),
    path("<int:pk>/delete/", TopicDeleteView.as_view(), name="topic_delete"),
]