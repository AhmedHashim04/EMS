import EMSData as EMSD
# محاولات الدخول علي السيستيم
login_tries=0
# بيانات المحاضرين من لدكاترة
Lecturers_data=[]
# بيانات الكورسات 
Courses_data=[]
#بيانات الطلاب  
Students_data=[]
# بيانات المعيدين
TAs_data=[]
# الرسائل بين مستخدمي السيستيم
Massages=[]
Lecturers_data,Courses_data,Students_data,TAs_data,Massages=EMSD.Lecturers_data,EMSD.Courses_data,EMSD.Students_data,EMSD.TAs_data,EMSD.Massages
def Update_Data():
    with open("EMSData.py","a") as C_data:
         C_data.write("\n")
         C_data.write("\n")
         C_data.write("#")
         C_data.write("----------------------"*30)
         C_data.write("\n")
         C_data.write("\n")
         C_data.write(f"Courses_data={Courses_data}\n")
         C_data.write(f"Lecturers_data={Lecturers_data}\n")
         C_data.write(f"Students_data={Students_data}\n")
         C_data.write(f"TAs_data={TAs_data}\n")
         C_data.write(f"Massages={Massages}\n")
    print("Successfull to Save Data !")
# دالة تقوم بعمل خطوط بعد كل متغير لطلب مدخلات لتنظيم الشكل العام
#دالة لإظهار الكورسات التي يمتلكها المحاضر او الطالب واخفاء ما لا يملك
def View_arranged_course_not_have():
        print(f"[0] - Back , {user["Name"]}")
        for i,crs in enumerate(Courses_data,1):
            if crs["Code"] not in user["Courses"]:
                print(f"[{i}] - {crs["Code"]} , Name :  {crs["Name"]}")
##دالة لإظهار الكورسات التي لا يمتلكها المحاضر او الطالب واخفاء ما  يملك
def View_arranged_course_have():
        print(f"[0] - Back , {user["Name"]}")
        for i,crs in enumerate(Courses_data,1):
            if crs["Code"] in user["Courses"]:
                print(f"[{i}] - {crs["Code"]} , Name :  {crs["Name"]}")
def ExitSystem():
    Update_Data()
    quit()   
#---------------------------0Screen--------------------
# الدالة الرأيسية
def main_sys():
    print(""" Please make choice :
              [1] -  Login
              [2] -  Sign up
                  -------------
              [3] -  Close System
              """)
    Sys_0_Face=int(input(" Choose from [1-3] : "))
    if Sys_0_Face==1:
        login()
    elif Sys_0_Face==2:
        sign_up()
    else:
        ExitSystem()
