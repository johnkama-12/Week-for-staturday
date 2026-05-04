print("*************** STUDENT RECORD MANAGEMANT SYSTEM ************************")
login_name={}
login_id=0

student_information = {
    1200:{"student_name":"Alfred Vandy", "email" : "alfredvandy782@gmail.com", "parent_phonenumber": "088952467",   "program":"Dit", "subject":"PROGRAMMING\n COMPUTERISE MATH\n SOFTWARE ENGEERING" },
    1301:{"student_name":"George Ngolo", "email" : "georgengolo782@gmail.com", "parent_phonenumber": "09968790",    "program":"Bit" , "subject":"Multimedia\n Digital Maketing\n SOFTWARE ENGEERING" },
    1402:{"student_name":"Kabbia",       "email" : "kabbia782@gmail.com",      "parent_phonenumber": "088952467",   "program":"Dit", "subject":"Graphic Design\n Computer Skills\n SOFTWARE ENGEERING"  },
    1503:{"student_name":"Caper Chino",  "email" : "caperchino782@gmail.com",  "parent_phonenumber": "091238428" ,  "program":"Bit", "subject":"Creative Art\n  MATHEMATICS\n SOFTWARE ENGEERING" },
    1604:{"student_name":"Big WIz",      "email" : "bigwiz782@gmail.com",      "parent_phonenumber": "090909090" ,  "program":"Bict", "subject":"PROGRAMMING\n COMPUTERISE MATH\n SOFTWARE ENGEERING" },
    1705:{"student_name":"Sombie Blessing","email": "sombieblessing782@gmail.com","parent_phonenumber": "088999900","program":"Bsem" ,"subject":"Maketing\n English\n Packing ART" },
    1806:{"student_name":"Angela Yankuba","email" : "angelayankuba782@gmail.com", "parent_phonenumber": "1122334459","program":"Babj","subject":"BROADCASTING\n MULTIMEDIA\n DEBATING"  },
    1907:{"student_name":"French Genuis","email" : "frenchgenuis782@gmail.com", "parent_phonenumber": "999999999999","program":"Cit", "subject":"ENGLISH\n NETWORKING\n SOFTWARE ENEERING" },
    1008:{"student_name":"Sallieu Mansary", "email" : "smmanasary782@gmail.com", "parent_phonenumber": "08112233444","program":"Bict", "subject":"PROGRAMMING\n COMPUTERISE MATH\n SOFTWARE ENGEERING" },
    1109:{"student_name":"Kadija Bah", "email" : "kadijabah782@gmail.com", "parent_phonenumber": "789023456" ,       "program":"Bsem", "subject":"Creative Art\n  MATHEMATICS\n SOFTWARE ENGEERING" },
    2100:{"student_name":"Alfred Vandy", "email" : "alfredvandy782@gmail.com", "parent_phonenumber": "088952467" ,   "program":"Babj", "subject":"Creative Art\n  MATHEMATICS\n SOFTWARE ENGEERING" }
}
def Admin_access(ID, name):
    admin_list={    
        1111:{"name": "Christian Effiong"},
        2222:{"name": "Amkam Amadu"},
        3333:{"name": "Ansu Samura"},
        4444:{"name": "Engineer Kalokoh"},
        5555:{"name": "Hassan Kamara"}
    }
    if ID not in admin_list and name not in admin_list:
        return f"no data found for the name {name} and ID {ID}"
    login_name={}
    ask={}
    login_id=0
    if ID in admin_list:
        information=admin_list[ID]
        
        for pid, User in admin_list.items():
           if information["name"] == name:
             print (f"Lecturer name: {name} Leturer ID: {ID}")
             print("Do you want to search for a student ?. ")
             try:
               ask=input("Enter yes or no: ").lower().strip()
               ask=int(ask)
               if isinstance(ask, int):
                   print("Not valid")
                   continue
               else:
                   break
             except ValueError:
                 if ask =="yes":
                     break
                 elif ask=="no":
                     break
                 
             if ask == "yes":
                try:
                   login_name=input("Enter the student name: ").title()
                   login_id=int(input("Enter the student Id: ") or 0)
                   login_name=int(login_name)
                   if isinstance(login_name, int):
                       print("student name should be a string or an letter")
                       continue
                   
                except ValueError:
                    break
            
             elif ask=="no":
                 print("Exiting Now, Good bye.")
                 exit()
             else:
                 print("did not understand what you wrote")
                 break
             
             try:     
                
                  login_id=int(login_id)
                  if isinstance(login_id, str) or login_id == 0:
                      print("the student id cannot be an integer !.")
                      continue
                  else:
                      break
             except ValueError:
                        break
    else:
        pass
                
                


    if login_id in student_information:
                     student_info=student_information[login_id]["student_name"]
                     status1=student_information[login_id]["email"]
                     status2=student_information[login_id]["parent_phonenumber"]
                     status3=student_information[login_id]["program"]
                     status4=student_information[login_id]["subject"]
        
                     for sid, name in student_information.items():
                        if student_info==login_name:
                         return f"student name: {login_name}, \nID: {login_id} \nemail: {status1} \nPhonenumber: {status2} \nProgram: {status3} \n Subjects: \n{status4}" 
            
                        else:
                            return f"student name {login_name} and \nid {login_id} not in the list"
                         
                     else:
                      return f"no informaton entered {lecturer_name} and ID {lecturer_id} was not found !."
    else:
        return "student information not found"            
                 

