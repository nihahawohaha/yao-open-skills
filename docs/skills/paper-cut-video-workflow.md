# Paper-Cut Video Workflow

`paper-cut-video-workflow` 是一个从产品简报到最终交付的剪纸风短视频制作 Skill。它把脚本、分镜、关键帧、透明 PNG 分层、动画、旁白、镜头时长、配乐音效、合成和质检组织成可确认、可修改、可追踪的导演式流程。

## 适合什么时候用

- 制作 20-60 秒的竖屏产品短视频或品牌内容
- 把产品信息整理成旁白、字幕和镜头表
- 统一剪纸、纸张纤维、切边、阴影和定格动画的视觉语言
- 使用 HyperFrames 或静态关键帧兜底完成运动设计
- 规划 IndexTTS-2、MiniMax、ElevenLabs 或真人录音路线
- 根据旁白实际时长锁定镜头节奏
- 完成音乐、动作音效、人声 ducking、技术质检和人耳检查

## 核心工作流

1. 产品简报与边界确认
2. 脚本、旁白和分镜确认
3. 剪纸视觉规范与关键帧提示词
4. HyperFrames、透明 PNG 分层与静态兜底动画
5. 合规旁白路线与声音生成
6. 旁白驱动的镜头时长锁定
7. 配乐、动作音效与人声 ducking
8. 最终合成、技术质检、画面质检和人耳检查
9. 修改分类、交付清单和隐私要求

## 跨平台安装

核心格式遵循文件夹式 Agent Skills：`SKILL.md` 是唯一工作流入口，所有参考文档、模板和脚本都使用相对路径。

| 工具 | 项目级安装位置 | 触发方式 |
|---|---|---|
| Codex | `.agents/skills/paper-cut-video-workflow/` | 自然语言或 Skill 名称 |
| Claude Code | `.claude/skills/paper-cut-video-workflow/` | `/paper-cut-video-workflow` 或自然语言 |
| Trae | `.trae/skills/paper-cut-video-workflow/` | Skill 名称或自然语言 |
| Cursor | `.cursor/skills/paper-cut-video-workflow/`，并安装附带 `.mdc` 规则 | 自然语言或规则名称 |
| 其他文件型 Agent | `skills/paper-cut-video-workflow/`，并合并附带 `AGENTS.md` | 自然语言 |

Cursor 需要把 [`paper-cut-video-workflow.mdc`](../../skills/paper-cut-video-workflow/adapters/cursor/paper-cut-video-workflow.mdc) 复制到项目的 `.cursor/rules/`。其他不能自动发现 Skill 的工具可以使用 [`AGENTS.md`](../../skills/paper-cut-video-workflow/adapters/generic/AGENTS.md) 作为入口。

更详细的安装与降级策略见 [`platform-compatibility.md`](../../skills/paper-cut-video-workflow/references/platform-compatibility.md)。

## 默认触发语

> 帮我做一个剪纸风格短视频，从产品简报、脚本、分镜、关键帧、旁白、配乐、合成到最终质检交付。

## 交付物

- 产品简报
- 脚本、旁白与分镜
- 剪纸视觉规范
- 关键帧和透明分层提示词
- 旁白路线与音频计划
- 镜头时间表
- 配乐、音效与 ducking 方案
- 技术、画面和人耳质检报告
- 修改清单、交付清单和隐私记录

## 验证

公开包包含跨平台验证器，会检查：

- `SKILL.md` frontmatter 和名称
- Codex、Claude Code、Trae、Cursor、通用代理五类目标
- 相对路径是否断裂
- 平台适配入口是否齐全
- 是否出现本机绝对路径、常见令牌或私钥片段
- 两个辅助脚本是否可执行

## 隐私与版权边界

- 声音样本、声纹模型、参考视频、生成旁白和客户素材只放项目目录，不放 Skill 目录。
- 仅在获得明确授权时使用私人声纹或模仿性声音。
- 音乐和音效需要保存来源、授权范围和许可证记录。
- 参考视频用于分析节奏、构图和方法，不应未经授权重新分发。

## 主要入口

- [Skill 入口](../../skills/paper-cut-video-workflow/SKILL.md)
- [平台兼容说明](../../skills/paper-cut-video-workflow/references/platform-compatibility.md)
- [关键帧提示词模板](../../skills/paper-cut-video-workflow/assets/prompt-templates/keyframe-prompts.md)
- [镜头表模板](../../skills/paper-cut-video-workflow/assets/project-templates/shotlist.csv)
- [时长规划脚本](../../skills/paper-cut-video-workflow/scripts/plan_scene_durations.py)
- [交付清单脚本](../../skills/paper-cut-video-workflow/scripts/make_delivery_manifest.py)
