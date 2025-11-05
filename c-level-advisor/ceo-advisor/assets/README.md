# CEO Advisor - Sample Assets

This directory contains sample data for financial scenario analysis and strategic company analysis.

## Sample Files

### 1. sample-scenarios.json
**Purpose:** Financial scenarios for CEO scenario planning and decision analysis

**Description:** Realistic Series A company with three scenarios:
- **Base Case** (50% probability): Conservative growth, realistic assumptions
- **Optimistic** (25% probability): Strong product-market fit, market adoption
- **Pessimistic** (25% probability): Market headwinds, competitive pressure
- **Moonshot** (10% probability): Viral growth, exceptional reception

**Key Data:**
- Revenue, growth rates, margins
- Operating expenses and burn rate
- Discount rates (WACC assumptions)
- Key assumptions for each scenario
- Investment decision frameworks

**How to Use:**
```bash
# Analyze financial scenarios
python ../scripts/financial_scenario_analyzer.py sample-scenarios.json

# Get JSON output for further analysis
python ../scripts/financial_scenario_analyzer.py sample-scenarios.json --output json

# Save detailed report
python ../scripts/financial_scenario_analyzer.py sample-scenarios.json -o json -f analysis.json
```

**What to Expect:**
- Scenario comparison with key metrics
- Sensitivity analysis (which assumptions matter most?)
- Risk-adjusted returns
- Recommendation on best course of action
- Payback period analysis

---

### 2. sample-company.json
**Purpose:** Comprehensive company data for strategic analysis

**Description:** Complete Series A company snapshot including:
- Company fundamentals and stage
- Current financials and metrics
- Market analysis (TAM, SAM, competitive landscape)
- Product portfolio and performance
- Customer metrics and cohort analysis
- Team structure and hiring plan
- Competitive positioning
- Strategic risks and opportunities
- 2-year strategic priorities

**Sections:**
- `company_info`: Basic company information
- `financial_summary`: Current financial performance
- `market_analysis`: TAM, competitors, trends
- `product_portfolio`: Product performance and metrics
- `customer_metrics`: Acquisition, retention, satisfaction
- `team_structure`: Organization and hiring plans
- `competitive_positioning`: Differentiation and advantages
- `strategic_priorities`: Goals for current and next year

**How to Use:**
```bash
# Analyze strategic position
python ../scripts/strategy_analyzer.py sample-company.json

# Get strategic recommendations
python ../scripts/strategy_analyzer.py sample-company.json --output json

# Export for board deck
python ../scripts/strategy_analyzer.py sample-company.json -o json -f strategy-report.json
```

**What to Expect:**
- Strategic assessment (strengths, weaknesses, opportunities, threats)
- Competitive positioning analysis
- Growth levers and optimization areas
- Risk assessment and mitigation strategies
- Strategic recommendations and priorities

---

## Using These Samples

### Quick Start - Financial Analysis

```bash
cd /Users/ricky/Library/CloudStorage/GoogleDrive-rickydwilson@gmail.com/My\ Drive/Websites/GitHub/claude-skills/c-level-advisor/ceo-advisor/

# Run scenario analysis
python scripts/financial_scenario_analyzer.py assets/sample-scenarios.json

# Get JSON output for board presentation
python scripts/financial_scenario_analyzer.py assets/sample-scenarios.json -o json
```

### Quick Start - Strategic Analysis

```bash
# Analyze company strategy
python scripts/strategy_analyzer.py assets/sample-company.json

# Get detailed insights
python scripts/strategy_analyzer.py assets/sample-company.json -o json
```

---

## Financial Scenario Planning

### Scenario Framework

**Base Case:** Most likely outcome
- Conservative growth estimate
- Realistic market conditions
- Probability: 50%
- Used for business plan and budgeting

**Optimistic:** Strong execution
- Product-market fit achieved
- Market adoption exceeds expectations
- Probability: 25%
- Upside possibility

