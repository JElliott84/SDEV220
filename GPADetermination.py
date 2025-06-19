#Jason Elliott
#GPADetermination
#This app should allow the user to input whether or not their GPA is on the Deans List or Honor Roll

student_lastname = input("What is your last name? Enter ZZZ to stop")

if student_lastname == "ZZZ":
    print("Sorry, you have quit")

else:
    student_firstname = input("What is your first name?")
    GPA_number = input( "What is your GPA?")
    GPA = float(GPA_number)

    if GPA >= 3.5:
        print (student_firstname, ",You have made the deans list!")

    elif GPA >= 3.25 and GPA < 3.5:
        print (student_firstname, ",You have made the Honor Roll")

    else:
        print (student_firstname, "You did not make the list!")

    