import json

"""
这段Python代码的功能是将输入的GIF动画文件分离成多个PNG图片，并将这些图片保存到一个指定的文件夹中。然后，这些图片会被转换成JSON格式的数据，并保存在另一个文件中。

下面是这段代码的详细解释：

导入需要的库：json用于处理JSON数据，PIL（Pillow）用于处理图片，os和sys用于处理操作系统相关的功能。

定义frames_to_files函数：这个函数接受两个参数，一个是GIF文件的路径，另一个是输出文件夹的路径。它会将GIF文件中的每一帧都保存为一个PNG图片，并保存在指定的输出文件夹中。

首先，它会检查输出文件夹是否存在，如果不存在，则创建这个文件夹。
然后，使用Pillow库打开GIF文件，并循环遍历每一帧。对于每一帧，它会拼接输出文件的路径，并保存这一帧为一个PNG图片。同时，它会将保存的路径添加到一个列表中。
定义main函数：这个函数首先提示用户输入GIF文件的路径和输出文件夹的路径，然后调用frames_to_files函数将GIF文件转换为PNG图片，并保存在指定的输出文件夹中。

定义Extract_RGB_from_a_9_by_9_grid_image函数：这个函数接受一个图片文件的路径作为参数，然后提取这个图片中所有像素的RGB值，并返回这些值的列表。

在主程序部分，首先提示用户输入GIF文件的路径和输出文件夹的路径，然后调用main函数执行主要的功能。

注意：在代码的最后，有一行img.close()用于关闭打开的图片对象，释放资源。这是一个良好的编程习惯，可以避免因为忘记关闭文件而导致的资源泄露。

"""
from PIL import Image
import os
import sys

import numpy as np


def frames_to_files(input_file, output_folder, postfix):
    """
    将GIF文件分离成多个PNG图片并保存到指定文件夹中

    Args:
        input_file (str): GIF文件的路径
        output_folder (str): 输出文件夹的路径

    Returns:
        list: 所有输出的图片文件列表
    """
    filename = input_file
    pictures = []
    # 如果输出文件夹不存在，则创建输出文件夹
    # 如果输出文件夹不存在，则创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with Image.open(input_file) as im:
        i = 0
        filename = generate_output_picture_filename(
            input_file, output_folder, postfix, i
        )
        im.save(filename, "PNG")
        pictures.append(filename)
        print(f"图片文件已保存到：{filename}")
        i = 1
        # 拼接输出文件路径
        # 拼接输出文件路径
        filename = generate_output_picture_filename(
            input_file, output_folder, postfix, i
        )
        # 保存第一帧图片
        # 保存第一帧图片
        im.save(filename, "PNG")
        print(f"图片文件已保存到：{filename}")
        pictures.append(filename)
        try:
            # 循环遍历GIF文件的每一帧
            # 循环遍历GIF文件的每一帧
            while 1:
                # 向下一帧移动
                # 向下一帧移动
                im.seek(im.tell() + 1)  # 向下一帧移动
                filename = generate_output_picture_filename(
                    input_file, output_folder, postfix, i
                )
                # 保存当前帧图片
                # 保存当前帧图片
                im.save(filename, "PNG")  # 保存下一帧
                print(f"图片文件已保存到：{filename}")
                pictures.append(filename)
                i = i + 1
        except EOFError:
            pass
    # im.close()  # 关闭打开的图片文件
    return pictures


def generate_output_picture_filename(input_file, output_folder, postfix, i):
    """
    生成输出图片的文件名。

    Args:
        input_file: 输入图片的文件路径。
        output_folder: 输出文件夹的路径。
        postfix: 新生成文件的后缀名。
        i: 当前迭代的次数。

    Returns:
        生成的输出图片的文件名。

    """
    # 使用os模块中的join函数拼接文件路径
    filename = os.path.join(
        output_folder,
        # 获取输入文件的基本名称（不包含路径）
        os.path.splitext(os.path.basename(p=input_file))[0] +  # 分割文件扩展名并获取基本名称
        # 拼接后缀名和新文件扩展名
        postfix + f"-{i}.png",
    )

    return filename


