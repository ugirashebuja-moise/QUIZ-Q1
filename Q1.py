def calculate_grade(score):
    if  80<=score: 
        return ("Distinction")
    elif 60<=score<=79: 
        return ("Credit")
    elif 50<=score<=59: 
        return ("Pass")
    else:
        return ("Fail")
print (calculate_grade(50.1))