---
title: FastFence
hide:
  - navigation
  - toc
---
# FastFence

**Security policies between AI agents, models and tools.**

[Documentation ↗](https://fastfence.dev/){ .md-button .md-button--primary }
[GitHub ↗](https://github.com/llama-lovers/FastFence){ .md-button }

## The problem

AI agents interact with models, APIs and tools. These interactions can expose sensitive information, invoke unauthorized operations or consume excessive resources. Rules scattered across application code are difficult to maintain and test consistently.

## Our approach

FastFence centralizes controls between an application and its models or tools. It combines local rules with semantic assessment. In the management console, users can describe a supported rule with Laya, inspect the proposed change, test examples and activate a reviewed policy without restarting the gateway.

## Capabilities

- **Policy controls:** permissions, model and tool allowlists, resource limits and estimated-cost budgets.
- **Sensitive-data protection:** secret detection, configured attack-pattern checks and sanitized decision records.
- **Integrations:** REST, OpenAI-compatible, MCP and synchronous plain-text ACP interfaces.
- **Reviewable changes:** YAML configuration, policy tests, diffs and an activity dashboard.

## HackYeah 2026

Built for the Goldman Sachs **AI control layer** partner challenge. The final demonstration covers policy editing, protection decisions, Laya review, document processing and integration examples.

[Presentation and demo →](../presentations.md){ .md-button }
[Hackathon context →](../hackathons.md){ .md-button }

## Run locally

Use the [current installation guide](https://fastfence.dev/) for requirements and setup. Source code, examples and presentation materials are available in the [repository](https://github.com/llama-lovers/FastFence).
