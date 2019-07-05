import pandas as pd
import os
os.chdir('C:/Users/Adrian/Documents/Data_Journalism/DataCamp\
         Lesson Datafiles/')
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

for person in flash:
    print(person)

superspeed = iter(flash)

print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))

small_value = iter(range(3))
print(next(small_value))
print(next(small_value))
print(next(small_value))

for num in range(3):
    print(num)

googol = iter(range(10 ** 100))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

values = range(10, 21)
print(values)

values_list = list(values)
print(values_list)

values_sum = sum(values)
print(values_sum)

mutants = ['charles xavier',
           'bobby drake',
           'kurt wagner',
           'max eisenhardt',
           'kitty pryde']

mutant_list = list(enumerate(mutants))
print(mutant_list)

for index1, value1 in enumerate(mutants):
    print(index1, value1)

for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)

aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']

powers = ['telepathy',
          'teleportation',
          'thermokinesis',
          'magnetokinesis',
          'intangibility']

mutant_data = list(zip(mutants, aliases, powers))
print(mutant_data)

mutant_zip = zip(mutants, aliases, powers)
print(mutant_zip)

for value1, value2, value3 in zip(mutants, aliases, powers):
    print(value1, value2, value3)

z1 = zip(mutants, powers)
print(z1)
z1 = zip(mutants, powers)
result1, result2 = zip(*z1)
print(result1 == mutants)
print(result2 == powers)

counts_dict = {}
for chunk in pd.read_csv('tweets.csv', chunksize=10):
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1
print(counts_dict)


def count_entries(csv_file, c_size, colname):
    counts_dict2 = {}
    for chunk in pd.read_csv(csv_file, chunksize=c_size):
        for entry in chunk[colname]:
            if entry in counts_dict2.keys():
                counts_dict2[entry] += 1
            else:
                counts_dict2[entry] = 1
    return counts_dict2


result_counts = count_entries('tweets.csv', 10, 'lang')
print(result_counts)
