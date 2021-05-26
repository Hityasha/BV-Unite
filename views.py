from django.shortcuts import render,redirect
from .models import user,active,verify,contact,anouncement,Profile,Post,Message
from django.http import HttpResponse,HttpResponseBadRequest
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.urls import reverse

# Create your views here.
def first(request):
    return render(request,'first.html')

def first_page(request):
    return render(request,'first.html')
  
def home(request):
    if request.session.has_key('id') and (request.method!="POST"):
         obj=request.session['id']
         data2=user.objects.get(uid=obj)
         data4=Profile.objects.get(Pr_id=obj)
         data=anouncement.objects.all().order_by("-id")[:3]
         post = Post.objects.all().order_by("-id")
         data6=user.objects.all()
         print("if")
         if data2.urole=="Teacher" or data2.urole=="Alumini":
            result2=Profile.objects.exclude(Pr_id=obj).order_by("Pr_name")
            result1=user.objects.exclude(uid=obj).order_by("uname")
            return render(request,"home (2).html",{"msg":data,"msg1":data2,"msg2":data4,"post":post,"All_user":result1,"All_profile":result2,"msg6":data6})
         else:
            result2=Profile.objects.exclude(Pr_id=obj).order_by("Pr_name")
            result1=user.objects.exclude(uid=obj).order_by("uname")
            return render(request,"home(1).html",{"msg":data,"msg1":data2,"msg2":data4,"post":post,"All_user":result1,"All_profile":result2,"msg6":data6})
    elif (request.method=="POST"):
        print("else")
        ptext=request.POST["pmsg"]
        obj=request.session['id']
        data2=user.objects.get(uid=obj)
        data4=Profile.objects.get(Pr_id=obj)
        data=anouncement.objects.all().order_by("-id")[:3]
        data6=user.objects.all()
        post = Post.objects.all().order_by("-id")
        if 'ppost' in request.FILES:
            file_data = request.FILES["ppost"]
            fs2=FileSystemStorage()
            ppost=fs2.url(fs2.save(file_data.name,file_data))
            print(data4.Pr_id)
            pid=Profile.objects.filter(Pr_id=obj).only("Pr_id")
            Post.objects.create(P_author=pid.first(),P_content=ptext,P_img=ppost,P_name=data2.uname,P_name_img=data4.Pr_img)
        else:
            pid=Profile.objects.filter(Pr_id=obj).only("Pr_id")
            Post.objects.create(P_author=pid.first(),P_content=ptext,P_name=data2.uname,P_name_img=data4.Pr_img) 
        if data2.urole=="Teacher" or data2.urole=="Alumini":
            result2=Profile.objects.exclude(Pr_id=obj).order_by("Pr_name")
            result1=user.objects.exclude(uid=obj).order_by("uname")
            return render(request,"home (2).html",{"msg":data,"msg1":data2,"msg2":data4,"post":post,"All_user":result1,"All_profile":result2,"msg6":data6})
        else:
            result2=Profile.objects.exclude(Pr_id=obj).order_by("Pr_name")
            result1=user.objects.exclude(uid=obj).order_by("uname")
            return render(request,"home(1).html",{"msg":data,"msg1":data2,"msg2":data4,"post":post,"All_user":result1,"All_profile":result2,"msg6":data6})

