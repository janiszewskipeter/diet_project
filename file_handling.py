def import_data(filename):
    '''
    data_format = [['ID', 'Name', 'Calories', 'Restrictions'],\
            ['726dbj', 'Vegan', 1456, 'Vegan, Vegetarian, LowFat'], \
            ['ndkw23', 'Vegetarian', 1342, 'Vegetarian, LowFat'] \
            ['sdq345', 'Low Fat', '1225', 'LowFat'] \
            ['uek937', 'Paleo Diet', '1876', ''] \
            ['hg92k1', 'Mediterranean Diet', 1763, '']]
    '''

    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.strip().split(','))

    return data


def data_export(filename, data):
    '''
    profile_format = [['ID','Name', 'Weight', 'Height', 'BMI', Restrictions],\
                ['ddve90','John', 134, 176, 72, 'Vegan'], \
                ['fkl78Q', 'Mario', 122, 165, 87, 'Vegetarian'], \
                ['hgt423', 'Gustav', 98, 170, 67, ''], \
                ['ubk329', 'Sam', 152, 201, 78, 'LowFat'], \
                ['mq820w', Mirek, 132, 186, 74, ' ']
    '''

    with open(filename, 'w') as f:
        for line in data:
            f.write(line)


