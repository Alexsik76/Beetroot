from vehicles2 import save_csv, generate

price_of_fuel = 25
data = generate.generate()
path = input('Enter file name for the data:') + '.csv'
save_csv.csv_writer(data, path)
# data = read_csv.read(path)
# print(data)
# statistic.statistic(data)
