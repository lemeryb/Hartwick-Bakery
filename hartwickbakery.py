# Title: Hartwick Bakery
# Author: Benjamin Lemery
# Date: 10/14/19
# This program is designed to allow the user to input some data regarding sales figures of cookies and candy to recieve some statistics about the data inputted.

from multiprocessing import Process


# Determines how many cookie sales were generated in a month.
def cookie_sales():
    cookies = []
    months = 6
    # Runs through a loop and appends inputted data into a list
    for i in range(0, months):
        cookies.append(int(input("Enter the cookie sales in a given month.")))
    return(cookies)


# Determines how many candy sales were generated in a month.
def candy_sales():
    candy = []
    months = 6
    # Runs through a loop and appends inputted data into a list
    for i in range(0, months):
        candy.append(int(input("Enter the candy sales in any given month.")))
    return(candy)

# Determines the total number of candy sales
def monthly_average_candy_sales(candy):
    total = 0
    # Runs through a loop based on how large the candy list is, averages out the candy list and invokes the next candy functions
    for i in range(0, len(candy)):
        total = total + candy[i]
        average = round(total / len(candy))
    print('The average number of pieces of candy sold per month is ' + str(average))
    maximum_candy_sales(candy)
    minimum_candy_sales(candy)


# Determines the total number of candy sales
def monthly_average_cookie_sales(cookies):
    total = 0
    # Runs through a loop based on how large the cookie list is, averages out the cookie list and invokes the next cookie functions
    for i in range(0, len(cookies)):
        total = total + cookies[i]
        average = round(total / len(cookies))
    print('\nThe average number of cookies sold per month is ' + str(average))
    maximum_cookie_sales(cookies)
    minimum_cookie_sales(cookies)


# Prints the highest and lowest number of cookies and candies sold in any given month.
def maximum_cookie_sales(cookies):
    max_cookies = print("The highest number of cookies sold in any given month was " + str(max(cookies)))


def minimum_cookie_sales(cookies):
    min_cookies = print("The lowest number of cookies sold in any given month was " + str(min(cookies)))


def maximum_candy_sales(candy):
    max_candy = print("The highest number of pieces of candy sold in any given month was " + str(max(candy)))


def minimum_candy_sales(candy):
    min_candy = print("The lowest number of pieces of candy sold in any given month was " + str(min(candy)))


# Determines which candy is more popular based on the total sum of each list
def popular_opinion(cookie_total,candy_total):
    print('\nThe total number of cookies sold equates to: ' +  str(cookie_total))
    print('The total number of pieces of candy sold equates to ' + str(candy_total))

    if cookie_total < candy_total:
        print("Candy is the more popular item.")
    elif cookie_total == candy_total:
        print("Cookies and candy are equally popular.")
    else:
        print("Cookies are the more popular item.")


# Manages certain elements of the programs flow control
def __init__():
    # Grabs the data set from both functions.
    cookie_values = cookie_sales()
    candy_values = candy_sales()

    # Begins multitasking in order to calculate the necessary data between both cookies and candy simultaneously
    p1= Process(target = monthly_average_cookie_sales(cookie_values))
    p1.start()

    p2 = Process(target= monthly_average_candy_sales(candy_values))
    p2.start()
    # Sends the summed up values of both data sets to the popular opinion function
    popular_opinion(sum(cookie_values),(sum(candy_values)))
    # Terminates the processes
    p1.terminate()
    p2.terminate()

# Begins the program
__init__()
