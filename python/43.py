import configparser
import os

class Config:
    def __init__(self, filename="db.ini"):
        self.filename = filename
        self.config = configparser.ConfigParser()

class DatabaseConfig(Config):
    def load(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                f.write("[database]\nhost = localhost\nport = 5432")
                
        self.config.read(self.filename)
        if 'database' in self.config:
            db_config = self.config['database']
            host = db_config.get('host', 'unknown')
            port = db_config.get('port', 'unknown')
            print(f"DB Host: {host}, Port: {port}")
        else:
            print("Missing database section")

db_config = DatabaseConfig()
db_config.load()
