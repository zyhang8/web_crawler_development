# 潮汐项目相关杂项

## distance.py

遍历ports.csv文件，读取每条数据，然后到allports.csv中查找所有行，找到与ports.csv中所选行坐标所对应的点最近的那个点，然后输出到results.csv。results.csv中列为
Seq， station， lat， lon， country， gloss_number, distance
其中Seq， station， lat， lon， country是ports.csv中的列名，gloss_number是从allports.csv中查到最近点的gloss_number，distance是ports.csv所选行站点与allports.csv中最近点的距离。
