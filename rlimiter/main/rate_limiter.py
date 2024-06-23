from typing import List
from datetime import datetime, timedelta
from models import *
from data import ApiLimit, ClientRateLimitData

# def save_api_limit():

class RateLimitingService:
    def verify_api_limit(client_api_request : ClientApiRequest):
        try:
            with client_lock_service.acquire_lock(client_api_request.client_id):
                current_timestamp = datetime.now()

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

                    elapsed_time_units = time_unit_conversion_util.convert(
                        elapsed_time.total_seconds(), client_api_limit.time_unit
                    )

                    updated_available_permits = min(
                        client_api_limit.max_permits,
                        client_api_limit.available_permits + elapsed_time_units * client_api_limit.max_permits
                    )

                    if updated_available_permits > client_api_limit.available_permits:

                        return Status.FAILURE

                    # Update Current Limit
                    updated_available_permits -= 1
                    client_api_limit.available_permits = updated_available_permits
                    client_api_limit.last_request_timestamp = current_timestamp

                    ApiLimit.save(client_api_limit)

                return Status.SUCCESS
        finally:
            client_lock_service.release_lock(client_api_request.client_id)