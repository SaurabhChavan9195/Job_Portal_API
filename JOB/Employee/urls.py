import imp
from django.contrib import admin
from django.urls import path 
from Employee.views import (RegistrationView , LoginView , ProfileView , ResumeView,EductaionView , ExperienceView , BasicprofileView,
ProjectView , SkillView , additionalInfoView,ChangePasswordView ,PasswordRestEmail , restpasswordView,SocialProfileView)
from django.conf import settings
from django.conf.urls.static import static

 



urlpatterns = [
    path('register/', RegistrationView.as_view() , name="Register"),
    path('login/', LoginView.as_view() , name="Login"),
    path('profile/', ProfileView.as_view() , name="Profile"),


    path('basicprofile/', BasicprofileView.as_view() , name="Profile"),
    path('resume/' , ResumeView.as_view() , name ="resume_upload"),
    
    path('education/', EductaionView.as_view() , name="education"),
    path('education/<int:id>', EductaionView.as_view() , name="education"),

    path('experiance/', ExperienceView.as_view() , name="experiance"),
    path('experiance/<int:id>', ExperienceView.as_view() , name="experiance"),
    
    path('projects/', ProjectView.as_view() , name="projects"),
    path('projects/<int:id>', ProjectView.as_view() , name="projects"),

    path('skills/', SkillView.as_view() , name="skills"),

    path('sociallinks/', SocialProfileView.as_view() , name="sociallinks"),

    path('additionalinfo/', additionalInfoView.as_view() , name="additionalInfo"),
    path('additionalinfo/<int:id>', additionalInfoView.as_view() , name="additionalInfo"),

    path('changepassword/', ChangePasswordView.as_view() , name="changepassword"),
    path('password-Rest-Email/' , PasswordRestEmail.as_view() , name = "password-Rest-Email"),
    path('password-rest/<uid>/<token>/' ,restpasswordView.as_view()  , name = "password-rest"),
    # path('logout/', LogoutAPIView.as_view(), name='logout'),
    
] 
if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
