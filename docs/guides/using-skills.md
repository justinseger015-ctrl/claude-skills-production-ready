# Using Skills: Practical Workflows Guide

**For:** Anyone who wants to USE skills (not build them)
**Time to Read:** 10 minutes
**Goal:** Learn exactly how to use skills in your daily work

---

## How to Read This Guide

Each section shows a **real task** and **exactly how** to use skills to do it faster.

**Format:**
- ⏱️ **Without Skills:** Time it takes the old way
- ✨ **With Skills:** Time with skills + exact steps
- 💾 **Copy-Paste Commands:** Ready to use

---

## For Content Creators & Marketers

### Task 1: Write an SEO-Optimized Blog Post

⏱️ **Without Skills:** 3 hours (research, write, optimize, check)

✨ **With Content Creator Skill:** 1.5 hours

**Step-by-Step:**

```bash
# 1. Start with a template (2 minutes)
cp skills/marketing-team/content-creator/assets/blog-post-template.md my-blog.md

# 2. Write your content using the template structure (60 min)
# (Just write - the template already has SEO-friendly structure)

# 3. Run SEO analysis (30 seconds)
python skills/marketing-team/content-creator/scripts/seo_optimizer.py my-blog.md "your target keyword"

# Output tells you EXACTLY what to fix:
# SEO Score: 68/100
# ❌ Keyword density: 0.8% (need 1-2%)
# ❌ Missing H2 with keyword
# ✓ Meta description length: 155 chars
# ❌ Need 2 more internal links
```

```bash
# 4. Check brand voice (30 seconds)
python skills/marketing-team/content-creator/scripts/brand_voice_analyzer.py my-blog.md

# Output:
# Formality: 7/10 (Professional) ✓
# Tone: Authoritative, Informative ✓
# Readability: 65 (College level) ✓
# Active voice: 62% (recommend 70%+) ⚠️
```

```bash
# 5. Fix issues and re-run (20 minutes)
# 6. Done!
```

**Time Saved:** 1.5 hours (50%)

---

### Task 2: Create a Week of Social Media Posts

⏱️ **Without Skills:** 4 hours (research formats, write, optimize for each platform)

✨ **With Content Creator Skill:** 1 hour

**Step-by-Step:**

```bash
# 1. Open the social media template
open skills/marketing-team/content-creator/assets/social-media-templates.md

# You'll see ready-to-use formats for:
# - LinkedIn (thought leadership, how-to, case study)
# - Twitter/X (thread starters, polls, quick tips)
# - Instagram (captions, carousel)

# 2. Pick the LinkedIn "How-To" template:
```

**Template Example:**
```
🎯 [Bold Statement]

Here's how to [solve problem]:

1. [Step 1 with emoji]
2. [Step 2 with emoji]
3. [Step 3 with emoji]

💡 Pro tip: [insider insight]

What's your experience with [topic]?
```

**Your Post (5 min per post):**
```
🎯 Marketing automation doesn't have to be complex

Here's how to start automating your content in 3 steps:

1. 📊 Analyze what's working (run metrics on top posts)
2. 🔄 Create templates for winners (save 2-3 hours/week)
3. 🤖 Schedule with tools like Buffer

💡 Pro tip: Start with just ONE platform to avoid overwhelm

What's your experience with automation?
```

**Total: 7 posts × 5 minutes = 35 minutes**

```bash
# 3. (Optional) Check each post's tone
python skills/marketing-team/content-creator/scripts/brand_voice_analyzer.py post1.txt
# Takes 10 seconds per post
```

**Time Saved:** 3 hours (75%)

---

## For Product Managers

### Task 3: Prioritize 30 Feature Requests

⏱️ **Without Skills:** 4 hours (spreadsheet, RICE calculations, debates)

✨ **With Product Manager Toolkit:** 30 minutes

**Step-by-Step:**

```bash
# 1. Create a CSV with your features (10 min)
nano features.csv
```

**CSV Format:**
```csv
feature,reach,impact,confidence,effort
User Dashboard,500,3,0.8,5
API Rate Limiting,1000,2,0.9,3
Dark Mode,300,1,1.0,2
Mobile App,2000,3,0.7,13
```

**What the numbers mean:**
- **Reach:** Users affected per month/quarter
- **Impact:** 1 (minimal) to 3 (massive)
- **Confidence:** 0.0 to 1.0 (how sure you are)
- **Effort:** Story points or days

```bash
# 2. Run RICE prioritizer (10 seconds)
python skills/product-team/product-manager-toolkit/scripts/rice_prioritizer.py features.csv --capacity 30

# Output:
# === RICE Prioritization Results ===
#
# 1. API Rate Limiting
#    RICE Score: 600  | Reach: 1000 | Impact: 2 | Effort: 3
#    Priority: HIGH | Quick Win ⚡
#
# 2. User Dashboard
#    RICE Score: 300  | Reach: 500 | Impact: 3 | Effort: 5
#    Priority: HIGH | Big Bet 🎯
#
# 3. Dark Mode
#    RICE Score: 150  | Reach: 300 | Impact: 1 | Effort: 2
#    Priority: MEDIUM | Quick Win ⚡
#
# 4. Mobile App
#    RICE Score: 323  | Reach: 2000 | Impact: 3 | Effort: 13
#    Priority: LOW | Big Bet 🎯 (over capacity)
#
# === Portfolio Analysis ===
# Quick Wins: 2 features (total effort: 5 days)
# Big Bets: 1 feature (total effort: 5 days)
# Total Selected: 3 features (10 days, fits 30-day capacity)
```