#تسجيل حساب جديد في السيستيم 
def sign_up():
    print("""
          Welcome in EMS...you can register a new account
                    -What is your Rank ?
          [1] - Lecturer
          [2] - Student
          [3] - Teaching Assisstant
              -----------------
          [4] - Close System
          """)
    
    new_rank=int(input(" Choose from [1-4] :  ")) #بتدخل المكانة العلمية 
    if new_rank==1:#لو اختارت محاضر
        new_rank="Lecturer"
        
        LecrrUsername=input(" please give me Username for easy login :  ")

        UsernamesLecrr=[]
        for us in Lecturers_data:
            UsernamesLecrr.append(us["Username"])
        while LecrrUsername in UsernamesLecrr :
            print("wrong!! Username exist")
            LecrrUsername=input(" please give me Username for easy login :  ")
    
        LecrrPassword=input(" please give me Password to Protect your login :  ")

        Name =input(" please give me Name for easy Call :  ")

        LecrrAge=int(input(" please give me your Age :  "))

        Lecrr_data={"Username":LecrrUsername,
         "Password":LecrrPassword,
         "Name":Name,
         "Age":LecrrAge,
         "Courses":[]
         }
        
        finish_Choicing=0
        while finish_Choicing==0:

            print(f"[0] - To Finish sign , Dr. {Lecrr_data["Name"]}")
                    #بيعرض الكورسات الي لسا فاضلة وممكن تختارها 
            for i,crs in enumerate(Courses_data,1):
                if crs["Code"] not in Lecrr_data["Courses"]:
                    print(f"[{i}] - {crs["Code"]} , Name :  {crs["Name"]}")
                                                                            
            Courses_Choicing=int(input(f"Please Dr : {Name} choose The Courses That you Can teach : "))    
    

            
            if Courses_Choicing in range(1,len(Courses_data)+1):
                if  len(Courses_data[Courses_Choicing-1]["Lecturers"])>0 :
                    print(f"You can,t choose it !, there are Dr.{Courses_data[Courses_Choicing-1]["Lecturers"][0]}")
            
                else:
                    Lecrr_data["Courses"].append(Courses_data[Courses_Choicing-1]["Code"])                    

            else:
                finish_Choicing=1

        for i,m in enumerate(Lecrr_data["Courses"]):
            Courses_data[i]["Lecturers"].append(Lecrr_data["Name"])
        Lecturers_data.append(Lecrr_data)
        print("Successfuly To Creat Account ! ")
        Update_Data()
        login()

    if new_rank==2:#لو المكانة العلمية طالب
        new_rank="Student"
        StdUsername=input(" please give me Username for easy login :  ")

        UsernamesStd=[]
        for us in Students_data:
            UsernamesStd.append(us["Username"])
        while StdUsername in UsernamesStd:
            print("wrong!! Username exist")
            StdUsername=input(" please give me Username for easy login :  ")
    
        StdPassword=input(" please give me Password to Protect your login :  ")

        Name =input(" please give me Name for easy Call :  ")

        finish_Choicing=0
        Std_data={"Username":StdUsername,
                     "Password":StdPassword,
                     "Name":Name,
                     "Courses":[],
                     "Assignments":0
                     }
        
        while finish_Choicing==0:
            print(f"[0] - To Finish sign , {Std_data["Name"]}")
            #بيعرض الكورسات الي لسا فاضلة وممكن تختارها 
            for i,crs in enumerate(Courses_data,1):
                if crs["Code"] not in Std_data["Courses"]:
                    print(f"[{i}] - {crs["Code"]} , Name :  {crs["Name"]}")  
                      
            Courses_Choicing=int(input(f"Please {Name} choose The Courses That you Can teach : "))
    

            if Courses_Choicing in range(1,len(Courses_data)+1):
                if Courses_data[Courses_Choicing-1]["Code"] in Std_data["Courses"]:
                    print("You Had Choosed it before !")
                else:
                    Std_data["Courses"].append(Courses_data[Courses_Choicing-1]["Code"])
                    Courses_data[Courses_Choicing-1]["Students"].append(Std_data["Name"])
            else:
                finish_Choicing=1
        Students_data.append(Std_data)
        
        print("Successfuly To Creat Account ! ")
        Update_Data()
        login()
    if new_rank==3:#لو اختارت معيد
        new_rank="TA"

        #تعريف اليوسرنيم والباسورد
        TA_Username=input(" please give me Username for easy login :  ")

        Usernames_TA=[]
        for us in TAs_data:
            Usernames_TA.append(us["Username"])
        while TA_Username in Usernames_TA  :
            print("wrong!! Username is exist")
            TA_Username=input(" please give me Username for easy login :  ")
    
        TA_Password=input(" please give me Password for Secure login :  ")
        #---------

        Name =input(" please give me Name for easy Call :  ")

        TA_Age=int(input(" please give me your Age :  "))

        TA__data={"Username":TA_Username,
         "Password":TA_Password,
         "Name":Name,
         "Age":TA_Age,
         "Courses":[]
         }
        #تسجيل الكورسات في أول إنشاء الحساب
        finish_Choicing=0
        while finish_Choicing==0:
            print(f"[0] - To Finish sign , Dr. {TA__data["Name"]}")
                    #بيعرض الكورسات الي لسا فاضلة وممكن تختارها 
            for i,crs in enumerate(Courses_data,1):
                if crs["Code"] not in TA__data["Courses"]:
                    print(f"[{i}] - {crs["Code"]} , Name :  {crs["Name"]}")
                                                                            
            Courses_Choicing=int(input(f"Please Dr : {Name} choose The Courses That you Can teach : "))    
    

            
            if Courses_Choicing in range(1,len(Courses_data)+1):
                TA__data["Courses"].append(Courses_data[Courses_Choicing-1]["Code"])                    

            else:
                finish_Choicing=1
        for i in enumerate(TA__data["Courses"]):
            Courses_data[i]["Lecturers"].append(TA__data["Name"])

        TAs_data.append(TA__data)
        
        print("Successfuly To Creat Account ! ")
        Update_Data()
        login()
    else:ExitSystem()

