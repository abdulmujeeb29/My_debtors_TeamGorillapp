from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response 
from accounts.serializer import StudentSerializer
from . models import *
from django.http import HttpResponse
from .permissions import IsAuthorOrReadOnly
# Create your views here.


def landing_page(request):
    return render (request,'index.html')

def parentsignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        surname =request.POST['surname']
        email =request.POST['email']
        phone_number = request.POST['phone_number']
        contact_address = request.POST['contact_address']
        occupation  =request.POST['occupation']
        school_of_children = request.POST['school_of_children']
        number_of_children = request.POST['number_of_children']
        password1 =request.POST['password1']
        password2 =request.POST['password2']


        my_user = User.objects.create_user(username=username,email=email,password=password1)
        my_user.surname = surname
        my_user.phone_number=  phone_number
        my_user.contact_address = contact_address
        my_user.occupation =occupation
        my_user.school_of_children =school_of_children


        my_user.save();
        return redirect('parentlogin')


        # if password1== password2 :
        #     if User.objects.filter(email=email).exists():
        #         messages.info(request,'Email already registered')
        #         return redirect('parentregister')

        #     elif len(password1) < 5 :
        #         messages.info(request,'Password must exceed 5 characters ')
        #         return redirect ('parentregister')


        #     else :
        #         my_user.save();
        #         return redirect('parentlogin')

        # else:
        #     messages.info(request,'Psswords does not match ')
        #     return redirect('parentregister')


        
    return render(request,'parentregister.html')



def parentlogin(request):
    if request.method == 'POST':
        #email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']

        my_user = auth.authenticate(username=username,password=password1)

        if my_user is not None:
            auth.login(request,my_user)
            return redirect('parent')

        else :
            messages.info(request,'Invalid Credentials')
            return redirect('parentlogin')

    return render(request,'parentlogin.html')




def signout(request):
    auth.logout(request)
    return redirect ('/')


def schoolregister(request):
    if request.method == 'POST':
        username =request.POST['username']
        school_address =request.POST['school_address']
        year_founded =request.POST['year_founded']
        date_of_accreditation =request.POST['date_of_accreditation']
        Accreditation_number =request.POST['Accreditation_number']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']


        # if password1 == password2 :
        #     if User.objects.filter(email=email).exists():
        #         messages.info(request,'Email already registered ')
        #         return redirect('schoolregister')

        #     else :
        user2 =User.objects.create_user(username=username,email=email,password=password1)
        user2.save();
        return redirect('schoollogin')
                

    return render(request,'schoolregister.html')


        
def schoollogin(request):
    
    if request.method== 'POST':
        username= request.POST['username']
        password = request.POST['password']

        user2 = auth.authenticate(username=username ,password=password)

        if user2 is not None:
            auth.login(request,user2)
            return redirect('school')

        else:
            messages.info(request,'invalid credentials ')
            return redirect('schoollogin')


    return render(request,'schoollogin.html')

def parent(request):
    student =Student.objects.all()
    return render(request,'parent.html',{'student':student})


def school(request):
    return render(request,'school.html')


def forgot(request):
    return render(request,'forgot.html')


#api implementation to post new data about debtor

@api_view(['GET' ])
def student_debtors(request):
    students=Student.objects.all()
    serializer = StudentSerializer(students ,many=True)
    return Response (serializer.data)

@api_view(['POST'])
def post_debtors(request):
    students=Student.objects.all()
    serializer= StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    else:
        return Response(serializer.errors)



@api_view(['GET', 'DELETE'])
#@permission_classes([IsAuthorOrReadOnly])
def student_particular(request,pk):
    students=Student.objects.get(id=pk)

    if request.method == 'GET':
        serializer = StudentSerializer(students)
        return Response(serializer.data)


    elif request.method == 'DELETE' :
        students.delete()
        return Response('Succesfully deleted')


def about_us(request):
    return render(request,'aboutus.html')



def contact_us(request):
    return render(request,'contactus.html')

def faq(request):
    return render(request,'faq.html')

def addstudent(request):
    # student = Student(school_id = request.POST['school_id'],Name=request.POST['Name'],Class=request.POST['Class'],debt_owed =request.POST['debt_owed'])
    # student.save();

    #return redirect('addstudent')
    return render(request,'addstudent.html')