from typing import List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime, timedelta

class ApiMethod(Enum):
    GET = 0
    POST = 1

class LimitType(Enum):
    API = 0
    METHOD = 1
    DEFAULT = 2

class Status(Enum):
    SUCCESS = 0
    FAILURE = 1

class TimeUnit(Enum):
    SEC = 0
    MIN = 1
    HOUR = 2
    WEEK = 3
    MONTH = 4

class ClientIntervalRequestsLimit:
    TimeUnit timeUnit
    maxRequests: long

@dataclass
class Message:
    SUCCESS = "Success"
    FAILURE = "Failure"
    ADD_CLIENT_SUCCESS = "Client configured successfully"
    NO_LIMIT_APPLICABLE = "No limits applicable"

class ClientLimitsConfigRequest:
    limit_type: LimitType
    limit_name: str
    time_interval_limits: List[ClientIntervalRequestsLimit]
}

@dataclass
class ClientRateLimitData:
    client_id: str
    limit_name: str
    limit_type: str
    max_permits: int
    available_permits: int
    time_unit: str
    last_request_timestamp: datetime

@dataclass
class ClientApiRequest:
    client_id str
    method ApiMethod
    api_name str

def fetch_applicable_api_limits_in_order(client_id : str, method_name : str, api_name : str):
    return []

def save_api_limit():

def verify_api_limit(client_api_request : ClientApiRequest):
    try:
        with client_lock_service.acquire_lock(client_api_request.client_id):
            current_timestamp = datetime.now()

            applicable_api_limits = fetch_applicable_api_limits_in_order(
                client_api_request.client_id,
                str(client_api_request.method_name),
                client_api_request.api_name
            )

            if not applicable_api_limits:
                logger.info(f"No API limits found for ClientData-Id: {client_api_request.client_id}... returning")
                return (Status.SUCCESS, Message.NO_LIMIT_APPLICABLE)

            for client_api_limit in applicable_api_limits:
                elapsed_time = current_timestamp - client_api_limit.last_request_timestamp

                elapsed_time_units = time_unit_conversion_util.convert(
                    elapsed_time.total_seconds(), client_api_limit.time_unit
                )

                updated_available_permits = min(
                    client_api_limit.max_permits,
                    client_api_limit.available_permits + elapsed_time_units * client_api_limit.max_permits
                )

                if updated_available_permits < 1:
                    logger.warn(
                        f"API rate limit reached for ClientData-Id: {client_api_limit.client_id}, "
                        f"availablePermits: {client_api_limit.available_permits}, "
                        f"maxPermits: {client_api_limit.max_permits}, "
                        f"limitType: {client_api_limit.limit_type}, "
                        f"timeUnit: {client_api_limit.time_unit}"
                    )
                    return (
                        Status.FAILURE,
                        f"Limit: {client_api_limit.limit_name}, limitType: {client_api_limit.limit_type}, "
                        f"timeUnit: {client_api_limit.time_unit} breached for the client"
                    )

                # request went through
                logger.info(
                    f"API rate limit passed for ClientData-Id: {client_api_limit.client_id}, "
                    f"availablePermits: {client_api_limit.available_permits}, "
                    f"maxPermits: {client_api_limit.max_permits}, "
                    f"limitType: {client_api_limit.limit_type}, "
                    f"timeUnit: {client_api_limit.time_unit}"
                )

                # decrease the no. of available permits by 1 for current request
                updated_available_permits -= 1
                client_api_limit.available_permits = updated_available_permits
                client_api_limit.last_request_timestamp = current_timestamp

                save_api_limit(applicable_api_limits)

            return (Status.SUCCESS, Message.SUCCESS)
    finally:
        client_lock_service.release_lock(client_api_request.client_id)