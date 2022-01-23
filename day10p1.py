def m_f(f_name, l_name):
    if f_name=="" or l_name=="":
        return "No input."
    n=f_name.title()
    s=l_name.title()
    return f"{n} {s}"
print(m_f(input("Enter the first name:"), input("Enter the last name:")))