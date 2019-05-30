# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 17:17
# @Author  : zyh
# @File    : distance1.py
# @Software: PyCharm


import csv
import os
from geopy.distance import geodesic

ports_list = []
allports_list = []


def csv_process(filepath, filepaths):
    with open(filepath, mode='r', encoding='utf-8', newline='') as a, open(filepaths, mode='r', encoding='GBK',
                                                                           newline='') as b, open("results.csv",
                                                                                                  "w") as c:
        # 此处读取到的数据是将每行数据当做列表返回的
        reader = csv.reader(a)
        reader1 = csv.reader(b)
        writer = csv.writer(c)
        writer.writerow(["Seq", "station", "lat", "lon", "country", "gloss_number", "distance"])
        for row in reader:
            # 此时输出的是一行行的列表
            ports_list.append(row)
        for row1 in reader1:
            # 此时输出的是一行行的列表
            allports_list.append(row1)
        print(allports_list)
        print(ports_list)
        for i in range(1, len(ports_list)):
            if ports_list[i][2].find("S") != -1:
                ports_list[i][6] = '-' + ports_list[i][6]
                print(ports_list[i][6])
            if ports_list[i][3].find("W") != -1:
                ports_list[i][7] = '-' + ports_list[i][7]
                # print(ports_list[i][7])
            min_distance = geodesic((ports_list[i][6], ports_list[i][7]), (allports_list[1][4], allports_list[1][5]))
            min_index = []
            for j in range(1, len(allports_list)):
                t = geodesic((ports_list[i][6], ports_list[i][7]), (allports_list[j][4], allports_list[j][5]))
                if t < min_distance:
                    min_distance = t
                    min_index.append(j)
            min_index = min_index[-1]
            #     print(j)
            # print(i)
            print(min_distance)
            writer.writerows([[ports_list[i][0], ports_list[i][1], ports_list[i][2],
                              ports_list[i][3],
                              ports_list[i][4], allports_list[min_index][0], min_distance]])


def csv_test(filepath, filepaths):
    name, index = os.path.splitext(filepath)
    name1, index1 = os.path.splitext(filepaths)
    if index == '.csv' and index1 == '.csv':
        csv_process(filepath, filepaths)


def main():
    filepath = 'ports.csv'
    filepaths = 'allports.csv'
    csv_test(filepath, filepaths)


if __name__ == '__main__':
    main()
