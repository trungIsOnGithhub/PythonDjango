import logging
from typing import Dict
from threading import Lock
from dataclasses import dataclass

@dataclass
class ClientData:
    client_id: str

class ClientDataSource:
    def find_all(self) -> list[ClientData]:
        return [ClientData(client_id='client-1'), ClienData(client_id='client-2'), ClientData('client-3')] # temporarily hard coded data

class ClientLockService:
    def __init__(self, data_source: ClientDataSource):
        self.data_source = data_source
        self.client_locks: Dict[str, Lock] = {}

        self.initialize_client_locks()

    def initialize_client_locks(self):
        configured_clients = self.data_source.find_all()
        self.client_locks = {client.client_id: Lock() for client in configured_clients}

    def add_client(self, client_id: str):
        self.client_locks[client_id] = Lock()

    def acquire_lock(self, client_id: str):
        client_lock = self.get_and_validate_client_lock(client_id)
        client_lock.acquire()

    def release_lock(self, client_id: str):
        client_lock = self.get_and_validate_client_lock(client_id)
        client_lock.release()

    def get_and_validate_client_lock(self, client_id: str) -> Lock:
        client_lock = self.client_locks.get(client_id)
        if client_lock is None:
            logging.error(f"Lock doesn't exist for ClientData-Id: {client_id}... Invalid client?")
            raise ValueError("Invalid client-id")
        return client_lock

