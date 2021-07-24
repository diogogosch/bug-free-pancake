import user

user_00 = user.UserClass('Diogo','04188442913','diogogosch@gmail.com','41988880087')
user_01 = user.UserClass('Ruy','51459418972','rvieirag@gmail.com','47984349315')
print(user_01.id)
print(user_01.name)
print(user_01.cpf)
print(user_01.email)
print(user_01.phone_number)
print(user_01.created_at)
print(user_01.updated_at)

user_01.name = 'Henrique'
print(user_01.name)
print(user_01.updated_at)

if __name__ == '__main__':
    print('app.py sendo executado')