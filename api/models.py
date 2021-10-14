from functools import total_ordering
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=400)
    completed = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
#------------------------------------Profile----------------------------------------------------------------------------#
class Degree (models.Model):
    degree_choice = (
        ('ปริญญาตรี' , 'ปริญญาตรี'),
        ('ปริญญาโท', 'ปริญญาโท'),
        ('ปริญญาเอก', 'ปริญญาเอก')
    )
    degree = models.CharField(max_length=50, blank=True, null=True, choices=degree_choice)
    faculty = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    province = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    study_date = models.DateField(blank=True , default=None)
    graduate = models.DateField(blank=True , default=None)
    gpa = models.FloatField()
    honors = models.CharField(max_length=100)
    use_choice = (
        ('ใช้','ใช้'),
        ('ไม่ใช้','ไม่ใช้')
    )
class Faculty(models.Model):
    faculty = models.CharField(max_length=100)

class Profile (models.Model):
    username = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    id_Position = models.CharField(max_length=20)
    title_choice = (
        ('นาย','นาย'),
        ('นาง','นาง'),
        ('นางสาว','นางสาว'),
    )
    title_name = models.CharField(max_length=10, blank=True, null=True, choices=title_choice)
    name_th = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)
    personal_choice = (
        ('พนักงานมหาวิทยาลัย','พนักงานมหาวิทยาลัย'),
        ('ลูกจ้างชั่วคราว','ลูกจ้างชั่วคราว')
    )
    personal_type = models.CharField(max_length=255, blank=True, null=True, choices=personal_choice)
    line_of_work_choice = (
        ('วิชาการ','วิชาการ'),
        ('สนับสนุน','สนับสนุน')
    )
    line_of_work = models.CharField(max_length=100, blank=True, null=True, choices=line_of_work_choice)
    position_choice = (
        ('อาจารย์','อาจารย์'),
        ('เจ้าหน้าที่บริหารงานทั้วไป','เจ้าหน้าที่บริหารงานทั้วไป'),
        ('บุคลากร','บุคลากร'),
        ('นักวิชาการศึกษา','นักวิชาการศึกษา'),
        ('นักวิเคราะห์นโยบายและเเผน','นักวิเคราะห์นโยบายและเเผน'),
        ('นักประชาสัมพันธ์','นักประชาสัมพันธ์'),
        ('นักวิทยาศาสตร์','นักวิทยาศาสตร์'),
        ('นักวิชาการโสตทัศนศึกษา','นักวิชาการโสตทัศนศึกษา'),
        ('นักวิชาการคอมพิวเตอร์','นักวิชาการคอมพิวเตอร์'),
        ('ครู','ครู')
    )
    position = models.CharField(max_length=100, blank=True, null=True, choices=position_choice)
    academic_choice = (
        ('ศาสตราจารย์','ศาสตราจารย์'),
        ('รองศาสตราจารย์','รองศาสตราจารย์'),
        ('ผู้ช่วยศาสตราจารย์','ผู้ช่วยศาสตราจารย์'),
        ('เชี่ยวชาญ','เชี่ยวชาญ'),
        ('ชำนาญการพิเศษ','ชำนาญการพิเศษ'),
        ('ชำนาญการ','ชำนาญการ')
    )
    academic_position = models.CharField(max_length=100, blank=True, null=True, choices=academic_choice)
    director_choice = (
        ('คณบดี','คณบดี'),
        ('รองคณบดี','รองคณบดี'),
        ('ผู้ช่วยคณบดี','ผู้ช่วยคณบดี'),
        ('ประธานหลักสูตร','ประธานหลักสูตร'),
        ('หัวหน้างาน','หัวหน้างาน')
    )
    director_position = models.CharField(max_length=100, blank=True, null=True, choices=director_choice)
    start_work_date = models.DateField(blank=True , default=None)
    placement_date = models.DateField(blank=True , default=None)
    status_job = models.DateField(blank=True , default=None)
    date_birth = models.DateField(blank=True , default=None)
    nationality = models.CharField(max_length=100)

    religion_choice = (
        ('พุทธ','พุทธ'),
        ('คริสต์','คริสต์'),
        ('อิสลาม','อิสลาม'),
        ('ยิว','ยิว'),
        ('ซิกข์','ซิกข์'),
        ('บาไฮ','บาไฮ'),
        ('โซโรอัสเตอร์','โซโรอัสเตอร์'),
        ('พราหมณ์-ฮินดู','พราหมณ์-ฮินดู'),
        ('เชน','เชน'),
        ('ไม่มีศาสนา','ไม่มีศาสนา')
    )
    religion_con = models.CharField(max_length=100, blank=True, null=True, choices=religion_choice)

    phone = models.CharField(max_length=10)
    email_UP = models.EmailField(max_length=255)
    email_private = models.EmailField(max_length=255)
    address = models.TextField()
    id_degree = models.ForeignKey(Degree , on_delete=models.CASCADE)
    faculty_id = models.CharField(max_length=100)

class Profile_faculty(models.Model):
    profile_id = models.OneToOneField(Profile , on_delete=models.CASCADE)
    id_faculty = models.OneToOneField(Faculty , on_delete=models.CASCADE)

class User_Degree(models.Model):
    degree_id = models.ForeignKey(Degree , on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile , on_delete=models.CASCADE)


class Approval(models.Model):
    date_request = models.DateField(blank=True , default=None)
    date_approval = models.DateField(blank=True , default=None)
    document = models.CharField(max_length=500)
    publicity = models.CharField(max_length=500)

