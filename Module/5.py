import auth
input_id = input("Request ID.\n")
if auth.login(input_id):
    print('Hello, '+input_id)
else:
    print('who are you?')
