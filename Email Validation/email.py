email = input("enter your email address:")
k = 0
j = 0
d = 0
if len(email) >= 6:  # smallest email address is 6 characters long for example g@g.in
    if email[0].isalpha():  # email should start with an alphabet
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):  # dot should be present at thrid last or fourth last position
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("wrong email")
                else:
                    print("right email")

            else:
                print("invalid position of dot")

        else:
            print("email should contain exactly one @ symbol")
    else:
        print("email should start with an alphabet")



else:
    print("email should be atleast 6 characters long")
