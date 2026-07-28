#!/usr/bin/env python3
"""把生圖結果置中裁切成目標比例（預設 16:9）。

多數生圖模型沒有 16:9 尺寸（例如 gpt-image-2 只有 1:1、3:2、2:3），
直接交給 verify_images.py 會全部判 INVALID。本腳本負責補這一段。

只做裁切，不做縮放、不重繪、不產生新畫面內容。
"""
import argparse
from pathlib import Path
import sys

try:
    from PIL import Image
except ImportError:
    raise SystemExit("Pillow is required: python -m pip install Pillow")


def parse_ratio(text):
    if ":" in text:
        width, height = text.split(":", 1)
        return float(width) / float(height)
    return float(text)


def crop_center(image, target_ratio):
    ratio = image.width / image.height
    if ratio > target_ratio:
        # 太寬，裁左右
        new_width = round(image.height * target_ratio)
        offset = (image.width - new_width) // 2
        return image.crop((offset, 0, offset + new_width, image.height))
    # 太高，裁上下
    new_height = round(image.width / target_ratio)
    offset = (image.height - new_height) // 2
    return image.crop((0, offset, image.width, offset + new_height))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--images-dir", required=True)
    parser.add_argument("--ratio", default="16:9")
    parser.add_argument("--tolerance", type=float, default=0.01)
    parser.add_argument("--outdir", help="省略則就地覆寫")
    parser.add_argument("--pattern", default="*.png")
    args = parser.parse_args()

    target_ratio = parse_ratio(args.ratio)
    folder = Path(args.images_dir)
    if not folder.is_dir():
        raise SystemExit(f"找不到目錄：{folder}")

    outdir = Path(args.outdir) if args.outdir else folder
    outdir.mkdir(parents=True, exist_ok=True)

    paths = sorted(folder.glob(args.pattern))
    if not paths:
        raise SystemExit(f"{folder} 裡沒有符合 {args.pattern} 的檔案")

    cropped = 0
    for path in paths:
        with Image.open(path) as image:
            ratio = image.width / image.height
            if abs(ratio - target_ratio) <= args.tolerance:
                print(f"{path.name}: {image.width}x{image.height} 已符合，略過")
                continue
            result = crop_center(image, target_ratio)
            target = outdir / path.name
            result.save(target)
            print(f"{path.name}: {image.width}x{image.height} -> {result.width}x{result.height}")
            cropped += 1

    print(f"完成：裁切 {cropped} 張，共 {len(paths)} 張")
    return 0


if __name__ == "__main__":
    sys.exit(main())
