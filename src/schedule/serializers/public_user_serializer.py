

def public_user(user):
    return {
        'cpf_user'  : user['cpf_user'],
        'birth_date': user['birth_date'],

        'fullname': user['fullname'],
        'mother_name':user['mother_name'],
        'phone_number':user['phone_number'],
        
        'status':user['status']
    }