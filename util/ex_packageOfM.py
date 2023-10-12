#扩增素材包
import os
import shutil

def copy_folders(source_path, destination_path, num_copies):
    # 获取源文件夹的名称
    folder_name = os.path.basename(source_path)

    # 循环复制文件夹
    for i in range(num_copies):
        new_folder_name = f"{folder_name}_{i+1}"  # 构建新文件夹名称
        new_folder_path = os.path.join(destination_path, new_folder_name)  # 构建新文件夹路径

        # 复制文件夹
        shutil.copytree(source_path, new_folder_path)

        print(f"复制文件夹 {new_folder_name} 成功")

# 指定源文件夹路径、目标文件夹路径和复制次数
source_folder_path = "D:\\Desktop\\测试材质包"
destination_folder_path = "C:\\Users\\Aoer\\Downloads\\富美家材質"
num_copies = 500

# 调用函数进行复制
copy_folders(source_folder_path, destination_folder_path, num_copies)