import cv2
import os

def extract_frames(video_path, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 使用OpenCV读取视频
    cap = cv2.VideoCapture(video_path)

    count = 0
    success = True

    while success:
        # 读取视频的下一帧
        success, image = cap.read()

        # 如果读取成功，则保存该帧为图片
        if success:
            if count > 30 and count <50:
                cv2.imwrite(os.path.join(output_folder, f"frame{count}.jpg"), image)
            count += 1
        else:
            break

    # 释放视频对象
    cap.release()

# 视频文件路径
video_path = 'a.webm'
# 输出文件夹路径
output_folder = './'

# 调用函数
extract_frames(video_path, output_folder)

print("视频截帧完成。")
