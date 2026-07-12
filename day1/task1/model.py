from dataclasses import dataclass, field;

@dataclass
class User:
    id: int
    name: str
    age: int
    skills: list[str] = field(default_factory=list)