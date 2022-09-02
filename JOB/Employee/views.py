
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import (LoginSerializer, ResumeSerializer,PasswordResetEmailSerializer, PasswordRestSerializer, BasicprofileSerializer,
ProfileSerializer,RegisterSerializer ,EducationSerializer , ExperienceSerializer , ProjectSerializer, SocialprofileSerializer,
skillSerializer ,additionalInfoSerializer,ChangePasswordSerializer)
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken , BlacklistedToken , OutstandingToken
from .models import Education, Experience, Profile,User, project , additionalInfo , resume , Basicprofile, skill, socialprofile
from rest_framework.permissions import IsAuthenticated

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegistrationView(APIView):
    def post(self , request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'msg':'Registration Successful' , }, status=status.HTTP_201_CREATED)
    

class LoginView(APIView):
    def post(self , request):
        serializer = LoginSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email , password=password)
        user1 = User.objects.filter(email=email)
        serializer2 = RegisterSerializer(user1 ,many=True)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'Token':token,'msg':'Login sucessfull',"user":serializer2.data} , status=status.HTTP_200_OK)
        else:
            return Response({'msg':'email or password is not valid !!'} , status=status.HTTP_404_NOT_FOUND)
   


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self , request ):
        serializer = RegisterSerializer(request.user)
        data = serializer.data.get("id")
        
        profile_view = Profile.objects.filter(user_id= data).all()
        serializer2 = ProfileSerializer(profile_view , many=True )

        Basic_View = Basicprofile.objects.filter(user_id = data).all()
        serializer8 = BasicprofileSerializer(Basic_View , many=True)

        Resume_View = resume.objects.filter(user_id = data).all()
        serializer7 = ResumeSerializer(Resume_View , many=True)

        education_view = Education.objects.filter(user_id = data).all()
        serializer3 = EducationSerializer(education_view , many=True)

        experinace_view = Experience.objects.filter(user_id = data).all()
        serializer4 = ExperienceSerializer(experinace_view , many = True)

        project_view = project.objects.filter(user_id = data).all()
        serializer5 = ProjectSerializer(project_view , many= True)

        skill_view = skill.objects.filter(user_id= data).all()
        serializer9 = skillSerializer(skill_view , many=True)

        Social_view= socialprofile.objects.filter(user_id=data).all()
        serializer10=SocialprofileSerializer(Social_view , many=True)

        additional_view = additionalInfo.objects.filter(user_id = data).all()
        serializer6 = additionalInfoSerializer(additional_view , many=True)

        return Response({"user":serializer2.data ,'Basic Deatils':serializer8.data,'Resume':serializer7.data, "Education": serializer3.data ,
        'Experinace':serializer4.data , 'projects':serializer5.data ,"skills":serializer9.data,'Social Links':serializer10.data, 'Additional Information' : serializer6.data}, status = 200)


class BasicprofileView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self ,request, format=None):
        serializer = BasicprofileSerializer( data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':" Basic Deatils created Successfully"} , status=status.HTTP_200_OK)

    def put(self , request , *args , **kwargs):
        user = RegisterSerializer(request.user)
        data = user.data.get("id")
        basic_obj=Basicprofile.objects.get(user_id=data)
        data=request.data
        basic_obj.name=data['name']
        basic_obj.about=data['about']
        basic_obj.designation=data['designation']
        basic_obj.location=data['location']
        basic_obj.experiance=data['experiance']
        basic_obj.CTC=data['CTC']
        basic_obj.phone=data['phone']
        basic_obj.email=data['email']
        basic_obj.notice_period=data['notice_period']

        basic_obj.save()
        serializer= SocialprofileSerializer(basic_obj)
        return Response({"msg": " Social Links Updated Successfully "} , status=200)


    def delete(self , request):
        user = RegisterSerializer(request.user)
        data = user.data.get("id")
        basic_obj = Basicprofile.objects.get(user_id = data)
        basic_obj.delete()
        return Response({"msg": " Resume Deleted  Successfully "} , status=200)


class ResumeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self , request):
        serializer = ResumeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg' : 'Resume Uploaded'} , status=200)
    
    def put(self , request , *args , **kwargs ):
        user = RegisterSerializer(request.user)
        data = user.data.get("id")
        print("sdhgfjsgf" , data)
        resume_obj = resume.objects.get(user_id = data)
        data = request.data
        resume_obj.resume = data["resume"]
        resume_obj.save()
        serializer = EducationSerializer(resume_obj)
        return Response({"msg": " Resume Updated Successfully "} , status=200)

    def delete(self , request):
        user = RegisterSerializer(request.user)
        data = user.data.get("id")
        resume_obj = resume.objects.get(user_id = data)
        resume_obj.delete()
        return Response({"msg": " Resume Deleted  Successfully "} , status=200)




