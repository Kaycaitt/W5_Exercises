address_dictionary  = {
    'name': 'Elena Gilbert',
    'address': '2104 Maple Street',
    'city': 'Mystic Falls',
    'state': 'Virginia',
    'zip': 73528
}

print(f"""{address_dictionary['name']}
{address_dictionary['address']}
{address_dictionary['city']},
{address_dictionary['state']},
{address_dictionary['zip']}""")

#noting that the output needs curly braces around each dictionary item that needs to be retrieved. Also need to refer to the specific dictionary collection when pulling the data.

del address_dictionary['name']

full_name = (
    {'first_name': 'Liv'},
    {'last_name': 'Parker'}
)

address_dictionary.update({'honorific': 'Ms.'})
address_dictionary.update({'first_name': 'Liv'})
address_dictionary.update({'last_name': 'Parker'})
#It took almost an hour, but I figured out that the tuple was not saving because I didn't add the update commands to first and last name.

print(f"""{address_dictionary['honorific']} {address_dictionary['first_name']} {address_dictionary['last_name']}
{address_dictionary['address']}
{address_dictionary['city']},
{address_dictionary['state']} {address_dictionary['zip']}""")