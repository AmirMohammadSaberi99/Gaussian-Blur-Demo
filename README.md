# Gaussian Blur Demo

A simple Python script that loads an image, applies a user-defined Gaussian blur, and displays the original and blurred images side by side.

## Features

- Customizable Gaussian kernel size (odd integers > 1)
- Adjustable sigma (standard deviation) or auto-calculated from kernel size
- Command-line interface using `argparse`
- Displays images with Matplotlib

## Prerequisites

- Python 3.7 or higher
- [OpenCV (cv2)](https://pypi.org/project/opencv-python/)
- [NumPy](https://pypi.org/project/numpy/)
- [Matplotlib](https://pypi.org/project/matplotlib/)

## Installation

1. Clone this repository or download `gaussian_blur_demo.py` and this `README.md`.

2. Create and activate a virtual environment (optional, but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate  # Windows PowerShell
   ```

3. Install dependencies:
   ```bash
   pip install opencv-python numpy matplotlib
   ```

## Usage

Run the script from your terminal or command prompt:

```bash
python Practice2.py <image_path> [--kernel KX KY] [--sigma SIGMA]
```

- `<image_path>`: Path to the input image (e.g. `test.jpg`, `/mnt/data/photo.jpg`).
- `--kernel KX KY`, `-k KX KY`: Two odd integers specifying the Gaussian kernel size. Default is `5 5`.
- `--sigma SIGMA`, `-s SIGMA`: Standard deviation in the X direction for the Gaussian kernel. `0` (default) auto-calculates sigma based on kernel size.

### Examples

Apply default blur (5×5 kernel, auto sigma):
```bash
python gaussian_blur_demo.py test.jpg
```

Apply a stronger blur (7×7 kernel, sigma=1.5):
```bash
python gaussian_blur_demo.py test.jpg --kernel 7 7 --sigma 1.5
```

## Script Overview

```python
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
        Size of the Gaussian kernel (odd and > 1). Default is (5, 5).
    sigma : float, optional
        Standard deviation for the Gaussian kernel. 0 auto-calculates sigma.

    Returns
    -------
    np.ndarray
        Blurred image in BGR.
    """
    # Validation and blurring logic...
```

The `main` function handles loading the image, calling the blur function, converting to RGB for Matplotlib, and displaying the results side by side.

## License

This project is licensed under the MIT License. Feel free to use and modify it for your own purposes.

