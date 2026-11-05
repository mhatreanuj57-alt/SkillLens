import re

# shortcut: fixed vocabulary misses unlisted skills; expand it when the MVP needs broader coverage.
SKILL_ALIASES = {
    "Agile": ("agile",),
    "AWS": ("aws", "amazon web services"),
    "Azure": ("azure", "microsoft azure"),
    "C": ("c",),
    "C++": ("c++",),
    "C#": ("c#", "c sharp"),
    "CSS": ("css",),
    "Data analysis": ("data analysis", "data analytics"),
    "Django": ("django",),
    "Docker": ("docker",),
    "Excel": ("excel", "microsoft excel"),
    "FastAPI": ("fastapi",),
    "Flask": ("flask",),
    "Git": ("git",),
    "Google Cloud": ("google cloud", "gcp"),
    "HTML": ("html",),
    "Java": ("java",),
    "JavaScript": ("javascript", "js"),
    "Kubernetes": ("kubernetes", "k8s"),
    "Linux": ("linux",),
    "Machine learning": ("machine learning",),
    "Node.js": ("node.js", "nodejs"),
    "Power BI": ("power bi",),
    "PostgreSQL": ("postgresql", "postgres"),
    "Python": ("python",),
    "React": ("react", "react.js", "reactjs"),
    "REST APIs": ("rest api", "restful api"),
    "Scrum": ("scrum",),
    "SQL": ("sql", "mysql", "sqlite"),
    "Tableau": ("tableau",),
    "TensorFlow": ("tensorflow",),
    "Terraform": ("terraform",),
    "TypeScript": ("typescript",),
}

_PATTERNS = {
    skill: tuple(
        re.compile(rf"(?<!\w){re.escape(alias)}(?!\w)", re.IGNORECASE)
        for alias in aliases
    )
    for skill, aliases in SKILL_ALIASES.items()
}


def evidence_for(text: str, skill: str) -> str | None:
    for pattern in _PATTERNS[skill]:
        match = pattern.search(text)
        if match:
            start = max(0, match.start() - 55)
            end = min(len(text), match.end() + 75)
            excerpt = " ".join(text[start:end].split())
            return f"...{excerpt}..." if start or end < len(text) else excerpt
    return None


def detect_skills(text: str) -> list[str]:
    return [skill for skill in SKILL_ALIASES if evidence_for(text, skill) is not None]