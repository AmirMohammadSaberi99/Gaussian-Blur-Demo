# Create a function that applies Gaussian blur with a user-defined kernel size and sigma.#!/usr/bin/env python3
"""
gaussian_blur_demo.py

Loads an image, applies a user‑defined Gaussian blur, and shows
the original and blurred images side by side.
"""

import sys
from typing import Tuple

import cv2
import numpy as np
import matplotlib.pyplot as plt


def apply_gaussian_blur(
    image: np.ndarray,
    kernel_size: Tuple[int, int] = (5, 5),
    sigma: float = 0
) -> np.ndarray:
    """
    Apply a Gaussian blur to an image.

    Parameters
    ----------
    image : np.ndarray
        Input image in BGR channel order (as returned by cv2.imread).
    kernel_size : tuple of two ints, optional
        Size of the Gaussian kernel (both must be odd and > 1).
        Default is (5, 5).
    sigma : float, optional
        Standard deviation in X direction for the Gaussian kernel.
        If 0, it is calculated from the kernel size. Default is 0.

    Returns
    -------
    blurred : np.ndarray
        The blurred image, same shape and dtype as input.
    """
    # Validate kernel
    kx, ky = kernel_size
    if kx % 2 == 0 or ky % 2 == 0 or kx < 1 or ky < 1:
        raise ValueError("kernel_size must be a pair of odd integers > 1, e.g. (5,5)")

    # Apply Gaussian blur
    return cv2.GaussianBlur(image, (kx, ky), sigma)


def main(img_path: str, kernel_size: Tuple[int, int], sigma: float):
    # 1. Load the image
    image_bgr = cv2.imread(img_path)
    if image_bgr is None:
        print(f"Error: could not load image at '{img_path}'", file=sys.stderr)
        sys.exit(1)

    # 2. Blur the image
    blurred_bgr = apply_gaussian_blur(image_bgr, kernel_size, sigma)

    # 3. Convert both to RGB for plotting
    image_rgb  = cv2.cvtColor(image_bgr,  cv2.COLOR_BGR2RGB)
    blurred_rgb = cv2.cvtColor(blurred_bgr, cv2.COLOR_BGR2RGB)

    # 4. Display side by side
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(image_rgb)
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    axes[1].imshow(blurred_rgb)
    axes[1].set_title(
        f"Gaussian Blur {kernel_size[0]}×{kernel_size[1]}, σ={sigma}"
    )
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Apply Gaussian blur to an image and display results."
    )
    parser.add_argument(
        "image_path",
        help="Path to the input image (e.g. 'test.jpg')"
    )
    parser.add_argument(
        "--kernel", "-k",
        type=int,
        nargs=2,
        default=(5, 5),
        metavar=("KX", "KY"),
        help="Gaussian kernel size (odd integers), e.g. --kernel 5 5"
    )
    parser.add_argument(
        "--sigma", "-s",
        type=float,
        default=0,
        help="Sigma (standard deviation). Zero means auto-calc from kernel size."
    )

    args = parser.parse_args()
    main(args.image_path, tuple(args.kernel), args.sigma)
