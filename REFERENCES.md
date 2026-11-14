# References

Where the ideas in this page come from.

## Starting point

| Item | Source |
|---|---|
| The post that showed a paint program painting a portrait by itself | NinjaCodex (@N1njaCodex), X, 2026-11-15. https://x.com/N1njaCodex/status/2121670607314072032 |
| The prompt for it (a reply by the same author) | https://x.com/N1njaCodex/status/2121670780983611455 |

The screen layout (app bar, brush row with eight sizes, canvas, Reference card, painting passes, stroke counter,
Pause / Restart / 1× / 3× / End / Change photo), the brush sizes and the one-line English note under the controls
follow that prompt and the video in the post. The prompt itself is not copied here. The code was written for this project.
The photo shown in the post is not included.

## Algorithm

| Paper | What was taken |
|---|---|
| Aaron Hertzmann, "Painterly Rendering with Curved Brush Strokes of Multiple Sizes", SIGGRAPH 98, pp. 453–460. https://mrl.cs.nyu.edu/publications/painterly98/ | The core method: layers from large brush to small, patch-wise comparison with a blurred photo, strokes along the normals of the luminance gradient, stopping where the painting is already closer |
| Peter Litwinowicz, "Processing Images and Video for an Impressionist Effect", SIGGRAPH 97, pp. 407–414. https://www.cs.princeton.edu/courses/archive/fall00/cs597b/papers/litwinowicz97.pdf | Stroke direction perpendicular to the image gradient, handling of flat areas |
| Paul Haeberli, "Paint by Numbers: Abstract Image Representations", SIGGRAPH 90, pp. 207–214. https://history.siggraph.org/?p=122064 | Picking colours from a photo to build a painting out of brush marks |

Differences from Hertzmann's paper: strokes are round-capped polylines of 2 to 8 steps instead of splines;
they are laid roughly top to bottom instead of in random order; each brush size has a stroke budget;
three box blurs stand in for a Gaussian.

## Interface

| Document | Applied to |
|---|---|
| WCAG 2.2, SC 1.4.3 Contrast (Minimum). https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html | Text colours, light and dark themes |
| WCAG 2.2, SC 2.5.8 Target Size (Minimum). https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html | Button heights |
| MDN, `prefers-reduced-motion`. https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion | With reduced motion on, the finished painting is shown at once |
| MDN, `prefers-color-scheme`. https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme | Light and dark themes |
| WAI-ARIA Authoring Practices Guide, Button pattern. https://www.w3.org/WAI/ARIA/apg/patterns/button/ | `aria-pressed` on the speed buttons |
| Jakob Nielsen, "10 Usability Heuristics for User Interface Design". https://www.nngroup.com/articles/ten-usability-heuristics/ | Visible status (brush, colour, pass, strokes, progress) and user control (Pause, Restart, End) |
