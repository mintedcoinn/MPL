import csv
import random
import pandas

csv_files = ("file1.csv","file2.csv","file3.csv","file4.csv","file5.csv")



for j in csv_files:
    letter_index = [] #нельзя использовать словарь тк буквы не уникальные
    num_data = []

    for i in range(10):
        letters = ["A", "B", "C", "D"]
        letter_index.append(random.choice(letters))
        num_data.append(random.random()*100)
    
    data_dict = {"category":letter_index,
                 "value":num_data}
    file_cont = pandas.DataFrame(data_dict)
    file_cont.to_csv(j)

