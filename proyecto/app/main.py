import utils as utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('./proyecto/app/data.csv')
    nombre = input('type Country =>  ')
    country = nombre.title()
    # print(f'the country', country)

    result = utils.population_by_country(data, country)
    # print(result)

    if len(result) > 0 :
        labels, values = utils.get_population(result)
    # print(values, labels)
    charts.generate_bar_chart(labels, values)



if __name__ == '__main__':
    run()