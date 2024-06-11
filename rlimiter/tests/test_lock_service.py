from rlimiter.main.lock_service import *

class TestDataSource(ClientDataSource):
    def find_all(self) -> list[ClientData]:
        return [ ClientData(client_id='client-1'), ClienData(client_id='client-2'), ClientData('client-3') ] # temporarily hard coded data

def test_lock_service():
    data_source = TestDataSource()
    lock_service = ClientLockService(data_source=data_source)

    