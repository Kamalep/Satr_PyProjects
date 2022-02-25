import random as r
import datetime as dt



# names list
male_names = ['Ali','Khalid','Salman','Abdallah','Hassan',
              'Fahd','Abdalaziz','Mohammed','Kamal','Hussain',
              'Abdirahman','Faisal','Saud','Iyad','Naif','Majid',
              'Badr','Bandar','Omar','Ammer','Saad','Saleh']

female_names = ['Nora','Dana','Hoor','Fatmah','Asma','Aisha','Rafa',
                'Iman','Amal','Sarah','Jood','Taraf','Reem','Aseel','Abrar',
                'Shurooq','Mashael','Ibtisam','Maha','Shahd','Hanadi','Hala'
                ]


# Function to choose a name from the names list.
def name(names) :
    return r.choice(names)

def person(gender) :
    d = {
        'FirstName' : name(male_names) if gender == 'm' else name(female_names),
        'SecondName' : 'AL-' + name(male_names),
        'Gender' : 'Male' if gender == 'm' else 'Female',
        'DateBirth': dt.date(r.randint(2000,2020),r.randint(1,12),r.randint(1,30)) ,
    }
    d['FullName'] = d['FirstName'] + ' ' + d['SecondName']
    d['Age'] = age(d['DateBirth'])
    return d

def age(birthdate):
    today = dt.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
def create_guests(n) :
    global guests
    guests = []
    for i in range(n) :
        guests.append(person(r.choice(['m','f'])))

def guest_info(card) :
    print('First name :', card['FirstName'])
    print('Full name :',card['FullName'])
    print('Age :', card['Age'])
    print('Gender :', card['Gender'])
    print('Date Birth :', card['DateBirth'])


def whois() :
    global old,young , names
    old = young = guests[0]
    names = ''
    for guest in guests :
        if guest['Age'] > old['Age'] :
            old= guest
        if guest['Age'] < young['Age']:
            young = guest
        names = names + guest['FullName'] + ', '
    names = names[:-2]

def howmany(gender) :
    count = 0
    for guest in guests:
        if guest['Gender'] == gender :
            count +=1
    return count





if __name__ == '__main__' :
    n = int(input('How many people do you want to invite to the Party :'))
    create_guests(n)
    whois()
    guest_info(old)
    guest_info(young)
    print('Guests Names :\n',names)
    print('The number of people who attended the party are',len(guests))
    print('The number of men who attended the party are',howmany('Male'))
    print('The number of women who attended the party are', howmany('Female'))








