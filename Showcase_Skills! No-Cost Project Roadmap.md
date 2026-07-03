# Conversation
- conversationId: 68396909-2987-4389-9b01-7b14af927c02
- endpoint: anthropic
- title: Showcase Skills: No-Cost Project Roadmap
- exportAt: 11:19:25 GMT+0530 (India Standard Time)

## Options
- presetId: null
- model: claude-haiku-4-5@20251001
- maxOutputTokens: 16000
- resendFiles: false
- greeting: Use Anthropic Claude Haiku 4.5 model to
help you achieve any task that involves complex code/creativity.
This model consumes consumes a significant amount of sustainable credits ⚡
To start, simply ask your question below.

- spec: Claude
- maxContextTokens: 200000
- endpoint: anthropic
- endpointType: undefined
- title: Showcase Skills: No-Cost Project Roadmap

## History
**User**
Help me create a project which will showcase my skills for the role of a forward deployed engineer. Consider the fact that I am in no position to make any kind of monetary investment. My only investment will be time. Create a week-by-week roadmap (agile methodology) along with github repo showcase. Right now, based on everything you know about me, design a problem statement and appropriate documentation.


**Claude**
{"type":"think","think":"Based on the user's profile:\n- Technical interests: programming, debugging, problem-solving\n- Prefers structured learning, step-by-step guidance\n- Prefers short answers in paragraph format\n- Working on AI Innovation Challenge reconciliation solution\n- Has experience with system integration (Scheme Reports, Way4, A4 GL)\n- Implementing proof-of-concept solutions\n- Zero monetary budget, time-based investment\n\nFor a Forward Deployed Engineer role, they need to showcase:\n1. Problem-solving in production-like environments\n2. System integration capabilities\n3. Debugging and troubleshooting\n4. Rapid prototyping\n5. Documentation and communication\n6. Working with ambiguous requirements\n7. Cross-team collaboration skills\n\nThe ideal project should:\n- Be free/open-source based\n- Leverage their existing knowledge of reconciliation/integration\n- Demonstrate real-world problem-solving\n- Build a portfolio on GitHub with strong documentation\n- Show ability to work with incomplete information\n- Be completable in a week with time-based investment\n\nI should create a problem statement that's relevant to their experience and the forward deployed role, then provide week-by-week roadmap and documentation template."}


**Claude**
# Forward Deployed Engineer Portfolio Project

## Problem Statement

**"Distributed System Health Monitor & Diagnostic Toolkit"**

You're a forward deployed engineer at a fintech company. Three critical systems—payment processor, ledger, and settlement—occasionally diverge, but teams lack real-time visibility into *why* or *where* they fail. They need a lightweight, deployable tool that identifies system mismatches, diagnoses root causes, and guides remediation without requiring backend access.

**Core Challenge:** Build a framework that mimics production reconciliation scenarios (payment delays, ledger inconsistencies, settlement gaps) and provides actionable diagnostics—proving you can work in constrained environments with incomplete data.

---

## Week-by-Week Agile Roadmap

### **Week 1: Foundation & MVP**

**Sprint 1.1 (Days 1-2): Architecture & Setup**
- GitHub repo: `distributed-system-diagnostics`
- Design 3-tier architecture: Data Simulator → Reconciliation Engine → Diagnostic API
- Setup: Python FastAPI, SQLite (free), Docker (optional)
- Document: Architecture diagram + ADR (Architecture Decision Record)

**Sprint 1.2 (Days 3-5): Build MVP**
- Create mock data generator (simulate payment/ledger/settlement records with synthetic mismatches)
- Build basic reconciliation logic (matching transactions across 3 systems)
- Create REST API endpoint: `/diagnose` (takes transaction logs, returns mismatch report)
- Write unit tests

**Sprint 1.3 (Day 6-7): Documentation & Demo**
- README with problem statement, architecture, setup instructions
- Add usage examples and sample API responses
- Record 2-min demo video showing diagnosis workflow

---

### **Week 2: Enhanced Diagnostics & Deployment**

**Sprint 2.1 (Days 1-3): Advanced Features**
- Add root-cause suggestions (e.g., "timestamp offset detected," "duplicate entry in System B")
- Implement confidence scoring (how certain is the diagnosis?)
- Add batch processing endpoint for large datasets
- Write integration tests

**Sprint 2.2 (Days 4-5): Real-World Simulation**
- Add 5-7 realistic reconciliation scenarios (timing issues, network failures, data corruption)
- Document each scenario as a test case with expected outputs

**Sprint 2.3 (Days 6-7): Deployment & Observability**
- Dockerize the application
- Add logging and metrics (JSON structured logs)
- Deploy to free tier: Render.com or Railway.app
- Document deployment steps

---

## GitHub Repository Structure

```
distributed-system-diagnostics/
├── README.md (problem statement, architecture, quick start)
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API_REFERENCE.md
│   ├── DEPLOYMENT.md
│   └── SCENARIOS.md (reconciliation scenarios)
├── src/
│   ├── simulator.py (mock data generator)
│   ├── reconciler.py (matching logic)
│   ├── diagnostics.py (root-cause engine)
│   └── api.py (FastAPI app)
├── tests/
│   ├── test_reconciler.py
│   └── test_diagnostics.py
├── docker-compose.yml
├── requirements.txt
└── .github/
    └── workflows/
        └── ci.yml (auto-test on push)
```

---

## Documentation Template

### **README.md Structure**
1. **Problem Statement** (1 paragraph)
2. **What This Solves** (bullet points)
3. **Quick Start** (5 lines to run)
4. **Architecture Diagram** (ASCII or link to Lucidchart free)
5. **API Examples** (3-4 curl requests)
6. **Deployment** (link to DEPLOYMENT.md)

### **ARCHITECTURE.md**
- Data flow diagram
- Why you chose each tech (FastAPI = lightweight, SQLite = zero cost, etc.)
- Design decisions for a FDE (deployability, debuggability, zero dependencies)

### **SCENARIOS.md**
Document 5 real-world cases:
- **Case 1:** Payment processed in System A but missing in System B (timing lag)
- **Case 2:** Duplicate transaction in System C (idempotency failure)
- **Case 3:** Currency mismatch in ledger entry
- **Case 4:** Settlement amount deviation (rounding error)
- **Case 5:** System failure during reconciliation window

For each: problem → diagnosis output → remediation steps.

---

## Why This Showcases FDE Skills

| FDE Skill | How It's Demonstrated |
|-----------|----------------------|
| **Debugging complex systems** | Diagnostic engine finds mismatches across 3 systems |
| **Working with constraints** | Zero budget, mock data only—shows creativity |
| **System integration** | Reconciles disparate data sources |
| **Documentation** | Clear setup, API docs, scenario walkthroughs |
| **Rapid prototyping** | Full POC in 2 weeks |
| **Observability** | Structured logs, confidence scoring on diagnoses |
| **Deployment mindset** | Containerized, free hosting, CI/CD included |

---

## GitHub Visibility Tips

1. **Commit messages:** `feat: add root-cause confidence scoring` (structured, show progression)
2. **Open issues:** "Enhancement: Support transaction retry logic" (shows forward thinking)
3. **Weekly PRs:** One per sprint, detailed descriptions linking to scenarios
4. **Badges:** Add CI/CD pass badge to README

---

Ready to start? Next step: I'll help you scaffold the initial project structure and write the first README. Do you want to proceed with this direction, or refine the problem statement first?


**User**
Help me fill these details


**Claude**
{"type":"think","think":"The user wants me to help fill in the GitHub repository creation form. Let me look at what needs to be filled:\n\n1. **Owner**: Already filled - `Atharvagarud137`\n2. **Repository name**: Already filled - `distributed-system-diagnostics`\n3. **Description**: Empty - needs to be filled\n4. **Visibility**: Already set to `Public`\n5. **Add README**: Currently `Off` - I should recommend turning this `On`\n6. **Add .gitignore**: Currently `No .gitignore` - should recommend `Python`\n7. **Add license**: Currently `No license` - should recommend `MIT`\n\nLet me provide recommendations for each field:\n\n**Description**: Should be concise, compelling, and clearly communicate the value. Given the problem statement, something like:\n\"A lightweight diagnostic toolkit that identifies and debugs mismatches across distributed systems. Demonstrates system integration, root-cause analysis, and deployment patterns for forward-deployed engineering roles.\"\n\n**Add README**: Turn `On` - we want to scaffold with the initial README template\n\n**Add .gitignore**: Select `Python` - this is a Python project\n\n**Add license**: Select `MIT` - MIT is permissive and good for portfolio projects\n\nLet me provide clear instructions for each."}


**Claude**
# GitHub Repository Setup Details

## Fill in These Fields:

### **Description** (350 characters)
```
A lightweight diagnostic toolkit that identifies and debugs transaction mismatches across distributed systems (payment processor, ledger, settlement). Built to demonstrate system integration, root-cause analysis, and deployment patterns—zero external dependencies.
```

---

### **Configuration Settings**

| Field | Setting | Reason |
|-------|---------|--------|
| **Visibility** | ✅ Public | Portfolio visibility for recruiters |
| **Add README** | ✅ Turn ON | Scaffold with initial template |
| **.gitignore** | Select `Python` | Ignore `__pycache__`, `.env`, `.venv`, etc. |
| **License** | Select `MIT` | Permissive, shows confidence in code quality |

---

## Why These Choices?

**Description:** 
- Short, punchy, shows technical depth
- Mentions distributed systems (FDE keyword)
- Highlights no dependencies (constraint you worked within)

**README ON:** 
- GitHub will auto-create a basic template you'll immediately customize

**.gitignore (Python):** 
- Prevents committing `.pyc`, virtual envs, API keys

**MIT License:** 
- Most common for portfolios
- Shows you're open to collaboration

---

## Next Steps After Creation:

1. Click **Create repository**
2. GitHub will give you clone instructions—copy them
3. I'll provide the exact file structure and first-commit content to paste

Ready? Should I give you the terminal commands to initialize locally?


**User**
GitHub repo created. Now, please give me commands to initialize locally


**Claude**
{"type":"think","think":"The user has created the GitHub repo and now wants the terminal commands to initialize it locally. I should provide:\n\n1. Clone the repo\n2. Create virtual environment\n3. Install dependencies (even if minimal at first)\n4. Create the initial folder structure\n5. Make the first commit\n\nGiven the user prefers short, actionable answers in paragraph format (based on memory point 4), I should keep this concise but clear.\n\nLet me provide step-by-step commands they can copy-paste."}


**Claude**
# Local Repository Initialization

