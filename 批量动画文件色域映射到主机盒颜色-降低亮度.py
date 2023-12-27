import os
import sys

import json

"""
    这段Python代码主要实现了一个功能：从输入的动画文件中读取像素的RGB值，并保存到指定的输出目录中。

下面是这段代码的详细解释：

首先，导入需要的模块，包括os（用于操作系统相关的功能）、sys（用于读取标准输入）、json（用于处理JSON数据）。
定义两个函数encode_json和decode_json，用于将Python对象编码为JSON字符串以及将JSON字符串解码为Python对象。
定义main函数，该函数从标准输入读取多个文件名和输出目录，并调用modify_animation函数处理这些文件。
定义modify_animation函数，该函数接收输入文件列表和输出目录作为参数。对于每个输入文件，它首先解码文件内容为JSON对象，然后遍历"anim"字段（应该是一个包含多个字典的列表，每个字典代表一帧图像的数据），查找特定RGB值的像素。如果找到，将这个像素修改为黑色；否则，将像素的RGB值乘以一个系数（这里为35/255和40/255）。处理完所有帧后，将新的数据编码为JSON并保存到指定的输出目录中。
如果这个Python文件是直接运行的，而不是被导入的，那么会调用main函数。
注意：这段代码需要从标准输入读取文件名和输出目录，所以你可能需要在命令行中运行它，并输入相应的信息。
    """


def encode_json(data):
    """
    将Python对象编码为JSON字符串。
    """
    # 使用json模块的dumps函数将Python对象编码为JSON字符串
    return json.dumps(data)


def decode_json(json_string):
    """
    将JSON字符串解码为Python对象。

    Args:
        json_string (str): 需要解码的JSON字符串。

    Returns:
        Any: 解码后的Python对象。

    """
    # 将JSON字符串解码为Python对象。
    return json.loads(json_string)


def main():
    """
    从标准输入读取多个文件和输出目录，调用modify_animation函数生成动画。

    Args:
        无参数。

    Returns:
        无返回值。

    """
    # 从标准输入读取多个文件和输出目录
    print("请输入多个动画图片文件名：")
    # 将输入的多个文件名以空格分隔，并去除首尾的空格
    input_files = [s.strip('"') for s in sys.stdin.readline().strip().split(" ")]
    # print(input_files)
    print("你输入的动画图片文件名是：", " ".join(input_files))
    print("请输入导出的动画文件夹：")
    # 获取输出的文件夹路径，并去除首尾的空格
    output_dir = sys.stdin.readline().strip().strip('"')
    print("你输入的导出的动画文件夹是：", output_dir)
    # 如果输出的文件夹不存在，则创建该文件夹
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # 调用modify_animation函数并传入参数
    # 调用修改动画函数并传入参数
    modify_animation(input_files, output_dir)


def modify_animation(input_files, output_dir):
    """
    修改输入的动画文件，将指定RGB值的像素修改为黑色，并保存到输出目录中。

    Args:
        input_files (List[str]): 输入的动画文件列表。
        output_dir (str): 输出目录路径。

    Returns:
        None
    """
    # 遍历输入的动画文件列表
    # 打开每个动画文件，读取每个像素的RGB值并修改
    k = 0
    for file in input_files:
        with open(file, "r") as f:
            content = f.read()
            data = decode_json(content)
            outputdata = decode_json(content)
            outputdata["anim"] = []
            for line in data["anim"]:
                # 解析每行数据，获取像素的RGB值
                values = line["frame"]
                new_values = []
                for i in range(0, len(values), 3):
                    r, g, b = int(values[i + 0]), int(values[i + 1]), int(values[i + 2])

                    new_r = r
                    new_g = g
                    new_b = b

                    new_r = int(new_r * 30 / 255)
                    new_g = int(new_g * 40 / 255)
                    new_b = int(new_b * 40 / 255)

                    new_values.extend((new_r, new_g, new_b))

                outputdata["anim"].append({"frame": new_values})
            outputfile = os.path.join(
                output_dir,
                os.path.splitext(os.path.basename(file))[0]
                + "-"
                + str(k)
                + os.path.splitext(file)[-1],
            )

            with open(
                outputfile,
                "w",
            ) as out_f:
                out_f.write(encode_json(outputdata))
                print(f"动画文件已保存到：{outputfile}")
        k = k + 1


if __name__ == "__main__":
    main()
