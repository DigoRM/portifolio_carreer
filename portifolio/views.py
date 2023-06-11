from multiprocessing import context
from tkinter import Frame
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from portifolio.forms import ProjectForm, UpdateForm
from .models import Course, Framework, ProgrammingLanguage, Project, Category, Update
from django.db.models import Count
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models import Sum
from .forms import CreateUserForm, CustomerForm


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect.')
    context={}
    return render(request, 'registration/login.html', context)    

def logoutUser(request):
    logout(request)
    return redirect('login')       


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')

                messages.success(request, "Welcome " + username + "!")
                
                
                return redirect('login')
        
        
        context = {
            'form':form,
                   }
        
        return render(request, 'registration/register.html', context)

def search(request):
    query = request.GET.get('query', '')
    projects = Project.objects.filter(Q(name__icontains = query) | Q(description__icontains=query) | Q(functions__icontains = query))
    categories = Category.objects.filter(Q(name__icontains = query) | Q(description__icontains=query))
    languages = ProgrammingLanguage.objects.filter(Q(name__icontains = query))
    frameworks = Framework.objects.filter(Q(name__icontains = query))

    context =  {'categories':categories, 'projects':projects , 'query':query,'frameworks':frameworks,'languages':languages}
    
    return render(request, 'search.html', context)

    

@login_required(login_url='login')
def profile(request):
    user = request.user
    customer = user.customer
    form = CustomerForm(instance=customer)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            
    context = {'form':form,
               'customer':customer,
               }
    return render(request, 'registration/profile.html', context)

def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    customer = user.customer
    programming_languages = ProgrammingLanguage.objects.all()
    frameworks = Framework.objects.all()
    categories = Category.objects.all()

    language_projects = []
    for language in programming_languages:
        projects = Project.objects.filter(programming_languages__name=language.name)
        courses = Course.objects.filter(programming_languages__name=language.name)
        course_count = courses.count()
        course_sum = courses.aggregate(Sum('courses'))['courses__sum'] or 0
        project_count = projects.count()
        project_sum = projects.aggregate(Sum('complexity'))['complexity__sum'] or 0
        score=course_sum + project_sum
        frameworks = Framework.objects.filter(language__name=language.name)
        framework_count = frameworks.count()
        language_projects.append({
            'name': language.name,'project_count':project_count, 'project_sum': project_sum, 'course_count': course_count,'course_sum':course_sum, 'score':score, 'framework_count': framework_count  # Wrap the count in a list
            })
        

    framework_projects = []
    for framework in frameworks:
        projects = Project.objects.filter(frameworks__name=framework.name)
        courses = Course.objects.filter(frameworks__name=framework.name)
        course_count = courses.count()
        course_sum = courses.aggregate(Sum('courses'))['courses__sum'] or 0
        project_count = projects.count()
        project_sum = projects.aggregate(Sum('complexity'))['complexity__sum'] or 0
        score=course_sum + project_sum
        framework_projects.append({'name': framework.name, 'project_count': project_count, 'course_count': course_count,'project_sum': project_sum, 'course_sum':course_sum, 'score':score})
        

    category_projects = []
    for category in categories:
        projects = Project.objects.filter(category__name=category.name)
        courses = Course.objects.filter(category__name=category.name)
        course_count = courses.count()
        course_sum = courses.aggregate(Sum('courses'))['courses__sum'] or 0
        project_count = projects.count()
        project_sum = projects.aggregate(Sum('complexity'))['complexity__sum'] or 0
        score=course_sum + project_sum
        frameworks = Framework.objects.filter(category__name=category.name)
        framework_count = frameworks.count()
        category_projects.append({'id':category.id,  'name': category.name, 'project_count': project_count, 'course_count': course_count, 'project_sum': project_sum, 'course_sum':course_sum, 'score':score, 'framework_count': framework_count})
        



    context = {
        'customer': customer,
        'user': user,
        'programming_languages': programming_languages,
        'language_projects': language_projects,
        'framework_projects':framework_projects,
        'category_projects':category_projects,
    }
    return render(request, 'registration/user_profile.html', context)

def framework_progress_language(request, language):
    frameworks = Framework.objects.filter(language__name=language)

    framework_projects = []
    for framework in frameworks:
        projects = Project.objects.filter(frameworks__name=framework.name)
        courses = Course.objects.filter(frameworks__name=framework.name)
        course_count = courses.count()
        course_sum = courses.aggregate(Sum('courses'))['courses__sum'] or 0
        project_count = projects.count()
        project_sum = projects.aggregate(Sum('complexity'))['complexity__sum'] or 0
        score=course_sum + project_sum
        framework_projects.append({'name': framework.name, 'project_count': project_count, 'course_count': course_count,'project_sum': project_sum, 'course_sum':course_sum, 'score':score})
    print(framework_projects)


    context = {
        'framework_projects':framework_projects,
    }
    return render(request, 'framework_progress_language.html', context)


