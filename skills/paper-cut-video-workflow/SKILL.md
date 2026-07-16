---
name: paper-cut-video-workflow
description: Create paper-cut style short videos from product brief to final delivery in Codex, Claude Code, Trae, Cursor, and other file-based AI agents. Use when the user asks for 剪纸风格视频, paper-cut animation, product brief to script, storyboard, keyframe prompts, layered transparent PNG assets, HyperFrames animation planning, IndexTTS-2 or alternate voiceover routes, music and SFX planning, audio ducking, final video composition, quality control, revision planning, or delivery checklists.
---

# Paper-Cut Video Workflow

## Purpose

Produce a paper-cut style short video through a controlled production pipeline: brief, script, storyboard, keyframes, layered assets, voiceover, timing, music/SFX, composition, QC, revisions, and delivery.

## Default Trigger

User intent may be phrased as:

> 帮我做一个剪纸风格短视频，从产品简报、脚本、分镜、关键帧、旁白、配乐、合成到最终质检交付。

## Operating Rules

- Resolve every relative file reference from the directory containing this `SKILL.md`, never from the user's current working directory.
- Read `references/platform-compatibility.md` only when installing, adapting, or troubleshooting this skill in a specific AI coding tool.
- Treat this as a director-style workflow, not a one-shot generation request.
- Confirm the product brief, script, and storyboard before generating final visual/audio assets.
- Keep private voice samples, reference videos, generated voices, and product-confidential files in the project folder only. Do not store them inside this skill.
- Prefer a 20-60 second vertical video unless the user specifies another platform, duration, or aspect ratio.
- When product details are missing, create a fillable project pack and clearly list what is needed before production.
- Use existing local video, FFmpeg, TTS, and image/video generation tools when available; otherwise provide exact production specs and placeholders.

## Workflow

1. Build or validate the product brief.
   - Read `references/intake-template.md`.
   - Confirm product, audience, platform, aspect ratio, target duration, language, offer, CTA, brand constraints, privacy constraints, and reference-video role.

2. Create script, narration, and storyboard.
   - Read `references/script-storyboard-template.md`.
   - Produce a hook, product promise, proof beats, CTA, spoken narration, screen text, shot list, transitions, and revision questions.
   - Stop for confirmation if the user has not approved the story direction.

3. Lock paper-cut visual standards and keyframe prompts.
   - Read `references/paper-cut-visual-spec.md`.
   - Use `assets/prompt-templates/keyframe-prompts.md` for image prompts.
   - Keep a consistent palette, paper fiber, cut edges, layered shadows, stop-motion feel, and simplified character/product shape language.

4. Plan layered PNGs, HyperFrames, and fallback animation.
   - Read `references/animation-layering.md`.
   - Split each shot into background, midground, foreground, product/character, props, text, and effect layers.
   - Use transparent PNG assets for controllable parallax and reveal animation.
   - If HyperFrames is unavailable, use static fallback animation: paper slide, mask reveal, scale push, rotation wobble, shadow pulse, and camera parallax.

5. Generate or collect voiceover.
   - Read `references/voice-routes.md`.
   - Use IndexTTS-2 only when local/private voice generation is required and permitted.
   - Use MiniMax, ElevenLabs, or human recording when they better fit speed, language, quality, or rights constraints.
   - Never clone or imitate a person without explicit rights or consent.

6. Lock shot duration from narration.
   - Use `scripts/plan_scene_durations.py` when a shot list CSV exists.
   - Fit visual timing to spoken narration first, then adjust motion density.
   - Keep text overlays readable and leave CTA breathing room.

7. Plan music, SFX, and ducking.
   - Read `references/audio-mix-qc.md`.
   - Place music below narration, duck under speech, and add motivated paper/transition SFX.

8. Compose and perform QC.
   - Read `references/final-qc.md`.
   - Check format, resolution, fps, codecs, loudness, decode integrity, subtitles/safe areas, black frames, alpha issues, pacing, pronunciation, and story clarity.

9. Revise and deliver.
   - Read `references/delivery-checklist.md` and `references/privacy-rules.md`.
   - Use `scripts/make_delivery_manifest.py` to create a manifest when final outputs exist.
   - Group revisions into script, visual, timing, voice, music/SFX, and export categories.

## Expected Project Outputs

- `01_brief.md`
- `02_script_storyboard.md`
- `03_visual_spec.md`
- `04_keyframe_prompts.md`
- `05_voiceover_plan.md`
- `06_timing_plan.csv`
- `07_audio_plan.md`
- `08_qc_report.md`
- `09_delivery_manifest.md`
- Final video, preview video, cover frame, narration audio, subtitle file, layered PNGs, source project, prompt log, music/SFX license notes, and privacy notes when available.

## Bundled Resources

- `references/intake-template.md`: Product brief fields.
- `references/script-storyboard-template.md`: Script, narration, and shot-list format.
- `references/paper-cut-visual-spec.md`: Visual style rules.
- `references/animation-layering.md`: Layer and motion planning.
- `references/voice-routes.md`: IndexTTS-2, MiniMax, ElevenLabs, and human recording routes.
- `references/audio-mix-qc.md`: Music, SFX, and ducking rules.
- `references/final-qc.md`: Technical and human review checklist.
- `references/delivery-checklist.md`: Final handoff package.
- `references/privacy-rules.md`: Privacy and voice rights boundaries.
- `references/platform-compatibility.md`: Codex, Claude Code, Trae, Cursor, and generic-agent installation routes.
- `assets/prompt-templates/keyframe-prompts.md`: Reusable keyframe prompt formulas.
- `assets/project-templates/shotlist.csv`: Shot-list starter table.
- `scripts/plan_scene_durations.py`: Estimate scene durations from narration.
- `scripts/make_delivery_manifest.py`: Create a deliverable inventory.
