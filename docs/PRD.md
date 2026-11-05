# SkillLens product requirements

## Purpose

Compare skills named in a resume with skills requested in a job description. The app is a human-review aid and does not make hiring, rejection, shortlist, or ranking decisions.

## MVP

- Accept a PDF resume and pasted job description.
- Extract selectable PDF text and detect skills from a fixed vocabulary.
- Show matched skills, missing skills, supporting text, and an explainable overlap score.
- Allow the user to delete the upload and current results in one action.
- Process data locally in memory; do not persist it or send it to external services.

## Fair use

Matching uses only job-related skill terms. It must not use name, photo, age, gender, address, caste, religion, or college prestige. Humans make all hiring decisions.

## Success criteria

- A valid text PDF under the size and page limits can be analyzed locally.
- Each shown match or gap includes evidence from the resume or job description.
- The user can clear the upload and results with one action.