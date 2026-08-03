# Independent School 21 Cybersecurity Workflow

Use this guide when an AI assistant is unavailable. Each project-specific `preparation/EXECUTION-RUNBOOK.md` contains the exact task sequence.

## The rule that prevents most mistakes

A task is complete only when all four are true:

1. You performed the action yourself.
2. You can explain why it is needed.
3. You verified it with real output/evidence.
4. You saved the exact required filename.

## Start every project

1. Read all tasks once without configuring anything.
2. List required inputs, tools, deliverables, and environmental blockers.
3. Clone the official GitLab repository.
4. Create and switch to `develop`.
5. Work only inside `src` unless the official task explicitly says otherwise.
6. Preserve original supplied files and hash evidence inputs when relevant.
7. Create a VM/GNS3 snapshot before risky changes.
8. Complete one task and its verification gate before starting the next.

## Evidence note template

Keep this outside the submitted `src` folder unless the task requests it:

```text
Task:
Goal:
Why:
Action/command:
Expected:
Observed:
Proof (frame/screenshot/log/file):
Problem:
Fix:
Retest:
Final deliverable:
```

## Safe AI prompt: learn one task

> I am completing School 21 project [PROJECT], task [TASK] in an authorized lab. The exact requirement is: [PASTE REQUIREMENT]. My environment is: [VERSIONS/TOPOLOGY]. Explain the goal in simple language, then give one step at a time. For every command/action explain why, what success looks like, and how to verify it. Do not invent output, filenames, flags, packet values, source lines, or screenshots. Mark assumptions and wait for my real result before continuing.

## Safe AI prompt: troubleshoot

> I expected [EXPECTED], but observed [EXACT SYMPTOM]. Here are the relevant outputs: [PASTE SANITIZED OUTPUT]. Give a ranked list of hypotheses tied to the evidence. Start with the least disruptive check. Change only one variable at a time, explain why, and include a rollback. Do not claim success until I paste verification output.

## Safe AI prompt: review a deliverable

> Review this deliverable against the exact task requirements below. Build a checklist with requirement, evidence present, missing/incorrect item, and minimal correction. Verify exact filenames and distinguish observed evidence from assumptions. Do not rewrite real evidence or fabricate missing results.

## Safe AI prompt: prepare for peer review

> Quiz me on this completed task. Ask one question at a time about what I configured, why each command/action was used, what protocol/security principle is involved, how I verified it, what failed, and what I would change in production. Do not give the answer until I attempt it.

## Troubleshooting loop

1. Freeze the current state or take a snapshot.
2. State one exact symptom.
3. Collect the smallest useful output.
4. Compare expected versus observed.
5. Test one hypothesis.
6. Make one change.
7. Repeat the original verification.
8. Save both failed and successful evidence when it explains the fix.

## Before pushing to School 21 GitLab

```bash
git status --short
find src -maxdepth 3 -type f | sort
git diff --check
git add src
git commit -m "Complete project tasks"
git push -u origin develop
```

Review the file list before `git add`. Never commit Cisco/VM images, recovery keys, production/private credentials, licenses, unrelated captures, or personal data.

## Peer-review defense

For each deliverable, be ready to answer:

- What problem does it solve?
- What is the minimum concept/protocol behind it?
- What did you change?
- Why did you choose those values?
- What command, frame, log, or source line proves it?
- What failed and how did you isolate it?
- What is safe for a lab but unsafe in production?
- How would you reverse the change?
