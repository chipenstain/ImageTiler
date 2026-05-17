# 🌍 ImageTiler — high‑res Earth texture tiler

Small Python tool to slice **huge images** (like NASA 21600×10800 Earth maps) into
**Web‑optimized tiles** for WebGL globes, maps, and mobile apps.

- ✅ Supports **GeoTIFF / JPG / PNG**
- ✅ Tiles into **N × M** grid (e.g. `16×4`, `8×2`, `12×12`, …)
- ✅ Outputs **WebP** tiles optimized for web/phones
- ✅ Simple naming: `x_y.webp` in a single output folder

---

## 🔧 Requirements

- Python **3.9+** (Windows / macOS / Linux)
- Virtualenv (optional, but recommended)
- Python packages:
    - `Pillow`

Install dependencies:

```bash
pip install pillow
```

Run:

```bash
python main.py sample/world.200407.3x21600x10800_geo.tif 16 2 -o out
```