class EductaionView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self , request , format=None):
        serializer= EducationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'msg':'Education Filled sucessfully'} , status=status.HTTP_200_OK)
        

    def put(self , request ,id = None ,  *args , **kwargs ):
        permission_classes = [IsAuthenticated]
        Edu_obj = Education.objects.get(edu_id = id)
        data = request.data
        Edu_obj.Education = data["Education"]
        Edu_obj.Name = data["Name"]
        Edu_obj.Percentage = data['Percentage']
        Edu_obj.Passing_Year = data["Passing_Year"]
        Edu_obj.save()
        serializer = EducationSerializer(Edu_obj)
        return Response({"msg": " Details Updated Successfully "} , status=200)

    def delete(self , request , id= None):
        permission_classes =[ IsAuthenticated]
        Edu_obj = Education.objects.get(edu_id = id)
        Edu_obj.delete()
        return Response({"msg": " Details Deleted  Successfully "} , status=200)


class ExperienceView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request ,format=None):
        serializer=ExperienceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({'msg':'Experience Filled sucessfully'} , status=status.HTTP_200_OK)
    

    def put(self , request ,id = None ,  *args , **kwargs ):
        Exp_obj = Experience.objects.get(id = id)
        data = request.data
        Exp_obj.companay_name = data["companay_name"]
        Exp_obj.location = data["location"]
        Exp_obj.joining_date = data['joining_date']
        Exp_obj.leaving_date = data["leaving_date"]
        Exp_obj.total_Experience = data["total_Experience"]
        Exp_obj.current_CTC = data["current_CTC"]
        Exp_obj.Notice_Period = data["Notice_Period"]
        Exp_obj.save()
        serializer = EducationSerializer(Exp_obj)
        return Response({"msg": " Details Updated Successfully "} , status=200)

    def delete(self , request , id= None):
        permission_classes =[ IsAuthenticated]
        Exp_obj = Experience.objects.get(id = id)
        Exp_obj.delete()
        return Response({"msg": " Details Deleted  Successfully "} , status=200)

class ProjectView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self , request , format=None):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = serializer.save()
        return Response({'msg':'Project details added successfull'} , status=status.HTTP_200_OK)


    def put(self , request ,id = None ,  *args , **kwargs ):
        permission_classes = [IsAuthenticated]
        proj_obj = project.objects.get(id = id)
        data = request.data
        proj_obj.project_name = data["project_name"]
        proj_obj.project_desc = data["project_desc"]
        proj_obj.start_date = data['start_date']
        proj_obj.end_date = data["end_date"]
        proj_obj.save()
        serializer = EducationSerializer(proj_obj)
        return Response({"msg": " Details Updated Successfully "} , status=200)

    def delete(self , request , id= None):
        permission_classes =[ IsAuthenticated]
        proj_obj = project.objects.get(id = id)
        proj_obj.delete()
        return Response({"msg": " Details Deleted  Successfully "} , status=200)

class SkillView(APIView):
    permission_classes = [IsAuthenticated]
    def post (self , request):
        serializer = skillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Skills added successfull'} , status=status.HTTP_200_OK)
      
class SocialProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def post (self , request):
        serializer= SocialprofileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Social Profile added successfull'} , status=status.HTTP_200_OK)

class additionalInfoView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self , request ):
        serializer = additionalInfoSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg': 'additional information Saved'} , status=200)
    
    def put(self , request ,id = None ,  *args , **kwargs ):
        obj = additionalInfo.objects.get(id = id)
        data = request.data
        obj.Marital_Status = data["Marital_Status"]
        obj.category = data["category"]
        obj.Differently_Abled = data['Differently_Abled']
        obj.Work_Permit_for_USA = data["Work_Permit_for_USA"]
        obj.Permanent_Address = data["Permanent_Address"]
        obj.Hometown = data["Hometown"]
        obj.Pincode = data["Pincode"]
        obj.Language = data["Language"]
        obj.save()
        serializer = EducationSerializer(obj)
        return Response({"msg": " Details Updated Successfully "} , status=200)

    def delete(self , request , id= None):
        obj = project.objects.get(id = id)
        obj.delete()
        return Response({"msg": " Details Deleted  Successfully "} , status=200)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request , format = None):
      serializer = ChangePasswordSerializer(data=request.data , context ={'user':request.user})
      serializer.is_valid(raise_exception=True)
      return Response({'msg':'password change successfully'}, status=status.HTTP_200_OK)
    
        
class PasswordRestEmail(APIView):
    def post (self , request):
        serializer = PasswordResetEmailSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Rest email sent successfully'} , status= status.HTTP_200_OK)
    

class restpasswordView(APIView):
    def post(self , request ,uid, token ):
        serializer = PasswordRestSerializer(data = request.data , context = {'uid' :uid ,'token' :token })
        print("UID checking ",serializer)
        serializer.is_valid(raise_exception=True)
        return Response({"msg" : "Password reset Successfully"} , status=status.HTTP_200_OK)
       


# class logout(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self , request):
#         tokens = OutstandingToken.objects.filter(user_id=request.user.id) 
#         for token in tokens:
#             t, _ = BlacklistedToken.objects.get_or_create(token=token)

#         return Response({"msg":"LOGOUT "},status=status.HTTP_205_RESET_CONTENT)
        
# class LogoutAPIView(generics.GenericAPIView):
#     serializer_class = LogoutSerializer

#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"msg":"Logout"},status=status.HTTP_204_NO_CONTENT)