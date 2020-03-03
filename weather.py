

######### You do not need to complete the functions' code to generate the documentation pages


# [ ] In this project, you will read a CSV file containing about 25K lines of weather information 
# and store the information in a Python dictionary. You will then use the dictionary to find out
# the hottest, coldest, rainiest years and so on...
# You will see that the dictionary's search optimization algorithms will allow you to explore 
# this large dataset without any noticeable delays.

# The logic of the program is in the `main` function, read it before writing any code.

# Use the description and examples under each of the following functions to implement them:
# 1) convert_file(file_path)
# 2) add_rainy(weather)
# 3) consolidate(weather)
# 4) year_info(year, yearly_weather)
# 5) hottest(yearly_weather)
# 6) coldest(yearly_weather)
# 7) rainiest_days(yearly_weather)
# 8) highest_prcp(yearly_weather)


from datetime import date, datetime

def convert_file(file_path):
    """
    Convert CSV file to a Python dictionary.
    
    The CSV file contains daily weather information arranged in rows,
    the rows contain  (date, precipitation (inches), maximum temperature (F), minimum temperature (F)) in order.
    First line in CSV file is a header (DATE, PRCP, TMAX, TMIN), the rest contain the weather data.
    
    The function should read the data in the file and generate a dictionary where:
        1) keys are date objects (from the datetime module), using the daily date info in the file
        2) values are lists containing [TMAX, TMIN, PRCP] in order
        
    args:
        file_path: path to the CSV file
    
    returns:
        weather: the generated dictionary using date objects as keys and lists of weather info as values
        
    examples:
    Input CSV file:
    DATE,PRCP,TMAX,TMIN
    12/10/2017,0,49,34
    12/11/2017,0,49,29
    12/12/2017,0,46,32
    12/13/2017,0,48,34
    12/14/2017,0,50,36
    12/15/2017,0.06,43,37
    12/16/2017,0.14,45,37
    12/17/2017,0.03,50,42
    12/18/2017,0.7,49,41
    12/19/2017,1,50,40
    12/20/2017,0.13,49,32
    12/21/2017,0.01,41,29
    12/22/2017,0.09,40,35
    12/23/2017,0,38,29
    12/24/2017,0.12,38,28

    Output dictionary (weather):
    {datetime.date(2017, 12, 10): [49, 34, 0.0],
     datetime.date(2017, 12, 11): [49, 29, 0.0],
     datetime.date(2017, 12, 12): [46, 32, 0.0],
     datetime.date(2017, 12, 13): [48, 34, 0.0],
     datetime.date(2017, 12, 14): [50, 36, 0.0],
     datetime.date(2017, 12, 15): [43, 37, 0.06],
     datetime.date(2017, 12, 16): [45, 37, 0.14],
     datetime.date(2017, 12, 17): [50, 42, 0.03],
     datetime.date(2017, 12, 18): [49, 41, 0.7],
     datetime.date(2017, 12, 19): [50, 40, 1.0],
     datetime.date(2017, 12, 20): [49, 32, 0.13],
     datetime.date(2017, 12, 21): [41, 29, 0.01],
     datetime.date(2017, 12, 22): [40, 35, 0.09],
     datetime.date(2017, 12, 23): [38, 29, 0.0],
     datetime.date(2017, 12, 24): [38, 28, 0.12]}
    """
    os.chdir("/home/nbuser/library/parent_dir")
    if (file_path not in os.listdir("/home/nbuser/library/parent_dir")):
        print("STOP!!!! Run the environment setup code!")
        return None
    else:
        weather = {}
        with open(file_path, 'r') as f:
            skip = f.readline()
            for a in range(0,25561):
                u = f.readline()
                u = u.rstrip()
                u = u.split(",")
                c = date_creater(u[0])
                if u[1] == "":
                    u[1] = 0
                if u[2] == "":
                    u[2] = 0
                if u[3] == "":
                    u[3] = 0
                weather[c] = [int(u[2]),int(u[3]),float(u[1])]
        return weather
    #TODO: Your code goes here, see hints below
    
    # open the file for reading (HINT: use `with` statement)

    # ignore the first header line (DATE, PRCP, TMAX, TMIN)

    # remove newline characters from end of each line (HINT: use str.rstrip())

    # split line into a list (HINT: use str.split(','))

    # create the date object from the first list element (HINT: use the date_creater(date_string) function provided below)

    # read the weather related variables
    # precipitation
    # maximum temperature
    # minimum temperature
    
    # create dictionary key:value pair

