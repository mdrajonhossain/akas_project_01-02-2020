from django.db import models
from django.contrib.auth.models import User


# Create your models here.
userr_type = (
    ('teacher', 'teacher'),
    ('Student', 'Student')
)

class Logintype(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Logintypee")
    user_type = models.CharField(choices=userr_type, default='Student', max_length=30)

    def __str__(self):
        return self.user_type



class studentformsave(models.Model):
    applicant_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=30)
    dateofbirth = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    departsubject = models.CharField(max_length=30)

    def __str__(self):
        return self.applicant_name

class Stdsubjectentry(models.Model):
    subjectnameentry = models.CharField(max_length=30)

    def __str__(self):
        return self.subjectnameentry


# completes
class stdsubjectlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stdsubjectlista")
    stdsubjectentry = models.ForeignKey(Stdsubjectentry, on_delete=models.CASCADE, related_name="stdsubjectlistaa")
    subject_code = models.CharField(max_length=30)

    def __str__(self):
        return self.subject_code


# completes
class stdclassrouting(models.Model):
    stdsubjectentry = models.ForeignKey(Stdsubjectentry, on_delete=models.CASCADE, related_name="stdclassrouting")
    date = models.DateField(max_length=100)
    time = models.TimeField(max_length=100)



class stdresult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stdresult")
    stdsubjectentry = models.ForeignKey(Stdsubjectentry, on_delete=models.CASCADE, related_name="stdresult")
    result_point = models.CharField(max_length=30)
    grate = models.CharField(max_length=30)

    def __str__(self):
        return self.grate

class stdaccountingsite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stdaccountingsite")
    selary_month = models.CharField(max_length=30)
    monthof_amount = models.CharField(max_length=30)

    def __str__(self):
        return self.selary_month



class stdnotice(models.Model):
    noticehead_name = models.CharField(max_length=30)
    description_notice = models.CharField(max_length=3000)

    def __str__(self):
        return self.noticehead_name


class teacherform(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacherforma")
    teacher_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=30)
    dateofbirth = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    departsubject = models.CharField(max_length=30)
    usertype = models.CharField(max_length=30)

    def __str__(self):
        return self.teacher_name