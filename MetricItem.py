from dataclasses import dataclass

@dataclass
class MetricItem:
    _id: str
    label: str
    score: float
    kind: str

    def __init__(self, _id: str, label: str, score: float, kind: str='checkbox') -> None:
        self._id = _id
        self.label = label
        self.score = score
        self.kind= kind
        