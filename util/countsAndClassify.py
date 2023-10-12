#扫描目标文件夹，统计总文件数、分类文件及其数量
import os

def count_file_types(folder_path):
    file_types = {}
    file_counts = 0

    # 遍历目标文件夹及其子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 获取文件后缀名
            _, ext = os.path.splitext(file)
            ext = ext.lower()  # 将后缀名转换为小写

            # 统计文件类型
            if ext in file_types:
                file_types[ext] += 1
            else:
                file_types[ext] = 1
            file_counts += 1

    # 打印文件后缀名及其数量
    for ext, count in file_types.items():
        print(f"{ext} 类文件数: {count} 个")
    print(f"总文件数: {file_counts} 个")

# 指定目标文件夹路径
folder_path = "C:\\Users\\Aoer\\Downloads\\富美家材質"

# 调用函数进行统计
count_file_types(folder_path)