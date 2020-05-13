import plotly.express as px
import pandas as pd
import csv
"""
Data Visualization of the correlation between Stress, Caffeine Rating, and
Gender as given in the "DALI_Data-Anon.txt"

@author: Laurel Dernbach
@date: May 12, 2020
"""


# data file, parse into desired lists, write into CSV files
def organize_data():
    with open('DALI_Data-Anon.txt', 'r') as file:
        raw_data = file.read().replace('\n', '').strip("[]")

    gender = list()
    caffeine = list()
    stress = list()

    profiles = raw_data.split("}, {")
    for person in profiles:
        stats = person.split(",")

        stat1 = stats[1].split(":")
        gen = stat1[1].replace('"', "").strip()
        gender.append(gen)

        stat2 = stats[4].split(":")
        strs = stat2[1].strip()
        stress.append(int(strs))

        stat3 = stats[8].split(":")
        caff = stat3[1].strip()
        caffeine.append(int(caff))

    with open('caffeine_stress_data.csv', 'w') as file:
        file = csv.writer(file)

        file.writerow(['Gender', 'Caffeine', 'Stress'])
        for i in range(len(gender)):
            file.writerow([gender[i], caffeine[i], stress[i]])
    print("CSV successfully written!")


# create CSV
# organize_data()

# read CSV as pandas DataFrame
data = pd.read_csv("caffeine_stress_data.csv")

# display data as a scatter plot
fig = px.scatter(data, x="Stress", y="Caffeine", color="Gender", symbol="Gender",
                color_discrete_map={"Male":"#0000FF", "Female":"#FF1493", "Other":"#008000"},
                title="Stress and Caffeine Consumption Correlation",
                width=800, height=500)
fig.show()
