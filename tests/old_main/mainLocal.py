import PySciT.UserActions as user
# from PySciT.MoreFunctions import *
# # from ManageItems import ManageTransformations as mo
import PySciT.ManageItems as M
from PySciT.Aditional.MoreFunctions import *

# from PySciT import UserActions as user
# from PySciT.MoreFunctions import *
# # from ManageItems import ManageTransformations as mo
# from PySciT import ManageItems as M

# import UserActions as user
# from MoreFunctions import *
# # from ManageItems import ManageTransformations as mo
# import ManageItems as M

menuOpciones = [
    "Status",
    "Seleccionar archivo",
    "Guardar Archivo en Data",
    # "Select Data",
    "Borrar Data",
    "Crear Pipeline",
    "Operar con un Pipeline",
    "Borrar Pipeline",
    "Salir"
]
pipeOpciones = [
    "Ver Steps",
    "Introducir transformación",
    # "Seleccionar Algoritmo",
    "Cambiar Steps",
    "Eliminar Step",
    "Fit con Data",
    "Predict",
    "Volver al menú inicial",
]


print("--Inicio del programa")
print('Creando user')
user1 = user.UserActions()
print('Creando Operador')
tr = M.TR.ManageTransformations()
alg = M.ALG.ManageAlgorithms()

opc = ''
file = 'Ninguno'
aux = ''
aux1 = ''

