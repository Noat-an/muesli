from jinja2 import Environment, FileSystemLoader
import yaml
import os

import config
import template

env = Environment(loader=FileSystemLoader(template.file_dir))
temp = env.get_template('dag_template.jinja2')


for filename in os.listdir(config.file_dir):
    if filename.endswith(".yaml"):
        with open(f"{config.file_dir}/{filename}", "r") as configfile:
            dag_config = yaml.safe_load(configfile)
            with open(
                f"Airflow/dag/get_{dag_config['dag_id']}_from_{dag_config['source']}_to_{dag_config['target']}.py", "w"
            ) as f:
                f.write(temp.render(dag_config))