```bash
# 3. Save as JSON for Jira import (2 min)
python skills/product-team/product-manager-toolkit/scripts/rice_prioritizer.py features.csv --output json > priorities.json
```

**Time Saved:** 3.5 hours (87%)

---

### Task 4: Analyze Customer Interview Transcripts

⏱️ **Without Skills:** 3 hours per interview (manual highlighting, note-taking, theme extraction)

✨ **With Product Manager Toolkit:** 5 minutes per interview

**Step-by-Step:**

```bash
# 1. Save your interview transcript as text
interview1.txt

# 2. Run analyzer (5 seconds)
python skills/product-team/product-manager-toolkit/scripts/customer_interview_analyzer.py interview1.txt

# Output:
# === Customer Interview Analysis ===
#
# 🔴 Pain Points (High Severity):
# - "It takes 3 hours to generate monthly reports manually"
# - "Can't see real-time data, always working with yesterday's numbers"
# Severity: 8/10
#
# 💡 Feature Requests:
# - Dashboard with live metrics
# - One-click report generation
# - Export to Excel/PDF
#
# 😊 Sentiment: Frustrated but hopeful (Score: 4/10)
#
# 🏷️ Key Themes:
# 1. Reporting automation (mentioned 5 times)
# 2. Real-time data visibility (mentioned 3 times)
# 3. Export flexibility (mentioned 2 times)
#
# 📋 Jobs-to-be-Done:
# - "When I need monthly reports, I want automated generation, so I can focus on analysis not data entry"
```

```bash
# 3. Analyze multiple interviews
for file in interview*.txt; do
    python skills/product-team/product-manager-toolkit/scripts/customer_interview_analyzer.py "$file" json >> all-interviews.json
done

# 4. See patterns across all interviews
```

**Time Saved:** 2.5 hours per interview

---

## For Engineers

### Task 5: Set Up a New Project

⏱️ **Without Skills:** 4 hours (research, setup, configuration, testing)

✨ **With Fullstack Engineer Skill:** 15 minutes

**Step-by-Step:**

```bash
# 1. Scaffold complete project (30 seconds)
python skills/engineering-team/senior-fullstack/scripts/project_scaffolder.py my-app --type nextjs-graphql

# Creates:
# my-app/
# ├── frontend/          # Next.js with TypeScript
# ├── backend/           # GraphQL API
# ├── database/          # PostgreSQL migrations
# ├── docker-compose.yml # Complete environment
# ├── .github/           # CI/CD workflows
# └── README.md          # Setup instructions
```

```bash
# 2. Start everything (1 minute)
cd my-app
docker-compose up -d

# ✓ Frontend running on http://localhost:3000
# ✓ GraphQL API on http://localhost:4000/graphql
# ✓ PostgreSQL database ready
# ✓ All environment variables configured
```

```bash
# 3. Verify it works (30 seconds)
open http://localhost:3000
# You'll see a working app with example queries!
```

**Time Saved:** 3.75 hours (94%)

---

### Task 6: Review Code Quality

⏱️ **Without Skills:** 2 hours (manual review, checklist, linting, security scan)

✨ **With Fullstack Engineer Skill:** 2 minutes

**Step-by-Step:**

```bash
# Run complete code quality analysis
python skills/engineering-team/senior-fullstack/scripts/code_quality_analyzer.py /path/to/project

# Output:
# === Code Quality Analysis ===
#
# 📊 Overall Score: 73/100
#
# ✅ Strengths:
# - TypeScript configured correctly
# - Good test coverage (78%)
# - No hardcoded secrets found
#
# ⚠️ Issues Found:
#
# 🐛 Code Smells (8 found):
# - src/utils/api.ts:45 - Function too long (82 lines, max 50)
# - src/components/Form.tsx:12 - Duplicate code block
#
# 🔒 Security (2 found):
# - package.json:15 - Dependency "axios" has known vulnerability
# - .env.example - Missing rate limiting configuration
#
# 📈 Complexity:
# - Average cyclomatic complexity: 12 (target: <10)
# - 3 functions above threshold
#
# 💡 Recommendations:
# 1. Run `npm audit fix` for security updates
# 2. Refactor api.ts utils into smaller functions
# 3. Add rate limiting middleware
```

**Time Saved:** 1.95 hours (98%)

---

## For Scrum Masters & PMs

### Task 7: Plan a Sprint

⏱️ **Without Skills:** 2 hours (capacity calc, story selection, sprint board setup)

✨ **With Agile Product Owner Skill:** 20 minutes

**Step-by-Step:**