def login(request):
    if request.method=="POST":
        arole=request.POST["member_level"]
        aid=request.POST["id"]
        apswd=request.POST["pass"]
        if user.objects.filter(uid=aid,upswd=apswd,urole=arole).exists():
            if active.objects.filter(aid=aid).exists():
                data2=user.objects.get(uid=aid,upswd=apswd)
                request.session['id']=aid
                if arole=="Teacher" or arole=="Alumini":
                    messages.success(request,"Login Successfully")
                    data=anouncement.objects.all().order_by("-id")[:3]
                    print(data)
                    data4=Profile.objects.get(Pr_id=aid)
                    data2=user.objects.get(uid=aid,upswd=apswd)
                    data6=user.objects.all()
                    post = Post.objects.all().order_by("-id")
                    result2=Profile.objects.exclude(Pr_id=aid).order_by("Pr_name")
                    result1=user.objects.exclude(uid=aid).order_by("uname")
                    return render(request,"home (2).html",{"msg":data,"msg1":data2,"msg2":data4,"post":post,"All_user":result1,"All_profile":result2,"msg6":data6})
                else:
                    messages.success(request,"Login Successfully")
                    data=anouncement.objects.all().order_by("-id")[:3]
                    data4=Profile.objects.get(Pr_id=aid)
                    data2=user.objects.get(uid=aid,upswd=apswd)
                    post = Post.objects.all().order_by("-id")
                    data6=user.objects.all()
                    result2=Profile.objects.exclude(Pr_id=aid).order_by("Pr_name")
                    result1=user.objects.exclude(uid=aid).order_by("uname")
                    return render(request,"home(1).html",{"msg":data,"msg1":data2,"msg2":data4,"post":post,"All_user":result1,"All_profile":result2,"msg6":data6})
            else:
                data2=user.objects.get(uid=aid,upswd=apswd)
                print(data2)
                data1=active(aid=aid)
                print(data1)
                data1.save()
                request.session['id']=aid
                if arole=="Teacher" or arole=="Alumini":
                    messages.success(request,"Login Successfully")
                    data=anouncement.objects.all().order_by("-id")[:3]
                    data6=user.objects.all()
                    data4=Profile.objects.get(Pr_id=aid)
                    data2=user.objects.get(uid=aid,upswd=apswd)
                    post = Post.objects.all().order_by("-id")
                    result2=Profile.objects.exclude(Pr_id=aid).order_by("Pr_name")
                    result1=user.objects.exclude(uid=aid).order_by("uname")
                    return render(request,"home (2).html",{"msg":data,"msg1":data2,"msg2":data4,"post":post,"All_user":result1,"All_profile":result2,"msg6":data6})
                else:
                    messages.success(request,"Login Successfully")
                    data=anouncement.objects.all().order_by("-id")[:3]
                    data6=user.objects.all()
                    data4=Profile.objects.get(Pr_id=aid)
                    data2=user.objects.get(uid=aid,upswd=apswd)
                    post = Post.objects.all().order_by("-id")
                    result2=Profile.objects.exclude(Pr_id=aid).order_by("Pr_name")
                    result1=user.objects.exclude(uid=aid).order_by("uname")
                    return render(request,"home(1).html",{"msg":data,"msg1":data2,"msg2":data4,"post":post,"All_user":result1,"All_profile":result2,"msg6":data6})

        else:
            messages.error(request,"**Please fill the right details")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        urole=request.POST["member_level"]
        uname=request.POST["name"]
        uid=request.POST["id"]
        uemail=request.POST["email"]
        upswd=request.POST["pass"]
        ucpswd=request.POST["cpass"]
        if verify.objects.filter(vid=uid,vname=uname).exists():
            if upswd==ucpswd:
                if user.objects.filter(uid=uid).exists():
                    messages.error(request,"**Already Exist Userid")
                    return render(request,'signup.html')
                elif user.objects.filter(uemail=uemail).exists():
                    messages.error(request,"**Email Id Is Taken")
                    return render(request,'signup.html')
                else:
                    data=user(urole=urole,uname=uname,uid=uid,uemail=uemail,upswd=upswd,ucpswd=ucpswd)
                    data.save()
                    Profile.objects.filter(Pr_id=uid).update(Pr_name=uname)
                    messages.success(request,"**Successfully inserted")
                    return render(request,'login.html')
            else:
                messages.error(request,"**please confirm the password")
                return render(request,'signup.html')
        else:
            messages.error(request,"**Only For The Banasthalites")
            return render(request,'signup.html')
    else:
        return render(request,'signup.html')

def contact_us_in(request):
    if request.method=="POST":
        cname=request.POST["name"]
        cemail=request.POST["email"]
        cmsg=request.POST["message"]
        Contact=contact(cname=cname,cemail=cemail,cmsg=cmsg)
        Contact.save();
        messages.success(request,'Message has been sent Successfully')
        if request.session.has_key('id'):
            obj=request.session['id']
            data=anouncement.objects.all().order_by("-id")[:3]
            data6=user.objects.all()
            data4=Profile.objects.get(Pr_id=obj)
            data2=user.objects.get(uid=obj)
            post = Post.objects.all().order_by("-id")
            result2=Profile.objects.exclude(Pr_id=obj).order_by("Pr_name")
            result1=user.objects.exclude(uid=obj).order_by("uname")
            if data2.urole=="Teacher" or data2.urole=="Alumini":
                return render(request,"home (2).html",{"msg":data,"msg1":data2,"msg2":data4,"msg6":data6,"post":post,"All_user":result1,"All_profile":result2})
            else:
                return render(request,"home(1).html",{"msg":data,"msg1":data2,"msg2":data4,"msg6":data6,"post":post,"All_user":result1,"All_profile":result2})
    else:
        return render(request,'contact_us_in.html')