# الدخول لحساب مسجل علي السيستيم
def login():
    global user
    global login_tries
    global Character_choice
    if login_tries == 3:
        print("You Had finished your Chances Please Come Tomorrow!")

        ExitSystem()

    print("""-----------------------------------------------
          you can login by write your username and password !
          -----------------------------------------------""")
    print(""" What is your rank ?
                                
                            [1] -  Lecturer
                            [2] -  Student 
                            [3] -  Teaching Assisstant 
                                ---------------------
                            [4] - Close System

                             """)
    Character_choice=int(input("Choose from [1-4] : "))#بتختار مكانتك العلمية

    
    if Character_choice==1:
        Username=(input(" Username :  ")).strip()

        Password=(input(" Password :  ")).strip()

        open=0
        for user in Lecturers_data:
            if user["Username"]==Username and user["Password"]==Password:
                First_Screen_After_Login()
                open=1
            else:pass
        if open==0:
            print("Sorry! wrong Username or Password")
            login_tries+=1
            login()
    elif Character_choice==2:
        Username=(input(" Username :  ")).strip()

        Password=(input(" Password :  ")).strip()

        open=0
        for user in list(Students_data):
            if user["Username"]==Username and user["Password"]==Password:
                First_Screen_After_Login()
                open=1
            else:pass
        if open==0:
            print("Sorry! wrong Username or Password")
            login_tries+=1
            login()
    elif Character_choice==3:
        Username=(input(" Username :  ")).strip()

        Password=(input(" Password :  ")).strip()

        open=0
        for user in TAs_data:
            if user["Username"]==Username and user["Password"]==Password:
                First_Screen_After_Login()
                open=1
            else:pass
        if open==0:
            print("Sorry! wrong Username or Password")
            login_tries+=1
            login()    
    else:ExitSystem()

#--------------------------------------------------------------------

#************************************************************************
    
#---------------------------1Screen---------------------
#العمليات التي تجري بعد الدخول لحساب المحاضر
def First_Screen_After_Login():
    global Screen0

    if Character_choice==1:
        print(f"Wellcome in Your Account Dr.{user["Name"]} : " )

        print(f"\nPlease Dr: {user["Name"]} choose any Decision :")  
        print("""
            [1] - Teach a new course 
            [2] - View my Courses
            [3] - Emails
                ---------------
            [4] - Close System
        """)
            # [2] - Unregister Course
        Screen0=int(input("Choose from [1-4] :  "))

        if Screen0 ==1:
            sign_course()
        elif Screen0 ==2:
            View_Courses_Screen()
        elif Screen0 ==3:
            Emails()
            

        else:ExitSystem()
    
    elif Character_choice==2:
        print(f"Wellcome in Your Account {user["Name"]} : " )

        print(f"\nPlease {user["Name"]} Choose any Decision :  ")
        print("""
            [1] - Learn a new course 
            [2] - View my Courses
            [3] - Emails
                ---------------
            [4] - Close System
        """)
            # [2] - Unregister Course
        Screen0=int(input("Choose from [1-4] :  "))

        if Screen0 ==1:
            sign_course()
        elif Screen0 ==2:
            View_Courses_Screen()
        elif Screen0 ==3:
            Emails()

        else:ExitSystem()

    elif Character_choice==3:
        print(f"Wellcome in Your Account Eng:{user["Name"]} : " )

        print(f"\nPlease {user["Name"]} Choose any Decision :  ")
        print("""
            [1] - Requiere To teach a course 
            [2] - View my Courses
            [3] - Emails
                ---------------
            [4] - Close System
        """)
            # [2] - Unregister Course
        Screen0=int(input("Choose from [1-4] :  "))

        if Screen0 ==1:
            TA_Requiere()
        elif Screen0 ==2:
            View_Courses_Screen()
        elif Screen0 ==3:
            Emails()
        else:ExitSystem()
    else:ExitSystem()