def student_grade(login_id):
    if login_id == 1200 :
        return 50 
        
        
        
            
    


while True:
    try:
        login_id=int(input("Enter your Id: ") or 0)
        if  login_id == 0:
            print("No value input !")
            
        else:
            break            
    except ValueError:
        print(f"only numerical values is allowed !.")
     

while True:
    login_name=input("Enter your name: ").title().strip()
    try:
        number=int(login_name)
        if isinstance(number , int):
            print(f"you entered a number {number}")
            continue 
        else:
            break  
    except ValueError:
             if len(login_name)<=0:
               print("No Value Entered !.")
               continue
             else:
                 break
        
        

if login_id in student_information:
    student_info=student_information[login_id]["student_name"]
    status1=student_information[login_id]["email"]
    status2=student_information[login_id]["parent_phonenumber"]
    status3=student_information[login_id]["program"]
    status4=student_information[login_id]["subject"]
    
    for sid, name in student_information.items():
        if student_info==login_name:
            print(f"student name: {student_info} \nID: {sid} \nemail: {status1} \nPhonenumber: {status2} \nProgram: {status3} \n Subjects: \n{status4}")
            exit()
        
        else:
            print(f"student name {login_name} is not in the list")
            continue
else:
    print("Student id is not correct") 
        
    

print("***************************LECTURERS LOGIN PANEL********************************************")
lecturer_name={}
lecturer_id=0
next={}
while True:
    print("Are you a lecturer ?.")
    next=input("Answer with yes or no: ").lower().strip()
    try:
        next=int(next)
        print(f"you entered {next}, and it is not valid.")
        continue
    except ValueError:
        if next =="yes":
            break
        elif next == "no":
            break
        else:
            continue    
while True:
        if next =="yes":
            try:
                lecturer_name=input("Enter your name: ").title()
                number=int(lecturer_name)
                if isinstance(number, int):
                    print(f"please you have entered a  number which is {number}")
                    continue
                               
            except ValueError:
                if len(lecturer_name)<=0:
                    print("not data inputed !.")
                    continue
                else:
                    break
            
        elif next=="no":
               print("you entered no")
            
               print("exiting now........")
               exit()
        else:
            print("data inputed !.")
            break
        
while True:
            try:
                lecturer_id=int(input("enter your ID: ") or 0)
                
                if isinstance(lecturer_id, str):
                    print("ID should be a letter.")
                    continue
                else:
                    add=Admin_access(lecturer_id, lecturer_name)
                    print(add)
                    break
                
            except ValueError:
                print("ID should be an integer")
                if lecturer_id:
                    add=Admin_access(lecturer_id, lecturer_name)
                    print(add)
                elif lecturer_id == 0:
                    print("no data inputed")
                else:
                    print("wrong data ")
                    break
                    
                
    
    
    
    