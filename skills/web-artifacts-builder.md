---
name: web-artifacts-builder
description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
license: Complete terms in LICENSE.txt
---

# Web Artifacts Builder

## Workflow
1.  **Initialize**: `npx create-vite-app` (or similar bootstrap) to set up a React/TypeScript project.
2.  **Develop**: Build components using Tailwind CSS and shadcn/ui.
3.  **Bundle**: Use a bundler (Vite, Parcel, or a custom script) to inline all CSS and JS into a single `bundle.html`.
4.  **Present**: Share the final HTML file with the user.

## Stack
- **React 18** + TypeScript
- **Tailwind CSS 3.4+**
- **shadcn/ui** components
- **Lucide React** icons

## Design Rules
- **Avoid "AI Slop"**: No purple gradients, no excessive centering, no Inter font by default.
- **Premium Design**: Use vibrant colors, glassmorphism, and smooth animations.
- **Responsive**: Ensure the artifact looks good on all screen sizes.

## Bundling Requirements
The final output must be a **single self-contained HTML file**. All scripts, styles, and assets (if small) should be inlined or linked to stable CDNs.
