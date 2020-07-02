import os

# 指定想要统计的文件类型
whitelist = ['py']


# 遍历文件, 递归遍历文件夹中的所有
def get_file(file_list, base_dir):
    for parent, dir_names, file_names in os.walk(base_dir):
        for filename in file_names:
            ext = filename.split('.')[-1]
            # 只统计指定的文件类型，略过一些log和cache文件
            if ext in whitelist:
                file_list.append(os.path.join(parent, filename))


# 统计一个文件的行数
def count_line(file, ):
    count = 0
    for file_line in open(file, encoding="utf-8").readlines():
        if file_line != '' and file_line != '\n':  # 过滤掉空行
            count += 1
    print(file + '----', count)
    return count


def main(base_dir):
    file_list = []
    get_file(file_list, base_dir)

    total_line = 0
    for file_list in file_list:
        total_line = total_line + count_line(file_list)
    print('total lines:', total_line)


if __name__ == '__main__':
    basedir = r'/root'
    main(basedir)