**Pessimistic:** Market challenges
- Competitive pressure
- Slower adoption
- Probability: 25%
- Downside protection planning

**Moonshot:** Exceptional outcome
- Viral growth
- Market leadership
- Probability: 10% (low but possible)
- Scenario that changes trajectory

### Key Metrics to Model

**Revenue Drivers:**
- Customer acquisition rate
- Customer lifetime value
- Churn rate
- Expansion revenue (upsells)

**Cost Structure:**
- COGS (cost of goods sold)
- Operating expenses
- R&D investment
- Sales & marketing spend

**Profitability:**
- Gross margin (revenue - COGS)
- Operating margin
- EBITDA
- Net income

**Cash Flow:**
- Burn rate (monthly cash used)
- Runway (months of cash left)
- CAC payback period
- Cash generation

---

## Strategic Analysis Framework

### Market Analysis

**Total Addressable Market (TAM)**
- Total market size if 100% market share
- Example: $45B for enterprise analytics

**Serviceable Addressable Market (SAM)**
- Realistic addressable market for this company
- Example: $8B (focusing on mid-market)

**Serviceable Obtainable Market (SOM)**
- Share you can realistically capture
- Example: $200M (2.5% of SAM)

**Market Growth**
- Annual growth rate
- Maturity of market
- Expansion opportunities

### Competitive Positioning

**Differentiation:**
- What makes you different?
- Why should customers choose you?
- What's defensible (hard to copy)?

**Competitive Advantages:**
- Product advantages
- Market advantages
- Team advantages
- Network advantages

**Threats:**
- Direct competitors
- Indirect competitors
- New entrants
- Substitutes

**Opportunities:**
- Market expansion
- Product expansion
- Geographic expansion
- Strategic partnerships

---

## Creating Your Own Scenarios

### Financial Model Template

```json
{
  "base_case": {
    "revenue": 5000000,
    "revenue_growth_rate": 0.35,
    "cogs_percent": 0.25,
    "operating_expenses": 1800000,
    "tax_rate": 0.21,
    "capex": 200000
  },
  "scenarios": [
    {
      "scenario_name": "Optimistic",
      "probability": 0.25,
      "revenue": 6500000,
      "revenue_growth_rate": 0.50,
      "assumptions": ["assumption1", "assumption2"]
    }
  ]
}
```

### Data Collection

**Financial Data:**
- Current and historical revenue
- Customer acquisition and churn
- Operating expenses by category
- R&D and marketing spend
- Capital requirements

**Market Data:**
- Total addressable market
- Growth rates by segment
- Competitive landscape
- Customer segmentation
- Pricing benchmarks

**Operational Data:**
- CAC by channel
- LTV calculations
- Unit economics
- Payback periods
- Runway analysis

---

## Scenario-Based Decision Making

### Format: Investment Decision

```json
{
  "question": "Should we raise Series B?",
  "options": [
    {
      "option": "Raise $3M aggressively",
      "capital_required": 3000000,
      "expected_runway_months": 24,
      "upside_scenario": "Moonshot",
      "downside_scenario": "Pessimistic"
    },
    {
      "option": "Raise $1.5M conservatively",
      "capital_required": 1500000,
      "expected_runway_months": 18,
      "upside_scenario": "Optimistic",
      "downside_scenario": "Base Case"
    }
  ]
}
```

### Decision Matrix

| Scenario | 12 Months | 24 Months | Runway | Action |
|----------|-----------|-----------|--------|--------|
| Optimistic | $6.5M ARR | $10M ARR | 24mo+ | Invest aggressively |
| Base Case | $5M ARR | $8.5M ARR | 20mo | Maintain discipline |
| Pessimistic | $3.5M ARR | $5.5M ARR | 14mo | Prepare contingency |

---

## Using for Board Presentations

### Key Slides

