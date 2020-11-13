import pandas as pd
import numpy as np
import os

path = './live_test_images/'

files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
training_labels = pd.read_csv('training_labels.csv')
columns = ['Name', 'Amusement park', 'Animals', 'Bench', 'Building', 'Castle',
       'Cave', 'Church', 'City', 'Cross', 'Cultural institution', 'Food',
       'Footpath', 'Forest', 'Furniture', 'Grass', 'Graveyard', 'Lake',
       'Landscape', 'Mine', 'Monument', 'Motor vehicle', 'Mountains', 'Museum',
       'Open-air museum', 'Park', 'Person', 'Plants', 'Reservoir', 'River',
       'Road', 'Rocks', 'Snow', 'Sport', 'Sports facility', 'Stairs', 'Trees',
       'Watercraft', 'Windows']
defaultOutputRow = np.full((500), False, dtype=bool)
df = pd.DataFrame() 
for column in columns:
    df[column] = defaultOutputRow
df['Name']=files
df.to_csv('output.csv', index=False)