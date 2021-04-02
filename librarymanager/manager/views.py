from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.template import RequestContext
from manager.forms import AddStudent, AddLibrarian
from manager.models import Book, User, Category

from manager.decorators import student_required, librarian_required

def base(request):
    num_books = Book.objects.all().count()


    context = {
        'num_books': num_books,
    }
    return render(request, 'base.html', context=context)


class SignUp(TemplateView):
    template_name = 'signup.html'


class AddLibrarian(CreateView):
    model = User
    form_class = AddLibrarian
    template_name = 'add_librarian.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'librarian'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class AddStudent(CreateView):
    model = User
    form_class = AddStudent
    template_name = 'add_student.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


@method_decorator([login_required, librarian_required], name='dispatch')
class AddBook(CreateView):
    model = Book
    template_name = 'add_book.html'
    fields = '__all__'
    success_url = reverse_lazy('add_book')

@method_decorator([login_required, librarian_required], name='dispatch')
class AddCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = ['name']
    success_url = reverse_lazy('add_category')

@method_decorator([login_required], name='dispatch')
class ViewBook(DetailView):
    model = Book
    template_name = 'view_book.html'
    context_object_name = 'book'

@method_decorator([login_required, librarian_required], name='dispatch')
class EditBook(UpdateView):
    model = Book
    template_name = 'edit_book.html'
    fields = '__all__'

@method_decorator([login_required, librarian_required], name='dispatch')
class DeleteBook(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    context_object_name = 'book'
    success_url = reverse_lazy('list_books')

@method_decorator([login_required, student_required], name='dispatch')
def search_book(request):
    return render(request, 'search_book.html')

@method_decorator([login_required], name='dispatch')
class ListBooks(ListView):
    model = Book
    template_name = 'list_books.html'
    context_object_name = 'books'
    queryset = Book.objects.filter(loaned__exact='available')
   

@method_decorator([login_required, student_required], name='dispatch')
class LoanBook(UpdateView):
    model = Book
    template_name = 'loan_book.html'
    fields = ['loaned']
    success_url = reverse_lazy ('list_books')

@method_decorator([login_required, student_required], name='dispatch')
class ListLoaned(ListView):
    model = Book
    template_name = 'list_loaned.html'
    context_object_name = 'books'
    

def get_user(request):
    user = request.session['user']
    return user


@method_decorator([login_required], name='dispatch')
class SearchByAuthor(ListView):
    model = Book
    template_name = 'search_author.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('author')
        return Book.objects.filter(
            Q(author__icontains=query)
        )
    


@method_decorator([login_required], name='dispatch')
class SearchByTitle(ListView):
    model = Book
    template_name = 'search_title.html'
    context_object_name = 'books'


    def get_queryset(self):
        query = self.request.GET.get('title')
        return Book.objects.filter(
            Q(title__icontains=query)
        )

