from PIL import Image

# 打开两张图片
image1 = Image.open('a1.jpg')
image2 = Image.open('a2.jpg')

# 获取两张图片的宽度和高度
width1, height1 = image1.size
width2, height2 = image2.size

# 计算合并后的图片的总高度和最大宽度
total_height = height1 + height2
max_width = max(width1, width2)

# 创建一个新的图片，用于存放合并后的图片
# 新图片的宽度为两张图片宽度的最大值，高度为两张图片高度之和
merged_image = Image.new('RGB', (max_width, total_height))

# 将第一张图片粘贴到合并后的图片上，位置为左上角
merged_image.paste(image1, (0, 0))

# 将第二张图片粘贴到合并后的图片上，位置为第一张图片的下方
merged_image.paste(image2, (0, height1))

# 保存合并后的图片
merged_image.save('merged_image.jpg')

# 显示合并后的图片
merged_image.show()