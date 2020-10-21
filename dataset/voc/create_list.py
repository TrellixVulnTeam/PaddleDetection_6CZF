# Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
用于将标注数据集转换为 VOC 格式
执行以下脚本，将根据 ImageSets/Main 目录下的 trainval.txt 和 test.txt 文件在数据集根目录生成最终的 trainval.txt 和 test.txt 列表文件：
"""

import sys
import os.path as osp
import logging
import argparse

# add python path of PadleDetection to sys.path
parent_path = osp.abspath(osp.join(__file__, *(['..'] * 3)))
if parent_path not in sys.path:
    sys.path.append(parent_path)

from ppdet.utils.download import create_voc_list
logging.basicConfig(level=logging.INFO)


def main(config):
    voc_path = config.dataset_dir
    create_voc_list(voc_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    default_voc_path = osp.split(osp.realpath(sys.argv[0]))[0]
    parser.add_argument(
        "-d",
        "--dataset_dir",        # VOC格式数据集所在文件夹路径
        # default=default_voc_path,
        default='E:/project/dataset/insect_voc',
        type=str,
        help="VOC dataset directory, default is current directory.")
    config = parser.parse_args()

    main(config)
