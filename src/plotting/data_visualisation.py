import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_data(data):
    # TODO: WRITE SOME FUNCTION TO VISUALISE THE DATA - BE CREATIVE, WHAT VISUALISATIONS WOULD MAKE SENSE?
    # i am going to plot , data of airline "AS" , with delay range and flight number

    data.head()


    # Getting data of Airlinee "AS"
    asFlightData = data.loc[data['AIRLINE'] == 'AS']

    #standardizing data
    asFlightData["DEPARTURE_DELAY"] = ((asFlightData["DEPARTURE_DELAY"] - asFlightData["DEPARTURE_DELAY"].min()) / (
            asFlightData["DEPARTURE_DELAY"].max() - asFlightData["DEPARTURE_DELAY"].min())) * 1
    delayMean = asFlightData["DEPARTURE_DELAY"].mean()
    asFlightData["DEPARTURE_DELAY"].fillna(delayMean, inplace=True)

    #plotting
    asFlightData.plot(kind='bar', x='FLIGHT_NUMBER', y='DEPARTURE_DELAY', color='red')

    plt.show()



if __name__ == "__main__":
    '''
    HOMEWORK: Write a function that outputs insights into the data. I.e. aggregated data, plots etc. that will
    tell a compelling story to Heathrow about trends that we have discovered in the airline industry.

    The output should be the repository that helped produce the insight and a deck (.pdf, no longer that 5 slides)
    which would be used to present the insights to the client. 

    Please do not spend more than 3 hours on this.
    '''
    flights_data = pd.read_csv('../../data/flights.csv')
    plot_data(flights_data)