#---------------------------2Screen--------------------
#لإضافة كورسات للمحاضر او لإضافة كورسات للطالب  بعد تسجيل الحساب
def sign_course():
    global Courses_Choicing
    # متغير يتغير بعد الانتهاء من اختيار الكورسات
    finish_Choicing=0
    while finish_Choicing==0:# طول مالمتغير زي ما هو 
        View_arranged_course_not_have()
        if Character_choice==1:
            Courses_Choicing=int(input(f"Please Dr : {user["Name"]} choose The Courses That you Can teach : "))
            if Courses_Choicing in range(1,len(Courses_data)+1):
                if  len(Courses_data[Courses_Choicing-1]["Lecturers"])>0 :
                    print(f"You can,t choose it !, there are Dr.{Courses_data[Courses_Choicing-1]["Lecturers"][0]}")
                else:
                    user["Courses"].append(Courses_data[Courses_Choicing-1]["Code"])
                    Courses_data[Courses_Choicing-1]["Lecturers"].append(user["Name"])
            else:
                finish_Choicing=1
                Update_Data()
                First_Screen_After_Login()
        elif Character_choice==2:
            Courses_Choicing=int(input(f"Please {user["Name"]} choose The Courses That you Can learn : "))
            if Courses_Choicing in range(1,len(Courses_data)+1):
                if Courses_data[Courses_Choicing-1]["Code"] in user["Courses"]:
                    print("You are already learning it !")
                else:
                    user["Courses"].append(Courses_data[Courses_Choicing-1]["Code"])
                    Courses_data[Courses_Choicing-1]["Students"].append(user["Name"])
                    user["Assignments"].append({Courses_data[Courses_Choicing-1]["Code"]:[]})
                    for Question in Courses_data[Courses_Choicing-1]["Assignments"]:
                        for i in user["Assignments"]:
                            if Courses_data[Courses_Choicing-1]["Code"] in i.keys():
                                i[Courses_data[Courses_Choicing-1]["Code"]].append((Question,"Solution : N/A","Degree : N/A"))      
            else:
                finish_Choicing=1
                Update_Data()
                First_Screen_After_Login()
#ارسال طلب من المعيد للدكتور لمساعدته في تدريس الكورس
def TA_Requiere():
    p=[]
    print(f"[0] - Back , {user["Name"]}")
    for i,crs in enumerate(Courses_data,1):
        if crs["Code"] not in user["Courses"]:
            if len(crs["Lecturers"])!=0 :
                    p.append(i)
                    print(f"[{i}] - {crs["Code"]} , Name :  {crs["Name"]} , for Dr:{crs["Lecturers"][0]}")
    want_course=int(input("choose course you want to require : "))
    if want_course in p:
        for r in Lecturers_data:
            if  r["Name"] in Courses_data[want_course-1]["Lecturers"]:
                if ((user["Name"],Courses_data[want_course-1]["Code"])) not in r["Requires"]:
                    r["Requires"].append((user["Name"],Courses_data[want_course-1]["Code"]))
                    Update_Data()
                else:
                    print("you had Required this course !")
    else:
        print("you are teaching it already !")
    First_Screen_After_Login()
