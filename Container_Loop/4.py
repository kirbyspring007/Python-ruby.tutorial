input_id = input("Request ID.\n")
members = ['egoing','k8805','leezche']
for member in members:
    if input_id == member:
        print('Hello!, '+member)
        import sys
        sys.exit()
print('who are you?')
