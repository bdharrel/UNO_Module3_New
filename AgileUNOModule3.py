# Module 3 Assignment
# Bridget D. Harrell

myfile = open("question.txt", "r+")

myquestion = myfile.read()

myresponse = input(myquestion)

myfile.write(myresponse)

myfile.close()