def contact_us_out(request):
    if request.method=="POST":
        cname=request.POST["name"]
        cemail=request.POST["email"]
        cmsg=request.POST["message"]
        Contact=contact(cname=cname,cemail=cemail,cmsg=cmsg)
        Contact.save();
        messages.success(request,'Message has been sent Successfully')
        return render(request,'first.html')
    else:
        return render(request,'contact_us_out.html')

def ancmnt(request):
      if request.session.has_key('id') and (request.method!="POST"):
        objj=request.session['id']
        data2=user.objects.get(uid=objj)
        context= {
            'info': data2,
            }
        return render(request,"add_ancmnt.html",context)
      elif request.method=="POST":
        objj=request.session['id']
        anc_uid=objj
        anc_dsc=request.POST["ancmnt"]
        obj=Profile.objects.get(Pr_id=anc_uid)
        anc_img=obj.Pr_img
        Anouncement=anouncement(anc_uid=anc_uid,anc_dsc=anc_dsc,anc_img=anc_img)
        Anouncement.save();
        messages.success(request,'Anouncement Has Been Made Successfully')
        data=anouncement.objects.all().order_by("-id")[:3]
        data6=user.objects.all()
        data4=Profile.objects.get(Pr_id=objj)
        data2=user.objects.get(uid=objj)
        post = Post.objects.all().order_by("-id")
        if data2.urole=="Teacher" or data2.urole=="Alumini":
            result2=Profile.objects.exclude(Pr_id=objj).order_by("Pr_name")
            result1=user.objects.exclude(uid=objj).order_by("uname")
            return render(request,"home (2).html",{"msg":data,"msg1":data2,"msg2":data4,"msg6":data6,"post":post,"All_user":result1,"All_profile":result2})
        else:
            result2=Profile.objects.exclude(Pr_id=objj).order_by("Pr_name")
            result1=user.objects.exclude(uid=objj).order_by("uname")
            return render(request,"home(1).html",{"msg":data,"msg1":data2,"msg2":data4,"post":post,"msg6":data6,"All_user":result1,"All_profile":result2})
      else:
        messages.error(request,'*Please Check The Details')
        return render(request,'add_ancmnt.html')


def ancmnt_view(request):
    data=anouncement.objects.all().order_by("-id")
    data2=user.objects.all()
    data3=User.objects.all()
    return render(request,"view_ancmnt.html",{"msg":data,"msg2":data2,"msg3":data3})

def logout(request):
    if request.session.has_key('id'):
         obj=request.session['id']
         data1=active.objects.filter(aid=obj).delete()
         data2=user.objects.get(uid=obj)
         auth.logout(request)
         messages.success(request,"You have successfully logged out!")
         return render(request,"first.html",{"msg":data2})

def change_psw(request):
    if request.session.has_key('id'):
         obj=request.session['id']
         print(obj)
         data2=user.objects.get(uid=obj)
         data1=Profile.objects.get(Pr_id=obj)
         if request.method=="POST":
            old_psw=request.POST["old_psw"]
            new_psw=request.POST["new_psw"]
            cnew_psw=request.POST["cnew_psw"]
            if user.objects.filter(uid=data2.uid,upswd=old_psw).exists():
                if new_psw==cnew_psw:
                    data3=user.objects.get(uid=data2.uid)
                    data3.upswd=new_psw
                    data3.save()
                    messages.success(request,"Password Has Been Changed Successfully")
                    data=anouncement.objects.all().order_by("-id")[:3]
                    data5=Profile.objects.get(Pr_id=obj)
                    data4=user.objects.all()
                    post = Post.objects.all().order_by("-id")
                    if  data2.urole=="Teacher" or data2.urole=="Alumini":
                        result2=Profile.objects.exclude(Pr_id=obj).order_by("Pr_name")
                        result1=user.objects.exclude(uid=obj).order_by("uname")
                        return render(request,"home (2).html",{"msg":data,"msg1":data2,"msg6":data4,"msg2":data5,"post":post,"All_user":result1,"All_profile":result2})
                    else:
                        result2=Profile.objects.exclude(Pr_id=obj).order_by("Pr_name")
                        result1=user.objects.exclude(uid=obj).order_by("uname")
                        return render(request,"home(1).html",{"msg":data,"msg1":data2,"msg6":data4,"msg2":data5,"post":post,"All_user":result1,"All_profile":result2})

                else:
                    messages.error(request,"*Please Confirm The Password")
                    return render(request,"change_password.html",{"msg":data2,"msg1":data1})  
            else:
                messages.error(request,"*Please Enter The Correct User Password")
                return render(request,"change_password.html",{"msg":data2,"msg1":data1})
         else:
            return render(request,"change_password.html",{"msg":data2,"msg1":data1})
