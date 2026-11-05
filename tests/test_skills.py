from src.skills import detect_skills, evidence_for


def test_detects_skills_case_insensitively_and_in_catalog_order():
    assert detect_skills("Built APIs with python, SQL and Docker.") == [
        "Docker",
        "Python",
        "SQL",
    ]


def test_java_does_not_match_javascript():
    assert "Java" not in detect_skills("Built a JavaScript frontend.")
    assert "JavaScript" in detect_skills("Built a JavaScript frontend.")


def test_evidence_contains_the_matched_skill():
    assert "Python" in evidence_for("Projects: Python service", "Python")