import csv
import os
from geopy.distance import geodesic

ports_list = []
allports_list = []


def geodistance(lng1, lat1, lng2, lat2):
    print(geodesic((-23, 120.12802999999997), (28.7427, 115.86572000000001)).km)  # 计算两个坐标直线距离



def csv_process(filepath, filepaths):
    with open(filepath, mode='r', encoding='utf-8', newline='') as a, open(filepaths, mode='r', encoding='GBK',
                                                                           newline='') as b:
        # 此处读取到的数据是将每行数据当做列表返回的
        reader = csv.reader(a)
        reader1 = csv.reader(b)
        for row in reader:
            # 此时输出的是一行行的列表
            # print(row)
            ports_list.append(row)
        for row1 in reader1:
            # 此时输出的是一行行的列表
            # print(row1)
            allports_list.append(row1)
        print(allports_list)
        print(ports_list)
        # print("A")
        # print(ports_list[1][6])
        print(len(ports_list))
        print(len(allports_list))
        # =LEFT(C2,FIND("°",C2)-1)+MID(C2,FIND("°",C2)+1,FIND("′",C2)-FIND("°",C2)-1)/60
        for i in range(1, len(ports_list)+1):
            # print(i)
            if ports_list[i][2].find("N") != -1:
                print(ports_list[i][6])
            elif ports_list[i][2].find("S") != -1:
                ports_list[i][6] = '-'+ports_list[i][6]
                print(ports_list[i][6])
            min_distance = geodesic((ports_list[i][6], ports_list[1][4]), (allports_list[5]))
            for j in range(1, len(allports_list)+1):


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
