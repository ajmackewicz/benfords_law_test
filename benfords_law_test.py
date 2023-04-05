import matplotlib
from matplotlib import pyplot as plt
from collections import defaultdict
import pandas as pd


# Variables
default_numb_data = 500
input_path = "population_data.xlsx"
output_path = "out_population.csv"


# Get data
numb_data = input("Enter the number of county populations to be graphed: ")
if not numb_data.isnumeric(): # Check if numb_data was skipped
	print(f"Number defaulted: {default_numb_data}")
	numb_data = default_numb_data
else: # If there was some input
	numb_data = int(numb_data) # then let it be the number
	
print(f"Number to be parsed: {numb_data}")

dataframe = pd.read_excel(input_path, header=None, names=["Population"], skiprows=range(0, 5), nrows=numb_data, usecols='B')

print(dataframe)

dataframe.to_csv(output_path)


# Parse csv data into matplotlib
count_numbers = [0] * 10

clean_frame = pd.read_csv(output_path, skiprows=0, nrows=numb_data, usecols=["Population"])

numb_parsed = numb_data
for i in range(0, numb_data):
	str_item = str(clean_frame.iat[i, 0])

	if str_item.lower() != "nan":
		start_item = int(str_item[0])
		count_numbers[start_item] += 1
	else: 
		numb_parsed = i
		print(f"Number of data parsed: {numb_parsed}\nEnd of data.")
		break
		
percent_numbers = [100 * x / numb_parsed for x in count_numbers[1:]]


# Output
print()
print(f"Number parsed: {numb_parsed}")
print("Digits and their counts:")
print(count_numbers)

fig, ax = plt.subplots()

ax.bar(range(1, 10), percent_numbers, label=str(range(1, 10)), color="tab:blue")
plt.xticks(range(1, 10))
ax.set_xlabel("digit")
ax.set_ylabel("frequency (%)")
ax.set_title(f"Frequency of First Digit for Data Set ({numb_parsed})")

plt.show()
