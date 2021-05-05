import numpy as np

dic_workclass = {

    "Private": 0,
    "Self-emp-not-inc": 1,
    'Self-emp-inc': 2,
    "Federal-gov": 3,
    "Local-gov": 4,
    "State-gov": 5,
    "Without-pay": 6,
    "Never-worked": 7,
    "?": -1

}

dic_education = {

    "Bachelors": 0,
    "Some-college": 1,
    "11th": 2,
    "HS-grad": 3,
    "Prof-school": 4,
    "Assoc-acdm": 5,
    "Assoc-voc": 6,
    "9th": 7,
    "7th-8th": 8,
    "12th": 9,
    "Masters": 10,
    "1st-4th": 11,
    "10th": 12,
    "Doctorate": 13,
    "5th-6th": 14,
    "Preschool": 15,
    "?": -1

}

dic_marital_status = {

    "Married-civ-spouse": 0,
    "Divorced": 1,
    "Never-married": 2,
    "Separated": 3,
    "Widowed": 4,
    "Married-spouse-absent": 5,
    "Married-AF-spouse": 6,
    "?": -1

}

dic_occupation = {

    "Tech-support": 0,
    "Craft-repair": 1,
    "Other-service": 2,
    "Sales": 3,
    "Exec-managerial": 4,
    "Prof-specialty": 5,
    "Handlers-cleaners": 6,
    "Machine-op-inspct": 7,
    "Adm-clerical": 8,
    "Farming-fishing": 9,
    "Transport-moving": 10,
    "Priv-house-serv": 11,
    "Protective-serv": 12,
    "Armed-Forces": 13,
    "?": -1

}

dic_relationship = {

    "Wife": 0,
    "Own-child": 1,
    "Husband": 2,
    "Not-in-family": 3,
    "Other-relative": 4,
    "Unmarried": 5,
    "?": -1
}

dic_race = {

    'White': 0,
    "Asian-Pac-Islander": 1,
    "Amer-Indian-Eskimo": 2,
    "Other": 3,
    "Black": 4,
    "?": -1
}

dic_sex = {

    "Female": 0,
    "Male": 1,
    "?": -1
}

dic_native_country = {

    "United-States": 0,
    "Cambodia": 1,
    "England": 2,
    "Puerto-Rico": 3,
    "Canada": 4,
    "Germany": 5,
    "Outlying-US(Guam-USVI-etc)": 6,
    "India": 7,
    "Japan": 8,
    "Greece": 9,
    "South": 10,
    "China": 11,
    "Cuba": 12,
    "Iran": 13,
    "Honduras": 14,
    "Philippines": 15,
    "Italy": 16,
    "Poland": 17,
    "Jamaica": 18,
    "Vietnam": 19,
    "Mexico": 20,
    "Portugal": 21,
    "Ireland": 22,
    "France": 23,
    "Dominican-Republic": 24,
    "Laos": 25,
    "Ecuador": 26,
    "Taiwan": 27,
    "Haiti": 28,
    "Columbia": 29,
    "Hungary": 30,
    "Guatemala": 31,
    "Nicaragua": 32,
    "Scotland": 33,
    "Thailand": 34,
    "Yugoslavia": 35,
    "El-Salvador": 36,
    "Trinadad&Tobago": 37,
    "Peru": 38,
    "Hong": 39,
    "Holand-Netherlands": 40,
    "?": -1

}
dic_50 = {
    "<=50K\n": 0, "<=50K.\n":0,
    ">50K\n": 1,">50K.\n":1,
    "?": -1
}

import csv
arr = []

readfile = open('datos/adult_data.txt', "r")

for line in readfile:
    Type = line.split(", ")
    arr.append(Type)

arr = arr[:len(arr)-1]
for i in arr:
	i[0] = int(i[0])//5 - 3
	i[1] = dic_workclass[i[1]]
	i[3] = dic_education[i[3]]
	i[5] = dic_marital_status[i[5]]
	i[6] = dic_occupation[i[6]]
	i[7] = dic_relationship[i[7]]
	i[8] = dic_race[i[8]]
	i[9] = dic_sex[i[9]]
	i[13] = dic_native_country[i[13]]
	i[14] = dic_50[i[14]]

for i in arr:
    del i[2]

arr = [list(map(int,i)) for i in arr]
atributos = 14
import pandas as pd
cols = ['edad', 'tipo de trabajo', 'nivel de educación', 'grado de educación','estatus marital', 
'ocupación', 'situación sentimental', 'raza', 'sexo', 'ganancias de capital','pérdidas de capital', 
'horas de trabajo semanal', 'país de origen', 'sueldo']
df = pd.DataFrame(arr, columns=cols)


vars = [0]*atributos
for j in range(atributos):
    vars[j] = [i[j] for i in arr]
    vars[j] = np.array(vars[j])
vars = np.array(vars)

means = np.zeros(atributos)
stds = np.zeros(atributos)
for i in range(atributos):
    means[i] = np.mean(vars[i])
    stds[i] = np.std(vars[i])
epsilon = 1e-10

fileEst = open('generalStats.txt', 'w')
for i in range(atributos):
    fileEst.write(str(cols[i])+"\tmedia:"+str(means[i])+"\tstd:"+str(stds[i])+"\n")
fileEst.close()


import matplotlib.pyplot as plt

corr_matrix = df.corr()
fig_cor, axes_cor = plt.subplots(1,1)
fig_cor.set_size_inches(6, 6)

myimage = axes_cor.imshow(corr_matrix)

labels = cols

plt.colorbar(myimage)

axes_cor.set_xticks(np.arange(0,corr_matrix.shape[0], corr_matrix.shape[0]*1.0/len(labels)))
axes_cor.set_yticks(np.arange(0,corr_matrix.shape[1], corr_matrix.shape[1]*1.0/len(labels)))

axes_cor.set_xticklabels([x[0:2] for x in cols])
axes_cor.set_yticklabels(cols)
plt.title('matriz de correlación')
plt.draw()
plt.show()