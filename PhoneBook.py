def phonebook(phone_db):
    while True:
        print('Write Action:')
        print('1.Add Contact\n2.Find Contact ')
        action = input('>>>>')
        print('-----------')
        if action == '1':
            contact_info  = input('write name surname of new contact( trough space): ')
            contact_phone_number = int(input('write phone number '))
            contact_info_key = {tuple(contact_info.split(" ")):contact_phone_number}
            for i_info in phone_db:
                if i_info in contact_info_key.keys():
                    print('the contact with name included is exist: ')
            phone_db.update(contact_info_key)
            print('------------------------')
        elif action == '2':
            user_info = input('write contact name : ')
            # user_info_dict = dict(user_info.split(" "))
            for i_index in phone_db.keys():
                    if i_index == tuple(user_info.split(" ")):
                       print('Contact Name: ',i_index[0],i_index[1])
                       print('Phone Number: ',phone_db[i_index])
            print("----------------------")

        else:
            print('Incorrect action try again!!!')




phonebook_dict = {
    ('Arsen', 'Torosyan'):374919432564,
    ('Babken' ,'Sargsyan'):3749393523654,
    ('Sargis', 'Sargsyan'):37499652536,
    ('Aram ','Aramyan'):37491582136
}
phonebook(phonebook_dict)