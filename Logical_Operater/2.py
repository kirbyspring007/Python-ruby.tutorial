input_id = input("Request id.\n")
input_pwd = input("Request pws.\n")
real_id = "egoing"
real_pwd = "11"
if real_id == input_id:
    if real_pwd == input_pwd:
        print("Hello!")
    else:
        print("Wrong pwd")
else:
    print("Wrong id")
