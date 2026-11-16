# Skill : /youtube script (claude-youtube, copie du 16/11/2026 : script et hook)

---
## Fichier : sub-skills/script.md

# Retention-Engineered Script

This sub-skill generates a full video script engineered for maximum audience retention, using proven structural patterns — hook-promise-stakes openings, pattern interrupts, forward hooks, and strategic CTAs — all calibrated to the target video length and audience type.

## Inputs Required

| Input | Required | Description |
|-------|----------|-------------|
| Topic | Yes | Video subject matter |
| Target length | Yes | Desired video duration in minutes |
| Channel type | Yes | Educational, entertainment, vlog, review, tutorial, commentary, etc. |
| Audience persona | Yes | Who is watching (age range, knowledge level, why they clicked) |
| Key points | Yes | Core information/arguments to cover (bullet list) |
| Tone | No | Casual, professional, energetic, conversational (default: conversational) |
| CTA goal | No | Subscribe, product, community, or custom (default: subscribe) |

## Reference Files

- `references/retention-scripting-guide.md`
- `references/algorithm-guide.md`

## Parallel Agents

Not required. This skill runs as a single sequential workflow.

## Execution Steps

1. **Load references**: Read `references/retention-scripting-guide.md` and `references/algorithm-guide.md` fully before writing.
2. **Calculate structure**: Based on target length, compute section durations. Hook: 0:00-0:30. Intro: 0:30-2:00. Mid-CTA: ~25% mark. Retention re-hook: ~60% mark. Outro: final 60 seconds. Remaining time divided among content blocks.
3. **Map key points to chapters**: Assign the provided key points to content blocks. Order them by engagement potential — strongest points early and late, weaker points in the middle (surrounded by pattern interrupts).
4. **Write the hook block**: Produce the 3-part hook (Grab, Promise, Stakes) targeting >70% retention at the 30-second mark.
5. **Write the intro**: Bridge from hook to content. Establish context, stakes, and viewer outcome.
6. **Write content blocks**: Each block opens with a pattern interrupt, delivers value, ends with a micro-summary and forward hook to the next section.
7. **Insert pattern interrupts**: Place one every 60-90 seconds. Mark each with its type tag.
8. **Place CTAs**: Soft mid-CTA at ~25%, hard CTA in outro.
9. **Write outro**: Hard CTA, end screen cue, next video tease.
10. **Annotate retention risks**: Scan the full script for drop-off danger zones. Mark each with a warning symbol and mitigation note.
11. **Add pacing notes**: Insert editor directions throughout.

## Output Template

