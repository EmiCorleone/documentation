from pathlib import Path

from PIL import Image


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    src = repo_root / "logo" / "Vector (9).png"
    dest = repo_root / "logo" / "vector-black.png"

    if not src.exists():
        raise FileNotFoundError(f"Source logo not found: {src}")

    image = Image.open(src).convert("RGBA")
    pixels = image.load()

    # Replace all non-transparent pixels with solid black to create a dark variant.
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue
            pixels[x, y] = (0, 0, 0, a)

    image.save(dest)
    print(f"Saved black logo to {dest}")


if __name__ == "__main__":
    main()

