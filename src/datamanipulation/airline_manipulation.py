import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



from src.datamanipulation.data_preprocessing import make_col_positive

# TODO: Initialise a simple logger and set the desired format to be: TIME LEVEL-module-function-line number-message

def transform_data(data):
    """
    Function to transform data according to some pre-defined steps.

    :param data: data to transform, dataframe format
    :return: transformed data
    """

    data.head()

    # TODO: drop column 'DAY_OF_WEEK'

    data.drop(columns = 'DAY_OF_WEEK')

    # TODO: Rename column 'WHEELS_OFF' to 'HAS_WHEELS'
    data.rename( columns = {'WHEELS_OFF': 'HAS_WHEELS'}, inplace = True)

    data.plot(kind='bar', x='DEPARTURE_DELAY', y='HAS_WHEELS', color='red')
    plt.show()


    # TODO: Fill blanks in column 'AIR_SYSTEM_DELAY' with the average of the values

    mean= data["AIR_SYSTEM_DELAY"].mean()
    data["AIR_SYSTEM_DELAY"].fillna(mean, inplace=True)




    # TODO: Scale values between 0 and 1 in 'DEPARTURE_DELAY' and put them in 'DEPARTURE_DELAY_NORMALISED'

    data["DEPARTURE_DELAY"] = ((data["DEPARTURE_DELAY"] - data["DEPARTURE_DELAY"].min()) / (
                data["DEPARTURE_DELAY"].max() - data["DEPARTURE_DELAY"].min())) * 1


    data['DEPARTURE_DELAY_NORMALISED'] = data['DEPARTURE_DELAY']


    # TODO: Make 'ARRIVAL_DELAY' column positive using a function imported from data_preprocessing.py

    data['ARRIVAL_DELAY'] =  make_col_positive(data,'ARRIVAL_DELAY')

    # TODO: take the log of the column DEPARTURE_DELAY

    data['DEPARTURE_DELAY_LOG'] = np.log(data['DEPARTURE_DELAY'])

    return data





if __name__ == "__main__":
    '''
    HOMEWORK: Write a function that outputs insights into the data. I.e. aggregated data, plots etc. that will
    tell a compelling story to Heathrow about trends that we have discovered in the airline industry.
    
    The output should be the repository that helped produce the insight and a deck (.pdf, no longer that 5 slides)
    which would be used to present the insights to the client. 
    
    Please do not spend more than 3 hours on this.
    '''
    flights_data = pd.read_csv('../../data/flights.csv')
    transformed = transform_data(flights_data)
    print(transformed)


