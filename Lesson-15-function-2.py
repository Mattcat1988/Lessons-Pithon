def create_record(name, telephone, address):
    """Create Record"""

    record = {
        'name': name,
        'phone': telephone,
        'address': address

    }
    return record


user1 = create_record("Vasya", "123123123123", "tunis")
user2 = create_record("Petya", "23424234", "cassia")
print(user1)
print(user2)


def give_award(medal, *persons):
    """Give Medals to persons"""
    for person in persons:
        print("Tovarisch " + person.title() + " nagrazdaeca medaliu " + medal)


give_award("Za Berlin", "Vasya", "Petya")
give_award("Za London", "Petya", "alexander", "valentin")
