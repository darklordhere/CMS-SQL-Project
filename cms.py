import mysql.connector as connector

mycon = connector.connect( host='localhost',port='3306', user='root', password="cshp", database="cmssql" )
mycursor = mycon.cursor()

# Function to display the menu

def mainmenu():
    print("*"*144)
    print(" COURSE MANAGEMENT SYSTEM ".center(140))
    print("MAIN MENU".center(140))
    print("1. ENROLL IN COURSE".center(140))
    print("2. CHECK THIS YEAR ENROLLMENT DETAILS".center(140))
    print("3. CHECK DETAILS BY ENTERING ID-NO".center(140))
    print("4. UPDATE REGISTRATION INFO".center(140))
    print("5. DELETE REGISTRATION INFO".center(140))
    print("6. REPORT AN ISSSUE OR SUBMIT FEEDBACK".center(140))
    print("7. ABOUT US - CONTACT US".center(140))
    print("8. EXIT".center(140))
    print("*"*144)

# Function to create table


def Create():
    try:
        mycursor.execute("CREATE TABLE IF NOT EXISTS info(NAME varchar(255), AGE int , IDNO int primary key auto_increment , BRANCH varchar(255) , COURSE varchar(255) , CITY varchar(255) , COUNTRY varchar(255) , EMAIL varchar(255) )")
        print("FILL YOUR DETAILS BELOW")
        Insert()
    except:
        print(" INVALID INPUT")


# Function for inserting data ( enroll in course)


def Insert():
    name = input("Enter your name :")
    age = int(input("Enter your age :"))
    idno = int(input("Enter your idno :"))
    branch = input("Enter your branch / stream :")
    course = input("Enter course which you want :")
    city = input("Enter city where you live in :")
    country = input("Enter country where you live in :")
    email = input("Enter your email :")
    xbb = """INSERT INTO info(NAME, AGE , IDNO, BRANCH, COURSE , CITY , COUNTRY , EMAIL)VALUES ('{}',{}, {}, '{}','{}', '{}' , '{}', '{}')"""
    mycursor.execute(xbb.format(name, age, idno, branch,
                                course,  city, country, email))
    mycon.commit()
    while True:
        lnz = input("TO SUBMIT YOUR REGISTRATION PRESS ( Y / y ):")
        if lnz == "y" or lnz == "Y":
            break
            print("YOUR DATA IS ADDED")


# Function to Display records as per ascending order of name


def dispsortname():
    try:
        cmd = "select * from info order by NAME"
        mycursor.execute(cmd)
        S = mycursor.fetchall()
        F = "%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("NAME", "AGE", "IDNO", " BRANCH",
                   "COURSE", "CITY", "COUNTRY", "EMAIL"))
        print("="*144)
        for i in S:
            for j in i:
                print("%15s" % j)
            print()
        print("="*144)
    except:
        print("Table doesn't exist")

# Function to Search for the Record from the File with respect to idno


def display_record_by_idno():
    try:
        lop = "select * from info"
        mycursor.execute(lop)
        k = mycursor.fetchall()
        mz = int(input("ENTER THE ID-NO TO BE SEARCHED :"))
        for i in k:
            if i[2] == mz:
                print("="*144)
                o = "%15s %15s %15s %15s %15s %15s %15s %15s"
                print(o % ("NAME", "AGE", "IDNO", " BRANCH",
                           "COURSE", "CITY", "COUNTRY", "EMAIL"))
                print("="*144)
                for j in i:
                    print('%15s' % j, end=' ')
                print()
                break
        else:
            print("Record Not found")
    except:
        print("Table doesn't exist")


# Function to update details of the person who enrolled in course

