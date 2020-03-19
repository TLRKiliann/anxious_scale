#!/usr/bin/python3
# -*- coding:utf-8 -*-


"""
This program is destinate to write an anxiety scale
Change the date before launching and print your sheet
before start the interview
"""

import csv
import numpy as np
import pandas as pd


echel_anx = [
    np.array([0, 1, 2]),
    np.array([0, 1, 2]),
    np.array([0, 1, 2]),
    np.array([0, 1, 2]),
    np.array([0, 1, 2]),
]

echel_anx_numpy = np.array(echel_anx)
print("\n")
print(echel_anx_numpy)

echel_anx_df = pd.DataFrame(echel_anx_numpy,
    index=['Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5'],
    columns=['Minimum', 'Medium', 'Maximum'])
print(echel_anx_df)

# write to txt file 
with open("anxity.txt", 'at') as file_df:
    CONTENT = file_df.write("\n\nEn date du ../../.... :\n")
    CONTENT = file_df.write("\n1.Vous êtes-vous souvent senti anxieux ? (0, 1, 2)\n")
    CONTENT = file_df.write("2.Avez-vous souvent soufert de symptômes somatiques de tension,")
    CONTENT = file_df.write("comme céphalées, palpitations, sueurs profuses ? (0, 1, 2)\n")
    CONTENT = file_df.write("3.Avez-vous beaucoup été parturbé par des peurs irrationnelles")
    CONTENT = file_df.write("(sans raisons apparente) ou des phobies ? (0, 1, 2)\n")
    CONTENT = file_df.write("4.Avez-vous fait des attaques de panique (anxiété")
    CONTENT = file_df.write("massive ou paralysante) (0, 1, 2)\n")
    CONTENT = file_df.write("5.Le patient s\'est senti très anxieux de façon chronique")
    CONTENT = file_df.write("ou a souvent souffert de symptômes somatiques d\'anxiété. (0, 1, 2)\n")
    CONTENT = file_df.write("\n")
    CONTENT = file_df.write(str(pd.DataFrame(echel_anx_numpy,
        index=['Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5'],
        columns=['Minimum', 'Medium', 'Maximum'])))
    print(CONTENT)


myData = [["Date", "Minimum", "Medium", "Maximum"],
          ["Question 1", "0", "1", "2"],
          ["Question 2", "0", "1", "2"],
          ["Question 3", "0", "1", "2"],
          ["Question 4", "0", "1", "2"],
          ["Question 5", "0", "1", "2"]]

myFile = open("csvfile.csv", 'at')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

print("Writing complete")
