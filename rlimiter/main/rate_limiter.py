from typing import List
from datetime import datetime, timedelta
from models import *
from data import ApiLimit, ClientRateLimitData
from rlimiter.main.lock_service import ClientLockService
from utils import convert_time

# def save_api_limit():

class RateLimitingService:
    def __init__(self, locks_container : ClientLockService):
        self.client_locks = locks_container

    def verify_api_limit(self, client_api_request : ClientApiRequest):
        try:
            with self.client_locks.acquire_lock(client_api_request.client_id):
                current_timestamp = int(datetime.timestamp(datetime.now()))

                applicable_api_limits = ApiLimit.get(
                    client_api_request.client_id,
                    str(client_api_request.method_name),
                    client_api_request.api_name
                )

                if not applicable_api_limits:
                    ApiLimit.addOne(client_api_request)
                    return Status.NO_LIMIT_APPLICABLE

                for client_api_limit in applicable_api_limits:
                    elapsed_time = current_timestamp - client_api_limit.last_request_timestamp

                    elapsed_time_units = convert_time(
                        elapsed_time, client_api_limit.time_unit
                    )

                    updated_available_permits = min(
                        client_api_limit.max_permits,
                        client_api_limit.available_permits + elapsed_time_units * client_api_limit.max_permits
                    )

                    if updated_available_permits < 1:
                        return Status.FAILURE

                    # Update Current Limit
                    updated_available_permits -= 1
                    client_api_limit.available_permits = updated_available_permits
                    client_api_limit.last_request_timestamp = current_timestamp

                    ApiLimit.save(client_api_limit)

                return Status.SUCCESS
        finally:
            self.client_locks.release_lock(client_api_request.client_id)