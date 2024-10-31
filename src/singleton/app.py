import threading


class AppContext:
    _instance = None
    _lock = threading.Lock()

    def __init__(self, config=None):
        if not config:
            raise ValueError("Configuration required.")
        self.config = config
        self.db_connection = None

    @classmethod
    def get_instance(cls, config=None):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = cls(config)
        return cls._instance

    def connect_db(self):
        self.db_connection = "DB Connected"
        print("Database connected.")

    def close_db(self):
        self.db_connection = None
        print("Database closed.")
