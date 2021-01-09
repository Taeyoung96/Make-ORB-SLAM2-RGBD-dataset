import os
import argparse

def get_args():
    parser = argparse.ArgumentParser('To make ORB_SLAM2 Custom Dataset (RGB-D) - Taeyoung96')
    parser.add_argument('--rgb_path', required=True, help="Absolute Path of rgb.txt", type=str)
    parser.add_argument('--depth_path', required=True, help="Absolute Path of depth.txt", type=str)
    parser.add_argument('--output', required=True, help="Output name of txt file", type=str)

    args = parser.parse_args()
    return args

def make_association(opt):
    file_rgb_path = opt.rgb_path
    file_depth_path = opt.depth_path
    output = opt.output

    f_rgb = open(file_rgb_path,'r')
    f_depth = open(file_depth_path,'r')
    result = open(output,'w')
    cnt = 0 # rgb.txt, depth.txt 3줄을 skip하기 위해서
    while True:

        line_rgb = f_rgb.readline().splitlines()  # 한 줄씩 읽어오고 개행문자 제거
        line_depth = f_depth.readline().splitlines()

        if not line_rgb and not line_depth: break  # 불러올 것이 없으면 break

        cnt += 1

        if cnt > 3:  # rgb.txt, depth.txt 3줄을 skip하기 위해서
            str = line_rgb[0] + " " + line_depth[0]
            result.write(str)
            result.write('\n')

    # All files closed
    f_rgb.close()
    f_depth.close()
    result.close()

if __name__ == '__main__':
    opt = get_args()
    make_association(opt)
