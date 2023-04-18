import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))

    if len(countries) != len(percentages):
        print("Error: El número de países y porcentajes debe ser el mismo.")
        return

    charts.generate_pie_chart(countries, percentages)

    country = input("Digite el país: ")

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
    run()
