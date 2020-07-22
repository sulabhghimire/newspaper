from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles_list.html'

class ArticleUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Article
    fields =  ['title', 'body', ]
    template_name = 'article_update.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author==self.request.user

class ArticleDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author==self.request.user

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    fields = ['title', 'body',]
    template_name = 'article_create.html'
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Create your views here.