Run these commands in order (replace `YOUR_USERNAME` with your GitHub username):

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/distributed-system-diagnostics.git
cd distributed-system-diagnostics

# Create Python virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate

# Create project structure
mkdir src tests docs
touch src/__init__.py tests/__init__.py

# Create initial files
touch src/simulator.py src/reconciler.py src/diagnostics.py src/api.py
touch tests/test_reconciler.py tests/test_diagnostics.py
touch requirements.txt docs/ARCHITECTURE.md docs/API_REFERENCE.md docs/DEPLOYMENT.md docs/SCENARIOS.md

# Create .env (for later use)
touch .env

# Initialize git tracking
git add .
git commit -m "feat: initial project structure"
git push origin main
```

**Verify setup:**
```bash
git log  # Should show your first commit
ls -la   # See all created folders
```

Once done, confirm and I'll provide the content for each file—starting with `requirements.txt` and the main README.


**User**
PS C:\Users\w191668\OneDrive - Worldline SA\Desktop\FDE\distributed-system-diagnostics> venv\Scripts\activate
venv\Scripts\activate : File C:\Users\w191668\OneDrive - Worldline SA\Desktop\FDE\distributed-system-diagnostics\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more 
information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ venv\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess


**Claude**
{"type":"think","think":"The user is getting a Windows PowerShell execution policy error. This is a common Windows issue where scripts are disabled by default. I need to give them a quick fix.\n\nThere are a few ways to solve this:\n1. Use `cmd.exe` instead of PowerShell\n2. Change execution policy (requires admin)\n3. Use the batch file directly\n\nThe easiest for them is to just use cmd.exe or use the batch file directly. Let me give them the simplest solution first.\n\nKeep it short per their preference."}


**Claude**
# Windows PowerShell Execution Policy Fix

Quick workaround—use **Command Prompt (cmd)** instead of PowerShell:

```bash
# Open Command Prompt (not PowerShell)
venv\Scripts\activate.bat
```

**Or**, if you want to fix PowerShell permanently:

```powershell
# Run PowerShell as Administrator, then:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then you can use `venv\Scripts\activate` normally.

---

**Recommended:** Just use `activate.bat` (cmd) for now. Once activated, your prompt should show:
```
(venv) PS C:\Users\w191668\...>
```

Try the `.bat` version and confirm activation. Then we'll move to file content.


**User**
This is my terminal inside VS Code


**Claude**
{"type":"think","think":"The user is showing me that VS Code's terminal is using PowerShell, and they've tried to activate the venv with `venv\\Scripts\\activate` which failed. Then they tried `venv\\Scripts\\activate.bat` which succeeded (you can see the PowerShell execution policy was temporarily set with `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`).\n\nLooking at the terminal output, I can see:\n1. They cloned the repo\n2. They navigated to the directory\n3. They ran `python -m venv venv`\n4. They tried `venv\\Scripts\\activate` - FAILED (red error)\n5. They tried `venv\\Scripts\\activate.bat` - SUCCESS (you can see the prompt changed)\n\nNow they're asking for help because they're showing me their terminal. The good news is they've successfully activated the venv! The prompt now shows they're in the venv environment (the `(venv)` prefix should appear or the terminal is ready).\n\nI should confirm they're good to go and move forward with creating the file structure and content."}


**Claude**
Perfect! I can see the `.bat` activation worked. Your virtual environment is now **active** (PS prompt is ready).

Now run the rest of the setup commands:

```bash
# Create project structure
mkdir src tests docs
mkdir src, tests, docs

# Create Python init files
New-Item src\__init__.py
New-Item tests\__init__.py

# Create main source files
New-Item src\simulator.py
New-Item src\reconciler.py
New-Item src\diagnostics.py
New-Item src\api.py

# Create test files
New-Item tests\test_reconciler.py
New-Item tests\test_diagnostics.py

# Create documentation files
New-Item docs\ARCHITECTURE.md
New-Item docs\API_REFERENCE.md
New-Item docs\DEPLOYMENT.md
New-Item docs\SCENARIOS.md

# Create config files
New-Item requirements.txt
New-Item .env
New-Item docker-compose.yml
```

Once done, confirm by running:
```bash
ls -Recurse  # See all created folders and files
```

Then let me know you're ready and I'll provide the **content for each file** (starting with `requirements.txt`, `README.md`, and project structure).


**User**
PS C:\Users\w191668\OneDrive - Worldline SA\Desktop\FDE\distributed-system-diagnostics> mkdir src tests docs
mkdir : A positional parameter cannot be found that accepts argument 'tests'.
At line:1 char:1
+ mkdir src tests docs
+ ~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [mkdir], ParameterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,mkdir


**Claude**
{"type":"think","think":"The user is trying to use the Linux/Unix style mkdir command with multiple directories at once, but PowerShell's mkdir (which is an alias for New-Item) doesn't work that way. In PowerShell, you need to create each directory separately or use a different syntax.\n\nThe correct PowerShell command would be:\n- `mkdir src, tests, docs` (with commas)\n- Or create each separately: `mkdir src; mkdir tests; mkdir docs`\n- Or use `New-Item -ItemType Directory -Name src, tests, docs`\n\nLet me give them the correct PowerShell syntax."}


**Claude**
Ah, PowerShell syntax! Use **commas** to separate directories:

```bash
mkdir src, tests, docs
```

Or create them one at a time:

```bash
mkdir src
mkdir tests
mkdir docs
```

Then create the files:

```bash
New-Item src\__init__.py
New-Item tests\__init__.py
New-Item src\simulator.py
New-Item src\reconciler.py
New-Item src\diagnostics.py
New-Item src\api.py
New-Item tests\test_reconciler.py
New-Item tests\test_diagnostics.py
New-Item docs\ARCHITECTURE.md
New-Item docs\API_REFERENCE.md
New-Item docs\DEPLOYMENT.md
New-Item docs\SCENARIOS.md
New-Item requirements.txt
New-Item .env
New-Item docker-compose.yml
```

Verify with:
```bash
ls -Recurse
```

Let me know once done!


**User**
Done. Should we complete the documentation part first? Or what would you suggest?


**Claude**
{"type":"think","think":"The user is asking for guidance on what to prioritize. Based on what I know about them:\n1. They value structured learning and step-by-step guidance\n2. They prefer tutoring style interaction\n3. They appreciate clear explanations and actionable tasks\n4. They prefer short answers in paragraph format\n\nFor a forward deployed engineer portfolio project, the strategic order should be:\n1. **Documentation first** - because it forces you to think through the problem clearly, and recruiters read README/docs first\n2. Then **core logic** (simulator, reconciler, diagnostics)\n3. Then **API** \n4. Then **tests**\n5. Then **deployment**\n\nDocumentation-first also:\n- Forces clarity on design decisions\n- Acts as a roadmap for coding\n- Makes the GitHub repo immediately professional\n- Helps with understanding requirements before coding\n\nI should give them a short, clear recommendation with reasoning."}


**Claude**
**Documentation first.** Here's why:

1. **Clarity before code** — Writing docs forces you to finalize your design decisions. You'll catch logic gaps early.
2. **GitHub impression** — Recruiters see your README first. A polished doc + structured plan impresses more than random code commits.
3. **Roadmap** — Clear docs act as your coding blueprint. You'll know exactly what each function needs to do.
4. **Week 1 agile flow** — Docs = Days 1-2, then code Days 3-5. You're on track.

**Order I suggest:**
1. `README.md` (problem statement, quick start, architecture overview)
2. `ARCHITECTURE.md` (tech choices, why FastAPI/SQLite, design decisions)
3. `SCENARIOS.md` (the 5 reconciliation cases—this clarifies your simulator logic)
4. `API_REFERENCE.md` (endpoint specs—guides your FastAPI code)
5. `requirements.txt` (dependencies—finalize after docs)

**Then code:** `simulator.py` → `reconciler.py` → `diagnostics.py` → `api.py` → tests.

Should I start filling in `README.md` with the template?


**User**
Yes


**Claude**
{"type":"think","think":"The user wants me to fill in the README.md file. I should create a comprehensive but concise README that follows the structure I outlined earlier. Let me make it tailored to their context as a Forward Deployed Engineer candidate working on a distributed systems reconciliation project.\n\nKey elements:\n1. Problem statement (short, punchy)\n2. What this solves (bullets)\n3. Quick start (minimal setup)\n4. Architecture diagram (ASCII)\n5. API examples (curl requests)\n6. Deployment\n7. Tech stack\n8. Project structure\n\nI should keep it detailed but scannable, and remember the user prefers short answers in paragraph format. However, a README naturally uses more structured format with headers, so that's appropriate here."}


**Claude**
# README.md Content

Copy this into your `README.md`:

```markdown
# Distributed System Health Monitor & Diagnostic Toolkit

A lightweight diagnostic tool that identifies and debugs transaction mismatches across distributed payment systems. Built to demonstrate system integration, root-cause analysis, and deployment patterns—zero external infrastructure required.

## Problem Statement

You're a forward deployed engineer at a fintech company. Three critical systems—**payment processor**, **ledger**, and **settlement**—occasionally diverge. Teams lack real-time visibility into *why* or *where* failures occur. They need a tool that:

- Identifies transaction mismatches across systems
- Diagnoses root causes (timing lag, duplicates, data corruption, rounding errors)
- Provides actionable remediation steps
- Works in constrained environments without backend access

This project simulates production reconciliation scenarios and provides a diagnostic engine—proving you can debug complex distributed systems under constraints.

## What This Solves

✅ **Mismatch Detection** — Compares transactions across 3 systems, flags divergences  
✅ **Root-Cause Analysis** — Suggests why mismatches occurred (with confidence scoring)  
✅ **Batch Processing** — Handles large transaction datasets  
✅ **Real-World Scenarios** — 5+ production-like test cases included  
✅ **Deployable** — Docker containerized, zero external dependencies  
✅ **Observable** — Structured logging for debugging

## Quick Start

### Prerequisites
- Python 3.9+
- Git

### Setup (5 minutes)

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/distributed-system-diagnostics.git
cd distributed-system-diagnostics

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the API server
python -m uvicorn src.api:app --reload
```

Server runs at `http://localhost:8000`

### First Request

```bash
# Health check
curl http://localhost:8000/health

# Run diagnosis on sample data
curl -X POST http://localhost:8000/diagnose \
  -H "Content-Type: application/json" \
  -d @sample_request.json
```

## Architecture

