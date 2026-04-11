---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.
license: Complete terms in LICENSE.txt
---

# Frontend Design Skill

This skill provides guidelines and best practices for creating distinctive, production-grade frontend interfaces. It focuses on high design quality and avoiding generic "AI aesthetics."

## Purpose

Use this skill when the user asks to build any of the following:
- Web components or React components
- Web pages (landing pages, dashboards, portfolios)
- HTML artifacts or posters
- Web applications or frontend layouts
- Requests to "style," "beautify," or "improve the design" of any web UI

## Design Principles

### 1. Avoid Generic AI Aesthetics

To avoid common AI-generated design patterns (often called "AI slop"), adhere to the following rules:

- **Colors**: Avoid overusing purple gradients and generic "AI purple" (#8A2BE2, #9400D3). Use curated palettes from established design systems or nature.
- **Typography**: Avoid defaulting to "Inter" for everything. Use characterful pairings (e.g., a serif for headings, a clean sans-serif for body).
- **Layout**: Avoid excessive use of `items-center justify-center`. Use structured, asymmetrical, or grid-based layouts to create visual interest.
- **Corners**: Avoid uniform `rounded-xl` or `rounded-2xl` on every element. Use deliberate corner radii (e.g., sharp for formal, mixed for organic).
- **Icons**: Don't just throw icons everywhere. Use them purposefully to aid navigation or highlight key information.

### 2. Prioritize Craftsmanship and Detail

Great design is in the details. Focus on:

- **Micro-interactions**: Use subtle transitions, hover effects, and feedback animations.
- **Visual Weight**: Clearly define a hierarchy using size, color, and spacing.
- **Spacing**: Use a consistent spacing scale (e.g., multiples of 4px or 8px) to create rhythm.
- **Accessibility**: Ensure high contrast ratios and proper ARIA labels.

## Implementation Guidelines

### 1. Technology Stack

- **React**: Preferred for complex state management and components.
- **Tailwind CSS**: Preferred for styling. Use it expressively, not just for basic layouts.
- **Shadcn/UI**: A great foundation, but always customize the default styles to fit the specific project's aesthetic.
- **Lucide React**: Preferred icon set.

### 2. Best Practices

- **Component-First**: Build modular, reusable components with clear prop interfaces.
- **Responsive Design**: Always prioritize a mobile-first approach.
- **Semantic HTML**: Use proper tags (`<header>`, `<main>`, `<nav>`, `<section>`, etc.) for better SEO and accessibility.
- **Performance**: Optimize images, use efficient CSS selectors, and avoid unnecessary re-renders.

## Workflow

1.  **Understand the Intent**: Clarify the purpose of the interface and the target audience.
2.  **Define the Aesthetic**: Choose a color palette and font pairing that matches the intent.
3.  **Build the Foundation**: Set up the layout and core components.
4.  **Refine and Polish**: Add micro-interactions, adjust spacing, and fine-tune the design details.
5.  **Verify**: Test responsiveness and accessibility.
