from django.db import models

from django.contrib.auth.models import User, auth
# Create your models here.

PENDING="Pending"
ONGOING="Ongoing"
CONFIRMED="Confirmed"

DR = "Dr"
MR = "Mr"
MRS = "Mrs"

class Event(models.Model):
	EVENT_CHOICES = (
	(PENDING, "Pending"),
	(ONGOING, "Ongoing"),
	(CONFIRMED, "Confirmed"),
	)
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	perks = models.TextField(blank=True)
	link = models.TextField(blank=True)
	whatsapp = models.TextField(blank=True)
	target = models.CharField(max_length=200, blank=True)
	status = models.CharField(max_length=200,choices=EVENT_CHOICES,default="Pending")
	poster = models.ImageField(upload_to='posters', blank=True)
	date = models.DateField(blank=True)
	tfrom = models.TimeField(blank=True)
	tto = models.TimeField(blank=True)
	regfrom = models.DateField(blank=True)
	regto = models.DateField(blank=True)
	etype = models.CharField(max_length=200, blank=True)
	presenter = models.CharField(max_length=200, blank=True)
	presenterd = models.CharField(max_length=200, blank=True)
	organizer = models.TextField(blank=True)
	teacher1 = models.CharField(max_length=200, blank=True)
	teacher2 = models.CharField(max_length=200, blank=True)
	teacher3 = models.CharField(max_length=200, blank=True)
	convener1 = models.CharField(max_length=200, blank=True)
	convener2 = models.CharField(max_length=200, blank=True)
	contact1 = models.CharField(max_length=200,  blank=True)
	contact2 = models.CharField(max_length=200,  blank=True)
	department = models.CharField(max_length=200, blank=True)
	certi = models.BooleanField(default=False)
	certion = models.BooleanField(default=False)
	pubdate = models.DateTimeField(auto_now_add=True)
	reminders = models.TextField(blank=True)
	tags = models.ManyToManyField(User, verbose_name=(u"Users"), blank=True, related_name='members_involved')
	by = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

class Messaging(models.Model):
	sender = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='user_who_sends_message')
	receiver = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='receiver_of_message')
	message = models.CharField(max_length=1000)
	messagedate = models.DateField(auto_now_add=True, blank=True)
	timee = models.TimeField(auto_now_add=True, blank=True)
	messagesenderid = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='just_an_id_of_the_sender')
	messagetag = models.ForeignKey('self',null=True, on_delete=models.CASCADE)
	poster = models.ImageField(upload_to='sharing', blank=True)
	messageseen = models.BooleanField(default=False)


class Comment(models.Model):
	ecref = models.ForeignKey(Event,null=True, on_delete=models.CASCADE)
	body = models.CharField(max_length=200)
	cby = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
	cdate = models.DateField(auto_now_add=True, blank=True)
	ctime = models.TimeField(auto_now_add=True, blank=True)



class Registration(models.Model):
	erref = models.ForeignKey(Event,null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, blank=True)
	reason = models.CharField(max_length=400,blank=True)
	extras1 = models.CharField(max_length=400,blank=True)
	extras2 = models.CharField(max_length=200,blank=True)
	extras3 = models.CharField(max_length=200,blank=True)
	rdate = models.DateField(auto_now_add=True, blank=True)
	rtime = models.TimeField(auto_now_add=True, blank=True)
	rby = models.ForeignKey(User,null=True, on_delete=models.CASCADE)


class Addreport(models.Model):
	erref = models.ForeignKey(Event,null=True, on_delete=models.CASCADE)
	rtitle = models.CharField(max_length=200, blank=True)
	body = models.CharField(max_length=500,blank=True)
	objectives = models.CharField(max_length=400,blank=True)
	keypoints = models.CharField(max_length=400,blank=True)
	outcomes = models.CharField(max_length=200,blank=True)
	feedback = models.CharField(max_length=200,blank=True)
	rdate = models.DateField(auto_now_add=True, blank=True)
	rtime = models.TimeField(auto_now_add=True, blank=True)
	rby = models.ForeignKey(User,null=True, on_delete=models.CASCADE)



class Details(models.Model):
	SAL_CHOICES = (
	(DR, "Dr"),
	(MR, "Mr"),
	(MRS, "Mrs"),
	)
	urref = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
	salutation = models.CharField(max_length=10,choices=SAL_CHOICES,default="MRS", blank=True)
	department = models.CharField(max_length=90, blank=True)
	designation = models.CharField(max_length=90, blank=True)
	contactinfo1 = models.CharField(max_length=12,blank=True)
	contactinfo2 = models.CharField(max_length=12,blank=True)
	color = models.CharField(max_length=8,blank=True)


class Groupmembers(models.Model):
	name = models.CharField(max_length=200)
	noofmembers = models.CharField(max_length=5, blank=True)
	gby = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
	members = models.ManyToManyField(User, verbose_name=(u"Users"), blank=True, related_name='group_members')


class Preevent(models.Model):
	EVENT_CHOICES = (
	(PENDING, "Pending"),
	(ONGOING, "Ongoing"),
	(CONFIRMED, "Confirmed"),
	)
	description = models.TextField(blank=True)
	target = models.CharField(max_length=200, blank=True)
	status = models.CharField(max_length=200,choices=EVENT_CHOICES,default="Pending")
	date = models.DateField(blank=True)
	tfrom = models.TimeField(blank=True)
	tto = models.TimeField(blank=True)
	regfrom = models.DateField(blank=True)
	regto = models.DateField(blank=True)
	presenter = models.CharField(max_length=200, blank=True)
	presenterd = models.CharField(max_length=200, blank=True)
	organizer = models.TextField(blank=True)
	budget = models.CharField(max_length=200, blank=True)
	department = models.CharField(max_length=200, blank=True)
	pubdate = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(User, verbose_name=(u"Users"), blank=True, related_name='members_involved_in_preevent')
	by = models.ForeignKey(User,null=True, on_delete=models.CASCADE)



class Groupmessages(models.Model):
	groupref = models.ForeignKey(Groupmembers,null=True, on_delete=models.CASCADE)
	gmessagesender = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
	gmessage = models.CharField(max_length=1000)
	gmessagedate = models.DateField(auto_now_add=True, blank=True)
	gtime = models.TimeField(auto_now_add=True, blank=True)
	eventref = models.ForeignKey(Event,null=True, on_delete=models.CASCADE)
	preevent = models.ForeignKey(Preevent,null=True, on_delete=models.CASCADE)
	gmessageseen = models.BooleanField(default=False)
	seen = models.ManyToManyField(User, verbose_name=(u"Users"), blank=True, related_name='group_message_seen')


class Precomment(models.Model):
	ecref = models.ForeignKey(Preevent,null=True, on_delete=models.CASCADE)
	body = models.CharField(max_length=200)
	cby = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
	cdate = models.DateField(auto_now_add=True, blank=True)
	ctime = models.TimeField(auto_now_add=True, blank=True)