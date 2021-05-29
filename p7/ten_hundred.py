# Name: Jiwon Song
# NetID: jsong99
# WiscID: 9074018707
# Class: Spring 2020 CS 540


import csv
import math
import numpy as np
from datetime import date as dt


def load_data(filepath):
    data = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)

        header = next(reader)

        lat_idx = header.index('Lat')
        lon_idx = header.index('Long')

        header.remove('Lat')
        header.remove('Long')

        for row in reader:
            each_row = {}
            tmp = []
            row = row[:lat_idx] + row[lon_idx + 1:]

            for h in header:
                each_row[h] = row[header.index(h)]

            data += [each_row]

    return data


def convert(date):
    tmp = date.split('/')
    month = tmp[0]
    day = tmp[1]
    year = '20' + tmp[2]

    return dt(int(year), int(month), int(day))


def find_latest(first, dates):
    latest = first

    for d in dates:
        d = convert(d)
        if d >= latest:
            latest = d

    return latest


def calculate_x_y(time_series):
    dates = []
    for key in time_series.keys():
        if key != 'Province/State' and key != 'Country/Region':
            dates += [key]

    last_day = dates[-1]
    if time_series[last_day] == '0':
        return math.nan, math.nan

    first_day = convert(dates[0])

    # print(last_day)

    # find N
    n = int(time_series[last_day])
    threshold10 = (n / 10)
    threshold100 = (n / 100)
    xdays = []
    ydays = []

    # find dates that are N/10 and N /100
    for date in dates[::-1]:

        if float(time_series[date]) <= threshold10:
            xdays += [date]

        if float(time_series[date]) <= threshold100:
            ydays += [date]

    try:
        x = xdays[0]
        y = ydays[0]
        last = convert(last_day)
        xday = convert(x)
        yday = convert(y)

        return (last - xday).days, (xday - yday).days
    except:
        return math.nan, math.nan


def hac(dataset):
    finite = True
    # m by n ; m rows and n columns

    # filtering NaN values
    filtered_data = []
    for x in range(len(dataset)):
        if not (math.isnan(dataset[x][0]) or math.isnan(dataset[x][1])):
            filtered_data += [dataset[x]]

    # declaring variables
    m = len(filtered_data)
    n = len(filtered_data[0])
    cluster = {}

    # Numbering each of the starting points from 0 to m-1
    for i in range(m):
        cluster[i] = [filtered_data[i], {"num_points": 1}]

    # create an (m-1)*4 empty array
    result = np.zeros([m - 1, 4], dtype=np.float32)

    count = threshold = idx1 = idx2 = 0

    while len(cluster) > 1:
        distances = []
        thresh_reset = []

        for i in cluster.keys():
            src = cluster[i][0]
            tmp = {}

            for j in cluster.keys():
                if i != j:
                    dst = cluster[j][0]
                    distance = abs((dst[1] - src[1]) ** 2) + ((dst[0] - src[0]) ** 2)

                    if distance <= threshold and not i > j:
                        distances += [(i, j)]
                        tmp[(i, j)] = distance

            if len(distances) == 0:
                threshold += 1
            else:
                minimum_distance = min(tmp.values())
                if minimum_distance <= threshold:
                    threshold = minimum_distance

                res = []
                res += [key for key in tmp if tmp[key] == minimum_distance]

                idx1 = min(res)[0]
                idx2 = min(res)[1]

                src = cluster[idx1][0]
                dst = cluster[idx2][0]

                distance = abs((dst[1] - src[1]) ** 2) + ((dst[0] - src[0]) ** 2)

                num_points = cluster[idx1][1]["num_points"] + cluster[idx2][1]["num_points"]

                # add the shortest distance
                result[count] = [idx1, idx2, distance, num_points]

                pt1 = cluster[idx1][0]
                pt2 = cluster[idx2][0]

                cluster[m + count] = [((pt1[0] + pt2[0])/2, (pt1[1] + pt2[1])/2), {"num_points": num_points}]
                count += 1

                del cluster[idx1]
                del cluster[idx2]

                break

    return result
