def find_emp():
 a=0
 while a<1:
  skills={""}
  print("Welcome to the job hunt market")
  print("Eniolas job hunt company is responsible for linking up those who are job hunting for the companies or individuals looking for an employee.")
  comp_name=input("What is the name of your company?: ")
  comp_job=input("What is the job title you are looking for?: ")
  print("Enter the skills you are looking for using only space to end a requirement.")
  comp_skills=input("What skills are you in search for?: ")
  q1=comp_skills.lower()
  words=q1.split()
  skills.remove("")
  skills.update(words)
  print("Your information is being displayed below")
  print("Name: ",comp_name)
  print("Title:", comp_job)
  print("Skills:",skills)
  print("Would you like to change anything you've added?, restart ,or confirm ")
  t=int(input("Enter (1)Change or edit (2)To restart and (3)To confirm: "))
  if t==1:
   b=0
   while b<1:
    print("What do you want to edit??")
    t=int(input("(1)To change company name. (2)To change job title . (3)To edit the skills needed . (4)Confirm :"  ))
    if t==1:
     comp_name=input("What is the name of your company?: ")
     print("Name: ",comp_name)
     continue
    elif t==2:
     comp_job=input("What is the job title you are looking for?: ")
     print("Title:", comp_job)
     continue
    elif t==3:
     c=0
     while c<1:
      print("Do you wish to add or remove?")
      t=int(input("(1)To add . (2)To remove . (3)View . (4)End . "  ))
      if t==1:
         comp_skills=input("What skills are you in search for?: ")
         q1=comp_skills.lower()
         words=q1.split()
         skills.update(words)
         continue
      if t==2:
         comp_skills=input("What skills are you in not in need for? : ")
         q1=comp_skills.lower()
         words=q1.split()
         skills.remove(words)
         continue
      if t==3:
         print(skills)
         continue
      if t==4:
       break
    elif t==4:
     print("Your values have been updated.")
     print("Your information is being displayed below")
     print("Name: ",comp_name)
     print("Title:", comp_job)
     print("Skills:",skills)
     break
     
    else:
     print("You have entered the wrong value, program being terminated")
     break

  elif t==2:
   print("You will be directed to where you will restart")
   skills.clear()
   continue
  elif t==3:
   print("Thank you for your time, we will the confirming your entry now!")
   break
  else:
   print("Entered the wrong value, program will be terminated")
   break
  return "Sucessfully entered"
find_emp()



  

 

 