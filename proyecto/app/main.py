import utils as utils
import read_csv
import charts

"""grafica poblacion de un pais"""
def run():
    data = read_csv.read_csv('./proyecto/app/data.csv')
    # nombre = input('type Country =>  ')
    # country = nombre.title()
    # # print(f'the country', country)

    # result = utils.population_by_country(data, country)
    # # print(result)

    # if len(result) > 0 :
    #     labels, values = utils.get_population(result)
    # # print(values, labels)
    # charts.generate_bar_chart(labels, values)



# """ grafica publacion mundial"""
    
    nombre = input('type Continet =>  ')
    continet = nombre.title()
    result = list(filter(lambda x : x['Continent'] == continet, data))
    ciudades = list(map(lambda x : x['Country'],result))
    P_mundial = list(map(lambda y : y['World Population Percentage'], result))
    # print(ciudades,P_mundial)
    charts.generate_pie_chart(ciudades, P_mundial)
if __name__ == '__main__':
    run()