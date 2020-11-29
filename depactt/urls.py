from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-login', views.login, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-login'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-signup', views.signup, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-signup'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-home', views.home, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-home'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-profile', views.profile, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-profile'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-help', views.help, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-help'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-addevent', views.addevent, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-addevent'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-preevent', views.preevent, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-preevent'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-groups', views.groups, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-groups'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-addgroup', views.addgroup, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-addgroup'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-groupmessages', views.groupmessages, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-groupmessages'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-allevents', views.allevents, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-allevents'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-upcomingevents', views.upcomingevents, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-upcomingevents'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-finishedevents', views.finishedevents, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-finishedevents'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-messaging', views.messaging, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-messaging'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-fullmessages', views.fullmessages, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-fullmessages'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-userdetails', views.userdetails, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-userdetails'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-eventdetails', views.eventdetails, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-eventdetails'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-eventdetails2', views.eventdetails2, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-eventdetails2'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-editevent', views.editevent, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-editevent'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-forgotpassword', views.forgotpassword, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-forgotpassword'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-forgotpassword2', views.forgotpassword2, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-forgotpassword2'),

    path('email',views.email, name='email'),

    path('homelogout',views.homelogout, name='homelogout'),
    path('adddetails',views.adddetails, name='adddetails'),
    path('addposter',views.addposter, name='addposter'),
    path('alldel',views.alldel, name='alldel'),
    path('predel',views.predel, name='predel'),
    path('grdel',views.grdel, name='grdel'),
    path('comment',views.comment, name='comment'),
    path('precomment',views.precomment, name='precomment'),
    path('addreport',views.addreport, name='addreport'),
    path('register',views.register, name='register'),
    path('torep',views.torep, name='torep'),
    path('toreg',views.toreg, name='toreg'),
    path('ongoing',views.ongoing, name='ongoing'),
    path('confirmed',views.confirmed, name='confirmed'),
    path('pending',views.pending, name='pending'),
    path('pongoing',views.pongoing, name='pongoing'),
    path('pconfirmed',views.pconfirmed, name='pconfirmed'),
    path('ppending',views.ppending, name='ppending'),
    path('toxl',views.toxl, name='toxl'),
    path('todocall',views.todocall, name='todocall'),
    path('totxtall',views.totxtall, name='totxtall'),
    path('topdfall',views.topdfall, name='topdfall'),
    path('topdfed',views.topdfed, name='topdfed'),
    path('todoced',views.todoced, name='todoced'),
    path('totxted',views.totxted, name='totxted'),
    path('toadmin',views.toadmin, name='toadmin'),
    path('tonormal',views.tonormal, name='tonormal'),
    path('tocerti',views.tocerti, name='tocerti'),
    path('toevent',views.toevent, name='toevent'),
]


#     path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-allevents', views.allevents, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-allevents'),
#     path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-upcomingevents', views.upcomingevents, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-upcomingevents'),
#     path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-finishedevents', views.finishedevents, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-finishedevents'),