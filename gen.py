from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Enable AVIF support via pillow-avif-plugin
try:
    import pillow_avif  # noqa: F401
    AVIF_SUPPORTED = True
except ImportError:
    AVIF_SUPPORTED = False

# Font configuration: use Roboto Bold from local static folder
FONT_PATH = Path("Roboto/static/Roboto-Bold.ttf")
if not FONT_PATH.exists():
    FONT_PATH = None

# Base specifications: size name -> (width, height)
specs = {
    "small":      (200, 150),
    "medium":     (400, 300),
    "large":      (800, 600),
    "verylarge": (1440, 1080),
}
# Densities and formats to generate
densities = [1, 2]
formats   = ["JPEG", "WEBP"] + (["AVIF"] if AVIF_SUPPORTED else [])

# Output directory
target_dir = Path("images")
target_dir.mkdir(exist_ok=True)

def generate_images():
    for name, (bw, bh) in specs.items():
        for d in densities:
            # Calculate actual pixel dimensions
            W, H = bw * d, bh * d
            text_label = f"{name} {d}x {W}x{H}"
            for fmt in formats:
                text = f"{text_label} {fmt.lower()}"

                # Create image canvas
                img  = Image.new("RGB", (W, H), (200,200,200))
                draw = ImageDraw.Draw(img)

                # Binary search for font size so text width <= 80% of canvas
                lo, hi, best = 6, H, 6
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if FONT_PATH:
                        font = ImageFont.truetype(str(FONT_PATH), size=mid)
                    else:
                        font = ImageFont.load_default()
                    tw = draw.textlength(text, font=font)
                    if tw <= W * 0.8:
                        best = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                # Final render with optimal size
                if FONT_PATH:
                    font = ImageFont.truetype(str(FONT_PATH), size=best)
                else:
                    font = ImageFont.load_default()
                tw = draw.textlength(text, font=font)
                th = best  # approximate line height = font size
                x = (W - tw) / 2
                y = (H - th) / 2
                draw.text((x, y), text, font=font, fill=(50,50,50))

                # Save with correct extension
                suffix = f"@{d}x" if d > 1 else ""
                filename = f"image-{name}{suffix}.{fmt.lower()}"
                img.save(target_dir / filename, format=fmt)

if __name__ == "__main__":
    generate_images()
