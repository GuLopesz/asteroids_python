from abc import ABC, abstractmethod

class Obj(ABC):
    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass