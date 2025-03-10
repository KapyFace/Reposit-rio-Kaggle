from abc import ABC, abstractmethod

class IDataRepository(ABC):
    
    
    @abstractmethod
    def download_data(self):
        pass

    @abstractmethod
    def load_data(self, file_name):
        pass