"""Build the single-file page: inline the two fonts into src/painter.src.html.

    python tools/build.py   ->  index.html

Needs only Python 3. The page must not carry any photo, so the build stops if it finds one.
"""
import base64
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def data_uri(path: pathlib.Path, mime: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def main() -> int:
    src = (ROOT / "src" / "painter.src.html").read_text(encoding="utf-8")
    if "data:image" in src:
        print("FAIL: the source must not carry a photo")
        return 1
    parts = {
        "__FONT_FIGTREE__": data_uri(ROOT / "assets" / "figtree" / "Figtree-wght.woff2", "font/woff2"),
        "__FONT_MONO__": data_uri(ROOT / "assets" / "jetbrains-mono" / "JetBrainsMono-Regular.woff2", "font/woff2"),
    }
    for key, value in parts.items():
        if src.count(key) != 1:
            print(f"FAIL: expected exactly one {key} in the source, found {src.count(key)}")
            return 1
        src = src.replace(key, value)
    out = ROOT / "index.html"
    out.write_text(src, encoding="utf-8", newline="\n")
    print(f"wrote {out} ({out.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
