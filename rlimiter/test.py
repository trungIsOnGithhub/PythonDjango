
# from tests.test_lock_service import test_lock_service

# if __name__ == '__main__':
#     test_lock_service()

from main.lock_service import *
# import unittest

class TestDataSource(ClientDataSource):
    def find_all(self) -> list[ClientData]:
        return [ ClientData(client_id='client-1'), ClientData(client_id='client-2'), ClientData('client-3') ] # temporarily hard coded data

# class TestLockService(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         self.data_source = TestDataSource()
#         self.lock_service = ClientLockService(data_source=data_source)

#     def test_
if __name__ == '__main__':
    data_src = TestDataSource()
    lock_service = ClientLockService(data_source=data_src)

    lock_service.initialize_client_locks()
    lock_service.add_client('client-69')

    print(lock_service.get_and_validate_lock('client-1'))
    print(lock_service.get_and_validate_ lock('client-69'))