1. **Revenue Scenarios** (3 bar chart)
   - Base, Optimistic, Pessimistic
   - Show probability weights
   - Expected value calculation

2. **Financial Metrics** (dashboard)
   - Key metrics by scenario
   - Trend lines
   - Comparison to targets

3. **Risk Assessment**
   - What could derail base case?
   - Mitigation strategies
   - Monitoring metrics

4. **Recommended Action**
   - Which scenario should we prepare for?
   - What investments are needed?
   - How do we reduce downside risk?

---

## Integration with Strategy

### Strategy-to-Financials

```
Strategic Goal: "Become market leader"
  ↓
Operational Plan: "3 new integrations, 50% customer growth"
  ↓
Financial Model: Revenue $6.5M (Optimistic scenario)
  ↓
Funding Required: $3M Series B
  ↓
Runway: 24 months at planned burn
```

### Financial Health Indicators

**Green Flags (Healthy):**
- 18+ months runway
- Revenue growth >30% QoQ
- CAC payback < 12 months
- NRR > 110%
- Gross margin > 60%

**Yellow Flags (Watch):**
- 12-18 months runway
- Revenue growth 10-30% QoQ
- CAC payback 12-18 months
- NRR 100-110%
- Gross margin 40-60%

**Red Flags (Risk):**
- < 12 months runway
- Revenue growth < 10% QoQ
- CAC payback > 18 months
- NRR < 100%
- Gross margin < 40%

---

## Creating Your Company Analysis

### Data Structure

```json
{
  "company_info": {
    "name": "Your Company",
    "stage": "Series A",
    "founded": "2022-01-01"
  },
  "financial_summary": {
    "arr": 2400000,
    "runway_months": 14,
    "burn_rate_monthly": 180000
  },
  "market_analysis": {
    "tam": 45000000000,
    "market_growth_rate": 0.25
  }
}
```

### What to Include

**Always Include:**
- Financial metrics (ARR, burn, runway)
- Customer metrics (NPS, churn, LTV/CAC)
- Market opportunity (TAM, competition)
- Strategic priorities (2-3 key goals)

**Frequently Include:**
- Product performance by segment
- Competitive positioning
- Team structure and key hires
- Risk assessment

**Nice to Include:**
- Historical financial trends
- Customer success stories
- Product roadmap alignment
- Industry benchmarks

---

## Best Practices

1. **Scenario Probability**
   - Must sum to 100%
   - Base case typically 50%+
   - Adjust based on execution risk

2. **Assumptions Documentation**
   - Write down all key assumptions
   - Validate with data when possible
   - Update quarterly as conditions change

3. **Sensitivity Analysis**
   - Which 2-3 assumptions matter most?
   - What if revenue is 20% below plan?
   - What if burn is 30% higher?

4. **Regular Updates**
   - Monthly: Compare actual vs. plan
   - Quarterly: Remodel scenarios
   - Annually: Refresh strategic direction

---

## File Specifications

**sample-scenarios.json:**
- Format: JSON
- Encoding: UTF-8
- Required: base_case, scenarios array
- Each scenario: all financial fields
- Validate: Probabilities should sum to 1.0

**sample-company.json:**
- Format: JSON
- Encoding: UTF-8
- Required: company_info, financial_summary, market_analysis
- Optional: All other sections
- Size: ~30-50KB for typical company

---

## Related Documentation

- **Financial Scenario Analyzer:** [../scripts/financial_scenario_analyzer.py](../scripts/financial_scenario_analyzer.py)
- **Strategy Analyzer:** [../scripts/strategy_analyzer.py](../scripts/strategy_analyzer.py)
- **CEO Advisor Guide:** [../SKILL.md](../SKILL.md)

---

**Last Updated:** November 5, 2025
**Format:** Sample Assets README
**Included Files:** 2 (sample-scenarios.json, sample-company.json)
**Script Versions:** financial_scenario_analyzer.py 2.0.0, strategy_analyzer.py 1.0.0