```
## Script Metadata

- **Topic**: [topic]
- **Target length**: [X] minutes ([Y] words at ~150 words/minute)
- **Channel type**: [type]
- **Audience**: [persona summary]
- **Estimated word count**: [total words]

---

## HOOK (0:00 — 0:30) | Target: >70% retention at 0:30

### Grab (0:00 — 0:05)
[Opening line — the single most important sentence in the video]

[PACING: Deliver fast. No intro graphics. Start mid-thought or mid-action.]

### Promise (0:05 — 0:15)
[What the viewer will get from watching. Specific, tangible outcome.]

### Stakes (0:15 — 0:30)
[Why it matters. What they lose by clicking away. Emotional or practical consequence.]

⚠️ RETENTION RISK: [If applicable — e.g., "Generic promise language. Make the outcome hyper-specific."]

---

## INTRO (0:30 — 2:00) | Context + Credibility

[CAMERA CHANGE]

[Context paragraph: Why this topic, why now, why from this creator.]

[Viewer outcome restatement: "By the end of this video, you'll..."]

[PACING: Moderate. Establish trust but don't linger. Viewers who survived the hook want content.]

---

## CONTENT BLOCK 1: [Chapter Title] (2:00 — X:XX)

[GRAPHIC: Chapter title card]
[Pattern interrupt: opening line that resets attention]
[Core content — spoken-word style: short sentences, direct address ("you"), rhetorical questions.]
[B-ROLL CUE: Describe what should appear on screen]
[Micro-summary: One sentence recap] → [Forward hook: "But that's only half the picture..."]
⚠️ RETENTION RISK: [If applicable — e.g., "Dense info block. Break with visual at 4:30."]

---

## CONTENT BLOCK 2: [Chapter Title] (X:XX — X:XX)

[SOUND EFFECT: Transition sting]
[Pattern interrupt] → [Content delivery] → [UNEXPECTED STAT]
[Micro-summary] → [Forward hook]

---

## MID-CTA (~25% mark, approximately X:XX)

[CAMERA CHANGE] [Soft CTA — conversational, tied to content just delivered. 10-15 seconds max.]
> "If you're finding this useful, hit subscribe — I break down [niche topic] like this every [cadence]."

---

## CONTENT BLOCKS 3+: [Chapter Titles] (X:XX — X:XX)

[Continue pattern: interrupt → content → B-ROLL → micro-summary → forward hook]

## RETENTION RE-HOOK (~60% mark, approximately X:XX)

[CAMERA CHANGE] [Why the remaining content is the most valuable part.]
⚠️ RETENTION RISK: [60% mark is a common drop-off cliff. This re-hook must feel like a second hook.]

---

## OUTRO (final 60 seconds, X:XX — end)

### Hard CTA (15 seconds)
[Direct call-to-action tied to the video's value delivery.]

> "[Specific CTA: subscribe, comment a specific thing, check link in description]"

### End Screen Cue (15 seconds)
[GRAPHIC: End screen overlay]

> "If you liked this, you'll want to watch [related video topic] — I'll put it right here."

[Point to end screen card position]

### Next Video Tease (15 seconds)
[Brief, compelling preview of the suggested next video. Create a mini curiosity gap.]

[PACING: Keep energy up through the final second. No "thanks for watching" wind-down.]

---

## Pattern Interrupt Log

| Timestamp | Type | Description |
|-----------|------|-------------|
| X:XX | [CAMERA CHANGE] | [Brief note] |
| X:XX | [B-ROLL CUE] | [Brief note] |
| X:XX | [GRAPHIC] | [Brief note] |
| X:XX | [SOUND EFFECT] | [Brief note] |
| X:XX | [UNEXPECTED STAT] | [Brief note] |

**Total pattern interrupts**: [X] | **Average interval**: [X] seconds

## Retention Risk Map

| Timestamp | Risk Level | Issue | Mitigation |
|-----------|------------|-------|------------|
| X:XX | ⚠️ High | [Description] | [Solution] |
| X:XX | ⚠️ Medium | [Description] | [Solution] |

## Editor Notes

- [Pacing guidance for specific sections]
- [Music/sound design suggestions]
- [Cut rhythm recommendations]
- [Thumbnail moment candidates with timestamps]
```

## Quality Criteria

- Word count must match target length at ~150 words per minute (within 10% tolerance)
- The hook must contain all three elements: Grab (0-5s), Promise (5-15s), Stakes (15-30s)
- Pattern interrupts must appear every 60-90 seconds — verify by checking the interrupt log timestamps
- Every content block must end with both a micro-summary AND a forward hook
- Mid-CTA must appear at approximately the 25% mark, not earlier
- Retention re-hook must appear at approximately the 60% mark
- All production cue tags must use the exact bracket format: [CAMERA CHANGE], [B-ROLL CUE], [GRAPHIC], [SOUND EFFECT], [UNEXPECTED STAT]
- At least 3 retention risk points must be identified and marked with mitigations
- The script must read as natural spoken language, not written prose — short sentences, contractions, direct address
- The outro must never contain filler phrases like "thanks for watching" or "don't forget to" — maintain energy to the final second


---
## Fichier : sub-skills/hook.md

# First-30-Second Hook Writer

