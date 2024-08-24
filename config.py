class Config:
    storage_path: str

    def __init__(self, storage_path='data.csv'):
        self.storage_path = storage_path
