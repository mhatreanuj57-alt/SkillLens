from src.skills import detect_skills, evidence_for


def match_resume_to_job(resume_text: str, job_description: str) -> dict:
    requested = detect_skills(job_description)
    if not requested:
        raise ValueError(
            "No supported skills were identified in the job description. "
            "Try a description that names skills from the current vocabulary."
        )

    matched = []
    missing = []
    for skill in requested:
        job_evidence = evidence_for(job_description, skill)
        resume_evidence = evidence_for(resume_text, skill)
        if resume_evidence is None:
            missing.append({"skill": skill, "job_evidence": job_evidence})
        else:
            matched.append(
                {
                    "skill": skill,
                    "resume_evidence": resume_evidence,
                    "job_evidence": job_evidence,
                }
            )

    return {
        "score": round(100 * len(matched) / len(requested)),
        "matched_count": len(matched),
        "requested_count": len(requested),
        "matched": matched,
        "missing": missing,
    }