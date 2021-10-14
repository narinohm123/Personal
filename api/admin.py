from django.contrib import admin
from .models import *

admin.site.register(Degree)
admin.site.register(Faculty)
admin.site.register(Profile)
admin.site.register(Profile_faculty)
admin.site.register(User_Degree)

admin.site.register(Manpower_Academic)
admin.site.register(Manpower_support)
admin.site.register(Manpower_AC)
admin.site.register(Manpower_SC)

admin.site.register(Document)

admin.site.register(Event)
admin.site.register(Year_Event)
admin.site.register(Event_connect)

admin.site.register(Budget)
admin.site.register(Budget_con)

admin.site.register(Study_leave)

admin.site.register(Human_resource)
admin.site.register(Year_HR)
admin.site.register(Human_resource_con)

admin.site.register(Report)
admin.site.register(Year_R)
admin.site.register(Report_con)

admin.site.register(Pending)

admin.site.register(Outstanding_Academic)
admin.site.register(Year_Out)
admin.site.register(Outstanding_Service)
admin.site.register(Year_con)

admin.site.register(Approval)
admin.site.register(Approval_name)





# Register your models here.
