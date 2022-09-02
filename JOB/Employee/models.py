

from tkinter import CASCADE
from taggit.managers import TaggableManager
from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
from django.db.models.signals import post_save

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, name , DOB,age,gender, Phone_number,Country,state,city,password=None , password2=None):
        """
        Creates and saves a User with the given email, name , DOB , age ,gender , and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),name= name,DOB=DOB ,age=age ,gender=gender ,
        Phone_number=Phone_number, Country=Country , state=state , city=city)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, DOB , age , gender , Phone_number,Country,state,city,password=None):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(email,password=password,name = name ,DOB=DOB ,age=age ,gender=gender , Phone_number=Phone_number, Country=Country , state=state , city=city )
        user.is_admin = True
        user.save(using=self._db)
        return user 

# custome user model 
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email ',max_length=255,unique=True,)
    name = models.CharField( max_length=50)
    DOB = models.DateField(max_length=8)
    age = models.BigIntegerField()
    gender = models.CharField(max_length=10) 
    Phone_number = models.CharField(max_length = 13, default=None)   
    Country = models.CharField(max_length=255 , default=None)
    state = models.CharField(max_length=255 , default=None)
    city = models.CharField(max_length=255 , default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    crated_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name' , 'DOB' , 'age' , 'gender' , 'Phone_number' , 'Country' ,'state', 'city']

    # def __str__(self):
        # return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Profile(models.Model):
    #id = models.AutoField(primary_key=True)
    user= models.OneToOneField( User, on_delete=models.CASCADE)
    Profile_image = models.ImageField(upload_to ='media/' , default= 'media/default.jpg')
    background_image = models.ImageField(upload_to ='media/' , default= 'media/default.jpg')

    def __str__(self):
        return self.user.email 
    
def create_profile(sender, **kwargs):                                                                    
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)




class resume(models.Model):
    user_id = models.OneToOneField(User , on_delete=models.CASCADE )
    resume = models.FileField(upload_to='resume/' , max_length=250)

    def __str__(self):
        return self.user_id.email

class Education(models.Model):
    EDUCATION_CHOICE = (
        ( 'SSC','Secondary School Certificate'),
        ('HSC','Higher Secondary School Certificate' ),
        ('Graduation','Graduation'),
    )
    edu_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    Education = models.CharField(max_length=255, choices= EDUCATION_CHOICE)
    Name = models.CharField(max_length=255)
    Percentage = models.PositiveIntegerField()
    Passing_Year = models.DateField(max_length=6)
    
    def __str__(self):
        return self.user_id.email

class Experience(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)   
    id=models.AutoField(primary_key=True)  
    companay_name=models.CharField(max_length=255)
    location= models.CharField(max_length=255)
    joining_date=models.DateField()
    leaving_date=models.DateField()
    currently_working=models.DateField(auto_now=True)
    total_Experience=models.IntegerField()
    current_CTC=models.IntegerField()
    Notice_Period=models.IntegerField()

    def __str__(self):
        return self.user_id.email

class project(models.Model):
    user_id = models.ForeignKey(User ,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    project_desc = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.user_id.email 

class skill(models.Model):
    # SKILLLS_CHOICES = (
    #     ('PYTHON', 'Backend'),
    #     ('JAVA', 'Backend'),
    #     ('HTML5','Frontend'),
    #     ('CSS3','Frontend'),
    #     ('JAVASCRIPT','Frontend'),
    #     ('ANGULAR','Framework'),
    #     ('DJANGO','Framework'),
    #     ('FLASK','Framework')
    # )
    id = models.AutoField(primary_key=True)
    user_id = models.ManyToManyField(User)
    skills = models.CharField(max_length=20)
    
    tags = TaggableManager()





class Basicprofile(models.Model):
    user_id = models.OneToOneField(User , on_delete=models.CASCADE)
    name = models.CharField(User , max_length=255)
    about = models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    location = models.CharField(Experience , max_length=255)
    experiance = models.IntegerField(Experience)
    CTC =models.IntegerField(Experience)
    phone = models.IntegerField( User)
    email = models.EmailField(User)
    notice_period = models.IntegerField()

    def __str__(self):
        return self.user_id.email


class socialprofile(models.Model):
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    Social_Profile = models.CharField(max_length=250)
    URL = models.URLField(max_length=255)

    def __str__(self):
        return self.user_id.email 


class additionalInfo(models.Model):
    MARITAL_STATUS_CHOICES = (
        ('Single' , 'Single/Unmarried'),
        ('Married' , 'Married'),
        ('Divorced' , 'Divorced'),
        ('Seprated' , 'Seprated'),
        ('Other' , 'Other')
    )
    CATEGORIES_CHOICES = (
        ("Genral" , "Genral"),
        ("SC" , "Scheduled Cast"),
        ("ST" , "Scheduled Tribe"),
        ('OBC' , "Other backword"),
        ('Other' , 'Other')
    )
    LANGUAGE_CHOICES = (
        ('Hindi' , 'Hindi'),
        ('English' , 'English'),
        ('Marathi' , 'Marathi'),
    )
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User , on_delete=models.CASCADE)
    Marital_Status = models.CharField(max_length=255 , choices=MARITAL_STATUS_CHOICES)
    category = models.CharField(max_length=255 , choices=CATEGORIES_CHOICES)
    Differently_Abled= models.BooleanField(default=False)
    Work_Permit_for_USA = models.BooleanField(default=False)
    Permanent_Address = models.CharField(max_length=255)
    Hometown = models.CharField(max_length=255)
    Pincode = models.PositiveIntegerField()
    Language = models.CharField(max_length=15 , choices=LANGUAGE_CHOICES )


    def __str__(self):
        return self.user_id.email