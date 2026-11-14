# Photo Painter

A single web page that paints any photo you give it, stroke by stroke, from a 126 px brush down to 3 px.

[한국어 README](README.ko.md)

## Use

Open `index.html` in a browser. Nothing to install, and it works offline.

1. Drop a photo on the page, choose one, or paste one with Ctrl+V.
2. Watch it paint. `Pause`, `Restart`, `1×`, `3×` and `End` control the run.
3. `Save PNG` saves the painting as it is at that moment.

The photo stays in your browser. The page makes no network requests and bundles no photo.

Keys: `Space` pause, `R` restart, `1` / `3` speed, `E` finish at once, `S` save, `O` choose a photo.

The page comes in English and Korean; the button at the top right switches.

## How it paints

It follows Aaron Hertzmann's "Painterly Rendering with Curved Brush Strokes of Multiple Sizes" (SIGGRAPH 98).
For each brush size, large to small, it blurs the photo to match the brush, compares it with the painting so far,
and starts a stroke at the worst pixel of each patch that is still far off. A stroke takes its colour from the photo,
follows the edge it is on, and stops where the painting is already closer to the photo.
The same photo always gives the same painting.

## Build

`index.html` is built from `src/painter.src.html` by inlining the two fonts. It needs only Python 3.

```bash
python tools/build.py
```

## Credits and licence

- Code: MIT, see [LICENSE](LICENSE).
- Fonts and icons keep their own licences, see [CREDITS.md](CREDITS.md).
- Ideas, papers and the post this page started from are in [REFERENCES.md](REFERENCES.md).
