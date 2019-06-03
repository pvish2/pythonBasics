import os

import pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston

from src.datamanipulation.data_preprocessing import make_col_positive
from sklearn import preprocessing

# TODO: Initialise a simple logger and set the desired format to be: TIME LEVEL-module-function-line number-message

def transform_data(data):
    """
    Function to transform data according to some pre-defined steps.

    :param data: data to transform, dataframe format
    :return: transformed data
    """

    data.head()

    # print(data)

    # TODO : data cleaning
    data['A'].fillna((data['A'].median()), inplace=True)
    data['B'].fillna((data['B'].median()), inplace=True)

    data['C'].fillna((data['C'].median()), inplace=True)

   # data['D'].fillna((data['D'].median()), inplace=True)
    #
    data['E'].fillna((data['E'].median()), inplace=True)
    #
    data['F'].fillna((data['F'].median()), inplace=True)
    #
    data['G'].fillna((data['G'].median()), inplace=True)
    #
    data['H'].fillna((data['H'].median()), inplace=True)








# 1. TODO: Import the cars dataset and assign column names to the data.

    data.rename(index=str, columns={"A": "MPG", "B": "CYLINDERS","C": "DISPLACEMENT","D": "HORSE_POWER","E": "WEIGHT","F": "ACCELERATION","G": "MODEL_YEAR","H": "ORIGIN","I": "CAR_NAME"},inplace = True)



# 2. TODO: ‘Clean’ the empty cars dataset. Explore the variables to find data points that shouldn't be there. There are many ways to treat outliers and NaN values. These can be discussed in more detail next week!



# 3. TODO: Assign features to X and target to y. We are trying to predict the MPG of the cars in this case.

    columns = ['MPG', 'CYLINDERS', 'DISPLACEMENT', 'HORSE_POWER', 'WEIGHT', 'ACCELERATION', 'MODEL_YEAR', 'ORIGIN', 'CAR_NAME']
    x = load_boston()
    df = pd.DataFrame(x.data, columns=x.feature_names)
    df["MPG"] = x.target
    X = df.drop("MPG", 1)  # Feature Matrix
    y = df["MPG"]  # Target Variable
    # print(df.head(5))

# 4. TODO: Normalise the columns in the data, i.e. scale all of the variables inearly between 0 and 1.

    x = data.values  # returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    data = pandas.DataFrame(x_scaled)
    # print(data.head(5))

# 5. TODO: Split data into testing and training sets.



# 6. TODO: Carry out a linear regression and calculate the RMSE and accuracy scores. What do these two values mean and when should we use them?



# 7. TODO: Create a new set of X and y, with the original data. We are going to
# repeat the process, but transforming the features, to see if we can achieve
# better accuracy.



# 8. TODO: Make transformations: Inverse Transform ‘displacement’ and ‘weight’,
# Power (^2) transform ‘horsepower’ and ‘model year’ and log transform
# ‘acceleration’. Why are we doing this, why transform the data at all?



# 9. TODO: Normalise the columns in the transformed data.



# 10. TODO: Split the transformed data into test and train sets.



# 11. TODO: Fit a linear regression model on transformed data and calculate the
# RMSE and accuracy scores. Can we compare it directly to the previous
# results? If yes, why? If not, why?

# 12. TODO: BONUS: So far we have improved the score slightly. Try different
# transformations and see if you can improve this score further. The best
# score is the winner. Is there a way to automate this? How can we be smarter
# about picking the best transformations for the data



    return data





if __name__ == "__main__":
    '''
    HOMEWORK: Write a function that outputs insights into the data. I.e. aggregated data, plots etc. that will
    tell a compelling story to Heathrow about trends that we have discovered in the airline industry.
    
    The output should be the repository that helped produce the insight and a deck (.pdf, no longer that 5 slides)
    which would be used to present the insights to the client. 
    
    Please do not spend more than 3 hours on this.
    '''
    car_data = pd.read_fwf('../../data/auto-mpg-data.txt', names=['A', 'B', 'C', 'D', 'E', 'F','G','H','I'])


    # columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin',
    #            'car_name']
    # df = pd.read_fwf("../../data/auto-mpg-data.txt", names=columns)
    # print(df)

    # index_col = ['First Name', 'Last Name']
    transformed = transform_data(car_data)
   # print(transformed)