def add_rainy(weather):
    """
    Emphasize rainy days using Boolean values.
    
    Modify the weather dictionary by adding another Boolean element to the values' lists. 
    If precipitation is observed on a day (more than 0"), the associated list is appended by True.
    If precipitation is not observed (0"), the associated list is appended by False.
    
    args:
        weather: dictionary, keys are date objects and values are lists [TMAX, TMIN, PRCP]
        
    returns:
        None: the weather dictionary is modified directly, keys are date objects and values are lists [TMAX, TMIN, PRCP, RAINY_DAY]
        
    examples:
    Input weather dictionary:
    {datetime.date(2017, 12, 10): [49, 34, 0.0],
     datetime.date(2017, 12, 11): [49, 29, 0.0],
     datetime.date(2017, 12, 12): [46, 32, 0.0],
     datetime.date(2017, 12, 13): [48, 34, 0.0],
     datetime.date(2017, 12, 14): [50, 36, 0.0],
     datetime.date(2017, 12, 15): [43, 37, 0.06],
     datetime.date(2017, 12, 16): [45, 37, 0.14],
     datetime.date(2017, 12, 17): [50, 42, 0.03],
     datetime.date(2017, 12, 18): [49, 41, 0.7],
     datetime.date(2017, 12, 19): [50, 40, 1.0],
     datetime.date(2017, 12, 20): [49, 32, 0.13],
     datetime.date(2017, 12, 21): [41, 29, 0.01],
     datetime.date(2017, 12, 22): [40, 35, 0.09],
     datetime.date(2017, 12, 23): [38, 29, 0.0],
     datetime.date(2017, 12, 24): [38, 28, 0.12]}
    
    Updated weather dictionary with Boolean values
    {datetime.date(2017, 12, 10): [49, 34, 0.0, False],
     datetime.date(2017, 12, 11): [49, 29, 0.0, False],
     datetime.date(2017, 12, 12): [46, 32, 0.0, False],
     datetime.date(2017, 12, 13): [48, 34, 0.0, False],
     datetime.date(2017, 12, 14): [50, 36, 0.0, False],
     datetime.date(2017, 12, 15): [43, 37, 0.06, True],
     datetime.date(2017, 12, 16): [45, 37, 0.14, True],
     datetime.date(2017, 12, 17): [50, 42, 0.03, True],
     datetime.date(2017, 12, 18): [49, 41, 0.7, True],
     datetime.date(2017, 12, 19): [50, 40, 1.0, True],
     datetime.date(2017, 12, 20): [49, 32, 0.13, True],
     datetime.date(2017, 12, 21): [41, 29, 0.01, True],
     datetime.date(2017, 12, 22): [40, 35, 0.09, True],
     datetime.date(2017, 12, 23): [38, 29, 0.0, False],
     datetime.date(2017, 12, 24): [38, 28, 0.12, True]}
    """
    #TODO: Your code goes here
    for a in weather.keys():
            if weather[a][2] > 0:
                weather[a].append(True)
            else:
                weather[a].append(False)

