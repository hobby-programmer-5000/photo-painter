# Photo Painter (사진 그리기)

사진을 넣으면 126 px 붓에서 3 px 붓까지, 붓 자국을 하나씩 놓아 그림으로 그려 주는 단일 웹 페이지입니다.

[English README](README.md)

> **이 저장소는 보관 처리되었습니다.** Photo Painter는 이제 tools 사이트에 있습니다:
> **https://hobby-programmer-5000.github.io/tools/photo-painter/**
> ([소스](https://github.com/hobby-programmer-5000/tools/tree/main/photo-painter)). 그쪽 버전에는 여기에 없는 수정이 들어 있습니다
> (투명 이미지, 페이지 어디에나 사진 놓기, 아주 가는 사진, 멈추지 않는 끝 버튼).
> 여기 있는 것은 오프라인 단일 파일로는 여전히 동작합니다. `index.html`을 내려받아 여세요.

## 쓰는 법

`index.html`을 브라우저로 엽니다. 설치할 것이 없고 인터넷 연결 없이도 동작합니다.

1. 사진을 페이지에 끌어다 놓거나, 고르거나, Ctrl+V로 붙여 넣습니다.
2. 그리는 모습을 봅니다. `일시정지`, `다시 그리기`, `1×`, `3×`, `끝`으로 조절합니다.
3. `PNG 저장`은 그 순간의 그림을 저장합니다.

사진은 브라우저 밖으로 나가지 않습니다. 페이지는 네트워크 요청을 하지 않고, 안에 사진이 들어 있지도 않습니다.

단축키: `Space` 일시정지, `R` 다시 그리기, `1` / `3` 속도, `E` 바로 완성, `S` 저장, `O` 사진 고르기.

화면은 한국어와 영어를 지원하고, 오른쪽 위 버튼으로 바꿉니다.

## 그리는 방법

Aaron Hertzmann의 "Painterly Rendering with Curved Brush Strokes of Multiple Sizes" (SIGGRAPH 98)를 따릅니다.
큰 붓에서 작은 붓 순서로, 붓 크기에 맞춰 흐리게 한 사진과 지금까지의 그림을 비교해서
아직 많이 다른 칸마다 가장 틀린 픽셀에서 붓 자국을 시작합니다. 붓 자국은 사진에서 색을 가져오고,
윤곽선을 따라가다가, 그림이 이미 사진에 더 가까운 곳에서 멈춥니다.
같은 사진은 항상 같은 그림이 됩니다.

## 빌드

`index.html`은 `src/painter.src.html`에 글꼴 두 개를 넣어 만듭니다. Python 3만 있으면 됩니다.

```bash
python tools/build.py
```

## 출처와 라이선스

- 코드: MIT. [LICENSE](LICENSE) 참고.
- 글꼴과 아이콘은 각자의 라이선스를 따릅니다. [CREDITS.md](CREDITS.md) 참고.
- 참고한 아이디어, 논문, 이 페이지의 출발점이 된 게시물은 [REFERENCES.md](REFERENCES.md)에 있습니다.
