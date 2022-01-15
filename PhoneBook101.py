
# declaration Dictionary is named Phone Book contains Names and Phone Numbers.
PhoneBook = {
    1 : {
        'name' : 'Rafa',
        'Phone' : '1'
},
    2 : {
        'name' :'Dana',
        'Phone' : '2'
},
    3 : {
        'name' : 'Abdalaziz',
        'Phone' : '3'
},
    4 : {
        'name' :'Nora',
        'Phone' : '4'
},
    5 : {
        'name' : 'Joseph',
        'Phone' : '5'
},
    6 : {
        'name' :'Daniel',
        'Phone' : '6'
},
    7 : {
        'name' : 'Shaikh Maeroof',
        'Phone' : '7'
},
    8 : {
        'name' :'Furgan',
        'Phone' : '8'
},
    9 : {
        'name' :'Kamal',
        'Phone' : '9'
}
}


# function to looking who's the owner the number.
def get_name(number) :
    output = None
    for i in PhoneBook.keys() :
        for k,v in PhoneBook[i].items() :
            if v== number :
                output = f'The owner of the number {v} is {PhoneBook[i]["name"]}'
    return output

while True :
    # getting the number from user
    get_number = input("May you tell me What\'s the number are you looking for ? : ")
    name = get_name(get_number)
    if name == None :
        print('Phone Number Not Detected')
        press = input('To exit Press [ 1 ] or press anykey to continue : ')
        if press == '1' : break
    else:
        print(name)
        press = input('To exit Press [ 1 ] or press anykey to continue : ')
        if press == '1' : break