from django.contrib import admin
from Employee.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Education, Experience, Profile, project, resume, skill , additionalInfo ,Basicprofile, socialprofile
# Register your models here.

class UserModelAdmin(BaseUserAdmin):
  # The fields to be used in displaying the User model.
  # These override the definitions on the base UserModelAdmin
  # that reference specific fields on auth.User.
  list_display = ('id', 'email', 'name', 'is_admin')
  list_filter = ('is_admin',)
  fieldsets = (
      ('User Credentials', {'fields': ('email', 'password')}),
      ('Personal info', {'fields': ('name', 'DOB', 'age' , 'gender' ,  'Phone_number' , 'Country' ,'state', 'city' )}),
      ('Permissions', {'fields': ('is_admin',)}),
  )
  # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
  # overrides get_fieldsets to use this attribute when creating a user.
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'name', 'password1', 'password2'),
      }),
  )
  search_fields = ('email',)
  ordering = ('email','id')
  filter_horizontal = ()


class MyModelAdmin(admin.ModelAdmin):
    list_display = ['tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(Profile)
admin.site.register(Basicprofile)
admin.site.register(resume)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(project)
admin.site.register(skill)
admin.site.register(socialprofile)
admin.site.register(additionalInfo)
