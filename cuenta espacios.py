def check_space(string):
    count = 0
     
    # loop for search each index
    for i in string:
         
        # Check each char
        # is blank or not
        if i == " ":
            count += 1
         
    return count
 
# driver node
string = "Welcome to geeksforgeeks, Geeks!"
 
# call the function and display
print("number of spaces ",check_space(string))