This sub-skill generates five distinct hook variants for a video's opening 30 seconds, each using a different psychological mechanism, rated for drop-off risk and optimized traffic source, giving creators a tested menu of openings to choose from based on their channel size and content type.

## Inputs Required

| Input | Required | Description |
|-------|----------|-------------|
| Topic | Yes | Video subject matter |
| Channel niche | Yes | Content category (tech, fitness, finance, etc.) |
| Hook style preference | No | If creator wants to bias toward a specific style |
| Channel size | No | Helps calibrate the decision guide (default: small) |
| Video format | No | Long-form, Short, tutorial, commentary, etc. (default: long-form) |

## Reference Files

- `references/retention-scripting-guide.md`

## Parallel Agents

Not required. This skill runs as a single sequential workflow.

## Execution Steps

1. **Load reference**: Read `references/retention-scripting-guide.md` fully before generating hooks.
2. **Analyze the topic**: Identify the core tension, surprising angle, common misconception, emotional stakes, and audience pain point related to the topic.
3. **Generate 5 hook variants**: Write each variant following the exact structure below. Each hook must be a complete 30-second script (approximately 75 words at spoken pace).
4. **Rate each hook**: Assign drop-off risk, optimal traffic source, and identify the psychological mechanism.
5. **Build the decision guide**: Based on reference file principles, map hook types to channel sizes and content types.
6. **Apply preference weighting**: If a hook style preference was provided, note which variant aligns and explain tradeoffs of the preferred vs recommended style.

## Output Template

