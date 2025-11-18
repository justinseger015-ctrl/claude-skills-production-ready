# How Skills and Agents Work Together

**For:** Anyone wanting to understand the complete picture
**Time to Read:** 8 minutes
**Goal:** See how skills, agents, and tools connect

---

## The Big Picture (In One Sentence)

**Skills** provide the tools and knowledge → **Agents** know how to use them → **You** get expert results faster

---

## Visual Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                         YOU (The User)                           │
│                                                                   │
│  "I need to write SEO-optimized content for our product launch" │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│                    AGENT (cs-content-creator)                     │
│                                                                    │
│  "I'll guide you through content creation step-by-step"          │
│                                                                    │
│  Workflow 1: SEO Blog Post Creation                              │
│  Step 1: Use blog template                                       │
│  Step 2: Write draft                                             │
│  Step 3: Run SEO analyzer                                        │
│  Step 4: Check brand voice                                       │
│  Step 5: Optimize and finalize                                   │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│                  SKILL (content-creator)                          │
│                                                                    │
│  Python Tools:                                                    │
│  • seo_optimizer.py          → Analyze SEO instantly             │
│  • brand_voice_analyzer.py   → Check tone/voice                  │
│                                                                    │
│  Knowledge Bases:                                                 │
│  • SEO best practices        → Expert guidelines                 │
│  • Brand voice framework     → Tone definitions                  │
│  • Social media guides       → Platform specifics                │
│                                                                    │
│  Templates:                                                       │
│  • Blog post template        → Proven structure                  │
│  • Content calendar          → Planning framework                │
│  • Social media templates    → Ready formats                     │
└──────────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│                           OUTPUT                                   │
│                                                                    │
│  ✅ SEO-optimized blog post (Score: 92/100)                      │
│  ✅ Brand voice consistent (Matches guidelines)                  │
│  ✅ Ready to publish in 1.5 hours (vs 3 hours manually)          │
└──────────────────────────────────────────────────────────────────┘
```

---

## Example 1: Content Creation (Detailed)

### Scenario

You need to create a blog post about "Marketing Automation for SaaS."

### Step-by-Step Flow

#### 1. You Start

```
Your goal: Blog post, 1500 words, SEO-optimized, brand voice consistent
```

#### 2. Choose Your Path

**Option A: Use Agent (Guided)**
```bash
# Open cs-content-creator agent
open agents/marketing/cs-content-creator.md

# Agent tells you:
"Follow Workflow 2: SEO Blog Post Creation"
# Then guides you through 6 steps
```

**Option B: Use Skill Directly (Expert)**
```bash
# You already know what to do, just use the tools:
cd skills/marketing-team/content-creator/
```

#### 3. Agent Workflow (Option A)

**Step 1:** Agent says "Start with our blog template"
```bash
# Agent runs this for you:
cp ../../skills/marketing-team/content-creator/assets/blog-post-template.md draft.md
```

**Step 2:** Agent says "Write your draft following the template structure"
```
# You write for 60 minutes
```

**Step 3:** Agent says "Let's analyze SEO"
```bash
# Agent runs:
python ../../skills/marketing-team/content-creator/scripts/seo_optimizer.py draft.md "marketing automation"

# Output:
SEO Score: 68/100
- Keyword density: 0.8% (need 1-2%) ❌
- H2 with keyword: Missing ❌
- Meta description: Good ✅
- Internal links: Need 2 more ❌
```

**Step 4:** Agent says "Now check brand voice"
```bash
# Agent runs:
python ../../skills/marketing-team/content-creator/scripts/brand_voice_analyzer.py draft.md

# Output:
Formality: 7/10 ✅
Tone: Professional + Friendly ✅
Readability: 65 (College) ✅
Active voice: 62% (target 70%+) ⚠️
```

**Step 5:** Agent says "Fix the issues I found"
```
# You fix:
- Add keyword 3 more times
- Create H2 with keyword
- Add 2 internal links
- Convert 3 sentences to active voice
```

**Step 6:** Agent says "Let's verify"
```bash
# Agent re-runs:
python ../../skills/marketing-team/content-creator/scripts/seo_optimizer.py draft.md "marketing automation"

# Output:
SEO Score: 92/100 ✅
All checks passing!
```

**Done!** 1.5 hours total (vs 3 hours without)

---

## Example 2: Feature Prioritization

### Scenario

You have 30 feature requests and need to prioritize them.

### The Flow

#### 1. You Prepare Data

```csv
feature,reach,impact,confidence,effort
Dashboard,500,3,0.8,5
API,1000,2,0.9,3
Dark Mode,300,1,1.0,2
```

#### 2. Agent Guides You

**Agent:** cs-product-manager
**Workflow:** "Feature Prioritization with RICE"

**Step 1:** Agent validates your CSV format
```bash
# Checks that you have: feature, reach, impact, confidence, effort
```

**Step 2:** Agent runs RICE calculation
```bash
python ../../skills/product-team/product-manager-toolkit/scripts/rice_prioritizer.py features.csv --capacity 30

