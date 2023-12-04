from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Note, Topic

# Create your views here.
def login_page(request):
    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('note_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials. Please try again.'})
        
def logout_view(request):
    logout(request)
    return redirect('note_list')

class NoteListView(ListView):
    model = Note

class NoteDetailView(DetailView):
    model = Note
    
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['name', 'text', "topic"]
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)

class NoteUpdateView(UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['name', 'text', "topic"]
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self.get_object()  # Pobranie informacji o temacie
        notes = Note.objects.filter(topic=topic)  # Pobranie notatek związanych z tematem
        context['notes'] = notes  # Dodanie notatek do kontekstu szablonu
        return context

class TopicCreateView(CreateView):
    model = Topic
    fields = ['name', 'parent', 'public']
    success_url = reverse_lazy('topic_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TopicUpdateView(UpdateView):
    model = Topic
    fields = ['name', 'parent', 'public']
    success_url = reverse_lazy('topic_list')

class TopicDeleteView(DeleteView):
    model = Topic
    success_url = reverse_lazy('topic_list')
