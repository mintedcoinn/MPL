import random
import pandas
from concurrent.futures import ProcessPoolExecutor as ppexe

csv_filenames = ("file1.csv","file2.csv","file3.csv","file4.csv","file5.csv")
agg_functions = ["median", "std"]
letters = ["A", "B", "C", "D"]


def WriteToCSV(count = 10):# создание данных и запись в csv файлы
    for j in csv_filenames:
        letter_index = [] #нельзя использовать словарь тк буквы не уникальные
        num_data = []

        for i in range(count):
            letter_index.append(random.choice(letters))
            num_data.append(random.random()*100)
        
        data_dict = {"category":letter_index,
                     "value":num_data}
        
        file_cont = pandas.DataFrame(data_dict)
        file_cont.to_csv(j, index=False)


def StatsOperTier1(filename): # группировка по букве и вычисление медианы и стандартного отклонения
    data = pandas.read_csv(filename)
    proc_data = data.groupby(["category"]).agg({"value": agg_functions})
    return proc_data


def StatsOperTier2(concatdata): # объедененные в один датафрейм данные группируем и вычисляем необходимое
    proc_data = concatdata.groupby(["category"]).agg({('value',"median"):agg_functions})
    return proc_data


if __name__ == '__main__':# как я понял точка входа в программу на питоне обозначается так
    WriteToCSV(150)    
    with ppexe(max_workers=5) as executor:
        results = list(executor.map(StatsOperTier1, csv_filenames))
        concdata = pandas.concat(results)
    print(StatsOperTier2(concdata))
    
