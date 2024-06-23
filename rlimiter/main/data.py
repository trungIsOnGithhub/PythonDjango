from data import *
from datetime import datetime, timezone
from model import TimeUnit, LimitType

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
    dbCollection = [
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
    DEFAULT_MAX_PERMIT = 5
    DEFAULT_TIME_UNIT = TimeUnit.SEC

    def get(client_id : str, method_name : str, api_name : str):
        print(dbCollection)
        return dbCollection

    def object_map():
        pass

    def save(record : ClientRateLimitData):
        pass

    def addOne(client_api_request : ClientApiRequest):
        dbCollection.push(
            ClientRateLimitData(
                client_id='client-1',
                method_name=ApiMethod.GET,
                limit_type=LimitType.API,
                max_permits=5,
                available_permits=3,
                time_unit=TimeUnit.SEC,
                last_request_timestamp=datetime(2025, 2, 30, 0, 0, 0, 0, tzinfo=timezone.utc),
            )
        )

