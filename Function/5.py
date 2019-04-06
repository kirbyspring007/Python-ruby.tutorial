input_id = input("Request ID.\n")
def login(_id):
    members = ['egoing','k8805','leezche']
    for member in members:
        if _id == member:
            return True
    return False
if login(input_id):
    print('Hello, '+input_id)
else:
    print('who are you?')
