from django.db import models
import datetime
from django.core.validators import FileExtensionValidator
from django.db.models import Max


# Create your models here.

class user(models.Model):
    uid=models.CharField(max_length=10,blank=False, primary_key=True)
    urole=models.CharField(max_length=10,blank=False)
    uname=models.CharField(max_length=50,blank=False)
    uemail=models.CharField(max_length=70,blank=False)
    utime=models.DateTimeField(auto_now_add=True)
    upswd=models.CharField(max_length=20,blank=False)
    ucpswd=models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.uid
class active(models.Model):
    aid=models.CharField(primary_key=True,max_length=10)
    atime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.aid

class verify(models.Model):
    vrole=models.CharField(max_length=10,blank=False)
    vid=models.CharField(max_length=10,blank=False,primary_key=True)
    vname=models.CharField(max_length=20,blank=False)
    
    def __str__(self):
        return self.vid

class contact(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=50,blank=False)
    cemail=models.CharField(max_length=70,blank=False)
    ctime=models.DateTimeField(auto_now_add=True)
    cmsg=models.CharField(max_length=500,blank=False)

    def __str__(self):
        return self.cname

class anouncement(models.Model):
    anc_uid=models.CharField(max_length=10)
    anc_dsc=models.CharField(max_length=500,blank=False)
    anc_time=models.DateTimeField(auto_now_add=True)
    anc_img=models.ImageField(default='static/images/admin.jpg')
    def __str__(self):
        return self.anc_uid
    
class Profile(models.Model):
    Pr_name= models.CharField(max_length=200, blank=True)
    Pr_id = models.ForeignKey(user, on_delete=models.CASCADE)
    Pr_title = models.TextField(default="no title...", max_length=300)
    Pr_about = models.TextField(default="no description...", max_length=500)
    Pr_img = models.ImageField(default='static/profile_images/avatar.png', upload_to='static/profile_images/')
   
   
    def __str__(self):
        return (str)(self.Pr_id)
    def get_post_no(self):
        return self.ppost.all().count()



class Post(models.Model):
    P_content = models.TextField(blank=False)
    P_img = models.ImageField(upload_to='static/profile_images/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    P_liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    P_created = models.DateTimeField(auto_now_add=True)
    P_author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ppost')
    P_name= models.TextField(blank=True)
    P_name_img = models.ImageField(default='static/images/admin.jpg')

    def str(self):
        return str(self.P_created)

    def num_likes(self):
        return self.P_liked.all().count()


class Message(models.Model):
    m_user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='user')
    m_sender = models.ForeignKey(user, on_delete=models.CASCADE, related_name='from_user')
    m_recipient = models.ForeignKey(user, on_delete=models.CASCADE, related_name='to_user')
    m_body = models.TextField(max_length=1000, blank=True, null=True)
    m_date=models.DateTimeField(auto_now_add=True)
    m_is_read=models.BooleanField(default=False)

    
    def send_message(from_user, to_user, body) :
        sender_message = Message(
			m_user=from_user,
			m_sender=from_user,
			m_recipient=to_user,
			m_body=body,
			m_is_read=True)
        sender_message.save()
        recipient_message = Message(
			m_user=to_user,
			m_sender=from_user,
			m_body=body,
			m_recipient=from_user,)
        recipient_message.save()
        return sender_message

    def get_messages(curr_user):
        messages = Message.objects.filter(m_user=curr_user).values('m_recipient').annotate(last=Max('m_date')).order_by('-last')
        userlist= []
        for message in messages:
            userlist.append({
				'user': user.objects.get(pk=message['m_recipient']),
				'last': message['last'],
				'unread': Message.objects.filter(m_user=curr_user, m_recipient__pk=message['m_recipient'], m_is_read=False).count()
				})
        return userlist


