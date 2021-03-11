#functions with outputs
#return

#() takes input
def format_name(f_name,l_name):
    if f_name == "" or l_name=="":
        return "You did not provide a valid inputs."
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"{formatted_fname} {formatted_lname}"

formatted_name = format_name(input("Enter your first name. "),input("Enter your last name. "))
print(f"Your name is {formatted_name}")