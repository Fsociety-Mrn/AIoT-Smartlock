from validate_email_address import validate_email

def validate_credentials(email,password):
    
    data = {
        'Email': {
            'message': 'Message',
            'status': False
        },
        'Password': {
            'message': 'Message',
            'status': False
        }
    }

    
    # Validate email address
    if validate_email(email):
        data['Email']['message'] = ""
        data['Email']['status'] = False
    else:
        data['Email']['message'] = "Invalid email address"
        data['Email']['status'] = True      

    # Check password length
    if not len(password) < 6:
        data['Password']['message'] = ""
        data['Password']['status'] = False
    else:
        data['Password']['message'] = "Password should min 6 character"
        data['Password']['status'] = True        
    

    return data

# Example usage
# email = "examplhotsd-maddasdasdasdsdasdil.com"
# password = "password123"

# print(validate_credentials(email,password)['Email']['message'])
# if validate_credentials(email, password):
#     print("Credentials are valid!")
# else:
#     print("Invalid credentials.")