def update():
    try:
        nill = "select * from info"
        mycursor.execute(nill)
        J = mycursor.fetchall()
        Mk = int(input("ENTER THE ID-NO WHOSE DETAILS TO BE CHANGED :"))
        for h in J:
            h = list(h)
            if h[2] == Mk:
                p = input("Change Name(Y/N) :")
                if p == 'y' or p == 'Y':
                    h[0] = input("Enter Name :")

                e = input("Change Age(Y/N) :")
                if e == 'y' or e == 'Y':
                    h[1] = int(input("Enter Age :"))

                p = input("Change Branch(Y/N) :")
                if p == 'y' or p == 'Y':
                    h[3] = input("Enter Branch :")

                p = input("Change Course(Y/N) :")
                if p == 'y' or p == 'Y':
                    h[4] = input("Enter Course :")

                p = input("Change City(Y/N) :")
                if p == 'y' or p == 'Y':
                    h[5] = input("Enter City :")

                p = input("Change Country(Y/N) :")
                if p == 'y' or p == 'Y':
                    h[6] = input("Enter Country :")

                u = input("Change Email(Y/N) :")
                if u == 'y' or u == 'Y':
                    h[7] = input("Enter Email :")
                nill = """ UPDATE info SET NAME=%s, AGE=%s, BRANCH=%s , COURSE=%s, CITY=%s, COUNTRY=%s, EMAIL=%s WHERE IDNO=%s"""
                vac = (h[0], h[1], h[3], h[4], h[5], h[6], h[7], h[2])
                mycursor.execute(nill, vac)
                mycon.commit()
                print("ENROLLMENT DETAILS UPDATED")
                break
        else:
            print(" record not found")
    except:
        print(" invalid details")


# Function to delete the details of enrolle.

def delete():
    try:
        cmd = "select * from info"
        mycursor.execute(cmd)
        df = mycursor.fetchall()
        uii = int(input("ENTER THE ID-NO WHOSE DETAILS TO BE DELETED :"))
        for q in df:
            q = list(q)
            if q[2] == uii:
                ops = "delete from info where idno=%s"
                dff = (q[2],)
                mycursor.execute(ops, dff)
                mycon.commit()
                print("ACCOUNT DELETED")
                break
        else:
            print("Record not found")
    except:
        print("No such Table")


# function for report and sending feedback

def report():
    try:
        mycursor.execute(
            " CREATE TABLE IF NOT EXISTS repofed( id_no int , NAME varchar(255) , REPORT varchar(255) , FEEDBACK varchar(255))")
        fxx()
    except:
        print(" INVALID DETAILS")


# function for adding report and feedback with id_no and name

def fxx():
    idno = int(input("Enter your idno :"))
    name = input("Enter your name :")
    report = input("WRITE YOUR REPORT OR ISSUE :")
    feedback = input("WRITE YOUR FEEDBACK :")
    xmm = """ INSERT INTO repofed( id_no , NAME , REPORT , FEEDBACK )VALUES( {} , '{}' , '{}' , '{}' )"""
    mycursor.execute(xmm.format(idno, name, report, feedback))
    mycon.commit()
    while True:
        kjj = input(" TO SUBMIT YOUR REPORT OR FEEDBACK PRESS ( Y /y ) :")
        break


# function for about us

def about():
    print("="*144)
    print(" ABOUT US ".center(140))
    print("="*144)
    print(" PROJECT : COURSE MANAGEMENT SYSTEM ( CMS ) ".center(140))
    print(" PROJECT CREATED BY : SOURAV SINGH ".center(140))
    print(" 12 SCIENCE - A ".center(140))
    print("="*144)
    print(" CONTACT US ".center(140))
    print(" CONTACT NUMBER : 7678632149".center(140))
    print(" CMSCOURSE.COM".center(140))
    print(" HNO-3 , PRATAP VIHAR , GHAZIABAD ( 201009 )".center(140))
    print("="*144)


while True:
    mainmenu()
    ch = int(input(" ENTER YOUR CHOICE : "))
    if ch == 1:
        Create()
        print(" YOU ARE NOW ENROLLED IN COURSE !")

    elif ch == 2:
        dispsortname()
        break

    elif ch == 3:
        display_record_by_idno()
        break

    elif ch == 4:
        update()
        break

    elif ch == 5:
        delete()
        break

    elif ch == 6:
        report()
        print(" YOUR REPORT OR FEEDBACK IS SUBMITTED ")
        break

    elif ch == 7:
        about()
        break

    elif ch == 8:
        print(" EXITING..../n THANKS FOR VISITING !!!")
        break

    else:
        print(" KINDLY REFRESH THE PAGE....")
