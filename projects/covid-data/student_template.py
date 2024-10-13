import sys
import numpy as np
import pandas as pd

def Split(data):
    ## I just wanted to parse my data differently so I used this function
    df = data
    Harrisonburg_fips = 51660

    ## Get only Rockingham data
    Rockingham_initial = df[df["county"] == "Rockingham"]
    Rockingham = Rockingham_initial[Rockingham_initial["state"] == "Virginia"]

    ## Get only Harrisonburg data
    Harrisonburg = df[df["fips"] == Harrisonburg_fips]

    return Rockingham, Harrisonburg

def first_question(data, _rockingham, _harrisonburg):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    # Convert to numpy
    rock_dates = _rockingham["date"].to_numpy()

    # First value in Rockingham data set
    rock_first_date = rock_dates[0]

    # convert to numpy
    harris_dates = _harrisonburg["date"].to_numpy()

    # First value in Harrisonburg data set
    harris_first_date = harris_dates[0]

    # print stuff out
    print("The date of the first Covid case in Rockingham County is on", rock_first_date)
    print("The date of the first Covid case in Harrisonburg is on", harris_first_date)

def Difference(_data_set):
    ## Takes a data set and returns the difference between a_{n+1} and a_n for all n in {1,...,len(_data_set)-2}
    ## Also returns index where max(a_{n+1} - a_n) occurs

    differences = []
    n = 0

    while n <= len(_data_set) - 2:
        single_diff = _data_set[n + 1] - _data_set[n]
        differences.append(single_diff)
        n += 1

    ## Since we are subtracting a_{n+1} - a_n we have to add one to the index find where max day occurred
    max_index = np.argmax(differences) + 1

    return max_index, differences

def second_question(data, _rockingham, _harrisonburg):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    # Convert stuff to lists to make opperations super duper easy
    rock_cases = _rockingham["cases"].to_list()
    harris_cases = _harrisonburg["cases"].to_list()
    rock_dates = _rockingham["date"].to_list()
    harris_dates = _harrisonburg["date"].to_list()

    ## Apply Difference function to both data sets and only store max index (pass differences list)
    rock_index, _ = Difference(rock_cases)
    harris_index, _ = Difference((harris_cases))

    ## name the indices of the max Covid cases day
    rock_date = rock_dates[rock_index]
    harris_date = harris_dates[harris_index]

    # print result
    print("The date of the greatest number of new daily cases recorded in Rockingham was on", rock_date)
    print("The date of the greatest number of new daily cases recorded in Harrisonburg was on", harris_date)

    return

def third_question(data, _rockingham, _harrisonburg):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    # define an empty data set
    rock_data = []

    # Convert data sets to lists
    rock_cases = _rockingham["cases"].to_list()
    harris_cases = _harrisonburg["cases"].to_list()
    rock_dates = _rockingham["date"].to_list()
    harris_dates = _harrisonburg["date"].to_list()

    # apply difference function and save differences list
    _, rock_diff = Difference(rock_cases)
    _, harris_diff = Difference(harris_cases)

    # apply seven day function to determine bounds for max 7-day average
    rock_lower, rock_upper = seven_day(rock_cases, rock_dates)
    harris_lower, harris_upper = seven_day(harris_cases, harris_dates)

    # print results
    print("The worst week of Covid cases in Rockingham was from", rock_lower, "to", rock_upper)
    print("The worst week of Covid cases in Harrisonburg was from", harris_lower, "to", harris_upper)
    return

def seven_day(data_list, dates_list):
    ## Takes column of cases and column of corresponding dates, returns upper and lower bound for max 7-day interval

    ## Create an empty data set
    data = []

    ## Iterates through the entire cases data set
    for y in range(len(data_list) - 7):
        # Takes the (y+6)th element and subtracts the yth element
        seven_day = data_list[y + 6] - data_list[y]
        ##Appends the 7 day difference in cases
        data.append(seven_day)

    ## Add one to the max location to account for the fact we are taking the difference between (y+6)th element and yth element
    max_location = np.argmax(data) + 1

    ## Upper and lower date bounds
    max_date_lower = dates_list[max_location]
    max_date_upper = dates_list[max_location + 6]

    return max_date_lower, max_date_upper

if __name__ == "__main__":
    data = pd.read_csv('us-counties.csv')

    Rockingham, Harrisonburg = Split(data)
    Rockingham_cases = Rockingham["cases"].to_list()

    Difference(Rockingham_cases)

    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data,Rockingham,Harrisonburg)

    print("")
    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data,Rockingham,Harrisonburg)

    print("")
    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data,Rockingham,Harrisonburg)


