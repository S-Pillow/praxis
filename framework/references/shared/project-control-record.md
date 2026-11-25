## **Project Control Record Templates**

### **Full Project Control Record**

Project - ; AIPF/project-rule versions - ; record_revision/last_read_revision - ; profile ID when Platform Capability controls are active - ; execution-model summary when material - ; roles/transport - ; authoritative editable/version state - ; Control Ownership & Equivalence Map - ; Builder Access Map / equivalent execution-access map as applicable - ; phase/gate/authorization unit - ; accepted baseline - ; governing intent/protected invariants - ; canonical artifacts/IDs - ; state_revision/platform version/state_guard - ; execution-authority source - ; active unit ID/shape/planned transitions - ; treatment (Section 9.2): Compact / Managed - ; urgency overlay (Section 9.1): normal / urgent-corrective - ; authorization contract: actor/action/target/state-preconditions/constraints/stop - ; if work_allowance != none: {work_allowance - ; allowance_status - ; consumed/remaining only when measurable -} ; controlling-instruction source/authority scope - ; informational/agent-created content constraints - ; delegation parent/delegated-authority ceiling/privileged-access scope when applicable - ; decisions with owner/evidence/strength - ; blockers/current-impact risks plus stable references to unrelated accepted/deferred risks - ; governing-artifact identity/transition impact when applicable - ; if work was parked or independently continued: {parked workstreams/blockers/state - ; unaffected continuation/results -} ; preconditions - ; actor actions vs platform-owned automatic mutations/evaluations/triggers - ; scoped rules/corrections - ; evidence/recheck triggers - ; registered baseline relevance - ; operator gates - ; assessed Block B2 outcome/disposition, durability/closure fields, achieved evidence, and pending required observation - ; executor-report reference/discrepancy reason when different - ; next permitted/forbidden actions - ; refresh triggers - ; last reconciliation/disposition - .

### **Compact Project Control Record Entry**

Project - ; profile ID when Platform Capability controls are active - ; execution-model summary when material - ; record_revision - ; accepted baseline/authoritative state - ; state_revision/platform version/state_guard - ; governing intent/protected invariants - ; compact eligibility - ; urgency overlay (Section 9.1): normal / urgent-corrective - ; active unit ID/objective or batch IDs - ; planned procedural transitions - ; execution-authority source - ; authorized actor/action/target - ; if work_allowance != none: {work_allowance - ; allowance_status - ; consumed/remaining only when measurable -} ; delegation parent/delegated-authority ceiling/privileged-access scope when applicable - ; relevant locked rules/current-impact risks - ; if work was parked or independently continued: {parked workstreams/blockers/state - ; unaffected continuation/results -} ; evidence/observer/feasibility - ; assessed Block B2 outcome/disposition, durability/closure fields, achieved evidence, and pending required observation - ; executor-report reference/discrepancy reason when different - ; next permitted action/stop - .

### **State Write Record**

Use this embedded row only when canonical project state changes: revision_before - ; revision_after - ; authorized actor/source - ; fields changed - ; supporting evidence - ; superseded state/decision - ; reason - ; reconciliation required: yes/no - . Do not create a second state artifact for this purpose.

### **AI invariants**

• A stale revision never wins over a newer canonical state.

• A brief approval never becomes a stronger acceptance state than the owner actually expressed.

• Capability or tool access never substitutes for the Section 5 Action-scoped authorization contract.

• Batching reduces repeated envelope fields; it never removes item-level acceptance or evidence attribution.

