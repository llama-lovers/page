---
title: FastEcho
---
# FastEcho

**Say what you need. Hear what actually happened on the page.**

[GitHub ↗](https://github.com/llama-lovers/FastEcho){ .md-button .md-button--primary }
[Watch the demo ↗](https://youtu.be/zODavr68b5s){ .md-button }

## The problem

Screen readers make the web accessible, but locating a control or completing a complex form can take considerable effort. Unlabelled buttons, dynamic menus and poorly described fields add further barriers.

## Our approach

FastEcho is a Chrome extension for blind and low-vision users. It interprets Polish voice commands, reads the page structure and accessible labels, executes validated actions and describes the observed result. Users can hear responses through their screen reader or a local Piper voice.

## What the prototype does

- Describe the current page and suggest available actions.
- Click controls, fill ordinary form fields and scroll.
- Validate action targets and compare the page state after execution.
- Repeat responses, adjust detail and handle confirmation questions.
- Deliver feedback through a screen reader, local Piper or Chrome TTS fallback.

Press **Alt+Shift+A** to start recording, and press it again to submit a command.

## Architecture and privacy

The Manifest V3 extension works with a local FastAPI backend. The full voice workflow uses OpenRouter for transcription and model reasoning. Piper synthesizes responses locally.

Recognized sensitive data is masked in page context. The executor refuses protected fields and recognized CAPTCHA targets. Masking is heuristic, rather than a complete guarantee.

!!! note "Audio is a separate data path"
    In real transcription mode, recordings are sent to OpenRouter before transcript masking. Do not dictate passwords or secrets.

## Try it

The [FastEcho quick start](https://github.com/llama-lovers/FastEcho#quick-start) covers requirements, building the extension, starting the backend, local fixtures and Piper configuration.

[Hackathon context →](../hackathons.md)
