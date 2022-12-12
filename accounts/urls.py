from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_page),
    path('schoolregister',views.schoolregister,name='schoolregister'),
    path('schoollogin',views.schoollogin,name='schoollogin'),
    path('parentregister',views.parentsignup,name='parentsignup'),
    path('parentlogin',views.parentlogin,name='parentlogin'),
    path('parent',views.parent,name='parent'),
    path('school',views.school,name='school'),
    path('debtors',views.student_debtors,name='student_debtors'),
    path('post',views.post_debtors),
    path('debtors/<int:pk>',views.student_particular),
    path('aboutus',views.about_us,name='about_us'),
    path('contactus',views.contact_us,name='contact_us'),
    path('faq',views.faq,name='faq'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('forgot',views.forgot,name='forgot'),
    path('create',views.create,name='create'),
    path('testimonial',views.testimonial,name='testimonial'),

]

