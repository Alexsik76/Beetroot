from vehicles2 import save_csv, standard_data, read_csv
price_of_fuel = 25
# data = generate.generate()
data = standard_data.standard_vehicles()
path = input('Enter file name for the standard data:') + '_st.csv'
save_csv.csv_writer(data, path)
data = read_csv.read(path)
print(data)
# statistic.statistic(data)