```bash
# 1. Generate user stories from an epic (2 min)
python skills/product-team/agile-product-owner/scripts/user_story_generator.py sprint 30

# Input: "User Authentication" epic
#
# Output:
# === Sprint Plan (30 story points) ===
#
# US-001: Login Flow (8 points) [HIGH]
# As a user, I want to log in with email/password, so I can access my account
#
# Acceptance Criteria:
# - Given valid credentials, When I submit login, Then I'm authenticated
# - Given invalid credentials, When I submit login, Then I see error message
# - Given I check "Remember me", When I close browser, Then I stay logged in
#
# US-002: Password Reset (5 points) [HIGH]
# As a user, I want to reset my password via email, so I can recover my account
#
# Acceptance Criteria:
# - Given my email, When I request reset, Then I receive reset link
# - Given reset link, When I click it, Then I can set new password
# - Given expired link, When I click it, Then I see error message
#
# [... continues for 30 points worth of stories]
```

```bash
# 2. Copy to Jira
# Stories are ready to paste into Jira with acceptance criteria!
```

**Time Saved:** 1.75 hours (87%)

---

## Common Workflows

### Workflow 1: Content Creation Pipeline

```bash
# Morning: Plan content
cp skills/marketing-team/content-creator/assets/content-calendar.md this-week.md

# Afternoon: Write
# (use templates from assets/)

# Before publishing: Quality check
python skills/marketing-team/content-creator/scripts/seo_optimizer.py post.md "keyword"
python skills/marketing-team/content-creator/scripts/brand_voice_analyzer.py post.md

# Ship it! ✨
```

**Daily time saved:** 2 hours

---

### Workflow 2: Product Discovery

```bash
# After user interviews
for interview in interview*.txt; do
    python skills/product-team/product-manager-toolkit/scripts/customer_interview_analyzer.py "$interview" json
done > insights.json

# Prioritize features
python skills/product-team/product-manager-toolkit/scripts/rice_prioritizer.py features.csv

# Generate user stories
python skills/product-team/agile-product-owner/scripts/user_story_generator.py sprint 40

# Create PRD
cp skills/product-team/product-manager-toolkit/assets/prd-template.md new-feature-prd.md
```

**Weekly time saved:** 8 hours

---

### Workflow 3: Sprint Cycle

```bash
# Monday: Sprint planning
python skills/product-team/agile-product-owner/scripts/user_story_generator.py sprint 30

# Daily: Update Jira via MCP
# (Scrum master skill + Atlassian MCP)

# Friday: Retrospective
cp skills/delivery-team/scrum-master/assets/retrospective-template.md retro-sprint-42.md

# Analyze velocity
python skills/product-team/agile-product-owner/scripts/velocity_tracker.py last-5-sprints.csv
```

**Per-sprint time saved:** 4 hours

---

## Tips for Maximum Efficiency

### 1. Create Aliases

Add to your `~/.bashrc` or `~/.zshrc`:

```bash
# Content tools
alias analyze-seo='python ~/claude-skills/skills/marketing-team/content-creator/scripts/seo_optimizer.py'
alias check-voice='python ~/claude-skills/skills/marketing-team/content-creator/scripts/brand_voice_analyzer.py'

# Product tools
alias prioritize='python ~/claude-skills/skills/product-team/product-manager-toolkit/scripts/rice_prioritizer.py'
alias analyze-interview='python ~/claude-skills/skills/product-team/product-manager-toolkit/scripts/customer_interview_analyzer.py'

# Now just type:
analyze-seo my-post.md "keyword"
```

### 2. Chain Commands

```bash
# Write, analyze, fix loop
write-post.sh && analyze-seo post.md "keyword" && check-voice post.md
```

### 3. Use Output Directories

```bash
# Keep results organized
mkdir -p output/seo output/interviews output/priorities

analyze-seo post.md "keyword" > output/seo/$(date +%Y-%m-%d)-analysis.txt
```

### 4. Integrate with Your IDE

Most IDEs can run Python scripts from within the editor:
- VS Code: Terminal → Run Python File
- vim: `:!python skills/.../tool.py %`
- Add to your build scripts

---

## Troubleshooting

### "Command not found"

```bash
# Make sure you're in the claude-skills directory
cd /path/to/claude-skills

# Or use absolute paths
python /full/path/to/claude-skills/skills/.../tool.py
```

### "ModuleNotFoundError"

```bash
# Install dependencies
pip install -r requirements.txt

# Or activate virtual environment
source claude-skills_venv/bin/activate
```

### "File not found"

```bash
# Check the path exists
ls skills/marketing-team/content-creator/scripts/

# Use tab completion
python skills/market[TAB] → auto-completes
```

---

## Next Steps

**Want to understand how it all connects?**
→ Read [skill-to-agent-flow.md](skill-to-agent-flow.md)

**Ready to use agents for guided workflows?**
→ See `agents/[domain]/` for agent-guided multi-step processes

**Need help with a specific skill?**
→ Each skill has a `SKILL.md` with detailed docs

---

**Remember:** Skills are meant to be used daily. The more you use them, the more time you save!

---

**Last Updated:** November 17, 2025
**Difficulty:** Beginner-friendly with practical examples
**Estimated Reading Time:** 10 minutes
