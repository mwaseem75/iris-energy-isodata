from dataclasses import dataclass, field
from dataclasses_json import LetterCase, dataclass_json, config

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PostClass:
    title: str
    created_utc: float = field(metadata=config(field_name="created_utc"))
    fuel_mix: str = None
    demand: str = None
    supply: str = None