def consolidate(weather):
    """
    Consolidate the daily weather information by year.
    
    Use the weather dictionary to generate a new consolidated dictionary (yearly_weather). 
    The new dictionary uses years as keys, and the associated values are lists containing (in order):
        1) The average of the highest recorded temperatures in the year (AVG_TMAX)
        2) The average of the lowest recorded temperatures in the year (AVG_TMIN)
        3) The total recorded precipitation in the year (TOTAL_PRCP)
        4) The total number of rainy days in the year (TOTAL_RAINY_DAYS)
        5) The number of recorded days (TOTAL_DAYS). 
           This element is necessary to account for days where the station breaks (missing recordings),
           or if the year hasn't finished yet.
           
    args: 
        weather: dictionary, keys are date objects and values are lists [TMAX, TMIN, PRCP, RAINY_DAY]
    
    returns:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS]
                        
    examples:
    Input weather dictionary:
    {datetime.date(2017, 12, 10): [49, 34, 0.0, False],
     datetime.date(2017, 12, 11): [49, 29, 0.0, False],
     datetime.date(2017, 12, 12): [46, 32, 0.0, False],
     datetime.date(2017, 12, 13): [48, 34, 0.0, False],
     datetime.date(2017, 12, 14): [50, 36, 0.0, False],
     datetime.date(2017, 12, 15): [43, 37, 0.06, True],
     datetime.date(2017, 12, 16): [45, 37, 0.14, True],
     datetime.date(2017, 12, 17): [50, 42, 0.03, True],
     datetime.date(2017, 12, 18): [49, 41, 0.7, True],
     datetime.date(2017, 12, 19): [50, 40, 1.0, True],
     datetime.date(2017, 12, 20): [49, 32, 0.13, True],
     datetime.date(2017, 12, 21): [41, 29, 0.01, True],
     datetime.date(2017, 12, 22): [40, 35, 0.09, True],
     datetime.date(2017, 12, 23): [38, 29, 0.0, False],
     datetime.date(2017, 12, 24): [38, 28, 0.12, True]}
     
     Output yearly_weather dictionary:
     {2017: [45.666666666666664, 34.333333333333336, 2.28, 9, 15]}
    """    
    #TODO: Your code goes here
    pass

def year_info(year, yearly_weather):
    """
    Convert the year's weather information to a formatted string.
    
    Look for the weather information of `year` in the `yearly_weather` dictionary.
    If it exists, convert the information list into a formatted string:
            YEAR | AVG_TMAX | AVG_TMIN | TOTAL_PRCP | TOTAL_RAINY_DAYS | TOTAL_DAYS
    If it does not exist, the formatted string should be:
            N/A  |    N/A   |    N/A   |     N/A    |        N/A       |    N/A   
    
    args:
        year: int value to look for in the yearly_weather dictionary
        
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] 
    
    returns:
        formatted_string: containing the year's weather information
                          
    examples:
    Input yearly weather dictionary:
    {2017: [45.666666666666664, 34.333333333333336, 2.28, 9, 15]}
    
    Output formatted string:
    == year_info(2017, yearly_weather) == (contained in the dictionary)
    ' 2017 |         45.67 |        34.33 |   2.28" |            9 |             15 '
    
    == year_info(2055, yearly_weather) == (not contained in the dictionary)
    ' N/A  |      N/A      |     N/A      |   N/A   |     N/A      |      N/A       '
    """
    #TODO: Your code goes here
    pass

def hottest(yearly_weather):
    """
    Find the hottest year in yearly_weather.
    
    Look through all the years in the yearly_weather dictionary and return the year with 
    the highest average maximum temperature (highest AVG_TMAX)
    
    args:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] 
    
    returns:
        hottest_year: the year with the highest maximum temperature average (AVG_TMAX)
    """
    #TODO: Your code goes here
    pass

def coldest(yearly_weather):
    """
    Find the coldest year in yearly_weather.
    
    Look through all the years in the yearly_weather dictionary and return the year with 
    the lowest average minimum temperature (lowest AVG_TMIN)
    
    args:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] 
    
    returns:
        coldest_year: the year with the lowest minimum temperature average (AVG_TMIN)
    """
    #TODO: Your code goes here
    pass

def rainiest_days(yearly_weather):
    """
    Find the year with the largest number of rainy days in yearly_weather.
    
    Look through all the years in the yearly_weather dictionary and return the year with 
    the largest TOTAL_RAINY_DAYS
    
    args:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] 
    
    returns:
        rainiest_year: the year with the largest number of rainy days
    """
    #TODO: Your code goes here
    pass