def framework_progress_category2(request, pk):
    category = get_object_or_404(Category, pk=pk)
    frameworks = Framework.objects.filter(category__id=pk)

    framework_projects_category = []
    for framework in frameworks:
        projects = Project.objects.filter(frameworks__name=framework.name)
        courses = Course.objects.filter(frameworks__name=framework.name)
        course_count = courses.count()
        course_sum = courses.aggregate(Sum('courses'))['courses__sum'] or 0
        project_count = projects.count()
        project_sum = projects.aggregate(Sum('complexity'))['complexity__sum'] or 0
        score = course_sum + project_sum
        framework_projects_category.append({'name': framework.name, 'project_count': project_count, 'course_count': course_count, 'project_sum': project_sum, 'course_sum': course_sum, 'score': score})

    context = {
        'framework_projects_category': framework_projects_category,
        'category': category,
    }

    return render(request, 'framework_progress_category2.html', context)



def framework_progress_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    frameworks = Framework.objects.filter(category__id=pk)

    framework_projects = []
    for framework in frameworks:
        projects = Project.objects.filter(frameworks__name=framework.name)
        courses = Course.objects.filter(frameworks__name=framework.name)
        course_count = courses.count()
        course_sum = courses.aggregate(Sum('courses'))['courses__sum'] or 0
        project_count = projects.count()
        project_sum = projects.aggregate(Sum('complexity'))['complexity__sum'] or 0
        score=course_sum + project_sum
        framework_projects.append({'name': framework.name, 'project_count': project_count, 'course_count': course_count,'project_sum': project_sum, 'course_sum':course_sum, 'score':score})
    print(category)


    context = {
        'framework_projects':framework_projects,
        'category':category,
    },
    return render(request, 'framework_progress_category.html', context)


@login_required(login_url='login')
def new_update(request, pk):
    project = get_object_or_404(Project,pk=pk)

    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES)

        if form.is_valid():
            update = form.save(commit=False)
            update.project = project
            update.save()
            project.updates = update
            return redirect('project_detail',pk)

        else:
            print(form.errors)
    else:
        form = UpdateForm()
            
    context = {
        'form':form,'project':project,
               }
    return render(request, 'new_update.html', context)

def home(request):
    projects = Project.objects.annotate(num_updates=Count('updates')).order_by('-added_at')
    languages = ProgrammingLanguage.objects.all()
    frameworks = Framework.objects.all()
    categories = Category.objects.all()

    context = {'projects':projects,'languages':languages,'frameworks':frameworks,'categories':categories}

        
    return render(request, 'home2.html', context )

def categories(request):
    categories = Category.objects.annotate(num_projects=Count('projects')).order_by('-num_projects')

    context={'categories':categories}
    return render(request, 'categories.html', context)

def category_projects(request, pk):
    category = get_object_or_404(Category, pk=pk)
    projects = Project.objects.filter(category=category).annotate(num_updates=Count('updates')).order_by('-added_at')

    context = {'category':category,'projects':projects}
    return render(request, 'category_projects.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    category = project.category
    updates = Update.objects.filter(project=project)

    context = {'project':project,'updates':updates,'category':category}
    return render(request, 'project_detail.html', context)

def projects_language(request, language):
    projects = Project.objects.filter(programming_languages__name=language)

    context = {'projects':projects, 'language': language}
    return render(request, 'projects_language.html', context)

def projects_framework(request, framework):
    projects = Project.objects.filter(frameworks__name=framework)

    context = {'projects':projects, 'framework': framework}
    return render(request, 'projects_framework.html', context)

# Courses
def courses(request):
    courses = Course.objects.all().order_by('-date_created')

    languages = ProgrammingLanguage.objects.all()
    frameworks = Framework.objects.all()
    categories = Category.objects.all()

    context = {'courses':courses,'categories':categories,'frameworks':frameworks,'languages':languages}
        
    return render(request, 'courses.html', context )

def category_courses(request, pk):
    category = get_object_or_404(Category, pk=pk)
    courses = Course.objects.filter(category=category).order_by('-date_created')

    context = {'category':category,'courses':courses}
    return render(request, 'category_courses.html', context)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    context = {'course':course,}
    return render(request, 'course_detail.html', context)

def courses_language(request, language):
    courses = Course.objects.filter(programming_languages__name=language).order_by('-date_created')

    context = {'courses':courses, 'language': language}
    return render(request, 'courses_language.html', context)

def courses_framework(request, framework):
    courses = Course.objects.filter(frameworks__name=framework).order_by('-date_created')

    context = {'courses':courses, 'framework': framework}
    return render(request, 'courses_framework.html', context)

