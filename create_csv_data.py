import pandas as pd
import numpy as np

waste_categories = {
    'waste_categories':['Aluminium_cans','plastic_wrappers','Cardboard','Paper','PET','PVC','LDPE','HDPE','ALL']
}

robot_waste_type = {
    'R1':['Aluminium_cans'],
    'R4':['Aluminium_cans'],
    'R8':['Aluminium_cans'],
    'R2':['plastic_wrappers'],
    'R6':['plastic_wrappers'],
    'R10':['plastic_wrappers'],
    'R3':['Cardboard'],
    'R7':['Cardboard'],
    'R11':['Cardboard'],
    'R5':['Paper'],
    'R9':['paper'],
    'R12':['paper'],
    'R15':['PET'],
    'R13':['HDPE'],
    'R19':['PET'],
    'R14':['PVC'],
    'R17':['PVC'],
    'R21':['PVC'],
    'R16':['LDPE'],
    'R18':['LDPE'],
    'R22':['LDPE'],
    'R20':['HDPE'],
    'R23':['PET'],
    'R24': ['HDPE']

}

df = pd.DataFrame(waste_categories)
df.to_csv('./data/waste_categories.csv')

df = pd.DataFrame(robot_waste_type)
df.to_csv('./data/robot_waste_categories.csv')
y = 'PET'
x = (df.columns[df.isin(['{0}'.format(y)]).any()])
for robots in x:
    print(robots.type)
