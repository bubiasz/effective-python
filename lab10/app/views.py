from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Note, Topic

# Create your views here.
class NoteListView(ListView):
    model = Note

class NoteDetailView(DetailView):
    model = Note
    
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['name', 'text']
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdateView(UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['name', 'text']
    success_url = reverse_lazy('note_list')

    def test_func(self):
        return self.request.user == self.get_object().user

class NoteDeleteView(UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note_list')

    def test_func(self):
        return self.request.user == self.get_object().user or self.request.user.is_superuser

class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'

class TopicDetailView(DetailView):
    model = Topic
    success_url = reverse_lazy('topic_list')

class TopicCreateView(CreateView):
    model = Topic
    fields = ['name', 'parent', 'public']
    success_url = reverse_lazy('topic_list')

class TopicUpdateView(UpdateView):
    model = Topic
    fields = ['name', 'parent', 'public']
    success_url = reverse_lazy('topic_list')

class TopicDeleteView(DeleteView):
    model = Topic
    success_url = reverse_lazy('topic_list')
