import os
import yaml

import model


file_dir = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(file_dir):
    if filename.endswith(".yaml"):
        with open(f"{file_dir}/{filename}", "r") as file:
            conf = yaml.unsafe_load(file)
            print(
                ' ',
                f'-----{filename}-----',
                conf,
                sep='\n')
