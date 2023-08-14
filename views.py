import email
from pyexpat import model
from django.http import HttpResponse
from django.conf import settings
#for calling render module
from django.shortcuts import render,redirect
#for import models.py
from . import models

#for import mysqldb module
import MySQLdb

#for date and time module
import datetime

#for access current_url varaible
curl=settings.CURRENT_URL

def home(request):
 return render(request,"home.html",{'curl':curl}) 

def test(request):
 a=10
 b=20
 c=a+b
 print("c=",c)   
 return render(request,"test.html",{'curl':curl,'c':c}) 

def login(request):
 if request.method=="POST":
  emailid=request.POST.get("emailid")
  pwd=request.POST.get("pwd")
  query="select * from mstuser where emailid='%s' and pwd='%s'" %(emailid,pwd)             
  models.cursor.execute(query)
  result=models.cursor.fetchone()  

  #print("type=",type(result))
  role=result[4]
  fnm=result[0]
  print(role)
  #for create session .................
  request.session["emailid"]=emailid
  request.session["role"]=role
  request.session["fnm"]=fnm
  #....................................

  if role=="student":
   return redirect("/studenthome/")    
  else:
   return redirect("/adminhome/")    
  return render(request,"login.html",{'curl':curl}) 
 else:  
  return render(request,"login.html",{'curl':curl})      

def studenthome(request): 
 #for fetch data from session .................
  emailid=request.session["emailid"]
  role=request.session["role"]
  #....................................   
  return render(request,"studenthome.html",{'curl':curl,'emailid':emailid,'role':role})   


def adminhome(request):   
  #for fetch data from session .................
  emailid=request.session["emailid"]
  role=request.session["role"]
  #....................................  
  return render(request,"adminhome.html",{'curl':curl,'emailid':emailid,'role':role}) 

def courselist1(request): 
 query="select * from course"
 models.cursor.execute(query)
 result=models.cursor.fetchall() 
 print(result)    
 return render(request,"courselist1.html",{'curl':curl,'result':result}) 

def studentlist(request): 
 role="student" 
 query="select * from mstuser where role='%s' " %(role)
 models.cursor.execute(query)
 result=models.cursor.fetchall() 
 print(result)    
 return render(request,"studentlist.html",{'curl':curl,'result':result}) 

def addcourse(request):
 if request.method=="POST": 
  coursenm=request.POST.get("coursenm")         
  duration=request.POST.get("duration")
  fees=request.POST.get("fees")
  coursedetail=request.POST.get("coursedetail")
  query="insert into course(coursenm,duration,fees,coursedetail) values('%s',%s,%s,'%s')" %(coursenm,duration,fees,coursedetail)
  models.cursor.execute(query)
  models.db.commit()
  msg="Record Saved"
  return render(request,"addcourse.html",{'curl':curl,'msg':msg}) 
 else:
  return render(request,"addcourse.html",{'curl':curl,'msg':''})   

def register(request):
 if request.method=="POST":
  fnm=request.POST.get("fnm") 
  mno=request.POST.get("mno")       
  emailid=request.POST.get("emailid")
  pwd=request.POST.get("pwd")
  role="student"
  query="insert into mstuser values('%s',%s,'%s','%s','%s')" %(fnm,mno,emailid,pwd,role)
  #print(query)
  #for execute query
  models.cursor.execute(query)
  models.db.commit()
  msg="Regsitration Successfull"
  return render(request,"register.html",{'curl':curl,'msg':msg})     
 else:
  return render(request,"register.html",{'curl':curl,'msg':''})     

def searchcourse(request):
 if request.method=="POST":
   coursenm=request.POST.get("coursenm")
   query="select * from course where coursenm='%s'" %(coursenm)
   models.cursor.execute(query)
   rs=models.cursor.fetchone() 
   print(rs)
   return render(request,"displaycourse.html",{'curl':curl,'rs':rs}) 
 else:
  return render(request,"searchcourse.html",{'curl':curl}) 

def addbatch(request):
 if request.method=="GET":
  query="select courseid,coursenm from course"     
  models.cursor.execute(query)
  rs=models.cursor.fetchall()
  print(rs)
  return render(request,"addbatch.html",{'curl':curl,'rs':rs,'msg':''})   
 else:
  courseid=request.POST.get("courseid")  
  startdate=request.POST.get("startdate")  
  batchtime=request.POST.get("batchtime")  
  facultynm=request.POST.get("facultynm")  
  query="insert into batch1(courseid,startdate,batchtime,facultynm) values(%s,'%s','%s','%s') " %(courseid,startdate,batchtime,facultynm) 
  models.cursor.execute(query)
  models.db.commit()
  msg="Record Saved"
  return render(request,"addbatch.html",{'curl':curl,'rs':'','msg':msg})   

