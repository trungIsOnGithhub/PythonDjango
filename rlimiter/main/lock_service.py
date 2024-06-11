import logging
from typing import Dict
from threading import Lock
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class ClientData:
    client_id: str

class ClientDataSource(ABC):
    @abstractmethod
    def find_all(self) -> list[ClientData]:
        

class ClientLockService:
    def __init__(self, data_source: ClientDataSource):
        self.data_source = data_source
        self.client_locks: Dict[str, Lock] = {}

        self.initialize_client_locks()

    def initialize_client_locks(self):
        configured_clients = self.data_source.find_all()
        self.client_locks = { client.client_id: Lock() for client in configured_clients }

    def add_client(self, client_id: str):
        try:
            self.client_locks[client_id] = Lock()
        except:
            logging.error(f"Cannot create Lock for client id: {client_id}")

    def acquire_lock(self, client_id: str):
        client_lock = self.get_and_validate_client_lock(client_id)
        client_lock.acquire()

    def release_lock(self, client_id: str):
        client_lock = self.get_and_validate_client_lock(client_id)
        client_lock.release()

    def get_and_validate_client_lock(self, client_id: str) -> Lock:
        if client_id not in self.client_locks:
            logging.error(f"Access non-exist ClientId: {client_id}...")
            raise ValueError("Invalid client-id")

        client_lock = self.client_locks.get(client_id, None)

        if client_lock is None:
            logging.error(f"Access non-exist ClientId: {client_id}...")
            raise ValueError("Invalid client-id")

        return client_lock