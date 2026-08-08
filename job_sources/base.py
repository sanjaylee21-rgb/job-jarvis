from abc import ABC, abstractmethod


class JobSource(ABC):
    @abstractmethod
    def search(self, keywords: list[str], location: str) -> list[dict]:
        raise NotImplementedError
