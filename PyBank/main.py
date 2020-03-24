def main(directory, file_name):

    import os
    import csv

    csvpath = os.path.join("budget_data.csv")

    month_year_list = []
    revenue_list = []
    total_revenue = 0
    total_change = 0
    change_max = ['', 0]
    change_min = ['', 0]

    with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        if csv.Sniffer().has_header:
            next(csvreader)
        for row in csvreader:
            month_year = row[0]
            revenue = float(row[1])
            month_year_list.append(month_year)
            revenue_list.append(revenue)
            total_revenue =+ revenue
    
    total_month = len(month_year_list)
    for i in range(1, len(month_year_list)):
        change = revenue_list[i] - revenue_list[i-1]
        total_change =+ change
        if change > change_min[1]:
            change_max = [month_year_list[i], change]
        if change < change_min[1]:
            change_min = [month_year_list[i], change]
    change_average = total_change / total_month

    line1 = 'Financial Analysis'
    line2 = '------------------'
    line3 = 'Total Months: ' + str(total_month)
    line4 = 'Total Revenue: $' + str(total_revenue)
    line5 = 'Average Revenue Change: $' + str(round(change_average))
    line6 = 'Greatest Revenue Increase: ' + change_max[0] + ' ($' + str(round(change_max[1])) + ')'
    line7 = 'Greatest Revenue Decrease: ' + change_min[0] + ' ($' + str(round(change_min[1])) + ')'\

    summary = []
    summary.extend([line1, line2, line3, line4, line5, line6, line7])

    print('')
    print(file_name)
    for line in summary:
        print(line)
    print ('')


directory = 'raw_data'
file_name = 'budget_data.csv'
main(directory, file_name)

   # for row in csvreader:
       # count_of_months = len(list(csvreader))
       # print("Total Months: " + str(count_of_months))



#https://dfrieds.com/python/read-in-csv-files.html