def my_profile_view(request):
  print(request)
  if request.session.has_key('id') and (request.method!="POST"):
    
    obj=request.session['id']

    profile = Profile.objects.get(Pr_id=obj)
    current=user.objects.get(uid=obj)
    posts=Post.objects.filter(P_author=profile).order_by("-id")
    context = {
        'profile': profile,
        'current':current,
        'posts':posts,
    }
    return render(request, 'myprofile.html', context)
  elif request.method=="POST":
    obj=request.session['id']
    obj2=user.objects.filter(uid=obj)
    if 'picture' not in request.FILES:
        print("iff")
        obj3=Profile.objects.get(Pr_id=obj)
        ppicture=obj3.Pr_img
    else:
        print("elsee")
        file_data = request.FILES["picture"]
        fs=FileSystemStorage()
        ppicture=fs.url(fs.save(file_data.name,file_data))
    pname=request.POST["name"]
    pemail=request.POST["email"]
    ptitle=request.POST["title"]
    pabout=request.POST["about"]
    print(ppicture)
    Profile.objects.filter(Pr_id=obj).update(Pr_name=pname,Pr_title=ptitle,Pr_img=ppicture,Pr_about=pabout)
    user.objects.filter(uid=obj).update(uemail=pemail,uname=pname)
    anouncement.objects.filter(anc_uid=obj).update(anc_img=ppicture)
    profile = Profile.objects.get(Pr_id=obj)
    Post.objects.filter(P_author=profile).update(P_name=pname,P_name_img=ppicture)
    current=user.objects.get(uid=obj)
    posts=Post.objects.filter(P_author=profile).order_by("-id")
    context = {
        'profile': profile,
        'current':current,
         'posts':posts,
    }
    messages.success(request,"Profile Successfully Updated")
    return render(request, 'myprofile.html', context)

def profile_view(request):
        if(request.method == "POST"):
            idd = request.POST.get('submit')
            data1=Profile.objects.get(Pr_id=idd)
            data2=user.objects.get(uid=idd)
            posts=Post.objects.filter(P_author=data1).order_by("-id")
            context= {
                'profile': data1,
                'userr': data2,
                'posts':posts,
                }
            return render(request,"profile.html",context)
        else:
            return render(request,"view_ancmnt.html")

def contacts(request):
    curr=request.session['id']
    data2=user.objects.exclude(uid=curr).order_by("uname")
    data5=Profile.objects.exclude(Pr_id=curr).order_by("Pr_name")
    print(data5)
    print(data2)
    data1=active.objects.exclude(aid=curr).only("aid")
    data4=[]
    for k in data1:
        data4.append(k.aid)
    print("Data4")
    print(data4)
    context= {
                'msg1': data1,
                'msg2': data2,
                'msg3': data4,
                'msg4': data5,
             }
    return render(request,'contacts.html',context)