#لإزالة كورسات المحاضر او لإزالة كورسات الطالب  بعد تسجيل الحساب
def unsign_course():
    finish_Choicing=0
    while finish_Choicing==0:
        View_arranged_course_have()
        if Character_choice==1:
            Courses_Choicing=int(input(f"Please Dr : {user["Name"]} choose The Courses That you want to remove : "))
            if Courses_Choicing in range(1,len(Courses_data)+1):
                if Courses_data[Courses_Choicing-1]["Code"] in user["Courses"]:
                    user["Courses"].remove(Courses_data[Courses_Choicing-1]["Code"])
                    Courses_data[Courses_Choicing-1]["Lecturers"].remove(user["Name"])
                else:
                    print("you dont have it !")
            else:
                finish_Choicing=1
                Update_Data()
                First_Screen_After_Login()
        elif Character_choice==2:
            Courses_Choicing=int(input(f"Please {user["Name"]} choose The Courses That you Can remove : "))
            if Courses_Choicing in range(1,len(Courses_data)+1):
                if Courses_data[Courses_Choicing-1]["Code"] in user["Courses"]:
                    user["Courses"].remove(Courses_data[Courses_Choicing-1]["Code"])
                    Courses_data[Courses_Choicing-1]["Students"].remove(user["Name"])
                    for x in user["Assignments"]:
                        if Courses_data[Courses_Choicing-1]["Code"] in x.keys():
                            user["Assignments"].pop(user["Assignments"].index(x))
                else:
                    print("you dont have it !")
            else:
                finish_Choicing=1
                Update_Data()
                First_Screen_After_Login()
        elif Character_choice==3:
            Courses_Choicing=int(input(f"Please Eng : {user["Name"]} choose The Courses That you want to remove : "))
    
            if Courses_Choicing in range(1,len(Courses_data)+1):
                if Courses_data[Courses_Choicing-1]["Code"] in user["Courses"]:
                    user["Courses"].remove(Courses_data[Courses_Choicing-1]["Code"])
                    Courses_data[Courses_Choicing-1]["TAs"].remove(user["Name"])
                else:
                    print("you dont have it !")
            else:
                finish_Choicing=1
                Update_Data()
                First_Screen_After_Login()

#العمليات التي تجري بعد الدخول لحساب الطالب
def View_Courses_Screen():
    View_arranged_course_have()
    global v_c
    v_c=int(input("plese choose course to make operation in it : "))
    if Character_choice==1:    
        if v_c in range(1,len(Courses_data)+1) and user["Name"] in Courses_data[v_c-1]["Lecturers"]:
    
            print("""you had entered to course now just chose any option and i will make it for you :""")
            print("""
            [1] - View Assignments 
            [2] - Unsign from course
            [3] - Requires to Assist in Courses
                ---------------
            [0] - Back 
            """)
            opetion0=int(input("choose from [0-2] : "))
            if opetion0==1:                operations_On_Lecturer_Courses()
            elif opetion0==2:
                user["Courses"].remove(Courses_data[v_c-1]["Code"])
                Courses_data[v_c-1]["Lecturers"].remove(user["Name"])
                Update_Data()
                operations_On_Lecturer_Courses()
            elif opetion0==3:
                Accept_Reqs()
            else:
                View_Courses_Screen()
        else:
            First_Screen_After_Login()
    elif Character_choice==2:
        if v_c in range(1,len(Courses_data)+1) and user["Name"] in Courses_data[v_c-1]["Students"]:
            print("""you had entered to course now just chose any option and i will make it for you :""")
            print("""
            [1] - View Assignments 
            [2] - Unsign from course
                ---------------
            [0] - Back 
            """)
            opetion0=int(input("choose from [0-2] : "))
            if opetion0==1:                Assignment_info()
            elif opetion0==2:
                user["Courses"].remove(Courses_data[v_c-1]["Code"])
                Courses_data[v_c-1]["Students"].remove(user["Name"])
                Update_Data()
                operations_On_Lecturer_Courses()
            else:
                View_Courses_Screen()
        else:
            First_Screen_After_Login()
    elif Character_choice==3:
        if v_c in range(1,len(Courses_data)+1) and user["Name"] in Courses_data[v_c-1]["TAs"]:
            print("""you had entered to course now just chose any option and i will make it for you :""")
            print("""
            [1] - View Assignments 
            [2] - Unsign from course
                ---------------
            [0] - Back 
            """)
            opetion0=int(input("choose from [0-2] : "))
            if opetion0==1:    
                operations_On_Lecturer_Courses()
            elif opetion0==2:
                user["Courses"].remove(Courses_data[v_c-1]["Code"])
                Courses_data[v_c-1]["TAs"].remove(user["Name"])
                Update_Data()
                View_Courses_Screen()
            else:
                View_Courses_Screen()
        else:
            First_Screen_After_Login()
