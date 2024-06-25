
# def get_population():
#     keys = ['col', 'bol']
#     values = [30country_dict['2022 Population'], 400]
#     return keys, values

# def population_by_country(data, country):
#     result = list(filter(lambda x : x['Country'] == country, data))
#     return result

"""reutilisando funciones para el proyecto"""

def get_population(country_dict):
    population_dict = {
        '2022 Population' : country_dict ,
        '2020' : country_dict['2020 Population'],
        '2015' : country_dict['2015 Population'],
        '2010' : country_dict['2010 Population'],
        '2000' : country_dict['2000 Population'],
        '1990' : country_dict['1990 Population'],
        '1980' : country_dict['1980 Population'],
        '1970' : country_dict['1970 Population'],
    }
    labels = population_dict.keys() 
    values = population_dict.values()
    return  values, labels

def population_by_country(data, country):
    result = list(filter(lambda x : x['Country'] == country, data))
    return result[0]