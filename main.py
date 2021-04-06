import csv
import pandas
# PLACEHOLDER = "'temp'"
# with open("weather_data.csv", "r") as weather_file:
#     weather_res = weather_file.readlines()
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temparatures = []
#     for row in data:
#         if row[1] != "temp":
#             temparatures.append(int(row[1]))
#
# print(temparatures)

data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# num = len(temp_list)
# average_temps = sum(temp_list) / len(temp_list)
# print(average_temps)
#
# print(data["temp"].mean())
# print(data["temp"].max())

#print(data[data.day =="Monday"])

# print(data.temp.max())
#
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]

print(monday.temp * (9/5) + 32)

#create a dataframe from scratch

data_dict = {
    "students" : ["Jasper", "Betuel", "Leo"],
    "scores" : [88, 87, 55]
}

new_data_frame = pandas.DataFrame(data_dict)
print(new_data_frame)

# Convert to CSV
new_data_frame.to_csv("test.csv")


