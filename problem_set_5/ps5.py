# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
# Name: Yanuar Heru P
# Collaborators (discussion):
# Time:
import numpy
import pylab
import re
import os
# set the directory
code_dir = os.path.dirname(__file__)

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(os.path.normpath(code_dir + '/' + filename), 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    models = []
    for degint in degs:
        # produce model of each degree of order
        models.append(pylab.polyfit(x, y, degint))
    return models


def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    return (1 - ((estimated - y)**2).sum()/(numpy.var(y)*len(y)))

def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    # PROBLEM 3:
    for model in models:
        # produce estimated_y:
        deg = len(model) - 1
        estimated_y = pylab.polyval(model, x)
        r_2 = r_squared(y, estimated_y)
        # plot the y vs x in blue dots
        pylab.plot(x,y, 'bo')
        # plot the estimated_y vs x in red line (curve)
        pylab.plot(x, estimated_y, 'r')
        # put the title of the plot includes degree of regression model and R-square
        title = "Temperature Data with " + str(deg) + " degree model\n" + "R-square = " + str(round(r_2, 4))
        # put the axis label
        pylab.xlabel('years')
        pylab.ylabel('temperature C')
        # if the model order == 1 then add title with se_over_slope
        if deg == 1 :
            se = se_over_slope(pylab.array(x), pylab.array(y), pylab.array(estimated_y), model)
            title += " Std Error = " + str(round(se, 4))
        pylab.title(title)
        pylab.show()


def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    # PART B
    # prepare list of all national avg temperatures of all years
    temps = []
    for year in years:
        # prep for list national temperatures at certain year
        national_temp = []
        for city in multi_cities:
            temp_array = climate.get_yearly_temp(city, year)
            national_temp.append(numpy.mean(temp_array))
        # note: up to this point national_temp data structure is still LIST 
        # in order to calculate mean it is best to convert it into pylab.array
        temps.append(numpy.mean(pylab.array(national_temp)))
    return pylab.array(temps)

def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    result = []
    for i in range(1,(len(y) + 1)):
        inter_list = []
        # inter_list will be used to store the elements to be averaged as part of moving average

        if i < window_length:
            starting_point = 0
        else:
            starting_point = i - window_length
        
        # append inter_list elements from starting point to the index i from array y
        for k in range(starting_point, i):
            inter_list.append(y[k])
        
        # just use the numpy mean to make it easier basically it averaging the inter_list
        # then append the average into the result list
        result.append(numpy.mean(pylab.array(inter_list)))
    
    # return the pylab.array type of the result list
    return pylab.array(result)

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    N = len(y)
    SSE = 0
    for i in range(N):
        SSE += (y[i] - estimated[i])**2
    
    return (SSE/N)**0.5

def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    temps_stdev = []
    for year in years:
        daily_avg_temps = []
        for month in range(1,13):
            for day in range(1,32):
                # try to access dayly data on the specific city in multi_cities
                cities_daily_temps = []
                for city in multi_cities:
                    try:
                        cities_daily_temps.append(climate.get_daily_temp(city, month, day, year))
                    except:
                        # just break out the loop of city and proceed to next day
                        break
                if len(cities_daily_temps) > 0:
                    daily_avg_temps.append(numpy.mean(pylab.array(cities_daily_temps)))
        # NOTE: using nanstd instead of std since the dayly avg temps often contains NaN
        temps_stdev.append(numpy.std(pylab.array(daily_avg_temps)))

    return pylab.array(temps_stdev)

def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        # tag the degree
        deg = len(model) - 1
        # produce estimated data
        estimated_y = pylab.polyval(model, x)
        # evaluate the data
        rmse_y = rmse(y,estimated_y)
        # plot the data and evaluation
        pylab.plot(x, y, 'bo')
        pylab.plot(x, estimated_y, 'r')
        title = "Testing Temperature Date with " + str(deg) + " degree model\n" + "RMSE = " + str(round(rmse_y, 4))
        pylab.xlabel('years')
        pylab.ylabel('temperature C')
        pylab.title(title)
        pylab.show()

if __name__ == '__main__': 
    # # Part A.4-2
    # # create the data sample
    # # instantiate the climate data
    # climate_data = Climate("data.csv")
    # # prepare x axis:
    # years = []
    # # prepare y axis:
    # temps = []
    # # load the data value:
    # for year in TRAINING_INTERVAL:
    #     # append the year
    #     years.append(year)
    #     # get the whole year daily temperature data
    #     temp_array = climate_data.get_yearly_temp("NEW YORK", year)
    #     # only append the average of the whole year temperature data for NEW YORK
    #     temps.append(numpy.mean(temp_array))
    
    # models = generate_models(years, temps, [1,])
    # evaluate_models_on_training(years, temps, models)

    # __name__ == main:
    # # Part B
    # climate_data = Climate("data.csv")
    # years = []
    # for year in TRAINING_INTERVAL:
    #     years.append(year)
    # py_years = pylab.array(years)
    # py_temps = gen_cities_avg(climate_data, CITIES, py_years)
    # models = generate_models(py_years, py_temps, [1,])
    # evaluate_models_on_training(py_years, py_temps, models)
    
    # Part C
    # climate_data = Climate("data.csv")
    # years = []
    # for year in TRAINING_INTERVAL:
    #     years.append(year)
    # py_years = pylab.array(years)
    # py_temps = gen_cities_avg(climate_data, CITIES, py_years)
    # py_temp_mov_avg = moving_average(py_temps, 5)
    
    # models = generate_models(py_years, py_temp_mov_avg, [1,])
    
    # evaluate_models_on_training(py_years, py_temp_mov_avg, models)

    # Part D.2
    # create the data sample
    # # instantiate the climate data
    # climate_data = Climate("data.csv")
    # # prepare x axis:
    # years = []
    # for year in TRAINING_INTERVAL:
    #     years.append(year)
    # py_years = pylab.array(years)
    # # prepare train data
    # train_temps = gen_cities_avg(climate_data, CITIES, py_years)
    # models = generate_models(py_years, train_temps, [1,])
    # # tests the training models
    # years = []
    # for year in TESTING_INTERVAL:
    #     years.append(year)
    # py_years = pylab.array(years)
    # # prepare test data
    # test_temps = gen_cities_avg(climate_data, CITIES, py_years)
    # # we already have models then we just want to test it
    # evaluate_models_on_testing(years, test_temps, models)

    # PROBLEM 2.2 added Generate more models but only for NEW YORK
    climate_data = Climate("data.csv")
    # NOTE : this is shortcut to append years in TRAINING INTERVAL
    years = [*TRAINING_INTERVAL]
    # NOTE: this still will use gen_cities_avg but will use 1 element list consists only NEW YORK
    train_temps = gen_cities_avg(climate_data, ['NEW YORK',], years)
    # we can loop all years to append data using the get yearly temp from Climate class 
    # but this is less practical
    
    py_years = pylab.array(years)
    models = generate_models(py_years, train_temps, [1,2,20])
    # evaluate the train models
    evaluate_models_on_training(py_years, train_temps, models)

    # testings
    years = [*TESTING_INTERVAL]
    # get the test data with the same concept as train_temps data
    test_temps = gen_cities_avg(climate_data, ['NEW YORK',], years)
    
    py_years = pylab.array(years)
    # evaluate the testing
    evaluate_models_on_testing(py_years, test_temps, models)

    # Part E
    # TODO: replace this line with your code
