import numpy as np


def identify_quant_cols(data
):
    # TODO: write code that will return a list of the quantitative columns in a dataframe
    return data.columns


def make_col_positive(data, coloumn_name
):
    # TODO: Add transformations here to make an entire dataframe column positive.

    data[coloumn_name] = data[coloumn_name].abs()
    return data


def log_transform(
        data, coloumn_name
):
    # TODO: Add any code here to log transform an entire column.
    data[coloumn_name] = np.log(data[coloumn_name]);
    return data[coloumn_name]


