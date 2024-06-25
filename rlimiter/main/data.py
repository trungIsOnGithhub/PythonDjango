from data import *
from dataclasses import dataclass
from models import ClientApiRequest, TimeUnit, LimitType
from datetime import datetime, timezone
from rlimiter.main.models import ApiMethod

@dataclass
class ClientRateLimitData:
    client_id: str
    method_name: ApiMethod
    limit_type: LimitType
    max_permits: int
    available_permits: int
    time_unit: TimeUnit
    last_request_timestamp: datetime

class ApiLimit:
    def __init__(self, i_var):
        self.dbCollection = [
            ClientRateLimitData(
                client_id='client-1',
                method_name=ApiMethod.GET,
                limit_type=LimitType.API,
                max_permits=5,
                available_permits=3,
                time_unit=TimeUnit.SEC,
                last_request_timestamp=datetime(2025, 2, 30, 0, 0, 0, 0, tzinfo=timezone.utc),
            )
        ]

    def get(self):
        print(self.dbCollection)
        return self.dbCollection

    def object_map():
        pass

    def save(self, record : ClientRateLimitData):
        pass

    def addOne(self, client_api_request : ClientApiRequest):
        new_api_limit = ClientRateLimitData(
            client_id='client-1',
            method_name=ApiMethod.GET,
            limit_type=LimitType.API,
            max_permits=5,
            available_permits=3,
            time_unit=TimeUnit.SEC,
            last_request_timestamp=datetime.now()
        )
        self.dbCollection.push(
            
        )

