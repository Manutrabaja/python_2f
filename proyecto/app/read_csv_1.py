import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile,delimiter=',')
        country_dict = (list(reader))
        print(country_dict[0])
        
if __name__ == '__main__':
    read_csv('./proyecto/app/data.csv')