import json

data_to_write = {
    'places': [

    ],
    'inquires': [

    ],
    'bookings': [

    ]
}

data_to_write = {
    'places': [
        {
            'name': 'blue box',
            'type': 'apartment',
            'address': 'southampton',
            'available_rooms': '5',
            'cost_per_night': '20'
        },
        {
            'name': 'green box',
            'type': 'apartment',
            'address': 'portsmouth',
            'available_rooms': '2',
            'cost_per_night': '12'
        }
    ],
    'inquires': [
        {
            'accom_name': 'green box',
            'inquiry': 'waguan for dis place?'
        },
        {
            'accom_name': 'green box',
            'inquiry': 'how can this building be called green box?! LMAO'
        },
    ],
    'bookings': [
        {
            'accom_name': 'blue box',
            'customer_name': 'Neal Rigger',
        },
        {
            'accom_name': 'blue box',
            'customer_name': 'Holdin Hiscock',
        },
    ]
}


# storage.remove_data('places', 'name', 'cc')

# storage.save_data({'name': 'cc', 'age': '2'}, 'places')