```
┌─────────────────────────────────────────────┐
│         API Layer (FastAPI)                 │
│  /health, /diagnose, /batch-diagnose        │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│   Reconciliation Engine                     │
│  ├─ Transaction Matcher                     │
│  └─ Mismatch Detector                       │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│   Diagnostic Engine                         │
│  ├─ Root-Cause Suggester                    │
│  ├─ Confidence Scorer                       │
│  └─ Remediation Recommender                 │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│   Data Layer (SQLite + Simulator)           │
│  ├─ Payment Processor Simulator              │
│  ├─ Ledger Simulator                         │
│  └─ Settlement System Simulator              │
└─────────────────────────────────────────────┘
```

### Tech Stack

| Component | Choice | Why |
|-----------|--------|-----|
| **Framework** | FastAPI | Lightweight, async-ready, auto-docs |
| **Database** | SQLite | Zero setup, file-based, perfect for POC |
| **Container** | Docker | Portable, deployable anywhere |
| **Language** | Python | Fast iteration, FDE-friendly |

## API Reference

### `POST /diagnose`

Diagnose mismatches in transaction data.

**Request:**
```json
{
  "payment_processor_txns": [
    {
      "id": "PAY-001",
      "amount": 100.00,
      "timestamp": "2026-07-03T10:00:00Z",
      "status": "completed"
    }
  ],
  "ledger_txns": [
    {
      "id": "LED-001",
      "amount": 100.00,
      "timestamp": "2026-07-03T10:05:00Z",
      "status": "recorded"
    }
  ],
  "settlement_txns": [
    {
      "id": "SET-001",
      "amount": 99.50,
      "timestamp": "2026-07-03T10:10:00Z",
      "status": "settled"
    }
  ]
}
```

**Response:**
```json
{
  "matches": 1,
  "mismatches": 2,
  "total_transactions": 3,
  "diagnostics": [
    {
      "type": "timing_lag",
      "severity": "medium",
      "description": "Payment processed at 10:00 but recorded in ledger at 10:05 (5min lag)",
      "confidence": 0.92,
      "affected_systems": ["payment_processor", "ledger"],
      "remediation": "Check network latency or ledger async processing queue"
    },
    {
      "type": "amount_mismatch",
      "severity": "high",
      "description": "Settlement shows $99.50, ledger shows $100.00 (0.5 difference)",
      "confidence": 0.88,
      "affected_systems": ["ledger", "settlement"],
      "remediation": "Investigate rounding logic or exchange rate applied in settlement"
    }
  ]
}
```

### `POST /batch-diagnose`

Process multiple transaction batches (CSV upload).

### `GET /health`

Check API status.

## Project Structure

```
distributed-system-diagnostics/
├── src/
│   ├── __init__.py
│   ├── simulator.py        # Generates mock transaction data
│   ├── reconciler.py       # Matches transactions across systems
│   ├── diagnostics.py      # Root-cause analysis engine
│   └── api.py              # FastAPI endpoints
├── tests/
│   ├── test_reconciler.py  # Unit tests for matching logic
│   └── test_diagnostics.py # Unit tests for diagnosis
├── docs/
│   ├── ARCHITECTURE.md     # Design decisions & tech rationale
│   ├── API_REFERENCE.md    # Full API documentation
│   ├── DEPLOYMENT.md       # Docker & cloud deployment guide
│   └── SCENARIOS.md        # 5 real-world reconciliation cases
├── requirements.txt        # Python dependencies
├── docker-compose.yml      # Docker setup
├── .env                    # Environment variables (not committed)
└── README.md               # This file
```

## Deployment

### Local Docker

```bash
docker-compose up --build
# Runs on http://localhost:8000
```

### Cloud (Free Tier)

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for step-by-step guide to deploy on:
- Render.com (free tier, 0.50 CPU)
- Railway.app (free credits)

## Learning Outcomes

This project demonstrates:

- **System Integration** — Reconciling disparate data sources
- **Debugging** — Root-cause analysis under incomplete information
- **Rapid Prototyping** — Full POC in 2 weeks, zero budget
- **Deployment** — Containerized, cloud-ready architecture
- **Observability** — Structured logging and confidence scoring
- **Documentation** — Clear API specs, scenario walkthroughs, deployment guides

## Roadmap

- **Week 1:** MVP (reconciliation engine + basic API)
- **Week 2:** Advanced diagnostics + deployment

See [ARCHITECTURE.md](docs/ARCHITECTURE.md) for detailed sprint plan.

## Getting Help

- Check [SCENARIOS.md](docs/SCENARIOS.md) for example use cases
- Review [API_REFERENCE.md](docs/API_REFERENCE.md) for endpoint details
- Open an issue for bugs or feature requests

## License

MIT License — See LICENSE file for details

---

**Built to showcase Forward Deployed Engineer skills:** system debugging, constraint-based design, and production-ready code.
```

---

Now copy this entire block into your `README.md` file, save it, and commit:

```bash
git add README.md
git commit -m "docs: add comprehensive README with problem statement and API examples"
git push origin main
```

Next step: Should I fill `ARCHITECTURE.md`?


**User**
PS C:\Users\w191668\OneDrive - Worldline SA\Desktop\FDE> curl http://localhost:8000/health
curl : Unable to connect to the remote server
At line:1 char:1
+ curl http://localhost:8000/health
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-WebRequest], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeWebRequestCommand


Powershell in VS Code


**Claude**
{"type":"think","think":"The user is getting a connection error when trying to curl localhost:8000/health. This is expected because:\n\n1. They haven't created the `api.py` file with FastAPI code yet\n2. They haven't run `python -m uvicorn src.api:app --reload` to start the server\n\nThe error is not about PowerShell or curl - it's that there's no server running on port 8000.\n\nI should clarify:\n1. They need to first create the API code (api.py with the /health endpoint)\n2. Then start the server\n3. Then test the curl request\n\nSince they asked if we should complete documentation first, we were doing that. But now they're trying to test before the code is written. I should redirect them back to the documentation phase, then we'll write the code in Week 1.\n\nThey're trying to test prematurely. Let me remind them we're still in the documentation phase."}


**Claude**
Good catch! But we're **still in documentation phase**—we haven't written the API code yet. That's why the server isn't running.

The error is expected: **no server is listening on port 8000** because `api.py` is still empty.

**Here's the order:**
1. ✅ **README.md** — DONE
2. **ARCHITECTURE.md** — Next (documentation)
3. **SCENARIOS.md** — Then (documentation)
4. **API_REFERENCE.md** — Then (documentation)
5. **requirements.txt** — Then (dependencies list)
6. **CODE WRITING** — Then we'll write `api.py`, `simulator.py`, etc. and test

Once we finish all docs, we'll write `api.py` with the `/health` endpoint, and *then* you'll run:

```bash
python -m uvicorn src.api:app --reload
```

And the curl will work.

---

**For now:** Let's continue with **ARCHITECTURE.md** to document your design decisions. Should I provide that content?


**User**
Yes


**Claude**
{"type":"think","think":"The user wants me to provide the content for ARCHITECTURE.md. I should create a comprehensive architecture document that explains:\n1. Design decisions\n2. Why each technology choice (FastAPI, SQLite, Python, etc.)\n3. System design patterns\n4. Data flow\n5. How it relates to forward deployed engineer skills\n6. Component interactions\n\nI should keep it detailed but concise, matching their preference for structured information and clear explanations. This should flow naturally from the README and set up the rest of the documentation."}


**Claude**
# ARCHITECTURE.md Content

Copy this into your `docs/ARCHITECTURE.md`:

```markdown
# Architecture & Design Decisions

## System Design Overview

```
┌────────────────────────────────────────────────────────────────────┐
│                         CLIENT LAYER                               │
│                    (Curl, Python SDK, UI)                          │
└────────────────────────────┬─────────────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────────┐
│                    API LAYER (FastAPI)                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │ POST/diagnose│  │GET /health   │  │POST/batch    │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
└────────────────────────────┬─────────────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────────┐
│              BUSINESS LOGIC LAYER                                 │
│  ┌─────────────────────┐      ┌──────────────────────┐            │
│  │ Reconciler Module   │      │ Diagnostics Module   │            │
│  ├─ Transaction Match  │      ├─ Root-Cause Engine  │            │
│  ├─ Mismatch Detection │      ├─ Confidence Score   │            │
│  └─ Gap Analysis       │      └─ Remediation Hints  │            │
│  └─────────────────────┘      └──────────────────────┘            │
└────────────────────────────┬─────────────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────────┐
│                  DATA LAYER (SQLite)                              │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐      │
│  │ Transactions   │  │ Reconciliation │  │ Diagnostics    │      │
│  │ Table          │  │ Results        │  │ Cache          │      │
│  └────────────────┘  └────────────────┘  └────────────────┘      │
└────────────────────────────┬─────────────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────────┐
│              SIMULATOR LAYER (Mock Data)                          │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐      │
│  │ Payment Proc   │  │ Ledger System  │  │ Settlement Sys │      │
│  │ Simulator      │  │ Simulator      │  │ Simulator      │      │
│  └────────────────┘  └────────────────┘  └────────────────┘      │
└────────────────────────────────────────────────────────────────────┘
```

## Technology Choices

### 1. **Framework: FastAPI**

**Decision:** Use FastAPI for REST API.

**Why:**
- **Lightweight** — Minimal boilerplate, ~15 LOC for a working endpoint
- **Async-ready** — Built-in async/await support for concurrent requests
- **Auto-documentation** — Swagger UI at `/docs` (impresses recruiters)
- **Type hints** — Built-in validation via Pydantic models
- **Low overhead** — Deployable on 0.5 CPU free tier
- **FDE relevant** — Debugging async code is a real-world FDE skill

**Alternative considered:** Flask (simpler but less feature-rich); Django (overkill for this scope).

---

### 2. **Database: SQLite**

**Decision:** Use SQLite for data persistence.

**Why:**
- **Zero setup** — File-based, no external DB server required
- **Zero cost** — Included with Python
- **Sufficient for POC** — Perfect for reconciliation datasets (millions of rows still queryable)
- **Deployable** — Single `.db` file can ship with Docker container
- **FDE mindset** — Shows you can work without cloud infrastructure

**Schema trade-off:** No horizontal scaling (not needed for demo).

**Alternative considered:** PostgreSQL (overkill); MongoDB (unnecessary for structured txn data).

---

### 3. **Language: Python**

**Decision:** Build in Python.

**Why:**
- **Fast iteration** — Write logic in 10 lines vs 30 in Java
- **Data science libraries** — Pandas for transaction analysis if needed
- **FDE friendly** — Debugging is simpler; clear error messages
- **Broad ecosystem** — FastAPI, SQLAlchemy, pytest all battle-tested

