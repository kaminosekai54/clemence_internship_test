#Import of packages
import pandas as pd



################################################################################
# Reading the excell file in a variable, to be able to get a data frame pear sheet
xls= pd.ExcelFile("2022-09 Exo recrutement stagiaire NR.xlsx")
# getting each of the sheet of the excell file in a seperate data frame
df1 = pd.read_excel(xls, 'Inputs')
df2 = pd.read_excel(xls, 'Modèle')
df3 = pd.read_excel(xls, 'Sources FE')

# print(df)
# print(df1.columns)
# print(df2.columns)
# print(df3.columns)


# creating a new dataframe to implement the model
# we take by default the columns name of the model sheet
model_implementation_df = pd.DataFrame(columns= df2.columns)
# print(df1["Variable"])
print(df1["Valeur"].where(df1["Variable"] == "Nb utilisateurs / an"))
# print(df1[df1["Valeur"] & (df1["Variable"] == "Nb utilisateurs / an")])
# print(df1.query("Variable == 'Nb utilisateurs / an'"))
# print(df1.query("Variable == 'Nb utilisateurs / an'")["Valeur"])
# filling our column with the list of value
# I do it by attributing a list of value for the none computable variable
model_implementation_df["Catégorie"] = ["Calcul intermédiaire", "Calcul intermédiaire", "Consommation élec", "Consommation élec", "Consommation élec", "Consommation élec", "Impact fabrication", "Impact fabrication", "Impact run", "Impact run", "Impact run", "Impact run"]
model_implementation_df["Variable"] = ["Durée totale sessions", "Data totale échangée", "Smartphones", "Laptops", "Réseau WIFI", "Réseau mobile",  "Smartphones", "Laptops", "Smartphones", "Laptops", "Réseau WIFI", "Réseau mobile"]
# definding the Valeur column, each line correspond to a formula in the model sheet
model_implementation_df["Valeur"] = [
    # df1["Valeur"].where(df1["Variable"] == "Nb utilisateurs / an").notna() * df1["Valeur"].where(df1["Variable"] == "Nb sessions / utilisateur / an").notna() * df1["Valeur"].where(df1["Variable"] == "Durée moyenne session").notna()  * 60, 
    # df1.query("Variable == 'Nb utilisateurs / an'")["Valeur"] * df1.query("Variable == 'Nb sessions / utilisateur / an'")["Valeur"] * df1.query("Variable == 'Durée moyenne session'")["Valeur"] * 60, 
    df1.query("Variable == 'Nb utilisateurs / an'")["Valeur"].sum() * df1.query("Variable == 'Nb sessions / utilisateur / an'")["Valeur"].sum()  * df1.query("Variable == 'Durée moyenne session'")["Valeur"].sum()  * 60, 
    df1["Valeur"].where(df1["Variable"] == "Nb utilisateurs / an")*df1["Valeur"].where(df1["Variable"] == "Nb sessions / utilisateur / an")* df1["Valeur"].where(df1["Variable"] == "Nb sessions / utilisateur / an") * df1["Valeur"].where(df1["Variable"] == "Poids moyen d’une page compressée")/1000, 
    pd.NA, #df1["Valeur"].where(df1["Variable"] == "Fraction smartphone")*"C2"* df3["Valeur"].where(df3["Variable"] == "!E13/G2"), 
    pd.NA, # df1["Valeur"].where(df1["Variable"] == Fraction laptop")*"C2"*df3["Valeur"].where(df3["Variable"] == "!E11/G2"), 
    pd.NA, # (df1["Valeur"].where(df1["Variable"] == "Fraction laptop") + df1["Valeur"].where(df1["Variable"] == "Fraction smartphone") * (1-df1["Valeur"].where(df1["Variable"] == "Fraction réseau mobile pour smartphone")))* "C3" *df3["Valeur"].where(df3["Variable"] == "E7"), 
    pd.NA, # df1["Valeur"].where(df1["Variable"] == "Fraction smartphone")*df1["Valeur"].where(df1["Variable"] == "Fraction réseau mobile pour smartphone")* "C3" *df3["Valeur"].where(df3["Variable"] == "E6"), 
    pd.NA, # df1["Valeur"].where(df1["Variable"] == "Fraction smartphone")*"C2"*df3["Valeur"].where(df3["Variable"] == "E5") / (df1["Valeur"].where(df1["Variable"] == "Durée de vie moyenne smartphone")*df1["Valeur"].where(df1["Variable"] == "Utilisation quotidienne moyenne smartphone")*60*60*365), 
    pd.NA, # df1["Valeur"].where(df1["Variable"] == "Fraction laptop")*"C2"*df3["Valeur"].where(df3["Variable"] == "E3")/(df1["Valeur"].where(df1["Variable"] == "Durée de vie moyenne laptop")*df1["Valeur"].where(df1["Variable"] == "Utilisation quotidienne moyenne laptop")*60*60*365), 
    pd.NA, # "C4"*df3["Valeur"].where(df3["Variable"] == "E$8"), 
    pd.NA, # "C5"*df3["Valeur"].where(df3["Variable"] == "E$8"), 
    pd.NA, # "C6"*df3["Valeur"].where(df3["Variable"] == "E$8"), 
    pd.NA] # "C7"*df3["Valeur"].where(df3["Variable"] == "E$8")]
print(model_implementation_df.Valeur)
print(df2.Valeur)
model_implementation_df["Unité"] = ["s", "Go", "kWh/an", "kWh/an", "kWh/an", "kWh/an", "kgCO2eq/an", "kgCO2eq/an", "kgCO2eq/an", "kgCO2eq/an", "kgCO2eq/an", "kgCO2eq/an"]
# model_implementation_df["Soit"] =  ["C2/3600", pd.NA, pd.NA, pd.NA, pd.NA, pd.NA, C8/SOMME(C$8:C$9), C9/SOMME(C$8:C$9), C10/SOMME(C$10:C$13), C11/SOMME(C$10:C$13), C12/SOMME(C$10:C$13), C13/SOMME(C$10:C$13)]
model_implementation_df["Unité1"] = ["heures", pd.NA, pd.NA, pd.NA, pd.NA, pd.NA, "du total fabrication", "du total fabrication", "du total run", "du total run", "du total run", "du total run"]
# print(model_implementation_df.Catégorie)

# model_implementation_df["Variable"] = df1["Variable"] 


# print(model_implementation_df)

# model_implementation_df["Valeur"] = df1



#  remarks, avoid accent in the column name and in the data in general
# print(model_implementation_df)
# colum = {"col1":[1,2,3], "col2":["z"]}
# colum2 = ["col1", "col2"]

# model_implementation_df["Valeur"] = df1[""]