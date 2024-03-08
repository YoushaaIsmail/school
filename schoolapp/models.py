from django.db import models
from Account.models import Parent,Account
from django_resized import ResizedImageField

def upload_to(inst,filename):
      base_path="profile"
      safe_filename=str(filename)
      final_path=os.path.join(base_path,safe_filename)
      return final_path

class School(models.Model):

   name =models.CharField(max_length=100)
   Location=models.CharField(max_length=200)
   Rating=models.FloatField()
   Des=models.CharField(max_length=1000)
   Installment=models.FloatField()

class SchoolAwareModel(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE)

class Class(SchoolAwareModel):
    level=models.FloatField()
    number=models.FloatField()

class Teacher(SchoolAwareModel):
            account=models.OneToOneField(Account,on_delete=models.CASCADE,
            related_name='teacher', null=True, blank=True)

class Supervisor(SchoolAwareModel):
            account=models.OneToOneField(Account,on_delete=models.CASCADE,
            related_name='supervisor', null=True, blank=True)

class Employee(SchoolAwareModel):
            account=models.OneToOneField(Account,on_delete=models.CASCADE,
            related_name='employee', null=True, blank=True)   

class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    Birthday=models.DateTimeField()
    photo=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    hisparent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    hisclass=models.ForeignKey(Class,on_delete=models.CASCADE)
    supervisor=models.ForeignKey(Supervisor,on_delete=models.CASCADE)

class Course(models.Model):
    name=models.CharField(max_length=30)
    Time_Quiz=models.DateTimeField()
    Time_final=models.DateTimeField()
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    hisclass=models.ForeignKey(Class,on_delete=models.CASCADE)

class CourseDate(models.Model):
    listt1=(
       ('friday', 'Friday'),
       ('saturday', 'Saturday'),
       ('sunday', 'Sunday'),
      ('monday', 'Monday'),
      ('tuesday','Tuesday'),
      ('wednesday','Wednesday'),
      ('thursday','Thursday')
)
    Day=models.CharField(max_length=15,choices=listt1)
    time=models.TimeField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

class Homework(models.Model):
    Des=models.CharField(max_length=150)
    Course_ID=models.ForeignKey(Course,on_delete=models.CASCADE)
    Teacher_ID=models.ForeignKey(Teacher,on_delete=models.CASCADE)

class StudentINCourse(models.Model):
    state=models.BooleanField(default=True)
    Date=models.DateTimeField()
    Student_ID=models.ForeignKey(Student,on_delete=models.CASCADE)
    Course_ID=models.ForeignKey(Course,on_delete=models.CASCADE)

class mark(models.Model):
    mark_Quiz=models.FloatField()
    mark_final=models.FloatField()
    mark_Works=models.FloatField()
    student_Mark=models.ForeignKey(Student,on_delete=models.CASCADE) 
    course_Mark=models.ForeignKey(Course,on_delete=models.CASCADE)    

class Order_meeting(models.Model):
    listt2=(
       ('acceptable', 'Acceptable'),
       ('rejected', 'Rejected'),
       ('waiting', 'Waiting')

)
    state=models.CharField(max_length=15,choices=listt2)
    Date=models.DateTimeField()

class order_join(models.Model):
    listt3=(
       ('acceptable', 'Acceptable'),
       ('rejected', 'Rejected'),
       ('waiting', 'Waiting')

)              
    listt4=(
       ('first', 'First'),
       ('second', 'Second'),
       ('third', 'Third'),
       ('third', 'Third'),
        ('fourth', 'Fourth'),
        ('fifth', 'Fifth'),
        ('sixth', 'Sixth')


) 
    state=models.CharField(max_length=15,choices=listt3)
    StudentName=models.CharField(max_length=50)
    His_level=models.CharField(max_length=15,choices=listt4)
    Is_pay=models.BooleanField(default=False)
    Img1=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    Img2=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    Img3=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    Img4=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    parentjoin=models.ForeignKey(Parent,on_delete=models.CASCADE)    
    Schooljoin=models.ForeignKey(School,on_delete=models.CASCADE)
    
class Activites(models.Model):
    listt5=(
       ('healthy', 'Healthy'),
       ('sport', 'Sport'),
       ('intellectual', 'Intellectual'),
       ('general', 'General')


) 
    Type=models.CharField(max_length=15,choices=listt5)
    level=models.CharField(max_length=15)
    Des=models.CharField(max_length=100)
    Student_active=models.ForeignKey(Student,on_delete=models.CASCADE)
    
class Notifications(SchoolAwareModel):
    Des=models.CharField(max_length=100)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    
 