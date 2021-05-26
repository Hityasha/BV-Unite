from django.contrib import admin
from .models import user,active,verify,contact,anouncement,Profile,Post,Message
# Register your models here.
class useradmin(admin.ModelAdmin):
    list_display=("urole","uname","uid","uemail","upswd","utime")
    list_filter=['utime']
admin.site.register(user,useradmin)

class activeadmin(admin.ModelAdmin):
    list_display=("aid","atime")
    list_filter=['atime']
admin.site.register(active,activeadmin)

class verifyadmin(admin.ModelAdmin):
    list_display=("vrole","vid","vname")
    
admin.site.register(verify,verifyadmin)

class contactadmin(admin.ModelAdmin):
    list_display=("cid","cname","cemail","cmsg","ctime")
    list_filter=['ctime']
admin.site.register(contact,contactadmin)

class anouncementadmin(admin.ModelAdmin):
    list_display=("anc_uid","anc_dsc","anc_time","anc_img")
    list_filter=['anc_time']
admin.site.register(anouncement,anouncementadmin)

class Profileadmin(admin.ModelAdmin):
    list_display=("Pr_id","Pr_name","Pr_title","Pr_about","Pr_img")
admin.site.register(Profile,Profileadmin)



admin.site.register(Post)

admin.site.register(Message)


