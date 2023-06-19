import pandas as pd
import json

df_lov = pd.read_csv("/home/20014946/Documents/Final_Project_PEM/Project_PEM_app_django/Final_Project_Django/pem_app_django/static/lov_code_map_FR.csv")

df_lov.drop_duplicates(inplace=True)

df_lov.lov_code = df_lov.lov_code.apply(lambda x: str(x).zfill(5))
print(df_lov.head())

df_lov_label = df_lov.groupby('lov_code')['lov_label'].agg(list).to_dict()

print(df_lov_label['00900'])

path=("/home/20014946/Documents/Final_Project_PEM/Project_PEM_app_django/Final_Project_Django/pem_app_django/static/lov_code_map_FR.json")
with open(path, "w") as f:
    json.dump(df_lov_label, f, sort_keys=True, indent=4, ensure_ascii=False)