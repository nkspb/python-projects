"""Find mean and median values in a list.

By Nikolay Komolov 
github.com/nkspb
2019
"""

def main():
    """Find mean and median values in a list."""
    universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500],
    ]

    def enrollment_stats(universities):
        """Return numeric values from a list."""
        enrollment_values = []
        tuition_fees = []
        for item in universities:
            enrollment_values.append(item[1])
            tuition_fees.append(item[2])
        return (enrollment_values, tuition_fees)

    def mean(items):
        total = 0
        for val in items:
            total += val

        return total / len(items)

    def median(items):
        items.sort()
        num_of_items = len(items)
        if num_of_items % 2 == 0:
            median = (items[num_of_items / 2] + items[num_of_items / 2 + 1]) / 2
        else:
            median = items[int(num_of_items / 2)]
        return median

    enr_stats = enrollment_stats(universities)

    total_students = sum(enr_stats[0])
    total_tuition = sum(enr_stats[1])

    student_mean = mean(enr_stats[0])
    student_median = median(enr_stats[0])

    tuition_mean = mean(enr_stats[1])
    tuition_median = median(enr_stats[1])

    print(f'''**************************\n
          Total students: {total_students}\n
          Total tuition: $ {total_tuition}\n\n
          Student mean: {int(student_mean)}\n
          Student median: {int(student_median)}\n\n
          Tuition mean: $ {int(tuition_mean)}\n
          Tuition median: $ {int(tuition_median)}\n
          **************************\n''')

if __name__ == '__main__':
    main()
