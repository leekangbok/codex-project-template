---
name: slack-gif-creator
description: Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack."
license: Complete terms in LICENSE.txt
---

# Slack GIF Creator

## Slack Requirements
- **Emoji GIFs**: 128x128 (max 3 seconds)
- **Message GIFs**: 480x480
- **FPS**: 10-20
- **Colors**: 48-128

## Core Workflow
Use Python's `Pillow` (PIL) and `imageio` to build GIFs:

```python
from PIL import Image, ImageDraw
# 1. Generate frames
frames = []
for i in range(20):
    img = Image.new('RGB', (128, 128), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Draw logic here...
    frames.append(img)

# 2. Save
frames[0].save('output.gif', save_all=True, append_images=frames[1:], duration=100, loop=0)
```

## Animation Concepts
- **Shake**: Oscillate position using `math.sin()`.
- **Pulse**: Scale size rhythmically between 0.8x and 1.2x.
- **Bounce**: Use easing functions (e.g., `bounce_out`) for movement.
- **Particles**: Radiating shapes that fade over time.

## Design Tips
- **Thick Lines**: Always use `width=2` or higher for outlines.
- **Vibrant Colors**: Use high-contrast palettes.
- **Visual Depth**: Layer shapes and use gradients.
- **Polished Graphics**: Avoid basic placeholders; make them look meticulously crafted.

## Optimization
- Reduce FPS or number of colors (e.g., `colors=64`) to keep file size small.
- Use `optimize=True` in Pillow's save method.
