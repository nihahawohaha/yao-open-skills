# Animation And Layering

## Layer Plan

For every shot, define only the layers needed for control:

- `bg`: background paper texture or scene base.
- `mid`: scenery, counters, landscape, or context.
- `fg`: foreground paper frame, leaves, hands, props.
- `subject`: product, character, mascot, or main object.
- `text`: screen label or subtitle-safe overlay.
- `fx`: paper dust, stamp mark, sparkle, line accent, transition wipe.

## HyperFrames Route

- Use transparent PNG layers when the scene needs parallax or independent motion.
- Name layers by shot and depth: `s03_bg.png`, `s03_subject_product.png`, `s03_text.png`.
- Keep important layers larger than frame bounds when they need camera movement.

## Static Fallback Route

When advanced animation is unavailable, create motion with:

- paper slide-in and slide-out
- mask reveal like scissors cutting across paper
- subtle 1-2 degree rotation wobble
- parallax push-in across depth layers
- shadow pulse on product reveal
- frame-by-frame stop-motion jitter at low amplitude
