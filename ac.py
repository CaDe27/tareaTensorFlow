accuracies =[]

for i in range(14): 
    model_path = "modelos3/modelo{}/accuracy.txt".format(i)
    fi = open(model_path, "r")
    linea = fi.readline()
    linea = linea[0:len(linea)-2]
    accuracies.append(linea)
    fi.close()
atributos = ['edad', 'tipo de trabajo', 'nivel de educación', 'grado de educación','estatus marital', 
'ocupación', 'situación sentimental', 'raza', 'sexo', 'ganancias de capital','pérdidas de capital', 
'horas de trabajo semanal', 'país de origen', 'sueldo']
generalAccuracy = open("modelos3/accuracies.txt", "w")
for i in range(len(accuracies)):
	generalAccuracy.write(atributos[i]+":\t\t\t"+accuracies[i]+"\n")
generalAccuracy.close()