def newbatchlist1(request): 
 query="""select  a.batchid,b.coursenm,
DATE_FORMAT(a.startdate,'%d-%m-%Y') as startdate,
a.batchtime,b.duration,b.fees
from batch1 as a
inner join course as b on a.courseid=b.courseid
where a.batchstatus=1"""
 models.cursor.execute(query)
 result=models.cursor.fetchall() 
 print(result)    
 return render(request,"newbatchlist1.html",{'curl':curl,'result':result})   

def courselist3(request): 
 query="select * from course"
 models.cursor.execute(query)
 result=models.cursor.fetchall() 
 print(result)    
 return render(request,"courselist3.html",{'curl':curl,'result':result}) 

def admission(request): 
 #for fetch query string value 
 batchid=request.GET.get("batchid")
 #end here..............................
 query="select a.batchid,b.coursenm,a.startdate,a.batchtime,b.duration,b.fees from batch1 as a inner join course as b on a.courseid=b.courseid where a.batchstatus=1 and a.batchid='%s'" %(batchid)
 #print(query)
 models.cursor.execute(query)
 result=models.cursor.fetchone() 
 #print(result)
 
 return render(request,"admission.html",{'curl':curl,'result':result}) 

def bookbatch(request):
 if request.method=="POST":
  batchid=request.POST.get("batchid") 
  emailid=request.session["emailid"]
  x=datetime.datetime.now()
  admissiondate=x.strftime("%Y/%m/%d")
  query="insert into admission(batchid,emailid,admissiondate) values(%s,'%s','%s') " %(batchid,emailid,admissiondate)
  #print(query)
  models.cursor.execute(query)
  models.db.commit()  
  return redirect('/success/')
  #return render(request,"success.html",{'curl':curl,'msg':msg}) 

def success(request):
  msg="Batch Booked Successfully"
  return render(request,"success.html",{'curl':curl,'msg':msg}) 

def logout(request):
 if 'emailid' in request.session:
   del request.session['emailid']
   return render(request,'home.html',{'curl':curl})    

#dt 13 may
def searchprofile(request):
 emailid=request.session["emailid"]     
 query="select * from mstuser where emailid='%s'" %(emailid)
 models.cursor.execute(query)
 rs=models.cursor.fetchone()
 print(rs)
 return render(request,"searchprofile.html",{'curl':curl,'rs':rs})

def updateprofile(request):
 if request.method=="POST":
  fnm=request.POST.get("fnm")
  mno=request.POST.get("mno")
  emailid=request.POST.get("emailid")
  pwd=request.POST.get("pwd")
  query="""
    update mstuser set fnm='%s',mno=%s,pwd='%s' 
    where emailid='%s' """ %(fnm,mno,pwd,emailid)
  print(query)
  models.cursor.execute(query)
  models.db.commit()
  role=request.session["role"]
  #return render(request,"studenthome.html",{'curl':curl,'emailid':emailid,'role':role}) 
  return redirect('/profilesuccess/')

def newbatchlist2(request): 
 query="""select  a.batchid,b.coursenm,
DATE_FORMAT(a.startdate,'%d-%m-%Y') as startdate,
a.batchtime,b.duration,b.fees
from batch1 as a
inner join course as b on a.courseid=b.courseid
where a.batchstatus=1"""
 models.cursor.execute(query)
 result=models.cursor.fetchall() 
 print(result)    
 return render(request,"home.html",{'curl':curl,'result':result})   

def upcomingbatches(request): 
 query="""select  a.batchid,b.coursenm,
DATE_FORMAT(a.startdate,'%d-%m-%Y') as startdate,
a.batchtime,b.duration,b.fees
from batch1 as a
inner join course as b on a.courseid=b.courseid
where a.batchstatus=1"""
 models.cursor.execute(query)
 result=models.cursor.fetchall() 
 print(result)    
 return render(request,"newbatchlist2.html",{'curl':curl,'result':result})    

def contact(request):
 return render(request,"contact.html",{'curl':curl})     

def gallery(request):
 return render(request,"gallery.html",{'curl':curl})     

def profilesuccess(request):
  msg="Profile Updated"
  return render(request,"profilesuccess.html",{'curl':curl,'msg':msg})     

def addfaculty(request):
 if request.method=="POST": 
  fnm=request.POST.get("fnm")         
  qualification=request.POST.get("qualification")
  mno=request.POST.get("mno")
  emailid=request.POST.get("emailid")
  skills=request.POST.get("skills")
  query="insert into faculty(fnm,qualification,mno,emailid,skills) values('%s','%s','%s','%s','%s')" %(fnm,qualification,mno,emailid,skills)
  models.cursor.execute(query)
  models.db.commit()
  msg="Record Saved"
  return render(request,"addfaculty.html",{'curl':curl,'msg':msg}) 
 else:
  return render(request,"addfaculty.html",{'curl':curl,'msg':''})   

def facultylist(request): 
 query="select * from faculty"
 models.cursor.execute(query)
 result=models.cursor.fetchall() 
 print(result)    
 return render(request,"facultylist.html",{'curl':curl,'result':result}) 