#---------------------------3Screen--------------------
#دالة بتظهر للطالب الواجبات الي في الكورس وبتمكنة من الحل
def Assignment_info():
    view_assignment()
    Solve_One=int(input("solve Assignment number : "))
    if v_c in range(1,len(Courses_data)+1) and Solve_One in range(1,100) and len(Courses_data[v_c-1]["Assignments"])>(Solve_One-1) and Solve_One!=0:
        Solve_One=Courses_data[v_c-1]["Assignments"][Solve_One-1]
        for course in user["Assignments"]:
            if Courses_data[v_c-1]["Code"] in course:
                if (Solve_One, 'Solution : N/A', 'Degree : N/A') in course[Courses_data[v_c-1]["Code"]]:
                    solution=input("your solution txt / solution link is : ")
                    course[Courses_data[v_c-1]["Code"]].insert(course[Courses_data[v_c-1]["Code"]].index((Solve_One, 'Solution : N/A', 'Degree : N/A')),(Solve_One,solution,"N/A"))
                    course[Courses_data[v_c-1]["Code"]].remove((Solve_One, 'Solution : N/A', 'Degree : N/A'))
                    Update_Data()
                    Assignment_info()
                else:
                    print("you had solve this question one time ! please wait your Degree ")
            else:
                print("you not in course ")
    elif Solve_One==0:pass
    
    else:
        print("no assignment in this number")
    Update_Data()
    View_Courses_Screen()

#دالة بتدخل الدكتور لمكان التعامل مع الواجب من إضافة او حذف او تقييم لواجبات الطلاب
def operations_On_Lecturer_Courses():
    if v_c in range(1,len(Courses_data)+1):
        if Courses_data[v_c-1]["Code"] in user["Courses"]:
            view_assignment()
            print("""you had entered to course now just chose any option and i will make it for you :""")
            print("""
                [1] - Make new Assignment 
                [2] - Delete Assignment 
                [3] - Show Students Answers
                    -------------------
                [0] - Back   
                  """)
            operationincourse=int(input("Choose from[1-3] : "))
            if operationincourse==1:
                Make_assignment()
            elif operationincourse==2:
                Delete_assignment()
            elif operationincourse==3:
                Assignments_Solutions()
            else :
                View_Courses_Screen()
        else: 
            # print(f" You don,t teach this course {user["Name"]}")
            First_Screen_After_Login()
    else:
        View_Courses_Screen()