def like_unlike_post(request):
    id=request.POST.get('id')
    Like=False
    Unlike=False
    obj=request.session['id']
    print(obj)
    user2=Profile.objects.filter(Pr_id=obj)
    print("User2")
    print(user2)
    data=anouncement.objects.all().order_by("-id")[:3]
    data2=user.objects.get(uid=obj)
    result2=Profile.objects.exclude(Pr_id=obj).order_by("Pr_name")
    result1=user.objects.exclude(uid=obj).order_by("uname")
    data4=Profile.objects.get(Pr_id=obj)
    post = Post.objects.all().order_by("-id")
   
    if request.method=="POST":
        id=request.POST['id']
        get_post=Post.objects.get(id=id)
        print(get_post)
        print("Checking Likes:")
        print(get_post.P_liked.all())
        
        
        if user2.first() in get_post.P_liked.all():
            #print("STR1")
            #print(str1)
            print("Unlike")
            get_post.P_liked.remove(user2.first())
            print("Unlike")
            Like=False
        else:
            #print("STR1")
            #print(str1)
            print("Like")
            get_post.P_liked.add(user2.first())
            Like=True
        data5={
            "liked":Like,
            "likes_count":get_post.P_liked.all().count()
        }
        return JsonResponse(data5, safe=False)
    if data2.urole=="Teacher" or data2.urole=="Alumini":
        return redirect("home",{"msg":data,"msg1":data2,"msg2":data4,"post":post,"All_user":result1,"All_profile":result2})
    else:
        return redirect("home", {"msg":data,"msg1":data2,"msg2":data4,"post":post,"All_user":result1,"All_profile":result2})



def Inbox(request):
    curr=request.session['id']
    messages = Message.get_messages(curr_user=curr)
    #currentUser=user.objects.get(uid=curr)
    currentProfile=Profile.objects.get(Pr_id=curr)
    active_direct = None
    active_direct_profile=None
    messages_count =0
    directs = None
    profile=Profile.objects.exclude(Pr_id=curr).order_by("Pr_name")
    allusers=user.objects.exclude(uid=curr).order_by("uname")
    if messages:
        message = messages[0]
        active_direct = message['user'].uid
        active_direct_profile=Profile.objects.get(Pr_id=active_direct)
        directs = Message.objects.filter(m_user=curr, m_recipient=message['user'])|Message.objects.filter( m_sender=message['user']).order_by("m_date")
        directs.update(m_is_read=True)
        messages_count = Message.objects.filter(m_user=curr, m_recipient=message['user']).count()
        messages_count=messages_count+Message.objects.filter( m_sender=message['user']).order_by("m_date").count()
   
    print("Active Direct")
    print(active_direct)
    print("Directs")
    print(directs)
    print("Messages")
    print(messages)
    
    print("messages_count")
    print(messages_count)
    context = {
        'currentProfile':currentProfile,
		'directs': directs, 
		'messages': messages,
		'active_direct': active_direct,
        'profile':profile,
        'allusers':allusers,
        'messages_count':messages_count,
        'active_direct_profile': active_direct_profile,
		}

    template = loader.get_template('direct.html')
    return HttpResponse(template.render(context, request))


def Directs(request):
    curr=request.session['id']
    messages = Message.get_messages(curr_user=curr)
    userid=request.POST["submit"]
    currentProfile=Profile.objects.get(Pr_id=curr)
    active_direct = userid
    directs = None
    profile=Profile.objects.exclude(Pr_id=curr).order_by("Pr_name")
    allusers=user.objects.exclude(uid=curr).order_by("uname")
    directs = Message.objects.filter(m_user=curr, m_recipient=userid)|Message.objects.filter( m_sender=userid).order_by("m_date")
    directs.update(m_is_read=True)
    
    for message in messages:
        if message['user']== active_direct:
            message['unread'] = 0
    print("Active Direct")
    print(active_direct)
    print("Directs")
    print(directs)
    print("Messages")
    print(messages)
   
    active_direct_profile=Profile.objects.get(Pr_id=active_direct)
    context = {
        'currentProfile':currentProfile,
		'directs': directs, 
		'messages': messages,
		'active_direct': active_direct,  
        'profile':profile,
        'allusers':allusers,
        
        'active_direct_profile': active_direct_profile,
		}

    template = loader.get_template('direct.html')
    return HttpResponse(template.render(context, request))

def SendDirect(request):
    curr=request.session['id']
    from_user=user.objects.filter(uid=curr).only("uid")
    to_user=request.POST["to_user"]
    send_to_user=user.objects.filter(uid=to_user).only("uid")
    body=request.POST["body"]
    if request.method == 'POST':
        Message.send_message(from_user.first(), send_to_user.first(), body)
        return redirect('Inbox')
    else:
        HttpResponseBadRequest()












