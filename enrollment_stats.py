"""
    Calculate the mean and median from the values in a list
"""

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    enrollment = []
    fees = []

    for university in universities:
        enrollment.append(university[1])
        fees.append(university[2])

    return [enrollment, fees]

def mean(items):
    sum = 0
    for item in items:
        sum += item
    return sum / len(items)

def median(items):
    # sort items
    items.sort()
    # find items length
    items_len = len(items)
    # convert to int in case of odd length
    center = int(items_len / 2)
    # determine if there is an odd or even number of results
    if items_len % 2 == 0:
        # if there is an even number, the median is the mean of the
        # two central numbers
        result = mean(items[center - 1: center])
        # if there is an odd number, the median is the middle number
    else: 
        result = items[center]
    return result

enrollment = enrollment_stats(universities)[0]
fees = enrollment_stats(universities)[1]

print("*******************")
print("Total students: {}\nTotal tuition: $ {}\
      \n\nStudent mean: {}\nStudent median: {}\
      \n\nTuition mean: $ {}\nTuition median: $ {}".format(sum(enrollment), sum(fees), int(mean(enrollment)), int(median(enrollment)), int(mean(fees)), int(median(fees))))
print("*******************")
