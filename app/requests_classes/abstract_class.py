from abc import ABC, abstractmethod


class Servises(ABC):
    """Абстрактный метод-шаблон для запросов"""
    @abstractmethod
    def get_data(self):
        pass
