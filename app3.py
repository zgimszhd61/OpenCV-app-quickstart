from PIL import Image, ImageDraw, ImageFont

# 打开图片
image = Image.open('/Users/a0000/mywork/commonLLM/opensource/nnnew/OpenCV-app-quickstart/frame43.jpg')
width, height = image.size

# 创建一个可以在给定图片上绘图的对象
draw = ImageDraw.Draw(image)

# 指定中文字体和大小
font_cn = ImageFont.truetype('/System/Library/Fonts/STHeiti Light.ttc', size=44)
# 指定英文字体和大小
font_en = ImageFont.truetype('/System/Library/Fonts/STHeiti Light.ttc', size=30)

# 定义中英文文本
text_cn = "这里是你的字幕"
text_en = "This is your subtitle"

# 计算中文文本的位置，使其位于图片底部中央
bbox_cn = draw.textbbox((0, 0), text_cn, font=font_cn)
text_width_cn = bbox_cn[2] - bbox_cn[0]
text_height_cn = bbox_cn[3] - bbox_cn[1]
x_cn = (width - text_width_cn) / 2
y_cn = height - text_height_cn

# 计算英文文本的位置，使其位于中文文本上方一定距离
bbox_en = draw.textbbox((0, 0), text_en, font=font_en)
text_width_en = bbox_en[2] - bbox_en[0]
text_height_en = bbox_en[3] - bbox_en[1]
x_en = (width - text_width_en) / 2
y_en = y_cn - text_height_en - 10  # 在中文文本上方留出10像素的间距

# 打印英文字幕的位置坐标
print(f"英文字幕的位置坐标: ({x_en}, {y_en})")

# 添加英文文本
draw.text((x_en, y_en), text_en, fill="white", font=font_en)
# 添加中文文本
draw.text((x_cn, y_cn), text_cn, fill="white", font=font_cn)

# 根据英文字幕的位置坐标分割图片
cropped_image = image.crop((0, y_en, width, height))

# 保存分割后的图片
cropped_image.save('image_with_subtitle_cropped.jpg')