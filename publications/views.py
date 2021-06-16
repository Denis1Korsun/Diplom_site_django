from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import *
from .forms import RegistrationUserForm, AutorizationUserForm, CommunicationWhithCompanyForm
from .utils import *


class PublicationsHome(DataMixin, ListView):
    model = Publications
    template_name = 'publications/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Портал спорта')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Publications.objects.filter(is_published=True)


def about(request):
    return render(request, 'publications/about.html', {'menu': menu, 'title': 'О сайте'})


def about_authors(request):
    posts_authors = Author.objects.all()

    context = {
        'posts_authors': posts_authors,
        'menu': menu,
        'title': 'Авторы редакции',
    }

    return render(request, 'publications/info_about_authors.html', context=context)


def show_article_about_author(request, author_id):
    article_about_author = get_object_or_404(Author, id=author_id)

    context = {
        'article_about_author': article_about_author,
        'menu': menu,
        'title': article_about_author.summary,

    }

    return render(request, 'publications/article_about_author.html', context=context)


def about_athlete(request):
    posts_athlete = Athlete.objects.all()

    context = {
        'posts_athlete': posts_athlete,
        'menu': menu,
        'title': 'Спортсмены',
    }

    return render(request, 'publications/info_athlete.html', context=context)


class CommunicationFormView(DataMixin, FormView):
    form_class = CommunicationWhithCompanyForm
    template_name = 'publications/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Связь с редакцией')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def contact(request):
    return HttpResponse("Наши контакты")


def shop(request):
    return HttpResponse("Магазин товаров")


class ShowPost(DataMixin, DetailView):
    model = Publications
    template_name = 'publications/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class PublicationsCategory(DataMixin, ListView):
    model = Publications
    template_name = 'publications/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Publications.objects.filter(category__slug=self.kwargs['rubric_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Рубрика: ' + str(context['posts'][0].category),
                                      rubric_selected=context['posts'][0].category_id)
        context = dict(list(context.items()) + list(c_def.items()))
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegistrationUserForm
    template_name = 'publications/registration_user.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация пользователя')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AutorizationUserForm
    template_name = 'publications/login_user.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Вход в личный кабинет')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