def main():
    """
    从标准输入中读取文件名，将文件名分别存储到变量filename和outdir中。
    使用frames_to_files()函数将输入的动画图片文件名filename转换为图片文件，存储到outdir文件夹下。
    返回存储图片的文件夹路径。

    Args:
        无

    Returns:
        None
    """
    # 提示用户输入文件名
    print("请输入多个动画图片文件名：")

    # 从标准输入中读取文件名
    # 从标准输入中读取文件名
    filenames = [s.strip('"') for s in sys.stdin.readline().strip().split(" ")]

    # 打印文件名
    print("你输入的多个动画图片文件名是：", " ".join(filenames))

    # 提示用户输入文件名
    print("请输入导出的图片和动画文件夹：")

    # 从标准输入中读取文件名
    outdir = sys.stdin.readline().strip().strip('"')

    # 打印文件名
    print("你输入的导出的图片和动画文件夹是：", outdir)
    k = 0
    for filename in filenames:
        # 使用frames_to_files()函数将输入的动画图片文件名filename转换为图片文件，存储到outdir文件夹下。
        # 使用方式
        pictures = frames_to_files(filename, outdir, str(k))

        # 打印图片文件列表
        # print(pictures)
        filenameanim = os.path.join(
            outdir,
            os.path.splitext(os.path.basename(p=filename))[0] + "-" + str(k) + ".anim",
        )

        # 创建Python对象，保存动画信息
        animdata = {
            "name": os.path.splitext(os.path.basename(p=filename))[0],
            "createdate": "2023-11-15T15:33:29.5301256+08:00",
            "changedate": "2023-11-15T15:33:29.5301256+08:00",
            "fps": 10,
            "anim": [],
        }

        # 遍历图片文件列表，并将其转换为RGB值，保存到"anim"字段中
        # 遍历图片文件列表，并将其转换为RGB值
        for pic in pictures:
            animdata["anim"].append(
                {"frame": Extract_RGB_from_a_9_by_9_grid_image(pic)}
            )

        # 将Python对象转换为JSON字符串
        json_str = json.dumps(animdata)

        # 打开一个文件，准备写入JSON字符串
        with open(filenameanim, "w") as f:
            # 将JSON字符串写入文件
            f.write(json_str)

        # 关闭文件
        f.close()
        print(f"动画文件已保存到：{filenameanim}")
        k = k + 1


def Extract_RGB_from_a_9_by_9_grid_image(filename):
    """
    从9x9网格的图像中提取RGBA值。

    Args:
        filename: 包含9x9网格图像的文件名。

    Returns:
        包含所有像素RGB值的列表。

    """
    # 获取页面中第一个img元素
    # 获取图片对象
    img = Image.open(filename)  # 请将"your_image_path"替换为实际图片路径

    # 创建canvas并设置其大小与图片大小相同
    # 创建一个空画布，大小与图片相同
    canvas = Image.new("RGBA", img.size)

    # 将图片绘制到canvas上
    # 将原始图片复制到新创建的画布上
    canvas.paste(img, (0, 0))

    # 获取canvas的像素数据
    # 将画布的像素数据转换为数组，并压缩为一维数组
    pixels = np.array(canvas.getdata()).flatten()
    # 打印像素数据
    # print(pixels)

    # 计算区块大小
    # 计算每个区块的大小
    block_size = int(img.width / 9)

    # 初始化结果数组
    # 初始化结果列表
    res = []

    # 遍历每个区块，并对其像素进行处理
    for i in range(9):
        for j in range(9):
            # 计算每个区块的中心点坐标
            center_x = block_size * (j + 0.5)
            center_y = block_size * (i + 0.5)
            # 计算中心点对应的像素在数组中的索引位置（由于像素数据是RGBA格式，因此需要乘以4）
            index = int(center_y * img.width + center_x) * 4  # 由于像素数据是RGBA格式，因此需要乘以是4
            # 从像素数组中获取RGB值，并将它们添加到结果列表中。这里只是简单地将RGB值添加到结果列表中。
            r, g, b = pixels[index], pixels[index + 1], pixels[index + 2]
            a = pixels[index + 3]
            res.append(int(r * a / 255))  # 这里是将RGBA的R通道值乘以透明度a，再除以255，取整数部分添加到结果列表中。
            res.append(int(g * a / 255))  # 同上，处理G通道的值。
            res.append(int(b * a / 255))  # 同上，处理B通道的值。

    # 打印结果列表
    # print(res)
    # 将结果列表转换为JSON格式并输出（此行代码已被注释掉）
    # print(json.dumps(res))
    img.close()  # 关闭图片对象，释放资源。
    return res  # 返回包含所有像素RGB值的列表。


if __name__ == "__main__":
    main()
