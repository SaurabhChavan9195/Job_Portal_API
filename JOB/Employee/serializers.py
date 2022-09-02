from dataclasses import fields
from pyexpat import model
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import User , Profile , Education ,Experience , project, resume, skill ,socialprofile, additionalInfo , Basicprofile
from django.utils.encoding import smart_str , force_bytes , DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode , urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':'password'},write_only = True)
    class Meta:
        model = User
        fields = ['id','email' , 'name','DOB' , 'age','gender', 'Phone_number','Country','state','city','password','password2']


    extra_kwargs ={'password':{'write_only':True}}

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError("Oops!! password and confirm password does not match")
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = User
        fields = ["email" , "password"]
    
    extra_kwargs ={'password':{'write_only':True}}



class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = resume
        fields = ['user_id','resume']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['user_id','Education','Name' , 'Percentage' , 'Passing_Year' ]

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Experience
        fields=['user_id','companay_name','location','joining_date','leaving_date',
        'currently_working','total_Experience','current_CTC','Notice_Period']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ['id' , 'user_id' , 'project_name' , 'project_desc' , 'start_date','end_date']


class skillSerializer(TaggitSerializer,serializers.ModelSerializer):
    # tags = TagListSerializerField()
    user_id = serializers.CharField(write_only = True    )
    class Meta:
        model = skill
        fields = ['user_id' ,'skills']


class SocialprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = socialprofile
        fields = ['user_id','Social_Profile','URL']


class BasicprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basicprofile
        fields = ['user_id' , 'name' , 'about','designation','location' , 'experiance','CTC','phone','email','notice_period']

class additionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = additionalInfo
        fields = ['user_id' , 'Marital_Status' , 'category','Differently_Abled' ,
        'Work_Permit_for_USA' ,'Permanent_Address' , 'Hometown' ,  'Pincode','Language']


class ProfileSerializer(serializers.ModelSerializer):
    resume = ResumeSerializer(many=True , read_only = True)
    Education = EducationSerializer(many=True , read_only = True)
    Experience = ExperienceSerializer(many=True , read_only = True)
    Project = ProjectSerializer (many = True  , read_only = True )
    skills = skillSerializer(many = True , read_only = True )
    Social_Profile = SocialprofileSerializer (many = True , read_only = True)
    Basic_Profile =BasicprofileSerializer (many = True , read_only = True )
    additionalInfo=additionalInfoSerializer(many = True , read_only = True)

    class Meta:
        model =Profile
        fields = ['user' , 'Profile_image' , 'background_image' , 'resume' , 'Education','Experience','Project','skills','Social_Profile','Basic_Profile','additionalInfo']



class ChangePasswordSerializer(serializers.Serializer):
   password = serializers.CharField(max_length=255 , style={'input_type':'password'}, write_only =True)
   password2 = serializers.CharField(max_length=255 , style={'input_type':'password'}, write_only =True)
   class Meta:
    Feilds = ["password" , "password2"]
   
   def validate(self, data):
    password = data.get('password')
    password2 = data.get('password2')
    user = self.context.get('user')
    if password != password2:
        raise serializers.ValidationError("password and confirm password doesn't match")
    user.set_password(password)
    user.save()
    return data

class PasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length = 255)
    class Meta:
        fileds = ['email']


    def validate(self, data):
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print("Encoded ID" , uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print("Password reset Token" , token)
            link = 'http://localhost:3000/api/employee/reset/'+ uid+'/'+token
            print("password Rest link" , link)
            
            # body = 'click following link to reset your Password ' + link
            # data = {
            #     'subject' : 'Reset Your Password',
            #     'body' : body,
            #     'to_email':user.email
            # }
            # Util.send_email(data)

        else:
            raise ValidationErr("You are not a registered user")
        return data

class PasswordRestSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255 , style={'input_type':'password'}, write_only =True)
    password2 = serializers.CharField(max_length=255 , style={'input_type':'password'}, write_only =True)
    class Meta:
        Feilds = ["password" , "password2"]
   
    def validate(self, data):
        try:
            password = data.get('password')
            password2 = data.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError("password and confirm password doesn't match")
            id = smart_str(urlsafe_base64_decode(uid))
            print("id" , id)
            user = User.objects.get(id =id)
            if not PasswordResetTokenGenerator().check_token(user , token):
                raise ValidationErr("Token is not Valid or Expired")
            user.set_password(password)
            user.save()
            return data
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user , token)
            raise ValidationErr("Token is not Valid or Expired")

# class LogoutSerializer(serializers.Serializer):
#     refresh = serializers.CharField()

#     def validate(self, data):
#         self.token = data["refresh"]
#         return data

#         def save(self , **kawargs):
#             try:
#                 RefreshToken(self.token).blacklist()

#             except: 
#                 raise ValidationErr("Token is not valid or expaired")
