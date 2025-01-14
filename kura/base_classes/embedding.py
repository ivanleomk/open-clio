from abc import ABC, abstractmethod
from asyncio import Semaphore


class BaseEmbeddingModel(ABC):
    @abstractmethod
    async def embed(self, text: str) -> list[float]:
        """Embed a single text into a list of floats"""
        pass