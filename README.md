## SENTINEL 


📌 Project Timeline & Checklist

Project: Explainable Threat Prioritization System (Decision Support)
Focus: Defence Intelligence Assistance with Human-in-the-Loop Control

🗓️ Phase 0 — Problem Framing & Constraints (Week 1)
Objectives

Establish a narrow, defensible scope

Define system boundaries and non-goals

Checklist

 Define primary user persona (e.g., Intelligence Analyst)

 Clearly state what decisions the system assists

 Explicitly list decisions the system will NOT make

 Define operational context (near-real-time, advisory-only)

 Write a one-sentence mission success criterion

 Document ethical and policy constraints

 Freeze scope (no feature creep beyond this point)

Deliverable:
problem_statement.md

🗓️ Phase 1 — Threat Ontology & Data Modeling (Week 2)
Objectives

Define what constitutes a “threat”

Formalize data inputs and relationships

Checklist

 Define threat entity types (event / object / pattern)

 Define threat attributes (severity, confidence, source)

 Define temporal & spatial constraints

 Identify data source categories (sensor, report, log)

 Define trust levels for each data source

 Design data schemas (structured + unstructured)

 Decide how contradictory inputs are handled

Deliverable:
threat_ontology.md

🗓️ Phase 2 — System Architecture Design (Week 3)
Objectives

Design a minimal but realistic defence-grade architecture

Checklist

 Design secure data ingestion pipeline

 Define data validation & sanitization rules

 Design threat scoring / ranking module

 Define explainability layer

 Design immutable audit logging mechanism

 Define role-based access control

 Plan for offline / degraded operation

 Document all assumptions and limitations

Deliverable:
architecture_diagram.png + architecture_notes.md

🗓️ Phase 3 — Threat Prioritization Logic (Week 4)
Objectives

Implement interpretable decision logic

Checklist

 Choose interpretable models or rule-based logic

 Define scoring factors and weight rationale

 Implement confidence & uncertainty measures

 Ensure deterministic behavior for same inputs

 Enable human override hooks

 Version control decision logic

Deliverable:
threat_scoring_engine/

🗓️ Phase 4 — Explainability & Audit Layer (Week 5)
Objectives

Ensure every output is traceable and reviewable

Checklist

 Implement decision trace generation

 Store input data references per decision

 Log model / rule version used

 Capture user actions and overrides

 Ensure logs are append-only

 Enable decision reconstruction

Deliverable:
audit_log_spec.md + explainability_module/

🗓️ Phase 5 — Role-Based Interface (Week 6)
Objectives

Present information clearly without overload

Checklist

 Analyst view: detailed breakdown & reasoning

 Supervisor view: ranked summary & alerts

 Auditor view: logs, approvals, history

 Clearly label recommendation vs action

 Visualize uncertainty and confidence

 Display degraded mode indicators

Deliverable:
ui/

🗓️ Phase 6 — Security & Failure Handling (Week 7)
Objectives

Demonstrate defence-aware system behavior

Checklist

 Implement authentication & authorization

 Encrypt data at rest and in transit

 Disable external telemetry

 Simulate data source failure

 Test degraded operation behavior

 Validate safe failure modes

 Document security assumptions

Deliverable:
security_model.md

🗓️ Phase 7 — Evaluation & Validation (Week 8)
Objectives

Validate usefulness, not just accuracy

Checklist

 Test system with synthetic scenarios

 Evaluate prioritization consistency

 Measure explainability clarity

 Record false positive / negative cases

 Validate human override behavior

 Document limitations and known risks

Deliverable:
evaluation_report.md

🗓️ Phase 8 — Documentation & Demo (Week 9)
Objectives

Make the project defensible and presentable

Checklist

 Write a clear README

 Document design trade-offs

 Explain ethical boundaries

 Add architecture & flow diagrams

 Prepare demo scenarios

 Record demo (optional)

Deliverable:
README.md + demo assets

🏁 Definition of Done (Non-Negotiable)

 Every recommendation is explainable

 Every decision is auditable

 Human authority is preserved

 System fails safely

 Scope is controlled
