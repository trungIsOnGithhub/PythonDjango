from dataclasses import dataclass
from enum import Enum
from typing import List

class ApiMethod(Enum):
    GET = 0
    POST = 1
    PUT = 2
    DELETE = 3

class LimitType(Enum):
    API = 0
    METHOD = 1
    DEFAULT = 2

class Status(Enum):
    SUCCESS = 0
    FAILURE = 1
    NO_LIMIT_APPLICABLE = 2

class TimeUnit(Enum):
    SEC = 0
    MIN = 1
    HOUR = 2

class Message(Enum):
    SUCCESS = "Success"
    FAILURE = "Failure"
    ADD_CLIENT_SUCCESS = "Client configured successfully"
    NO_LIMIT_APPLICABLE = "No limits applicable"


@dataclass
class ClientIntervalRequestsLimit:
    timeUnit: TimeUnit
    maxRequests: int

@dataclass
class ClientLimitsConfigRequest:
    limit_type: LimitType
    limit_name: str
    time_interval_limits: List[ClientIntervalRequestsLimit]

@dataclass
class ClientApiRequest:
    client_id: str
    method: ApiMethod
    api_name: str