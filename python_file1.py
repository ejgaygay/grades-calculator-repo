import os
import sys
from os import path
#Open a file and have its contents be a list for us
#first element of files that are not the max will always have the weighting
def openFileAsList(inputfilename):
    try:
        file = open(inputfilename, 'r')
        pointsOfData = ""
        for numbers in file.readlines():
            pointsOfData += (numbers)
        pointsOfData = pointsOfData.split()
        return pointsOfData
    except IOError:
        create_file(inputfilename)
        openFileAsList(inputfilename)
        
def create_file(inputfilename):
    inputfilename = inputfilename.replace(" ",'')
    if path.exists(inputfilename) == False:
        file = open(inputfilename, 'w')
        file.close()
    else:
        return "File exists already"

def initialize_file(inputfilename):
    classes = open("classes.txt", 'a')
    classes.write(inputfilename.replace('.txt','') + " ")
    category = ""
    while category.lower() != "q":
        print("enter the categories that go into your final grade (q) to quit ")
        category = input("What category of grading is this? ")
        if category.lower() != "q":
            x = create_file(inputfilename.replace('.txt','') + "_categories.txt")
            f = open(inputfilename.replace('.txt','') + "_categories.txt", 'a')
            f.write(category + " ")
            catFile = inputfilename.replace('.txt','') + "_" + category + ".txt"
            weight = input("How much does this category weigh in on the final grade? ")
            f.write(weight + " ")
            file = os.path.basename(catFile)
            add_points(file)
    classes.close()

def calculate_grade(filename):
    fileName = filename + "_final_grade.txt"
    create_file("grades.txt")
    create_file(fileName)
    categories = openFileAsList(filename+"_categories.txt")
    pointsEarned = []
    maxPoints = []
    categoryWeight = []
    x = 1
    while x < len(categories):
        categoryWeight.append(categories[x])
        categories.pop(x)
        x += 1
    for items in categories:
        points = 0
        maxP = 0
        pointsMax = openFileAsList(filename + "_" + items + "_max.txt")
        pointsCat = openFileAsList(filename +"_"+ items + '.txt')
        for point in pointsCat:
            points += float(point)
        for point in pointsMax:
            maxP += float(point)
        pointsEarned.append(points)
        maxPoints.append(maxP)
    file = open(filename+"_final_grade.txt",'w')
    finalGrade = 0
    for index in range(len(categories)):
        file.write(str(categories[index]) + ": " + str(round((pointsEarned[index]/maxPoints[index]*int(categoryWeight[index])),2)) + "/" +str(categoryWeight[index]) +"\n")
        finalGrade += (pointsEarned[index]/maxPoints[index])*int(categoryWeight[index])
    if finalGrade > 92.5:
        letterGrade = "A"
    elif finalGrade >= 89.5 and finalGrade < 92.5:
        letterGrade = "A-"
    elif finalGrade >= 86.5 and finalGrade < 89.5:
        letterGrade = "B+"
    elif finalGrade >= 82.5 and finalGrade < 86.5:
        letterGrade = "B"
    elif finalGrade >= 79.5 and finalGrade < 82.5:
        letterGrade = "B-"
    elif finalGrade >= 76.5 and finalGrade < 79.5:
        letterGrade = "C="
    elif finalGrade >= 72.5 and finalGrade < 76.5:
        letterGrade = "C"
    elif finalGrade >= 69.5 and finalGrade < 72.5:
        letterGrade = "C-"
    elif finalGrade >= 66.5 and finalGrade < 69.5:
        letterGrade = "D+"
    elif finalGrade >= 62.5 and finalGrade < 66.5:
        letterGrade = "D"
    elif finalGrade >= 60 and finalGrade < 62.5:
        letterGrade = "D-"
    else:
        letterGrade = "F"
    grades = open("grades.txt", 'a')
    file.write("\nFinal Grade: " + letterGrade + " : " + str(round(finalGrade,2)) + "/" + str(100))
    grades.write(filename + " : " + letterGrade + " : " + str(round(finalGrade,2)) + "/" + str(100) + "\n")
    file.close()
    grades.close()
    
def view_class_grade(filename):
    os.startfile(filename + "_final_grade.txt")

#initialize the student assignments file along with the max points file without categories
def add_points(inputfilename):
    maxFile = inputfilename.replace('.txt','') + "_max.txt"
    create_file(inputfilename)
    create_file(maxFile)
    file = open(inputfilename, 'w')
    max_file = open(maxFile, 'w')
    x = ""
    while x != "n":
        x = input("Enter the points you received on an assignment \"n\" to quit ")
        x = x.strip()
        if x != "n":
            y = input("Enter the max points for the assignment ")
            y = y.strip()
            file.write(x + " ")
            max_file.write(y + " ")
        print()
    file.close()
    max_file.close()

#This program makes a lot of files so we should probably clean it up
def cleanUP():
    classes = openFileAsList("classes.txt")
    for files in os.listdir():
        for Class in classes:
            if Class in os.path.basename(files):
                os.remove(files)

#This gives us a file with all of the data from the text files call this with the cleanup to really clean up 
def makeCleanFile():
    
#Work on making it so you can add on to assignment points and such
def edit_file(inputfilename):
    file_contents = openFileAsList(inputfilename)

def calculate_all_grades():
    f = open("grades.txt",'w')
    f.close()
    classes = openFileAsList("classes.txt")
    for Class in classes:
        calculate_grade(Class)
    openSemesterGrades()

def openSemesterGrades():
    os.startfile("grades.txt")

def main():
    if os.path.exists("classes.txt") == False:
        os.startfile("GradeCalculatorInstructions.txt")
        print("We see that you do not have a gradebook set up for this term. \nLet's get you set up with one\nPlease delete all of the text files at the end of your term!\n")
        y = ""
        while y.lower() != "q":
            y = input("Enter the names of your classes (q) to quit ")
            if y.lower() != "q":
                className = y.replace(" ", "")
                className += ".txt"
                initialize_file(className)
    x = ""
    while x.lower() != "q":
        x = input("Hello!\nEnter a mode:\n(Q):Quit\n(V):View All Grades\n(A):Add Class\n(E):Edit Data \n(C):View a Grade\n(R):Reset Semester\n")
        if x.lower() == "v":
            calculate_all_grades()
        elif x.lower() == "a":
            className = input("Enter the class name ")
            className = className.replace(" ","")
            className += ".txt"
            initialize_file(className)
        elif x.lower() == "c":
            classes = openFileAsList("classes.txt")
            number = 1
            for items in classes:
                print(str(number) + ": " + items)
                number += 1
            index = input("which class would you like to see the final grade for? ")
            try:
                index = int(index)
            except:
                print("error")
            view_class_grade(classes[index-1])
        elif x.lower() == "r":
            classes = openFileAsList("classes.txt")
            for files in os.listdir():
                for Class in classes:
                    if Class in os.path.basename(files):
                        os.remove(files)
            os.remove("grades.txt")
            os.remove("classes.txt")
            os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
        elif x.lower() == "q":
            quit()
if __name__ == '__main__':
    main()