def highest_prcp(yearly_weather):
    """
    Find the year with the highest total precipitation in yearly_weather.
    
    Look through all the years in the yearly_weather dictionary and return the year with 
    the largest TOTAL_PRCP
    
    args:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists 
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] 
    
    returns:
        rainiest_year: the year with the highest total precipitation
    """
    #TODO: Your code goes here
    pass

def date_creater(date_string):
    """Convert the date_string (formatted as m/d/yyyy) to a date object."""
    d = datetime.strptime(date_string, "%m/%d/%Y")
    return d.date()

def dashes(count):
    """Print a fancy line of `count` dashes"""
    print("o" + count *'-' + "o")

def page_header(title):
    """Print a page header with a title surrounded by dashes"""
    dashes(78)
    print("|{:^78s}|".format(title))
    dashes(78)

def table_header():
    """Print the first row in a table  (header row)"""
    print()
    print(' {0:^4s} | {1:^13s} | {2:^12s} | {3:^7s} | {4:^12s} | {5:^14s} '.format("Year", "Avg High Temp", "Avg Low Temp", "Percip", "# Rainy days", "# Recorded days"))
    dashes(78)
    
def display(title, years, yearly_weather):
    """Print a page with a header, title, and the weather information of all years as found in yearly_weather"""
    clear_output()
    page_header(title)
    table_header()
    
    # if years contain a single int, convert to a single item list
    if type(years) is not list: years = [years]
    
    # print weather information for all years
    for year in years:
        print(year_info(year, yearly_weather)) 
        
    # display this page till you go back to the main menu
    while True:
        m = input("Return to main menu [y/n]?")
        if m in 'yesYesYES':
            break
            

def main():
    # convert the data in the (csv) file into a Python dictionary
    weather = convert_file("data/seattle_weather.csv")
    
    # highlight rainy days by adding a Boolean entry to the dictionary's values
    add_rainy(weather)
    
    # consolidate the weather data by year then store the result in a new dictionary
    yearly_weather = consolidate(weather)
    
    # earliest and latest years on record
    min_year = min(yearly_weather)
    max_year = max(yearly_weather)
    
    # menus functionality
    while True:
        clear_output()

        # display header
        page_header("Weather Records")

        # display main menu
        print()
        print("Main Menu (choose an option to display):\n")
        print("1. Summary of a certain year")
        print("2. All years summary table")
        print("3. Hottest year on record")
        print("4. Coldest year on record")
        print("5. Year with most rainy days")
        print("6. Year with the highest precipitation")
        print("7. Quit")
        print()

        # display footer with user input message
        dashes(78)
        while True:
            try:
                option = input("Select an option (1, 7): ")
                option = int(option)
                if 1 <= option <= 7:
                    break # break the user input loop only, main loop does NOT break
            except ValueError:
                print("Cannot convert {:} to int".format(type(option)))
        
        
        # execute relevant function
        # 1. Summary of a certain year
        if option == 1:
            # ask the user for a valid year
            while True:
                try:
                    year = input("Enter a year ({} - {})".format(min_year, max_year))
                    year = int(year)
                    if min_year <= year <= max_year:
                        break
                except ValueError:
                    print("Cannot convert {:} to int".format(type(option)))
            display("Year Summary", year, yearly_weather)

        # 2. All years summary table 
        elif option == 2:
            years = list(sorted(yearly_weather))
            display("Tabular Summary", years, yearly_weather)
       
        # 3. Hottest year on record
        elif option == 3:
            year = hottest(yearly_weather)
            display("Hottest year on record", year, yearly_weather)
            
        # 4. Coldest year on record   
        elif option == 4:
            year = coldest(yearly_weather)
            display("Coldest year on record", year, yearly_weather)
            
        # 5. Year with most rainy days    
        elif option == 5:
            year = rainiest_days(yearly_weather)
            display("Year with most rainy days", year, yearly_weather)
        
        # 6. Year with the highest precipitation
        elif option == 6:
            year = highest_prcp(yearly_weather)
            display("Year with the highest precipitation", year, yearly_weather)
            
        # 7. Quit    
        elif option == 7:
            clear_output()
            break
    


