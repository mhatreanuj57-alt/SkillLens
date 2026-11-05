# SkillLens

SkillLens compares skills named in a resume PDF with a pasted job description. It shows matched skills, missing skills, and the text evidence behind each result.

The score is the percentage of supported skills detected in the job description that also appear in the resume. It is a skill-overlap indicator only. SkillLens does not make hiring decisions or rank people; a human reviews every result.

## Run locally

Python 3.11 or newer is recommended.

    python -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    streamlit run app.py

## Privacy

PDFs are checked and read in memory. SkillLens does not write resumes or results to disk, log resume text, or call external services. Use the Delete uploaded data and results button to clear the upload widget and analysis from the current Streamlit session. Scanned PDFs without an embedded text layer are not processed; OCR is not included.

The app accepts PDFs up to 5 MB and extracts at most 100 pages. Only skills from the built-in vocabulary are detected, so results can miss skills outside that list. Review the evidence and make decisions independently.

## Tests

    python -m pytest

The PDF tests create synthetic files in memory; they do not use real resumes.

## Dependency note

PyMuPDF is distributed under AGPL-3.0 or a commercial license. Review its license terms before distributing a proprietary deployment.