class Approval_name(models.Model):
    A_name = models.OneToOneField(Profile , on_delete=models.CASCADE)

#-----------------------***Manpower***----------------------------------------------------------------------------------------------#

class Manpower_Academic(models.Model):
    year = models.CharField(max_length=4)

class Manpower_support(models.Model):
    year = models.CharField(max_length=4)

class Manpower_AC(models.Model):
    year_MS = models.OneToOneField(Profile , on_delete=models.CASCADE)

class Manpower_SC(models.Model):
    year_MS = models.OneToOneField(Profile , on_delete=models.CASCADE)

#-----------------------Document----------------------------------------------------------------------------------------------#

class Document(models.Model):
    pdf_id = models.FileField(null=True, blank=True,default='default.pdf',upload_to='uploads/%d/%m/%Y/')
    author = models.CharField(max_length=100)
    date_request = models.DateField(blank=True , default=None)
    date_evaluate = models.DateField(blank=True , default=None)
    date_expire = models.DateField(blank=True , default=None)
    level_evaluate_tech = models.CharField(max_length=100)
    level_evaluate_document = models.CharField(max_length=100)
    no_evaluate = models.IntegerField()

#---------------------------------------------------------------------------------------------------------------------------#
#------------------------------------Event----------------------------------------------------------------------------#
class Event(models.Model):
    faculty = models.CharField(max_length=100)
    total = models.IntegerField()
    training_people = models.IntegerField()
    training_time = models.IntegerField()
    seminars_people = models.IntegerField()
    seminars_time = models.IntegerField()
    events_people = models.IntegerField()
    events_time = models.IntegerField()

class Year_Event(models.Model):
    year = models.CharField(max_length=4)

class Event_connect(models.Model):
    id_event = models.OneToOneField(Event , on_delete=models.CASCADE)
    id_year = models.OneToOneField(Year_Event , on_delete=models.CASCADE)

#-----------------------Budget----------------------------------------------------------------------------------------------#

class Budget(models.Model):
    year = models.CharField(max_length=4)
    initial = models.IntegerField()
    total = models.IntegerField()
    balance = models.IntegerField()


class Budget_con(models.Model):
    id_budget = models.OneToOneField(Budget , on_delete=models.CASCADE)
    id_faculty = models.OneToOneField(Faculty , on_delete=models.CASCADE)

#--------------------------Study Leave-------------------------------------------------------------------------------------------#

class Study_leave(models.Model):
    name = models.CharField(max_length=100)
    begin = models.DateField(blank=True , default=None)
    end = models.DateField(blank=True , default=None)
    total_time = models.CharField(max_length=100)
    type = models.CharField(max_length=60)
    extend_time = models.CharField(max_length=50)
    extend_begin = models.DateField(blank=True , default=None)
    extend_end = models.DateField(blank=True , default=None)
    work = models.DateField(blank=True , default=None)
    approval = models.DateField(blank=True , default=None)
    requesting = models.DateField(blank=True , default=None)

#------------------------Human_resource---------------------------------------------------------------------------------------------#

class Human_resource(models.Model):
    master_PDF = models.FileField(null=True, blank=True,default='default.pdf',upload_to='uploads/%d/%m/%Y/')

class Year_HR(models.Model):
    year = models.CharField(max_length=9)

class Human_resource_con(models.Model):
    id_master_PDF = models.OneToOneField(Human_resource , on_delete=models.CASCADE)
    id_year = models.OneToOneField(Year_HR , on_delete=models.CASCADE)

#--------------------------Report---------------------------------------------------------------------------------------------#

class Report(models.Model):
    master_PDF = models.FileField(null=True, blank=True,default='default.pdf',upload_to='uploads/%d/%m/%Y/')

class Year_R(models.Model):
    year = models.CharField(max_length=9)

class Report_con(models.Model):
    id_master_PDF = models.OneToOneField(Report , on_delete=models.CASCADE)
    id_year = models.OneToOneField(Year_R , on_delete=models.CASCADE)

#--------------------------Pending---------------------------------------------------------------------------------------------#

class Pending(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    data_request = models.DateField(blank=True , default=None)
    data_request_evaluate = models.DateField(blank=True , default=None)
    data_evaluate = models.DateField(blank=True , default=None)
    data_full_term = models.DateField(blank=True , default=None)

    request_choice = (
        ('ศาสตราจารย์','ศาสตราจารย์'),
        ('รองศาสตราจารย์','รองศาสตราจารย์'),
        ('ผู้ช่วยศาสตราจารย์','ผู้ช่วยศาสตราจารย์'),
        ('เชี่ยวชาญ','เชี่ยวชาญ'),
        ('ชำนาญการพิเศษ','ชำนาญการพิเศษ'),
        ('ชำนาญการ','ชำนาญการ')
    )
    request_position = models.CharField(max_length=100, blank=True, null=True, choices=request_choice)
    
    status_pending = models.CharField(max_length=100)

#--------------------------Outstanding---------------------------------------------------------------------------------------------#

class Outstanding_Academic(models.Model):
    number = models.CharField(max_length=1)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

class Year_Out(models.Model):
    year = models.CharField(max_length=4)

class Outstanding_Service(models.Model):
    number = models.CharField(max_length=1)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

class Year_con(models.Model):
    id_year = models.OneToOneField(Year_Out , on_delete=models.CASCADE)
    id_oa = models.OneToOneField(Outstanding_Academic , on_delete=models.CASCADE)
    id_os = models.OneToOneField(Outstanding_Service , on_delete=models.CASCADE)

#---------------------------Approval------------------------------------------------------------------------------------------#





 

