from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register,Upload,Pdf
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from django.db.models import Q,QuerySet

from django.views.generic import TemplateView, ListView, CreateView
# Create your views here.



def index(request):
    if request.session.has_key('uid'):
        user=request.session['uid']
        return render(request, "index.html", {'use': user})
    else:
       return render(request,"index.html")


def register(request):
    return render(request,"register.html")


def signin(request):
    return render(request,"sign.html")

def entry(request):
    username = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('pass')
    if User.objects.filter(username=username).exists():
        messages.info(request,"username already exist")
        return redirect('register')
    elif User.objects.filter(email=email).exists():
        messages.info(request,"email exists")
        return redirect('register')
    else:

        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        messages.info(request,"user created")
        return redirect('/')
        #auth.login(request,user)
        #request.session['uid'] = request.POST.get('name')
        #form = BookForm(request.POST)
        #return render(request, 'bookupload.html', {'form': form})


def enter(request):
    if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                       auth.login(request,user)
                       request.session['uid']=request.POST.get('username')
                       return redirect('booklist')
            else:
                         messages.info(request,"failed")
                         return redirect("signin")

    else:
        return render(request,"sign.html")

def home(request):
     #new_upload = Upload.objects.all()
     return render(request,"main.html")


def logout(request):
    #del request.session['uid']
    auth.logout(request)
    return redirect('/')

#using models we can upload images
def upload(request):
   if request.method=='POST' and request.FILES["myfile"]:
       myfile = request.FILES['myfile']
       fs = FileSystemStorage()
       filename=fs.save(myfile.name, myfile)
       url=fs.url(filename)
       print(url)
       print(myfile.name)
       #data=Upload(
           #name=request.POST["name"],
           #file=url)
       #data.save()
       return render(request, "main.html")
   else:
      return redirect('/')

@login_required(login_url='signin/')
def upload_book(request):
    if request.method=='POST':
            a=request.session['uid']
            sname=Pdf(sname=a)
            form = BookForm(request.POST,request.FILES,instance=sname)
            if form.is_valid():
               title = request.POST.get('title')
               author = request.POST.get('author')
               pdf = request.POST.get('pdf')
               up = Pdf(title=title, author=author, pdf=pdf)
               messages.info(request,"Book added!!")
               form.save()
               return render(request,"bookupload.html", {'form':form})
            else:
              return HttpResponse('form is not valid')
    else:
        if request.session.has_key('uid'):

          form=BookForm()
          return render(request,'bookupload.html',{'form':form})
    return redirect('/')

@login_required(login_url='signin/')
def booklist(request):

    if request.GET.get('searcht'):
        search = request.GET.get('searcht').lower()
        book = Pdf.objects.all()
        if search != '' and search is not None:
            book=book.filter(Q(title=search) | Q(author=search)).distinct()
            return render(request, 'booklist.html', {'books': book})

    elif True:
        book = Pdf.objects.all()
        return render(request, 'booklist.html', {'books': book})



def delete(request,id):
    if request.method == 'POST':
       book=Pdf.objects.get(id=id)
       messages.info(request, "Book Deleted!!")
       book.delete()

       return redirect('booklist')


def update(request, id):
  book = Pdf.objects.get(id=id)
  if request.method=='POST':

     title = request.POST.get('title')
     author = request.POST.get('author')
     pdf = request.POST.get('pdf')
     form = BookForm(request.POST, request.FILES,instance=book)

     if form.is_valid():
         up = Pdf(title=title, author=author, pdf=pdf)
         messages.info(request, "Book Updated!!")
         form.save()
         return redirect('/booklist')

  form = BookForm(instance=book)
  return render(request, 'bookupload.html', {'form':form})


def weadd(request):
    add=Pdf.objects.filter(sname=request.session['uid'])

    return render(request,'weadd.html',{'use':add})









