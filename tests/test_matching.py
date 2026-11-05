import pytest

from src.matching import match_resume_to_job


def test_score_and_evidence_explain_overlap():
    result = match_resume_to_job(
        "Projects: Python API using Docker.",
        "Role requires Python and AWS.",
    )

    assert result["score"] == 50
    assert [item["skill"] for item in result["matched"]] == ["Python"]
    assert [item["skill"] for item in result["missing"]] == ["AWS"]
    assert "Python" in result["matched"][0]["resume_evidence"]
    assert "AWS" in result["missing"][0]["job_evidence"]


def test_requires_supported_job_skills():
    with pytest.raises(ValueError, match="No supported skills"):
        match_resume_to_job("Python", "Looking for a curious team player.")