def Accept_Reqs():
    print("""[0] - Back""" )
    for i,eng in enumerate(user["Requires"],1):
        print(f"""
        [{i}] - {Courses_data[v_c-1]["Code"]} - {eng[1]} - {eng[0]}
            """)
    acception=int(input("Accept require number : "))
    if acception in range(1,len(user["Requires"])+1):
        for i in TAs_data:
            if i["Name"] == (user["Requires"][acception-1][0]):

                i["Courses"].append((user["Requires"][acception-1][1]))
                Courses_data[v_c-1]["TAs"].append(i["Name"])

                user["Requires"].remove(((user["Requires"][acception-1][0],(user["Requires"][acception-1][1]))))
                Update_Data()
                View_Courses_Screen()
            else:
                View_Courses_Screen()
    else:
        Update_Data()
        View_Courses_Screen()
#دالة بتظهر الواجب للدكتور بشكل وللطالب بشكل
def view_assignment():
    print("[0] - Back")
    if (Character_choice==1 or Character_choice==3) and (v_c in range(1,len(Courses_data)+1)) and (user["Name"] in Courses_data[v_c-1]["Lecturers"] or user["Name"] in Courses_data[v_c-1]["TAs"]):
        print(f"your Assignments in {Courses_data[v_c-1]["Name"]} Course is : ")
        for i,asst in enumerate(Courses_data[v_c-1]["Assignments"],1):
            print(f"[{i}] - {asst}")

    elif Character_choice==2 and v_c in range(1,len(Courses_data)+1) and v_c in range(1,len(Courses_data)+1) and user["Name"] in Courses_data[v_c-1]["Students"]:
        print(f"your Assignments in {Courses_data[v_c-1]["Name"]} Course is : ")
        for i in (user["Assignments"]):
            if Courses_data[v_c-1]["Code"] in i.keys(): 
                for xs in i.values():
                    for z,asst in enumerate(xs,1):
                        print(f"[{z}] - Question : {asst[0]} |   {asst[1]} |  {asst[2]}")  

    else :
        View_Courses_Screen()
#دالة بتخلي الدكتور يضع واجب
def Make_assignment():
    if v_c in range(1,len(Courses_data)+1):
        print("you can make assigment and i will share it with student who study this course")
        view_assignment()
        assignment=input("write the questions here or share file link  : ")
        if assignment not in Courses_data[v_c-1]["Assignments"]:
            Courses_data[v_c-1]["Assignments"].append(assignment)
            Update_Data()
            operations_On_Lecturer_Courses()
        else :
            print("you had update this assignment before!")
            operations_On_Lecturer_Courses()
    else:
        View_Courses_Screen()
#دالة بتخلي الدكتور يشيل الواجب
def Delete_assignment():
    if v_c in range(1,len(Courses_data)+1):
        print("you can delete assigment and i will delete it from student who study this course")
        view_assignment()
        assignment_num=int(input("write num of the questions here  : "))

        if int(assignment_num-1) in range(len(Courses_data[v_c-1]["Assignments"])):
            for stud in Students_data:
                for crse in stud["Assignments"]:
                    for crs_name,crs_values in crse.items():
                        if crs_name==Courses_data[v_c-1]["Code"]:
                            for sol in crs_values:
                                if sol[0]==(Courses_data[v_c-1]["Assignments"][assignment_num-1]):
                                    crs_values.remove(sol)
            Courses_data[v_c-1]["Assignments"].remove(Courses_data[v_c-1]["Assignments"][assignment_num-1])
            Update_Data()
            operations_On_Lecturer_Courses()
        elif assignment_num==0:
            operations_On_Lecturer_Courses()
        else :
            print("you don,t have this assignment before!")
            operations_On_Lecturer_Courses()
    else:
        Update_Data()
        First_Screen_After_Login()
