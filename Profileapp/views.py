from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login
from Profileapp.forms import *
from Profileapp.models import *
import pandas as pd


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # user = authenticate(request, username=username, password=password)
            if username == "admin" and password == "123":
                # login(request,user)
                return redirect('dashboard')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = {{form.password1}}
            confirmPassword = {{form.password2}}
            if password == confirmPassword:
                form.save()
                # สร้าง user ในระบบ authen ของ Django ---
                username = {{form.username}}
                email = {{form.email}}
                user = User.objects.create_user(username, email, password)
                user.first_name = {{form.username}}
                user.is_staff = False
                user.save()
                # -------
            else:
                form.add_error(None, "password is not same")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def dashboard(request):
    return render(request, 'dashboard.html')


def home2(request):
    return render(request, 'home2.html')


def restaurantsList(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        context = Contents.objects.filter(cont_id=id)
        data = {'contents': context}
        return render(request, 'showContent.html', data)
    contents = Contents.objects.all().order_by('cat_id')
    data = {'contents': contents}
    return render(request, 'CRUD/restaurantsList.html', data)


def hotelList(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        context = Contents.objects.filter(cont_id=id)
        data = {'contents': context}
        return render(request, 'showContent.html', data)
    contents = Contents.objects.all().order_by('cat_id')
    data = {'contents': contents}
    return render(request, 'CRUD/hotelList.html', data)


def addContent(request):
    if request.method == 'POST':
        form = AddForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home2')
        else:
            context = {'form': form}
            return render(request, 'CRUD/addContent.html', context)
    else:
        form = AddForm()
        context = {'form': form}
        return render(request, 'CRUD/addContent.html', context)


def updateContent(request, cont_id):
    content = get_object_or_404(Contents, cont_id=cont_id)
    form = AddForm(data=request.POST or None, instance=content)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('home2')
        else:
            context = {'form': form}
            return render(request, 'CRUD/updateContent.html')
    else:
        context = {'form': form}
        return render(request, 'CRUD/updateContent.html', context)

def deleteContent(request, cont_id) :
    content = get_object_or_404(Contents, cont_id=cont_id)
    form = AddForm(data=request.POST or None, instance=content)
    if request.method == 'POST':
        content.delete()
        return redirect('home2')
    else:
        form.deleteForm()
        context = {'form': form}
        return render(request, 'CRUD/deleteContent.html', context)


def recipeList(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        context = Contents.objects.filter(cont_id=id)
        data = {'contents': context}
        return render(request, 'showContent.html', data)
    contents = Contents.objects.all().order_by('cat_id')
    data = {'contents': contents}
    return render(request, 'CRUD/recipeList.html', data)


def showhotel(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        context = Contents.objects.filter(cont_id=id)
        data = {'contents': context}
        return render(request, 'showContent.html', data)
    contents = Contents.objects.all().order_by('cat_id')
    data = {'contents': contents}
    return render(request, 'showhotel.html', data)


def showrestaurants(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        context = Contents.objects.filter(cont_id=id)
        data = {'contents': context}
        return render(request, 'showContent.html', data)
    contents = Contents.objects.all().order_by('cat_id')
    data = {'contents': contents}
    return render(request, 'showrestaurants.html', data)


def showrecipe(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        context = Contents.objects.filter(cont_id=id)
        data = {'contents': context}
        return render(request, 'showContent.html', data)
    contents = Contents.objects.all().order_by('cat_id')
    data = {'contents': contents}
    return render(request, 'showrecipe.html', data)


def showContent(request):
    return render(request, 'showContent.html')

def categoriesList(request):
    if request.method == 'POST':
        cat_id = request.POST.get('cat_id')
        context = Categories.objects.order_by(cat_id=cat_id)
        data = {'categories': context}
        return render(request, 'showContent.html', data)
    contents = Categories.objects.all().order_by('cat_id')
    data = {'categories': contents}
    return render(request, 'CRUD/categoriesList.html', data)

def addCategory(request):
    if request.method == 'POST':
        form = categoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categoriesList')
        else:
            context = {'form': form}
            return render(request, 'CRUD/addCategory.html', context)
    else:
        form = categoryForm()
        context = {'form': form}
        return render(request, 'CRUD/addCategory.html', context)

def updateCategory(request, cat_id):
    category = get_object_or_404(Categories, cat_id=cat_id)
    form = categoryForm(data=request.POST or None, instance=category)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('categoriesList')
        else:
            context = {'form': form}
            return render(request, 'CRUD/updateCategory.html')
    else:
        context = {'form': form}
        return render(request, 'CRUD/updateCategory.html', context)

    # content = get_object_or_404(Contents, cont_id=cont_id)
    # form = AddForm(data=request.POST or None, instance=content)
    # if request.method == 'POST':
    #
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home2')
    #     else:
    #         context = {'form': form}
    #         return render(request, 'CRUD/updateContent.html')
    # else:
    #     context = {'form': form}
    #     return render(request, 'CRUD/updateContent.html', context)

def deleteCategory(request, cat_id) :
    category = get_object_or_404(Categories, cat_id=cat_id)
    form = categoryForm(data=request.POST or None, instance=category)
    if request.method == 'POST':
        category.delete()
        return redirect('categoriesList')
    else:
        form.deleteForm()
        context = {'form': form}
        return render(request, 'CRUD/deleteCategory.html', context)

def contentChart(request):
    content_categories = Contents.objects.values('cont_date').annotate(count=Count('cont_id')).order_by('cont_date')
    labels = [category['cont_date'] for category in content_categories]
    # data = [category['count'] for category in content_categories]

    return render(request,'home2.html',{'labels':labels})
