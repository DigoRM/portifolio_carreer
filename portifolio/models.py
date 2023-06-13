from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    projects = models.ManyToManyField('Project', related_name='project_categories', blank=True)
    name = models.CharField(max_length=155)
    description = models.TextField()
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
    	return self.name

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

class Framework(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True , related_name='framework_category')
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE , related_name='framework_language',blank=True, null=True)
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

class Project(models.Model):

    BASIC = 1
    REGULAR =2
    HIGH = 4
    PROFESSIONAL = 10
    
    CHOICE = (
        (BASIC, 'Basic'),
        (REGULAR, 'Regular'),
        (HIGH, 'High'),
        (PROFESSIONAL, 'Professional')
    )

    category = models.ManyToManyField(Category, related_name='project')
    updates = models.ForeignKey('Update', related_name='project_updates', on_delete=models.SET_NULL, null=True, blank=True)
    programming_languages = models.ManyToManyField(ProgrammingLanguage, related_name='programming_languages',blank=True)
    frameworks = models.ManyToManyField(Framework, related_name='frameworks',blank=True)
    name = models.CharField(max_length=155)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)

    functions = models.TextField(blank=True, null=True)
    possible_upgrades = models.TextField(blank=True, null=True)
    complexity = models.PositiveSmallIntegerField(choices=CHOICE,blank=True, null=True)

    created_at = models.DateField()
    video = models.FileField(upload_to='video_project/', blank=True, null=True)
    image = models.ImageField(upload_to='image_project/', blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Update(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='update')
    title = models.CharField(max_length=155)
    description = models.TextField()
    image = models.ImageField(upload_to='image_update/', blank=True, null=True)
    video = models.FileField(upload_to='video_update/', blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=255,  null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True) 
    role = models.CharField(max_length=255, null=True, blank=True) 
    courses = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True, blank=True)
    soft_skills = models.TextField(null=True, blank=True) 
    hard_skills = models.TextField(null=True,blank=True)
    interests = models.TextField(null=True, blank=True) 
    profile_pic = models.ImageField(upload_to ='profile_pic', null=True, blank=True)
    date_created = models.DateTimeField(null=True)

    def __str__(self):
    	return self.name

class Course(models.Model):

    frameworks = models.ManyToManyField(Framework, related_name='course_frameworks',blank=True)
    programming_languages = models.ManyToManyField(ProgrammingLanguage, related_name='course_languages',blank=True)
    category = models.ManyToManyField(Category, related_name='course_category')
    name = models.CharField(max_length=255,  null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True) 
    company_icon = models.FileField(upload_to ='company_icon', null=True, blank=True)
    description = models.TextField(null=True, blank=True) 
    courses = models.IntegerField(blank=True, null=True)
    specialization = models.BooleanField(default=False)
    course_link = models.URLField(null=True, blank=True) 
    licence_link = models.URLField(null=True, blank=True) 
    licence_pic = models.FileField(upload_to ='licence_pic', null=True, blank=True)
    completed_at = models.DateField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
    	return self.name