while opc != "Salir":
    opc = choiceDialog(menuOpciones, "¿Qué operación desea realizar?")
    if opc == "Status":
        print(' + Estado actual: ')
        print('Total de Pipelines: ',len(user1.myPipelines))
        print(user1.getMyPipelinesNames())
        print('Total de Data: ',len(user1.myDatas))
        print(user1.getMyDatasNames())
        print('Archivo seleccionado: '+file)

    elif opc == "Seleccionar archivo":
        file = askFileLocation()
        print('Se ha seleccionado: '+file)

    elif opc == "Guardar Archivo en Data":
        if file == 'Ninguno':
            print('Seleccione un archivo primero')
        else:
            aux = user1.createData()
            print("Hecho, total de datas actuales: ",aux,", guardando datos...")
            user1.selectData(aux-1)
            user1.setDataFromFile(file)

    # elif opc == "Select Data":
    #     aux = user1.getMyDatasNames()
    #     if len(aux) > 0:
    #         aux = choiceDialog(aux, "Seleccione la Data", 2)
    #         print("Se ha seleccionado la Data: "+aux[1])
    #         user1.selectData(aux[0])
    #     else:
    #         print('No hay Datas')
    
    elif opc == "Borrar Data":
        aux = user1.getMyDatasNames()
        if len(aux) > 0:
            aux[len(user1.getMyDatasNames())] = 'Cancelar'
            aux = choiceDialog(list(aux.values()), "Seleccione la Data a eliminar", 2)
            print("Se ha seleccionado: "+aux[1])
            user1.delData(aux[0])
        else:
            print('No hay Datas')

    elif opc == "Crear Pipeline":
        aux1 = choiceDialog(alg.getAlgorithmsList(), "¿Qué algoritmo desea que opere el pipeline?")
        pipe = alg.getAlgorithmPipe(aux1, 'pepep')
        print(pipe)

        # pos = len(steps)
        # if pos > 0:
        #     steps[pos] = "Añadir al final"
        #     pos = choiceDialog(steps, "¿En cuál posición quiere introducir el algoritmo?", 0)
        # user1.setAlgorithmPipe(aStep, pos)
        print("Creando Pipeline...")
        aux = user1.addPipeline(pipe)
        print("Añadido")

        # aux = user1.createPipeline()
        print("Hecho, total de pipelines actuales: ", aux)
        print(user1.myPipelines)
    
    elif opc == "Operar con un Pipeline":
        aux = user1.getMyPipelinesNames()
        if len(aux) > 0:
            aux = choiceDialog(list(aux.values()), "Seleccione el Pipeline", 2)
            print("Se ha seleccionado el Pipeline: ", aux[1])
            user1.selectPipeline(aux[0])
            
            while opc != "Volver":
                opc = choiceDialog(pipeOpciones,
                                   ("¿Qué operación desea realizar con el Pipeline "+aux[1]+" nº "+str(aux[0])+"?"))
                
                if opc == "Ver Steps":
                    print(user1.getSteps())

                elif opc == "Introducir transformación":
                    aux1 = choiceDialog(tr.getTransformationsList(), "¿Qué operación desea introducir?")
                    aStep = tr.getTransformation(aux1)
                    steps = user1.getSteps().copy()
                    pos = len(steps)
                    if pos > 0:
                        steps.append("Añadir al final")
                        pos = choiceDialog(steps, "¿En cuál posición quiere introducir la transformación?", 0)
                    user1.addStep(aStep, pos)
                    print("Añadido")
        
                # elif opc == "Seleccionar Algoritmo":
                #     aux1 = choiceDialog(list(tr.Algorithms), "¿Qué algoritmo desea que opere el pipeline?")
                #     aStep = tr.getAlgorithm(aux1)
                #     steps = user1.getSteps().copy()
                #     pos = len(steps)
                #     if pos > 0:
                #         steps[pos] = "Añadir al final"
                #         pos = choiceDialog(steps, "¿En cuál posición quiere introducir el algoritmo?", 0)
                #     user1.setAlgorithmPipe(aStep, pos)
                #     print("Añadido")

                elif opc == "Cambiar de posición los Steps":
                    steps = user1.getSteps().copy()
                    if len(aux) > 0:
                        steps.append("Añadir al final")
                        aux1 = choiceDialog(aux, "Seleccione el Step a eliminar", 2)
                        print("Se ha seleccionado: "+aux[1])
                        user1.delData(aux[0])
                    else:
                        print('No hay Steps')

                elif opc == "Eliminar Step":
                    aux1 = user1.getSteps().copy()
                    if len(aux) > 0:
                        steps.append("Cancelar")
                        aux1 = choiceDialog(aux, "Seleccione el Step a eliminar", 2)
                        print("Se ha seleccionado: "+aux[1])
                        user1.delData(aux[0])
                    else:
                        print('No hay Steps')

                elif opc == "Fit con Data":
                # elif opc == "Select Data":
                    aux = user1.getMyDatasNames()
                    if len(aux) <= 0:
                        print('No hay Datas')
                    else:
                        aux = choiceDialog(list(aux.values()), "Seleccione la Data", 2)
                        print("Se ha seleccionado la Data: "+aux[1])
                        user1.selectData(aux[0])
                        user1.fitSelectData()

                elif opc == "Predict":
                        print(user1.predict())

                elif opc == "Volver al menú inicial":
                    opc = "Volver"
                
                else:
                    print("Opción no válida")
            else:
                print("Volviendo al menú anterior...")
            
        else:
            print('No hay Pipelines para operar')

    elif opc == "Borrar Pipeline":
        aux = list(user1.getMyPipelinesNames().values)
        if len(aux) > 0:
            aux.append('Cancelar')
            aux = choiceDialog(aux, "Seleccione el Pipeline a eliminar", 2)
            print("Se ha seleccionado: "+aux[1])
            user1.delPipeline(aux[0])
        else:
            print('No hay Pipelines para operar')

    elif opc == "Salir":
        print('¡Nos vemos!')
    else:
        print("Opción no válida")

else:
    print("Saliendo del programa")



# print(tr.Algorithms)
# fst = 'Linear Regression'
# print(fst)
# print(tr.thereIs(fst))
# got = tr.getAlgorithm(fst)
# print(got)

# print(user1.Name)
# print(user1.createPipeline())
# print(user1.getMyPipelinesNames())
# print('Select pipe')
# print(user1.selectPipeline(0))
# print(user1.getActualPipe())
# print(user1.getActualPipe().Name)
# print('Add Step')
# print(user1.addStep(got,0))
# print(user1.getActualPipe().steps())
# print(user1.delPipeline(0))

