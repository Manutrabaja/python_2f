
# def get_population():
#     keys = ['col', 'bol']
#     values = [30country_dict['2022 Population'], 400]
#     return keys, values

# def population_by_country(data, country):
#     result = list(filter(lambda x : x['Country'] == country, data))
#     return result

"""reutilisando funciones para el proyecto"""

def get_population(result):
    population_dict = {
        '1970' : result['1970 Population'],
        '1980' : result['1980 Population'],
        '1990' : result['1990 Population'],
        '2000' : result['2000 Population'],
        '2010' : result['2010 Population'],
        '2015' : result['2015 Population'],
        '2020' : result['2020 Population'],
        '2022' : result['2022 Population'],
    }
    labels = population_dict.keys() 
    values = population_dict.values()
    return  values, labels

def population_by_country(data, country):
    result = list(filter(lambda x : x['Country'] == country, data))
    return result[0]