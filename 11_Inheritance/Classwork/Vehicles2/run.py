from vehicles import generate, save_csv, read_csv, statistic

data = generate.generate()
path = input('Enter file name for the data:') + '.csv'
save_csv.csv_writer(data, path)
data = read_csv.read(path)
statistic.statistic(data)