```
## Topic Analysis

- **Core tension**: [The fundamental conflict or question in this topic]
- **Surprising angle**: [What most people get wrong or don't expect]
- **Audience pain point**: [The problem viewers are trying to solve]
- **Emotional stakes**: [What viewers stand to gain or lose]

---

## Hook Variant 1: Shock/Contradiction

**Mechanism**: Cognitive dissonance — presents a counterintuitive statement that conflicts with the viewer's existing belief, creating an information gap they must resolve.

> [Full 30-second spoken script, approximately 75 words]
>
> [Line 1: The counterintuitive claim — delivered with confidence, no hedging]
> [Line 2-3: Brief evidence or framing that makes the claim credible]
> [Line 4-5: Pivot to promise — "and in this video, I'll show you exactly why..."]

- **Word count**: [X] words (~30 seconds)
- **Drop-off risk**: [Low/Medium/High] — [one-sentence explanation]
- **Optimized for**: [Browse/Search/Suggested] — [why this traffic source]
- **Best when**: [Scenario where this hook type excels]
- **Avoid when**: [Scenario where this hook type backfires]

---

## Hook Variant 2: Problem-Agitation

**Mechanism**: Pain amplification — names a problem the viewer already recognizes, then intensifies the emotional weight before offering the video as relief.

> [Full 30-second spoken script, approximately 75 words]
>
> [Line 1: Name the pain directly — "You've tried X and it didn't work"]
> [Line 2-3: Twist the knife — show the consequences of the unsolved problem]
> [Line 4-5: Relief signal — "Here's what actually works..."]

- **Word count**: [X] words (~30 seconds)
- **Drop-off risk**: [Low/Medium/High] — [one-sentence explanation]
- **Optimized for**: [Browse/Search/Suggested] — [why this traffic source]
- **Best when**: [Scenario]
- **Avoid when**: [Scenario]

---

## Hook Variant 3: Story-Open

**Mechanism**: Narrative transportation — drops the viewer into the middle of an action or scene, activating the brain's story-processing mode which naturally resists disengagement.

> [Full 30-second spoken script, approximately 75 words]
>
> [Line 1: Mid-action scene — start in medias res, no setup]
> [Line 2-3: Sensory details or stakes that make the scene vivid]
> [Line 4-5: Bridge to topic — connect the story to the video's core content]

- **Word count**: [X] words (~30 seconds)
- **Drop-off risk**: [Low/Medium/High] — [one-sentence explanation]
- **Optimized for**: [Browse/Search/Suggested] — [why this traffic source]
- **Best when**: [Scenario]
- **Avoid when**: [Scenario]

---

## Hook Variant 4: Curiosity-Gap

**Mechanism**: Information gap theory — reveals enough to make the viewer aware of what they don't know, creating psychological tension that can only be resolved by watching.

> [Full 30-second spoken script, approximately 75 words]
>
> [Line 1: Tease the answer without giving it — "There's one thing that..."]
> [Line 2-3: Build the gap — add specificity that makes the unknown feel important]
> [Line 4-5: Promise the payoff — signal exactly when the answer comes]

- **Word count**: [X] words (~30 seconds)
- **Drop-off risk**: [Low/Medium/High] — [one-sentence explanation]
- **Optimized for**: [Browse/Search/Suggested] — [why this traffic source]
- **Best when**: [Scenario]
- **Avoid when**: [Scenario]

---

## Hook Variant 5: Social Proof

**Mechanism**: Authority bias + stakes — leads with credibility (results, credentials, or third-party validation) to earn trust instantly, then pivots to what's at stake.

> [Full 30-second spoken script, approximately 75 words]
>
> [Line 1: Credibility statement — specific result, number, or proof point]
> [Line 2-3: Stakes — what this means for the viewer]
> [Line 4-5: Promise — "I'm going to break down exactly how..."]

- **Word count**: [X] words (~30 seconds)
- **Drop-off risk**: [Low/Medium/High] — [one-sentence explanation]
- **Optimized for**: [Browse/Search/Suggested] — [why this traffic source]
- **Best when**: [Scenario]
- **Avoid when**: [Scenario]

---

## Decision Guide

### By Channel Size

| Channel Size | Recommended Hook | Reasoning |
|-------------|-----------------|-----------|
| Nano (<1K) | [Type] | [Why — e.g., "No established authority, so social proof is weak"] |
| Micro (1K-10K) | [Type] | [Why] |
| Small (10K-100K) | [Type] | [Why] |
| Mid (100K-500K) | [Type] | [Why] |
| Large (500K+) | [Type] | [Why] |

### By Content Type

| Content Type | Primary Hook | Secondary Hook | Avoid |
|-------------|-------------|----------------|-------|
| Tutorial/How-to | [Type] | [Type] | [Type + why] |
| Commentary/Opinion | [Type] | [Type] | [Type + why] |
| Review | [Type] | [Type] | [Type + why] |
| Entertainment | [Type] | [Type] | [Type + why] |
| Educational | [Type] | [Type] | [Type + why] |
| Vlog | [Type] | [Type] | [Type + why] |

### By Traffic Source Goal

| Traffic Source | Best Hook Types | Why |
|---------------|----------------|-----|
| Search | [Types] | [Explanation] |
| Browse/Home | [Types] | [Explanation] |
| Suggested | [Types] | [Explanation] |

## Recommendation

**For this video**: [Recommended variant number and name] — [2-sentence justification based on topic, niche, and channel context]

**Runner-up**: [Second choice] — [When to use this instead]
```

## Quality Criteria

- Each hook must be a complete, speakable 30-second script — approximately 75 words (65-85 acceptable range)
- All five hook types must be represented: Shock/Contradiction, Problem-Agitation, Story-Open, Curiosity-Gap, Social Proof
- Each hook must name its specific psychological mechanism with a one-sentence explanation of how it works
- Drop-off risk ratings must be justified, not arbitrary
- Traffic source recommendations must align with the retention scripting guide's principles
- The decision guide must cover all channel sizes AND all listed content types
- No two hooks may use the same opening structure or first sentence pattern
- Hooks must be written in natural spoken language — no written-prose phrasing
- The curiosity-gap hook must NOT give away the answer within the 30 seconds
- The story-open hook must start in medias res — no "Let me tell you about a time when..."

