import os
import shutil

def Copy_files(source_folder, destination_folder):
    # 遍历指定文件夹下的所有文件和子文件夹
    counts = 0
    fails = 0
    for root, dirs, files in os.walk(source_folder):
        # 遍历当前文件夹中的所有文件
        for file in files:
            # 构建源文件路径和目标文件路径
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)
            # 移动文件
            try:
                shutil.copy(source_path, destination_path)
                print(f"Copy {source_path} to {destination_path}")
                counts += 1
            except Exception as e:
                fails += 1
                print(f"移动文件失败:{source_path} and exception:{str(e)}")
    print(f"Successfully , copy {counts} files")
    print(f"Failed , copy {fails} files")

# 指定源文件夹和目标文件夹的路径
source_folder = "D:\\paradesign\\single_repository\\model"
destination_folder = "D:\\Desktop\\test_model_folder"

# 调用函数移动文件
Copy_files(source_folder, destination_folder)