# Skill returns:
1. API - Score: 600 (Quick Win ⚡)
2. Dashboard - Score: 300 (Big Bet 🎯)
3. Dark Mode - Score: 150
```

**Step 3:** Agent interprets results
```
"Focus on API first (highest ROI)
Then Dashboard (strategic value)
Dark Mode is nice-to-have"
```

**Step 4:** Agent exports for Jira
```bash
python ../../skills/product-team/product-manager-toolkit/scripts/rice_prioritizer.py features.csv --output json > priorities.json
```

**Done!** 30 minutes (vs 4 hours of spreadsheet work)

---

## The Relationship

### Skills Are Like:

**A Toolbox:**
- Contains specialized tools (Python scripts)
- Includes instruction manuals (knowledge bases)
- Provides templates (assets)

**You can use the toolbox directly if you know what you need**

### Agents Are Like:

**An Expert Craftsperson:**
- Knows which tools to use when
- Follows proven processes (workflows)
- Guides you step-by-step
- Ensures quality at each step

**You ask the expert when you need guidance**

---

## When to Use What

### Use SKILLS Directly When:

✅ **You're experienced** - You know exactly what you need
✅ **Quick tasks** - "Just run the SEO analyzer"
✅ **Automation** - Building scripts that use tools
✅ **Exploration** - Trying out tools to learn

**Example:**
```bash
# Quick SEO check before publishing
python skills/marketing-team/content-creator/scripts/seo_optimizer.py final-draft.md "keyword"
```

### Use AGENTS When:

✅ **You're learning** - Need step-by-step guidance
✅ **Complex workflows** - Multi-step processes
✅ **Best practices** - Want to follow proven patterns
✅ **Completeness** - Don't want to miss steps

**Example:**
```bash
# First time creating content strategy
# Open cs-content-creator agent
# Follow "Workflow 4: Content Strategy Development"
```

---

## Real-World Scenarios

### Scenario 1: New Content Writer

**Day 1:** Uses cs-content-creator agent
- Follows workflows step-by-step
- Learns which tools do what
- Understands the knowledge bases

**Week 2:** Mix of agent + direct tool use
- Uses agent for complex workflows
- Runs SEO optimizer directly for quick checks
- References knowledge bases as needed

**Month 2:** Mostly direct tool use
- Knows all the tools
- Has own workflows
- Only uses agent for new types of content

### Scenario 2: Product Manager

**Planning Week:** Uses cs-product-manager agent
- "Feature Prioritization" workflow
- "Customer Discovery" workflow
- "Roadmap Development" workflow

**Execution Week:** Direct skill use
- Quick RICE calculations
- Interview analysis
- Generates user stories

**Review Week:** Back to agent
- Uses "Quarterly Planning" workflow
- Comprehensive process
- Nothing forgotten

---

## How They Connect: Technical View

### File Structure

```
claude-skills/
│
├── agents/                          # Workflow guides
│   ├── marketing/
│   │   └── cs-content-creator.md   # Agent file
│   │       ↓
│   │       Uses skills via: ../../skills/marketing-team/content-creator/
│   │
│   └── product/
│       └── cs-product-manager.md    # Agent file
│           ↓
│           Uses skills via: ../../skills/product-team/product-manager-toolkit/
│
└── skills/                          # The toolboxes
    ├── marketing-team/
    │   └── content-creator/         # Skill package
    │       ├── scripts/             # Python tools
    │       ├── references/          # Knowledge
    │       └── assets/              # Templates
    │
    └── product-team/
        └── product-manager-toolkit/ # Skill package
            ├── scripts/
            ├── references/
            └── assets/
```

### Path Pattern

**Agents use relative paths to access skills:**

```markdown
# In: agents/marketing/cs-content-creator.md

## Python Tools

1. **SEO Optimizer**
   - Path: `../../skills/marketing-team/content-creator/scripts/seo_optimizer.py`
   - Usage: `python ../../skills/.../seo_optimizer.py file.md "keyword"`
```

This means:
- Agent knows WHERE the tools are
- Agent knows HOW to use them
- Agent follows proven WORKFLOWS

---

## Quick Reference

| Question | Answer |
|----------|--------|
| **I'm new, where do I start?** | Read an agent file for your role (agents/[domain]/) |
| **I know what I want** | Go directly to skills/[domain]/[skill]/ |
| **I need step-by-step help** | Follow an agent workflow |
| **Just checking one thing** | Run a skill tool directly |
| **Building automation** | Import skill tools into your scripts |
| **Learning workflows** | Study agent files |

---

## Summary

```
Skills = The capability (tools + knowledge + templates)
Agents = The guide (workflows + best practices)
You = The user (gets work done faster + better quality)

Together = Expert results in less time
```

**Skills** give you superpowers
**Agents** teach you how to use them
**You** accomplish more

---

## Next Steps

**Ready to try it?**
→ Go to [using-skills.md](using-skills.md) for step-by-step examples

**Still confused about skills?**
→ Read [understanding-skills.md](understanding-skills.md) for basics

**Want to build agents?**
→ (For developers) See `docs/agent-development/`

---

**Remember:** Skills and agents are designed to work together OR separately. Use whichever fits your workflow!

---

**Last Updated:** November 17, 2025
**Difficulty:** Intermediate (assumes basic understanding)
**Estimated Reading Time:** 8 minutes
