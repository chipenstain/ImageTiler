import argparse
import os

from PIL import Image

# allow huge images
Image.MAX_IMAGE_PIXELS = None


def ensure_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)


def main():
	parser = argparse.ArgumentParser(description="Universal image tiler NxM")
	parser.add_argument("input", help="Path to input image (GeoTIFF/JPG/PNG)")
	parser.add_argument("tiles_x", type=int, help="Number of tiles horizontally")
	parser.add_argument("tiles_y", type=int, help="Number of tiles vertically")
	parser.add_argument("-o", "--out", default="out", help="Output directory")

	args = parser.parse_args()

	ensure_dir(args.out)

	print("Loading:", args.input)
	img = Image.open(args.input)
	W, H = img.size
	print(f"Image size: {W}x{H}")

	Nx = args.tiles_x
	Ny = args.tiles_y

	tile_w = W // Nx
	tile_h = H // Ny

	print(f"Tiling into {Nx}x{Ny} tiles ({tile_w}x{tile_h} each)")

	for y in range(Ny):
		for x in range(Nx):
			left = x * tile_w
			top = y * tile_h
			right = left + tile_w
			bottom = top + tile_h

			tile = img.crop((left, top, right, bottom))

			out_name = f"{x}_{y}.webp"
			out_path = os.path.join(args.out, out_name)

			tile.save(
				out_path,
				"WEBP",
				quality=90,
				method=6,
				optimize=True,
				lossless=False
			)

			print("Saved:", out_name)

	print("Done.")


if __name__ == "__main__":
	main()