---

### 4. **Containerization: Docker**

**Decision:** Containerize with Docker.

**Why:**
- **Portability** — Runs identically on Windows, Mac, Linux, cloud
- **Deployment** — Ship entire environment (code + dependencies)
- **Resume value** — Docker is FDE requirement at most companies
- **Free tier ready** — Render.com, Railway.app accept Docker images

---

## Core Modules

### **simulator.py**
Generates mock transaction data with realistic mismatches.

**Responsibilities:**
- Create 3 systems' transaction logs with synthetic divergences
- Simulate timing lags, duplicates, amount mismatches, missing transactions
- Return JSON-serializable transaction objects

**Design:**
```python
class TransactionSimulator:
    def generate_matching_transactions(count: int)
    def inject_timing_lag(txns, lag_ms)
    def inject_duplicate(txns, duplicate_id)
    def inject_amount_mismatch(txns, system_id, variance)
    def get_sample_scenario(scenario_name: str)
```

---

### **reconciler.py**
Matches transactions across 3 systems and identifies divergences.

**Responsibilities:**
- Match transactions by ID across systems
- Detect missing transactions (System A has it, B doesn't)
- Identify timing lag between systems
- Flag amount mismatches

**Design:**
```python
class TransactionReconciler:
    def match_transactions(payment_txns, ledger_txns, settlement_txns)
    def find_mismatches() -> List[Mismatch]
    def calculate_match_confidence(txn1, txn2) -> float
```

**Matching logic:**
- Primary: Match by `transaction_id`
- Secondary: Match by `(amount, timestamp_window, status)` if ID missing
- Confidence scoring: How certain is the match?

---

### **diagnostics.py**
Analyzes mismatches and suggests root causes.

**Responsibilities:**
- Categorize mismatch type (timing lag, duplicate, amount, missing)
- Suggest root cause with confidence score
- Recommend remediation steps
- Provide actionable debugging hints

**Design:**
```python
class DiagnosticEngine:
    def diagnose_mismatch(mismatch: Mismatch) -> Diagnosis
    def suggest_root_cause(mismatch) -> (cause, confidence)
    def recommend_remediation(cause) -> str
```

**Diagnosis categories:**
1. **Timing Lag** — Transaction exists in all systems but at different times
   - Confidence: High if lag is consistent, medium if irregular
   - Remediation: "Check async processing queue" or "Network latency?"

2. **Missing Transaction** — Exists in System A but not in B/C
   - Confidence: High if APIs are healthy
   - Remediation: "Check settlement batch job logs"

3. **Duplicate Transaction** — Same ID appears twice in one system
   - Confidence: High
   - Remediation: "Idempotency key missing? Check API retry logic"

4. **Amount Mismatch** — Same transaction, different amounts
   - Confidence: Medium (could be rounding, fees, or corruption)
   - Remediation: "Investigate exchange rate or fee calculation"

5. **Data Corruption** — Amount/timestamp invalid in one system
   - Confidence: High if data fails validation
   - Remediation: "Check data pipeline; possible DB corruption"

---

### **api.py**
FastAPI application exposing reconciliation as REST endpoints.

**Endpoints:**

#### `GET /health`
- Response: `{"status": "healthy", "timestamp": "2026-07-03T10:00:00Z"}`
- Purpose: Liveness check for deployment monitoring

#### `POST /diagnose`
- Input: JSON with transaction arrays (payment_processor_txns, ledger_txns, settlement_txns)
- Output: JSON with matches, mismatches, detailed diagnostics
- Logic: Calls reconciler → diagnostics engine → formats response

#### `POST /batch-diagnose`
- Input: CSV file with transaction data
- Output: JSON diagnostics for entire batch
- Purpose: Handle large datasets

---

## Data Flow Example

**Request:**
```
Client sends 3 transaction lists to /diagnose
```

**Step 1: Reconciler matches**
```
Payment: PAY-001 ($100, 10:00)
Ledger:  LED-001 ($100, 10:05)  → Match found, 5min lag detected
Settlement: SET-001 ($99.50, 10:10)  → Amount mismatch
```

**Step 2: Diagnostics analyzes**
```
Mismatch 1: Payment vs Ledger timing lag
  → Root cause: "Async ledger processing"
  → Confidence: 0.92
  → Remediation: "Check queue depth"

Mismatch 2: Ledger vs Settlement amount
  → Root cause: "Rounding in settlement conversion"
  → Confidence: 0.88
  → Remediation: "Verify exchange rate"
```

**Step 3: API returns**
```json
{
  "matches": 1,
  "mismatches": 2,
  "diagnostics": [...]
}
```

---

## Deployment Architecture

### Local Development
```
Developer laptop
  ├─ venv (Python env)
  ├─ SQLite (local DB)
  ├─ FastAPI server
  └─ Test suite
```

### Docker Container
```
Docker image
  ├─ Python 3.9
  ├─ FastAPI + dependencies
  ├─ SQLite
  └─ App code
```

### Cloud (Free Tier)
```
Render.com / Railway.app
  ├─ Container deployment
  ├─ Auto-scaling (if needed)
  ├─ HTTPS endpoint
  └─ Logs + monitoring
```

---

## Design Patterns Used

### 1. **Separation of Concerns**
- Simulator ≠ Reconciler ≠ Diagnostics ≠ API
- Each module has one clear responsibility
- Easy to test, debug, extend

### 2. **Confidence Scoring**
- Don't just say "mismatch found"—say "95% confident it's a timing lag"
- Shows probabilistic thinking (FDE skill)
- Helps teams prioritize remediation

### 3. **Scenario-Based Testing**
- Real cases (timing lag, duplicates, etc.) drive development
- Easy to validate against production patterns
- Proves you understand fintech reconciliation

### 4. **Structured Logging**
- JSON logs (not plain text)
- Includes context: request_id, system_affected, confidence
- Deployable to ELK/Splunk

---

## Trade-offs & Constraints

| Aspect | Choice | Trade-off |
|--------|--------|-----------|
| **Database** | SQLite | No horizontal scaling (acceptable for POC) |
| **API** | Stateless | No session management (not needed) |
| **Matching** | ID-first, then heuristic | May miss obscure matches (acceptable) |
| **Diagnostics** | Rule-based | No ML (not justified for 5 scenarios) |
| **Deployment** | Free tier | Low performance (acceptable for demo) |

---

## Extensibility Roadmap

**Future enhancements (not in Week 1-2 scope):**
- Add ML-based mismatch classification
- Support more than 3 systems
- Real-time streaming diagnostics
- Historical trend analysis
- API rate limiting & authentication

---

## FDE Skills Demonstrated

✅ **System Integration** — Matching across 3 disparate systems  
✅ **Debugging** — Root-cause analysis with confidence scoring  
✅ **Constraints** — Zero budget, mock data only  
✅ **Scalability thinking** — Designed for large datasets  
✅ **Production-ready** — Docker, logging, health checks  
✅ **Documentation** — API specs, decision records, deployment guides  

---

**Next:** See [SCENARIOS.md](SCENARIOS.md) for concrete use cases this architecture handles.
```

---

Now copy this entire block into `docs/ARCHITECTURE.md`, save, and commit:

```bash
git add docs/ARCHITECTURE.md
git commit -m "docs: add architecture decision records and system design"
git push origin main
```

Next step: Should I provide `SCENARIOS.md`?


**User**
Just give the ARCHITECTURE.md content


**Claude**
{"type":"think","think":"The user is asking me to just provide the ARCHITECTURE.md content without the additional explanation and instructions around it. They want a more concise response - just the content to copy-paste.\n\nLooking back at their memory, they prefer short answers in paragraph format rather than long detailed responses. I should be more direct and just provide what they asked for."}


**Claude**
```markdown
# Architecture & Design Decisions

## System Design Overview

```
┌────────────────────────────────────────────────────────────────────┐
│                         CLIENT LAYER                               │
│                    (Curl, Python SDK, UI)                          │
└────────────────────────────┬─────────────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────────┐
│                    API LAYER (FastAPI)                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │ POST/diagnose│  │GET /health   │  │POST/batch    │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
└────────────────────────────┬─────────────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────────┐
│              BUSINESS LOGIC LAYER                                 │
│  ┌─────────────────────┐      ┌──────────────────────┐            │
│  │ Reconciler Module   │      │ Diagnostics Module   │            │
│  ├─ Transaction Match  │      ├─ Root-Cause Engine  │            │
│  ├─ Mismatch Detection │      ├─ Confidence Score   │            │
│  └─ Gap Analysis       │      └─ Remediation Hints  │            │
│  └─────────────────────┘      └──────────────────────┘            │
└────────────────────────────┬─────────────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────────┐
│                  DATA LAYER (SQLite)                              │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐      │
│  │ Transactions   │  │ Reconciliation │  │ Diagnostics    │      │
│  │ Table          │  │ Results        │  │ Cache          │      │
│  └────────────────┘  └────────────────┘  └────────────────┘      │
└────────────────────────────┬─────────────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────────┐
│              SIMULATOR LAYER (Mock Data)                          │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐      │
│  │ Payment Proc   │  │ Ledger System  │  │ Settlement Sys │      │
│  │ Simulator      │  │ Simulator      │  │ Simulator      │      │
│  └────────────────┘  └────────────────┘  └────────────────┘      │
└────────────────────────────────────────────────────────────────────┘
```

## Technology Choices

### 1. **Framework: FastAPI**

**Decision:** Use FastAPI for REST API.

**Why:**
- **Lightweight** — Minimal boilerplate, ~15 LOC for a working endpoint
- **Async-ready** — Built-in async/await support for concurrent requests
- **Auto-documentation** — Swagger UI at `/docs` (impresses recruiters)
- **Type hints** — Built-in validation via Pydantic models
- **Low overhead** — Deployable on 0.5 CPU free tier
- **FDE relevant** — Debugging async code is a real-world FDE skill

**Alternative considered:** Flask (simpler but less feature-rich); Django (overkill for this scope).

---

### 2. **Database: SQLite**

**Decision:** Use SQLite for data persistence.

**Why:**
- **Zero setup** — File-based, no external DB server required
- **Zero cost** — Included with Python
- **Sufficient for POC** — Perfect for reconciliation datasets (millions of rows still queryable)
- **Deployable** — Single `.db` file can ship with Docker container
- **FDE mindset** — Shows you can work without cloud infrastructure

**Schema trade-off:** No horizontal scaling (not needed for demo).

**Alternative considered:** PostgreSQL (overkill); MongoDB (unnecessary for structured txn data).

---

### 3. **Language: Python**

**Decision:** Build in Python.

**Why:**
- **Fast iteration** — Write logic in 10 lines vs 30 in Java
- **Data science libraries** — Pandas for transaction analysis if needed
- **FDE friendly** — Debugging is simpler; clear error messages
- **Broad ecosystem** — FastAPI, SQLAlchemy, pytest all battle-tested

---

### 4. **Containerization: Docker**

**Decision:** Containerize with Docker.

**Why:**
- **Portability** — Runs identically on Windows, Mac, Linux, cloud
- **Deployment** — Ship entire environment (code + dependencies)
- **Resume value** — Docker is FDE requirement at most companies
- **Free tier ready** — Render.com, Railway.app accept Docker images

---

## Core Modules

### **simulator.py**
Generates mock transaction data with realistic mismatches.

**Responsibilities:**
- Create 3 systems' transaction logs with synthetic divergences
- Simulate timing lags, duplicates, amount mismatches, missing transactions
- Return JSON-serializable transaction objects

**Design:**
```python
class TransactionSimulator:
    def generate_matching_transactions(count: int)
    def inject_timing_lag(txns, lag_ms)
    def inject_duplicate(txns, duplicate_id)
    def inject_amount_mismatch(txns, system_id, variance)
    def get_sample_scenario(scenario_name: str)
```

---

### **reconciler.py**
Matches transactions across 3 systems and identifies divergences.

**Responsibilities:**
- Match transactions by ID across systems
- Detect missing transactions (System A has it, B doesn't)
- Identify timing lag between systems
- Flag amount mismatches

**Design:**
```python
class TransactionReconciler:
    def match_transactions(payment_txns, ledger_txns, settlement_txns)
    def find_mismatches() -> List[Mismatch]
    def calculate_match_confidence(txn1, txn2) -> float
```

**Matching logic:**
- Primary: Match by `transaction_id`
- Secondary: Match by `(amount, timestamp_window, status)` if ID missing
- Confidence scoring: How certain is the match?

---

### **diagnostics.py**
Analyzes mismatches and suggests root causes.

**Responsibilities:**
- Categorize mismatch type (timing lag, duplicate, amount, missing)
- Suggest root cause with confidence score
- Recommend remediation steps
- Provide actionable debugging hints

**Design:**
```python
class DiagnosticEngine:
    def diagnose_mismatch(mismatch: Mismatch) -> Diagnosis
    def suggest_root_cause(mismatch) -> (cause, confidence)
    def recommend_remediation(cause) -> str
```

**Diagnosis categories:**
1. **Timing Lag** — Transaction exists in all systems but at different times
   - Confidence: High if lag is consistent, medium if irregular
   - Remediation: "Check async processing queue" or "Network latency?"

2. **Missing Transaction** — Exists in System A but not in B/C
   - Confidence: High if APIs are healthy
   - Remediation: "Check settlement batch job logs"

3. **Duplicate Transaction** — Same ID appears twice in one system
   - Confidence: High
   - Remediation: "Idempotency key missing? Check API retry logic"

4. **Amount Mismatch** — Same transaction, different amounts
   - Confidence: Medium (could be rounding, fees, or corruption)
   - Remediation: "Investigate exchange rate or fee calculation"

5. **Data Corruption** — Amount/timestamp invalid in one system
   - Confidence: High if data fails validation
   - Remediation: "Check data pipeline; possible DB corruption"

---

### **api.py**
FastAPI application exposing reconciliation as REST endpoints.

**Endpoints:**

#### `GET /health`
- Response: `{"status": "healthy", "timestamp": "2026-07-03T10:00:00Z"}`
- Purpose: Liveness check for deployment monitoring

#### `POST /diagnose`
- Input: JSON with transaction arrays (payment_processor_txns, ledger_txns, settlement_txns)
- Output: JSON with matches, mismatches, detailed diagnostics
- Logic: Calls reconciler → diagnostics engine → formats response

#### `POST /batch-diagnose`
- Input: CSV file with transaction data
- Output: JSON diagnostics for entire batch
- Purpose: Handle large datasets

---

## Data Flow Example

**Request:**
```
Client sends 3 transaction lists to /diagnose
```

**Step 1: Reconciler matches**
```
Payment: PAY-001 ($100, 10:00)
Ledger:  LED-001 ($100, 10:05)  → Match found, 5min lag detected
Settlement: SET-001 ($99.50, 10:10)  → Amount mismatch
```

**Step 2: Diagnostics analyzes**
```
Mismatch 1: Payment vs Ledger timing lag
  → Root cause: "Async ledger processing"
  → Confidence: 0.92
  → Remediation: "Check queue depth"

Mismatch 2: Ledger vs Settlement amount
  → Root cause: "Rounding in settlement conversion"
  → Confidence: 0.88
  → Remediation: "Verify exchange rate"
```

**Step 3: API returns**
```json
{
  "matches": 1,
  "mismatches": 2,
  "diagnostics": [...]
}
```

---

## Deployment Architecture

### Local Development
```
Developer laptop
  ├─ venv (Python env)
  ├─ SQLite (local DB)
  ├─ FastAPI server
  └─ Test suite
```

### Docker Container
```
Docker image
  ├─ Python 3.9
  ├─ FastAPI + dependencies
  ├─ SQLite
  └─ App code
```

### Cloud (Free Tier)
```
Render.com / Railway.app
  ├─ Container deployment
  ├─ Auto-scaling (if needed)
  ├─ HTTPS endpoint
  └─ Logs + monitoring
```

---

## Design Patterns Used

### 1. **Separation of Concerns**
- Simulator ≠ Reconciler ≠ Diagnostics ≠ API
- Each module has one clear responsibility
- Easy to test, debug, extend

### 2. **Confidence Scoring**
- Don't just say "mismatch found"—say "95% confident it's a timing lag"
- Shows probabilistic thinking (FDE skill)
- Helps teams prioritize remediation

### 3. **Scenario-Based Testing**
- Real cases (timing lag, duplicates, etc.) drive development
- Easy to validate against production patterns
- Proves you understand fintech reconciliation

### 4. **Structured Logging**
- JSON logs (not plain text)
- Includes context: request_id, system_affected, confidence
- Deployable to ELK/Splunk

---

## Trade-offs & Constraints

| Aspect | Choice | Trade-off |
|--------|--------|-----------|
| **Database** | SQLite | No horizontal scaling (acceptable for POC) |
| **API** | Stateless | No session management (not needed) |
| **Matching** | ID-first, then heuristic | May miss obscure matches (acceptable) |
| **Diagnostics** | Rule-based | No ML (not justified for 5 scenarios) |
| **Deployment** | Free tier | Low performance (acceptable for demo) |

---

## Extensibility Roadmap

**Future enhancements (not in Week 1-2 scope):**
- Add ML-based mismatch classification
- Support more than 3 systems
- Real-time streaming diagnostics
- Historical trend analysis
- API rate limiting & authentication

---

## FDE Skills Demonstrated

✅ **System Integration** — Matching across 3 disparate systems  
✅ **Debugging** — Root-cause analysis with confidence scoring  
✅ **Constraints** — Zero budget, mock data only  
✅ **Scalability thinking** — Designed for large datasets  
✅ **Production-ready** — Docker, logging, health checks  
✅ **Documentation** — API specs, decision records, deployment guides  

---

**Next:** See [SCENARIOS.md](SCENARIOS.md) for concrete use cases this architecture handles.
```


**User**
Can you write the SCENARIOS.md and give me a downloadable file for it?


**Claude**
{"type":"think","think":"The user is asking for the SCENARIOS.md content and wants a downloadable file. However, I'm a text-based AI and cannot actually generate downloadable files directly. What I can do is:\n\n1. Provide the complete SCENARIOS.md content that they can copy-paste\n2. Give them instructions on how to save it as a file\n\nI should provide the full SCENARIOS.md content with 5 real-world reconciliation scenarios that align with the fintech/payment processing context mentioned in the project.\n\nLet me create detailed scenarios that would be realistic for a distributed payment system, each with:\n- Problem statement\n- Systems involved\n- Expected diagnosis output\n- Root cause\n- Remediation steps\n\nI'll make it comprehensive but concise, following the pattern from the previous files."}


**Claude**
# SCENARIOS.md Content

I can't create actual downloadable files, but here's the complete content. **Copy-paste this into `docs/SCENARIOS.md`:**

```markdown
# Reconciliation Scenarios

Real-world payment system reconciliation cases that this toolkit diagnoses.

---

## Scenario 1: Timing Lag (Async Processing Delay)

### Problem Statement
A payment was successfully processed at 10:00 AM but didn't appear in the ledger until 10:05 AM. Settlement processed it at 10:10 AM. Teams report "missing transactions" but the money eventually arrives.

### Systems Involved
- **Payment Processor:** Processes and confirms payment immediately
- **Ledger:** Records transaction asynchronously (batch job every 5 minutes)
- **Settlement:** Settles only recorded ledger entries

### Sample Data

```json
{
  "payment_processor_txns": [
    {
      "id": "PAY-2026-001",
      "amount": 500.00,
      "currency": "USD",
      "timestamp": "2026-07-03T10:00:00Z",
      "status": "completed",
      "merchant_id": "MERCHANT-123"
    }
  ],
  "ledger_txns": [
    {
      "id": "LED-2026-001",
      "payment_id": "PAY-2026-001",
      "amount": 500.00,
      "currency": "USD",
      "timestamp": "2026-07-03T10:05:00Z",
      "status": "recorded",
      "batch_id": "BATCH-5MIN-001"
    }
  ],
  "settlement_txns": [
    {
      "id": "SET-2026-001",
      "ledger_id": "LED-2026-001",
      "amount": 500.00,
      "currency": "USD",
      "timestamp": "2026-07-03T10:10:00Z",
      "status": "settled",
      "settlement_batch": "DAILY-BATCH-001"
    }
  ]
}
```

### Expected Diagnosis Output

```json
{
  "scenario": "timing_lag",
  "matches": 1,
  "mismatches": 2,
  "total_transactions": 3,
  "diagnostics": [
    {
      "mismatch_id": "TIMING-LAG-001",
      "type": "timing_lag",
      "severity": "low",
      "description": "Transaction PAY-2026-001 processed at 10:00:00Z but recorded in ledger at 10:05:00Z (5 minute lag)",
      "affected_systems": ["payment_processor", "ledger"],
      "time_gap_seconds": 300,
      "confidence": 0.95,
      "root_cause": "Async batch processing in ledger system",
      "remediation": "This is expected behavior. Ledger batch job runs every 5 minutes. Verify batch job logs at /logs/ledger/batch-2026-07-03T10:05:00Z.log to confirm successful processing.",
      "action_items": [
        "Check ledger batch queue depth",
        "Verify no failed records in batch",
        "Monitor if lag exceeds 10 minutes (indicates backlog)"
      ]
    },
    {
      "mismatch_id": "TIMING-LAG-002",
      "type": "timing_lag",
      "severity": "low",
      "description": "Transaction recorded in ledger at 10:05:00Z but settled at 10:10:00Z (5 minute lag)",
      "affected_systems": ["ledger", "settlement"],
      "time_gap_seconds": 300,
      "confidence": 0.93,
      "root_cause": "Settlement processes on separate daily cycle",
      "remediation": "Settlement batch runs hourly. 5-minute lag is within SLA. Verify settlement job logs to confirm inclusion in DAILY-BATCH-001.",
      "action_items": [
        "Confirm settlement batch completed successfully",
        "Check if transaction included in next settlement window"
      ]
    }
  ],
  "summary": "All transactions matched successfully. Timing lags are within normal async processing windows. No action required."
}
```

### Root Cause
Ledger and Settlement systems process asynchronously via batch jobs, not real-time. This is **by design** for cost optimization.

### Remediation
- Monitor batch job execution logs
- Set up alerts if lag exceeds SLA (e.g., > 10 minutes)
- No code changes needed; this is expected behavior

---

## Scenario 2: Missing Transaction (Settlement Failed Silently)

### Problem Statement
A transaction was successfully recorded in the ledger but never made it to settlement. The $10,000 payment is "stuck" and customer hasn't received the money. Teams don't know why.

### Systems Involved
- **Payment Processor:** Confirmed payment
- **Ledger:** Recorded transaction
- **Settlement:** Transaction missing (likely failed validation)

### Sample Data

```json
{
  "payment_processor_txns": [
    {
      "id": "PAY-2026-002",
      "amount": 10000.00,
      "currency": "USD",
      "timestamp": "2026-07-03T11:00:00Z",
      "status": "completed",
      "recipient_account": "ACCOUNT-456",
      "recipient_bank_code": "SWIFT-UNKNOWN"
    }
  ],
  "ledger_txns": [
    {
      "id": "LED-2026-002",
      "payment_id": "PAY-2026-002",
      "amount": 10000.00,
      "currency": "USD",
      "timestamp": "2026-07-03T11:05:00Z",
      "status": "recorded",
      "batch_id": "BATCH-5MIN-002"
    }
  ],
  "settlement_txns": []
}
```

### Expected Diagnosis Output

```json
{
  "scenario": "missing_transaction",
  "matches": 1,
  "mismatches": 1,
  "total_transactions": 2,
  "diagnostics": [
    {
      "mismatch_id": "MISSING-TXN-001",
      "type": "missing_transaction",
      "severity": "critical",
      "description": "Transaction LED-2026-002 exists in Ledger but NOT in Settlement system",
      "affected_systems": ["ledger", "settlement"],
      "transaction_id": "PAY-2026-002",
      "amount": 10000.00,
      "confidence": 0.99,
      "root_cause": "Settlement validation failed (possible: invalid SWIFT code, missing beneficiary bank details, or settlement job crashed)",
      "remediation": "1) Check settlement job logs for failed validation errors. 2) Verify SWIFT code 'SWIFT-UNKNOWN' is valid. 3) Check if ledger entry has required settlement fields.",
      "action_items": [
        "Query settlement dead-letter queue: SELECT * FROM settlement_dlq WHERE ledger_id='LED-2026-002'",
        "Validate recipient bank code in external reference database",
        "Check settlement job error logs for timestamp 2026-07-03T11:05:00Z",
        "If validation error: fix bank code and resubmit",
        "If job crash: restart settlement job and retry"
      ]
    }
  ],
  "summary": "CRITICAL: $10,000 transaction stuck in ledger, not settled. Likely validation failure. Requires immediate investigation."
}
```

### Root Cause
Settlement system performs strict validation (e.g., SWIFT code format, beneficiary bank registration). Invalid data in ledger entry causes silent rejection.

### Remediation
- Query settlement dead-letter queue (DLQ) for error messages
- Validate bank codes against external registry
- Fix ledger entry and resubmit to settlement
- Set up alerts for DLQ growth

---

## Scenario 3: Duplicate Transaction (Idempotency Failure)

### Problem Statement
A customer complained they were charged twice. Investigation shows the same payment appears twice in the ledger but only once in settlement. Unclear if duplicate happened during payment processing or ledger entry.

### Systems Involved
- **Payment Processor:** One confirmed payment
- **Ledger:** Same payment recorded twice (idempotency failure)
- **Settlement:** One settled (deduped by settlement system)

### Sample Data

```json
{
  "payment_processor_txns": [
    {
      "id": "PAY-2026-003",
      "amount": 75.50,
      "currency": "USD",
      "timestamp": "2026-07-03T12:00:00Z",
      "status": "completed",
      "idempotency_key": "IDEMPOTENCY-KEY-ABC123",
      "customer_id": "CUST-789"
    }
  ],
  "ledger_txns": [
    {
      "id": "LED-2026-003-A",
      "payment_id": "PAY-2026-003",
      "amount": 75.50,
      "currency": "USD",
      "timestamp": "2026-07-03T12:05:00Z",
      "status": "recorded",
      "idempotency_key": "IDEMPOTENCY-KEY-ABC123"
    },
    {
      "id": "LED-2026-003-B",
      "payment_id": "PAY-2026-003",
      "amount": 75.50,
      "currency": "USD",
      "timestamp": "2026-07-03T12:05:15Z",
      "status": "recorded",
      "idempotency_key": "IDEMPOTENCY-KEY-ABC123"
    }
  ],
  "settlement_txns": [
    {
      "id": "SET-2026-003",
      "ledger_id": "LED-2026-003-A",
      "amount": 75.50,
      "currency": "USD",
      "timestamp": "2026-07-03T12:10:00Z",
      "status": "settled",
      "deduped": true,
      "duplicate_detected": "LED-2026-003-B"
    }
  ]
}
```

### Expected Diagnosis Output

```json
{
  "scenario": "duplicate_transaction",
  "matches": 1,
  "mismatches": 2,
  "total_transactions": 4,
  "diagnostics": [
    {
      "mismatch_id": "DUPLICATE-TXN-001",
      "type": "duplicate_transaction",
      "severity": "high",
      "description": "Ledger contains 2 entries (LED-2026-003-A, LED-2026-003-B) for same payment PAY-2026-003, recorded 15 seconds apart",
      "affected_systems": ["ledger"],
      "transaction_id": "PAY-2026-003",
      "duplicate_count": 2,
      "confidence": 0.99,
      "root_cause": "Ledger batch job did NOT check idempotency key before inserting. Possible causes: (1) Duplicate message in batch queue, (2) Ledger job retried with same batch, (3) Client sent duplicate payment request",
      "remediation": "1) Identify which LED entry is primary (usually first). 2) Check client retry logs to see if payment API was called twice. 3) Check ledger batch job logs for retries. 4) Implement idempotency key uniqueness constraint in ledger DB.",
      "action_items": [
        "SELECT * FROM ledger WHERE idempotency_key='IDEMPOTENCY-KEY-ABC123' to find all duplicates",
        "Check payment API access logs: was PAY-2026-003 requested twice?",
        "Verify ledger batch job idempotency: does it check existing keys before insert?",
        "Add DB constraint: ALTER TABLE ledger ADD UNIQUE(idempotency_key)",
        "Refund customer for duplicate charge (LED-2026-003-B): $75.50"
      ]
    },
    {
      "mismatch_id": "DUPLICATE-TXN-002",
      "type": "duplicate_transaction",
      "severity": "high",
      "description": "Settlement system detected and deduped the duplicate. Only settled LED-2026-003-A, marked LED-2026-003-B as duplicate.",
      "affected_systems": ["settlement"],
      "confidence": 0.98,
      "root_cause": "Settlement system has idempotency check. Good catch, but indicates ledger already had duplicate.",
      "remediation": "Settlement correctly deduped. Issue originated in ledger. See DUPLICATE-TXN-001 remediation.",
      "action_items": [
        "Verify settlement marked duplicate correctly: check SET-2026-003.duplicate_detected='LED-2026-003-B'",
        "Ensure settlement does NOT attempt to settle duplicates"
      ]
    }
  ],
  "summary": "HIGH: Duplicate transaction detected in ledger. Settlement system caught it, but refund required. Root cause: missing idempotency check in ledger batch job."
}
```

### Root Cause
Ledger batch job does not validate idempotency keys before inserting. This allows duplicates if the same batch message is processed twice.

### Remediation
- Add database UNIQUE constraint on `idempotency_key`
- Add idempotency check in batch job before insert
- Check payment API logs to see if client made duplicate request
- Issue refund for duplicate charge
- Monitor for idempotency failures in future batches

---

## Scenario 4: Amount Mismatch (Rounding Error)

### Problem Statement
A transaction shows $100.00 in payment processor, $100.00 in ledger, but $99.99 in settlement. The $0.01 discrepancy is small but causes reconciliation to fail. Teams report "amount mismatch" and don't know if it's a rounding error or data corruption.

### Systems Involved
- **Payment Processor:** Confirms amount as-is
- **Ledger:** Records amount as-is
- **Settlement:** Applies exchange rate / fee calculation, resulting in different amount

### Sample Data

```json
{
  "payment_processor_txns": [
    {
      "id": "PAY-2026-004",
      "amount": 100.00,
      "currency": "USD",
      "timestamp": "2026-07-03T13:00:00Z",
      "status": "completed"
    }
  ],
  "ledger_txns": [
    {
      "id": "LED-2026-004",
      "payment_id": "PAY-2026-004",
      "amount": 100.00,
      "currency": "USD",
      "timestamp": "2026-07-03T13:05:00Z",
      "status": "recorded"
    }
  ],
  "settlement_txns": [
    {
      "id": "SET-2026-004",
      "ledger_id": "LED-2026-004",
      "amount": 99.99,
      "currency": "USD",
      "timestamp": "2026-07-03T13:10:00Z",
      "status": "settled",
      "settlement_fee": 0.01,
      "exchange_rate": 1.0,
      "fee_calculation": "FLAT_1CENT_FEE"
    }
  ]
}
```

### Expected Diagnosis Output

```json
{
  "scenario": "amount_mismatch",
  "matches": 1,
  "mismatches": 1,
  "total_transactions": 3,
  "diagnostics": [
    {
      "mismatch_id": "AMOUNT-MISMATCH-001",
      "type": "amount_mismatch",
      "severity": "medium",
      "description": "Transaction amount differs across systems: Payment=$100.00, Ledger=$100.00, Settlement=$99.99 (variance: $0.01)",
      "affected_systems": ["ledger", "settlement"],
      "transaction_id": "PAY-2026-004",
      "amount_variance": -0.01,
      "variance_percentage": 0.01,
      "confidence": 0.85,
      "root_cause": "Settlement applies flat 1-cent fee. Variance is expected and NOT data corruption.",
      "remediation": "Verify settlement fee configuration matches business rules. Check if fee should be deducted from ledger or billed separately.",
      "action_items": [
        "Review settlement system fee policy: is 1-cent flat fee expected?",
        "Check if fee should appear in ledger as separate line item or deducted from amount",
        "If fee is deducted: amount match is correct. Reconciliation logic should account for settlement fees.",
        "If fee should be separate line item: investigate settlement system configuration"
      ]
    }
  ],
  "summary": "Amount variance of $0.01 detected. Likely due to settlement fee. NOT data corruption. Verify fee policy is applied correctly."
}
```

### Root Cause
Settlement system deducts a flat 1-cent fee from each transaction. This is expected behavior per business rules, but reconciliation logic didn't account for it.

### Remediation
- Update reconciliation logic to expect settlement fees
- Document fee policy in API spec
- Add `settlement_fee` field to diagnostic output
- Monitor variance percentage; alert if > 1%

---

## Scenario 5: System Outage (Data Corruption)

### Problem Statement
A settlement system outage occurred at 2:00 PM. When it came back online, a transaction appeared corrupted: timestamp is invalid (year 9999), amount is negative, status is "unknown". Teams don't know if it's a DB corruption, bad data ingestion, or a system bug.

### Systems Involved
- **Payment Processor:** Normal transaction
- **Ledger:** Normal transaction
- **Settlement:** Corrupted transaction (invalid data)

### Sample Data

```json
{
  "payment_processor_txns": [
    {
      "id": "PAY-2026-005",
      "amount": 250.00,
      "currency": "USD",
      "timestamp": "2026-07-03T14:00:00Z",
      "status": "completed"
    }
  ],
  "ledger_txns": [
    {
      "id": "LED-2026-005",
      "payment_id": "PAY-2026-005",
      "amount": 250.00,
      "currency": "USD",
      "timestamp": "2026-07-03T14:05:00Z",
      "status": "recorded"
    }
  ],
  "settlement_txns": [
    {
      "id": "SET-2026-005",
      "ledger_id": "LED-2026-005",
      "amount": -250.00,
      "currency": "USD",
      "timestamp": "9999-12-31T23:59:59Z",
      "status": "unknown",
      "raw_data": "0x0000DEADBEEF..."
    }
  ]
}
```

### Expected Diagnosis Output

```json
{
  "scenario": "data_corruption",
  "matches": 1,
  "mismatches": 2,
  "total_transactions": 3,
  "diagnostics": [
    {
      "mismatch_id": "DATA-CORRUPTION-001",
      "type": "data_corruption",
      "severity": "critical",
      "description": "Settlement transaction SET-2026-005 contains invalid data: amount is negative (-$250.00), timestamp is in year 9999 (invalid), status is 'unknown'",
      "affected_systems": ["settlement"],
      "transaction_id": "PAY-2026-005",
      "invalid_fields": ["amount", "timestamp", "status"],
      "confidence": 0.98,
      "root_cause": "System outage at 2:00 PM likely caused data corruption during write operation or recovery. Corrupted write buffer / incomplete transaction.",
      "remediation": "This is NOT a reconciliation logic issue. The settlement system DB is corrupted. Requires immediate investigation and possible data recovery from backup.",
      "action_items": [
        "CHECK settlement system error logs for timestamp 2026-07-03T14:00:00Z to 2026-07-03T14:10:00Z",
        "ALERT: Possible DB corruption or incomplete write during outage recovery",
        "ESCALATE: Contact DBA to check settlement DB integrity",
        "Run: SELECT * FROM settlement WHERE amount < 0 OR timestamp > '2100-01-01' (find all corrupted records)",
        "RESTORE: If DB is corrupted, restore from backup taken before 2026-07-03T14:00:00Z",
        "VERIFY: After restore, re-run reconciliation for affected time window",
        "MONITOR: Watch settlement system health metrics for 24 hours post-recovery"
      ]
    }
  ],
  "summary": "CRITICAL: Settlement transaction contains invalid data (negative amount, year 9999 timestamp). Likely DB corruption from system outage. Requires immediate DBA investigation and possible data recovery."
}
```

### Root Cause
Settlement system experienced an outage. During recovery, a write operation failed partially, leaving corrupted data in the DB.

### Remediation
- Check system error logs from outage window
- Run DB integrity checks
- Query for all corrupted records (negative amounts, invalid timestamps)
- Restore from pre-outage backup if corruption is widespread
- Re-reconcile after recovery
- Monitor for 24 hours

---

## Using These Scenarios in Testing

### Unit Test Example
```python
from src.diagnostics import DiagnosticEngine
from tests.scenarios import SCENARIO_TIMING_LAG

def test_timing_lag_diagnosis():
    engine = DiagnosticEngine()
    result = engine.diagnose(
        payment_txns=SCENARIO_TIMING_LAG['payment_processor_txns'],
        ledger_txns=SCENARIO_TIMING_LAG['ledger_txns'],
        settlement_txns=SCENARIO_TIMING_LAG['settlement_txns']
    )
    assert result['scenario'] == 'timing_lag'
    assert result['severity'] == 'low'
    assert result['confidence'] > 0.90
```

### Integration Test Example
```python
@pytest.mark.integration
def test_all_scenarios():
    scenarios = [
        SCENARIO_TIMING_LAG,
        SCENARIO_MISSING_TXN,
        SCENARIO_DUPLICATE,
        SCENARIO_AMOUNT_MISMATCH,
        SCENARIO_DATA_CORRUPTION
    ]
    
    for scenario in scenarios:
        result = api_client.post('/diagnose', json=scenario)
        assert result.status_code == 200
        assert 'diagnostics' in result.json()
```

---

## Summary

| Scenario | Severity | Root Cause | Remediation |
|----------|----------|-----------|-------------|
| **Timing Lag** | Low | Async batch processing | Monitor batch logs; expected behavior |
| **Missing Transaction** | Critical | Settlement validation failed | Query DLQ; fix data; resubmit |
| **Duplicate** | High | Idempotency check failed | Add DB constraint; fix client retry logic |
| **Amount Mismatch** | Medium | Settlement fee applied | Verify fee policy; update reconciliation logic |
| **Data Corruption** | Critical | System outage / DB corruption | DB recovery; restore from backup |

These scenarios drive the diagnostic engine logic. Each mismatch type maps to a diagnosis category with confidence scoring and actionable remediation steps.
```

---

## How to Save as File

Since I can't generate actual downloadable files, **copy the content above and:**

**Option 1: Paste in VS Code**
1. Open `docs/SCENARIOS.md` in VS Code
2. Select all (Ctrl+A) and delete existing content
3. Paste the content above
4. Save (Ctrl+S)

**Option 2: Use PowerShell to create file**
```powershell
# Copy entire content above, then:
@"
[PASTE ENTIRE MARKDOWN ABOVE HERE]
"@ | Out-File -FilePath docs/SCENARIOS.md -Encoding utf8
```

**Option 3: Git it directly**
```bash
git add docs/SCENARIOS.md
git commit -m "docs: add 5 production-like reconciliation scenarios"
git push origin main
```

Done? Then we move to `API_REFERENCE.md` or start coding?


**User**
All the above content goes into SCENARIOS.md file?


**Claude**
{"type":"think","think":"The user is asking for clarification - they want to confirm that all the content I provided above should go into the SCENARIOS.md file. Yes, that's correct. The entire markdown content I provided (starting from the first \"# SCENARIOS.md Content\" all the way through the end with the summary table) should be copied into the docs/SCENARIOS.md file.\n\nI should confirm this clearly and give them simple instructions to do it."}


**Claude**
**Yes, exactly.** All the content from the first line:

```markdown
# Reconciliation Scenarios
```

Through the last line:

```markdown
These scenarios drive the diagnostic engine logic. Each mismatch type maps to a diagnosis category with confidence scoring and actionable remediation steps.
```

**All goes into `docs/SCENARIOS.md`**

---

## Quick Steps:

1. Open `docs/SCENARIOS.md` in VS Code
2. Delete any existing placeholder content
3. Copy-paste the entire markdown block I provided
4. Save (Ctrl+S)
5. Commit:

```bash
git add docs/SCENARIOS.md
git commit -m "docs: add 5 production-like reconciliation scenarios"
git push origin main
```

That's it. The file will be ~500 lines with all 5 scenarios fully detailed.

Ready to move to next doc, or want to verify the file first?


**User**
Give me 3 blocks-
Block 1 - Complete content of README.md
Block 2 - Complete content of ARCHITECTURE.md
Block 3 - Complete content of SCENARIOS.md


These blocks should not contain anything else. Give me the content so that I can directly copy paste the content into the respective documents.


**Claude**
{"type":"think","think":"The user wants me to provide three separate, complete markdown content blocks that they can directly copy-paste into their files. No explanations, no instructions—just the raw content for:\n1. README.md\n2. ARCHITECTURE.md\n3. SCENARIOS.md\n\nI should provide them clearly labeled and ready to paste."}


**Claude**
# BLOCK 1: README.md

```markdown
# Distributed System Health Monitor & Diagnostic Toolkit

A lightweight diagnostic tool that identifies and debugs transaction mismatches across distributed payment systems. Built to demonstrate system integration, root-cause analysis, and deployment patterns—zero external infrastructure required.

## Problem Statement

You're a forward deployed engineer at a fintech company. Three critical systems—**payment processor**, **ledger**, and **settlement**—occasionally diverge. Teams lack real-time visibility into *why* or *where* failures occur. They need a tool that:

- Identifies transaction mismatches across systems
- Diagnoses root causes (timing lag, duplicates, data corruption, rounding errors)
- Provides actionable remediation steps
- Works in constrained environments without backend access

This project simulates production reconciliation scenarios and provides a diagnostic engine—proving you can debug complex distributed systems under constraints.

## What This Solves

✅ **Mismatch Detection** — Compares transactions across 3 systems, flags divergences  
✅ **Root-Cause Analysis** — Suggests why mismatches occurred (with confidence scoring)  
✅ **Batch Processing** — Handles large transaction datasets  
✅ **Real-World Scenarios** — 5+ production-like test cases included  
✅ **Deployable** — Docker containerized, zero external dependencies  
✅ **Observable** — Structured logging for debugging

## Quick Start

### Prerequisites
- Python 3.9+
- Git

### Setup (5 minutes)

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/distributed-system-diagnostics.git
cd distributed-system-diagnostics

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the API server
python -m uvicorn src.api:app --reload
```

Server runs at `http://localhost:8000`

### First Request

```bash
# Health check
curl http://localhost:8000/health

# Run diagnosis on sample data
curl -X POST http://localhost:8000/diagnose \
  -H "Content-Type: application/json" \
  -d @sample_request.json
```

## Architecture

```
┌─────────────────────────────────────────────┐
│         API Layer (FastAPI)                 │
│  /health, /diagnose, /batch-diagnose        │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│   Reconciliation Engine                     │
│  ├─ Transaction Matcher                     │
│  └─ Mismatch Detector                       │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│   Diagnostic Engine                         │
│  ├─ Root-Cause Suggester                    │
│  ├─ Confidence Scorer                       │
│  └─ Remediation Recommender                 │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│   Data Layer (SQLite + Simulator)           │
│  ├─ Payment Processor Simulator              │
│  ├─ Ledger Simulator                         │
│  └─ Settlement System Simulator              │
└─────────────────────────────────────────────┘
```

### Tech Stack

| Component | Choice | Why |
|-----------|--------|-----|
| **Framework** | FastAPI | Lightweight, async-ready, auto-docs |
| **Database** | SQLite | Zero setup, file-based, perfect for POC |
| **Container** | Docker | Portable, deployable anywhere |
| **Language** | Python | Fast iteration, FDE-friendly |

## API Reference

### `POST /diagnose`

Diagnose mismatches in transaction data.

**Request:**
```json
{
  "payment_processor_txns": [
    {
      "id": "PAY-001",
      "amount": 100.00,
      "timestamp": "2026-07-03T10:00:00Z",
      "status": "completed"
    }
  ],
  "ledger_txns": [
    {
      "id": "LED-001",
      "amount": 100.00,
      "timestamp": "2026-07-03T10:05:00Z",
      "status": "recorded"
    }
  ],
  "settlement_txns": [
    {
      "id": "SET-001",
      "amount": 99.50,
      "timestamp": "2026-07-03T10:10:00Z",
      "status": "settled"
    }
  ]
}
```

**Response:**
```json
{
  "matches": 1,
  "mismatches": 2,
  "total_transactions": 3,
  "diagnostics": [
    {
      "type": "timing_lag",
      "severity": "medium",
      "description": "Payment processed at 10:00 but recorded in ledger at 10:05 (5min lag)",
      "confidence": 0.92,
      "affected_systems": ["payment_processor", "ledger"],
      "remediation": "Check network latency or ledger async processing queue"
    },
    {
      "type": "amount_mismatch",
      "severity": "high",
      "description": "Settlement shows $99.50, ledger shows $100.00 (0.5 difference)",
      "confidence": 0.88,
      "affected_systems": ["ledger", "settlement"],
      "remediation": "Investigate rounding logic or exchange rate applied in settlement"
    }
  ]
}
```

### `POST /batch-diagnose`

Process multiple transaction batches (CSV upload).

### `GET /health`

Check API status.

## Project Structure

```
distributed-system-diagnostics/
├── src/
│   ├── __init__.py
│   ├── simulator.py        # Generates mock transaction data
│   ├── reconciler.py       # Matches transactions across systems
│   ├── diagnostics.py      # Root-cause analysis engine
│   └── api.py              # FastAPI endpoints
├── tests/
│   ├── test_reconciler.py  # Unit tests for matching logic
│   └── test_diagnostics.py # Unit tests for diagnosis
├── docs/
│   ├── ARCHITECTURE.md     # Design decisions & tech rationale
│   ├── API_REFERENCE.md    # Full API documentation
│   ├── DEPLOYMENT.md       # Docker & cloud deployment guide
│   └── SCENARIOS.md        # 5 real-world reconciliation cases
├── requirements.txt        # Python dependencies
├── docker-compose.yml      # Docker setup
├── .env                    # Environment variables (not committed)
└── README.md               # This file
```

## Deployment

### Local Docker

```bash
docker-compose up --build
# Runs on http://localhost:8000
```

### Cloud (Free Tier)

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for step-by-step guide to deploy on:
- Render.com (free tier, 0.50 CPU)
- Railway.app (free credits)

## Learning Outcomes

This project demonstrates:

- **System Integration** — Reconciling disparate data sources
- **Debugging** — Root-cause analysis under incomplete information
- **Rapid Prototyping** — Full POC in 2 weeks, zero budget
- **Deployment** — Containerized, cloud-ready architecture
- **Observability** — Structured logging and confidence scoring
- **Documentation** — Clear API specs, scenario walkthroughs, deployment guides

## Roadmap

- **Week 1:** MVP (reconciliation engine + basic API)
- **Week 2:** Advanced diagnostics + deployment

See [ARCHITECTURE.md](docs/ARCHITECTURE.md) for detailed sprint plan.

## Getting Help

- Check [SCENARIOS.md](docs/SCENARIOS.md) for example use cases
- Review [API_REFERENCE.md](docs/API_REFERENCE.md) for endpoint details
- Open an issue for bugs or feature requests

## License

MIT License — See LICENSE file for details

---

**Built to showcase Forward Deployed Engineer skills:** system debugging, constraint-based design, and production-ready code.
```

---

# BLOCK 2: ARCHITECTURE.md

```markdown
# Architecture & Design Decisions

## System Design Overview

```
┌────────────────────────────────────────────────────────────────────┐
│                         CLIENT LAYER                               │
│                    (Curl, Python SDK, UI)                          │
└────────────────────────────┬─────────────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────────┐
│                    API LAYER (FastAPI)                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │ POST/diagnose│  │GET /health   │  │POST/batch    │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
└────────────────────────────┬─────────────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────────┐
│              BUSINESS LOGIC LAYER                                 │
│  ┌─────────────────────┐      ┌──────────────────────┐            │
│  │ Reconciler Module   │      │ Diagnostics Module   │            │
│  ├─ Transaction Match  │      ├─ Root-Cause Engine  │            │
│  ├─ Mismatch Detection │      ├─ Confidence Score   │            │
│  └─ Gap Analysis       │      └─ Remediation Hints  │            │
│  └─────────────────────┘      └──────────────────────┘            │
└────────────────────────────┬─────────────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────────┐
│                  DATA LAYER (SQLite)                              │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐      │
│  │ Transactions   │  │ Reconciliation │  │ Diagnostics    │      │
│  │ Table          │  │ Results        │  │ Cache          │      │
│  └────────────────┘  └────────────────┘  └────────────────┘      │
└────────────────────────────┬─────────────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────────────┐
│              SIMULATOR LAYER (Mock Data)                          │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐      │
│  │ Payment Proc   │  │ Ledger System  │  │ Settlement Sys │      │
│  │ Simulator      │  │ Simulator      │  │ Simulator      │      │
│  └────────────────┘  └────────────────┘  └────────────────┘      │
└────────────────────────────────────────────────────────────────────┘
```

## Technology Choices

### 1. **Framework: FastAPI**

**Decision:** Use FastAPI for REST API.

**Why:**
- **Lightweight** — Minimal boilerplate, ~15 LOC for a working endpoint
- **Async-ready** — Built-in async/await support for concurrent requests
- **Auto-documentation** — Swagger UI at `/docs` (impresses recruiters)
- **Type hints** — Built-in validation via Pydantic models
- **Low overhead** — Deployable on 0.5 CPU free tier
- **FDE relevant** — Debugging async code is a real-world FDE skill

**Alternative considered:** Flask (simpler but less feature-rich); Django (overkill for this scope).

---

### 2. **Database: SQLite**

**Decision:** Use SQLite for data persistence.

**Why:**
- **Zero setup** — File-based, no external DB server required
- **Zero cost** — Included with Python
- **Sufficient for POC** — Perfect for reconciliation datasets (millions of rows still queryable)
- **Deployable** — Single `.db` file can ship with Docker container
- **FDE mindset** — Shows you can work without cloud infrastructure

**Schema trade-off:** No horizontal scaling (not needed for demo).

**Alternative considered:** PostgreSQL (overkill); MongoDB (unnecessary for structured txn data).

---

### 3. **Language: Python**

**Decision:** Build in Python.

**Why:**
- **Fast iteration** — Write logic in 10 lines vs 30 in Java
- **Data science libraries** — Pandas for transaction analysis if needed
- **FDE friendly** — Debugging is simpler; clear error messages
- **Broad ecosystem** — FastAPI, SQLAlchemy, pytest all battle-tested

---

### 4. **Containerization: Docker**

**Decision:** Containerize with Docker.

**Why:**
- **Portability** — Runs identically on Windows, Mac, Linux, cloud
- **Deployment** — Ship entire environment (code + dependencies)
- **Resume value** — Docker is FDE requirement at most companies
- **Free tier ready** — Render.com, Railway.app accept Docker images

---

## Core Modules

### **simulator.py**
Generates mock transaction data with realistic mismatches.

**Responsibilities:**
- Create 3 systems' transaction logs with synthetic divergences
- Simulate timing lags, duplicates, amount mismatches, missing transactions
- Return JSON-serializable transaction objects

**Design:**
```python
class TransactionSimulator:
    def generate_matching_transactions(count: int)
    def inject_timing_lag(txns, lag_ms)
    def inject_duplicate(txns, duplicate_id)
    def inject_amount_mismatch(txns, system_id, variance)
    def get_sample_scenario(scenario_name: str)
```

---

### **reconciler.py**
Matches transactions across 3 systems and identifies divergences.

**Responsibilities:**
- Match transactions by ID across systems
- Detect missing transactions (System A has it, B doesn't)
- Identify timing lag between systems
- Flag amount mismatches

**Design:**
```python
class TransactionReconciler:
    def match_transactions(payment_txns, ledger_txns, settlement_txns)
    def find_mismatches() -> List[Mismatch]
    def calculate_match_confidence(txn1, txn2) -> float
```

**Matching logic:**
- Primary: Match by `transaction_id`
- Secondary: Match by `(amount, timestamp_window, status)` if ID missing
- Confidence scoring: How certain is the match?

---

### **diagnostics.py**
Analyzes mismatches and suggests root causes.

**Responsibilities:**
- Categorize mismatch type (timing lag, duplicate, amount, missing)
- Suggest root cause with


