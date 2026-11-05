# SkillLens security and privacy

## Data handling

- Accept only files with a PDF signature; reject uploads over 5 MB.
- Read PDFs in memory and cap extraction at 100 pages.
- Reject encrypted, unreadable, and scanned PDFs without selectable text.
- Do not log, persist, or send resume or job-description text to external services.
- Do not place real resumes in Git, tests, screenshots, or demos.
- The delete action clears the current upload widget and result from Streamlit session state.

## Application controls

- Render evidence with Streamlit text elements; never mark user content as trusted HTML.
- Keep direct dependencies pinned and review updates regularly.
- Do not store secrets in source control.
- A deployed service needs HTTPS, upload rate limits, and an appropriate privacy notice.

## Fair-use boundary

SkillLens is not an automated employment decision tool. It does not shortlist, reject, or rank people. It only checks a fixed vocabulary of job-related skills and does not intentionally extract protected or unrelated personal attributes. Human review is required.