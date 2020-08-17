import os
import random
from argparse import ArgumentParser

import matplotlib
import matplotlib.pyplot as plt
import torch
import numpy as np
import base64
import io
import re

from PIL import Image
from torchvision import transforms

from gan_module import Generator

parser = ArgumentParser()
parser.add_argument('--image_dir', default='/Downloads/CACD_VS/', help='The image directory')


@torch.no_grad()
def agingTranslate(data):
    model = Generator(ngf=32, n_residual_blocks=9)
    ckpt = torch.load('pretrained_model/state_dict.pth', map_location='cpu')
    model.load_state_dict(ckpt)
    model.eval()
    trans = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    ])

    # base64 string을 이미지로 변환
    data = re.search(r'base64,(.*)', data).group(1)
    img = Image.open(io.BytesIO(base64.b64decode(data))).convert('RGB')

    img = trans(img).unsqueeze(0)
    aged_face = model(img)
    aged_face = (aged_face.squeeze().permute(1, 2, 0).numpy() + 1.0) / 2.0
    outimg = Image.fromarray((aged_face * 255).astype(np.uint8))

    # 이미지를 base64로 변환
    im_file = io.BytesIO()
    outimg.save(im_file, format="PNG")
    im_bytes = im_file.getvalue()
    im_b64 = base64.b64encode(im_bytes)

    return im_b64