#دالة بتظهر الحلول للطلاب للدكتور وبتمكنة من وضع درجات وتعليقات
def Assignments_Solutions():
    CorrectStudentName=[]
    print("[0] - Back")
    for stud in Students_data:
        if Courses_data[v_c-1]["Code"] in stud["Courses"]:
            CorrectStudentName.append(stud["Name"])
        for k,Studen in enumerate(CorrectStudentName,1):
            print(f"[{k}] - {Studen}")
        LL=int(input("Number of Student : "))

    if LL!=0 and LL in range(1,len(CorrectStudentName)+1):
        for i in Students_data:
            if i["Name"]==CorrectStudentName[LL-1]:
                if Courses_data[v_c-1]["Code"] in i["Courses"]:
                    for o in i["Assignments"]:
                        if Courses_data[v_c-1]["Code"] in o.keys():
                            x=Students_data.index(i)
                            z=(i["Assignments"]).index(o)
                            for h in o.values():
                                for j,assign in enumerate((h),1):
                                    print(f"[{j}] - Q:{assign[0]} | A:{assign[1]} | Degree:{assign[2]} ")
                            
        num_of_Question=int(input("give degree for question of num : "))
        if num_of_Question!=0 and num_of_Question in range(1,(len(Students_data[x]["Assignments"][z][(Courses_data[v_c-1]["Code"])]))+1):
            degreen=int(input("Degree for Assignment is : "))
            comment=input("your comment for Assignment is : ")
            degree=(f"{degreen} | Comment: {comment} ")
            u=[]
            for m in (Students_data[x]["Assignments"][z][(Courses_data[v_c-1]["Code"])][num_of_Question-1]):
                u.append(m)
            u.append(degree)
            del (Students_data[x]["Assignments"][z][(Courses_data[v_c-1]["Code"])][num_of_Question-1])
            Students_data[x]["Assignments"][z][(Courses_data[v_c-1]["Code"])].append((u[0],u[1],u[-1]))
            Update_Data()
            operations_On_Lecturer_Courses()
        else:operations_On_Lecturer_Courses()
    else:
        operations_On_Lecturer_Courses()
#--------------------------------------------------------------------
#قائمة الإيميلات
def Emails():
    print("""[0] Back
             [1] - View Emails 
             [2] - Send Email
          """)
    operate_in_Emails=int(input(" Choose from [0-2] : "))
    if operate_in_Emails==1:View_Emails()
    if operate_in_Emails==2:Write_Email()
    else:First_Screen_After_Login()
#إظهار الإيميلات المستلمة
def View_Emails():
    print("""[0] Back """)
    for num,Msg in enumerate(Massages,1):
        if Msg[1]==user["Name"]:
            print(f"""{num} | [ {Msg[0]} ]  """)
    want_to_join_Chat_num=int(input("I want to join chat num : "))
    if want_to_join_Chat_num!=0 and (want_to_join_Chat_num-1)<len(Massages):
        for x in Massages:
            if x[0]==Massages[want_to_join_Chat_num-1][0]:
                if Msg[1]==user["Name"]:
                    print("Time -->",x[2])
        Write_Email()
    else:Emails()
#كتابة ايميل لإرساله
def Write_Email():
    To=input("send email to : ")
    listofnamess=[]
    for s in Students_data :
        listofnamess.append(s["Name"])
    for l in Lecturers_data:
        listofnamess.append(l["Name"])
    for t in TAs_data:
        listofnamess.append(t["Name"])
    if To in listofnamess:
        MSG=input("What you want to send ? : ")
        Massages.append((user["Name"],To,MSG))
        Update_Data()
        Emails()
    else:
        print("There are no name Like This")
        Emails()
 
main_sys()

#تنظيم طلبات المعيدين والرد عليها
#50 try else لتصحيح الأخطاء    
#اضافة ايميل للدخول بجانب اليوزرنيم 10
#ضبط عدد الباسورد واليوزرنيم 10
#10 اضافة خاصية ال id وتعديل اللازم 
#ضبط التوقيتات وعمل شات بين المستخدمين

#تفعيل ال OOP
#تقعيل DB
#3000 سطر 
# اخره كمان شهر 

