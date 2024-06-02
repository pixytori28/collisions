# Name: victoria inahuazo
# Date: 04/12/24
# email: victoria.inahuazo11@myhunter.cuny.edu
# A program will ask the user for csv of collision data


import pandas as pd

def main ():
    csvF = input("Enter CSV file name:")
    collisions = pd.read_csv(csvF)
    contributing_factors = collisions['CONTRIBUTING FACTOR VEHICLE 1']

    factor_counts = contributing_factors.value_counts() #count occurences of each factor

    print("Top 3 contributing factors for collisions:")
    print(factor_counts.head(3))


if __name__ == "__main__":
    main()

