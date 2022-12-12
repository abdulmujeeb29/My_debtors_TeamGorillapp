from django.db import models

# Create your models here.


class School(models.Model):
    #School_id
    Name = models.CharField(max_length=1000)
    Address = models.CharField(max_length=1000)
    Phone_number =models.IntegerField()
    
    def __str__(self) -> str:
        return self.Name

class Guardian(models.Model):
    #Student_id = 
    Name = models.CharField(max_length=1000)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    #Guardian_id

    def __str__(self) -> str:
        return self.Name

Genders = (
    ('1', 'MALE'),
    ('2','FEMALE'),
)

class Student(models.Model):
    #School_id = models.ForeignKey(School,on_delete=models.CASCADE,blank=True)
    #Guardian_id = models.ForeignKey(Guardian,on_delete =models.CASCADE,blank=True)
    school_id = models.CharField(max_length=100,blank=True)
    Name = models.CharField(max_length=100)
    Class = models.CharField(max_length=100)
    Gender = models.CharField( max_length=10, choices=Genders,default=1)
    debt_owed = models.IntegerField()
    #studentid 

    def __str__(self) -> str:
        return self.Name

status = (
    ('1', 'PAID'),
    ('2','UNPAID'),
)




class Post(models.Model):
    School_id =models.ForeignKey(School, on_delete=models.CASCADE)
    Student = models.CharField(max_length=1000)
    Status = models.CharField(max_length=10,choices=status, default='1')
    created_at =models.DateTimeField()
    updated_at =models.DateTimeField()

    

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE,blank=True)
    body = models.CharField(max_length=1000000)
    created_at =models.DateTimeField()
    updated_at =models.DateTimeField()


made_payment = (
    ('yes', 'YES'),
    ('no', 'NO'),
)

class Contend(models.Model):
    Guardian_id =models.ForeignKey(Guardian,on_delete=models.CASCADE,blank=True)
    #Post
    reason_to_contend = models.CharField(max_length=100000)
    made_payment = models.CharField(max_length=10 ,choices=made_payment,default='yes')
    evidence_of_payment = models.FileField(upload_to="")
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()



