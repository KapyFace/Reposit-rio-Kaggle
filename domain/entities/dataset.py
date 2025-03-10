class Dataset:
    
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def get_summary(self):
        
        return self.data.describe()
