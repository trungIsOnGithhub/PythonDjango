import logging

from rlimiter.main.models import TimeUnit

def log_when_limit_reached():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.warning(f'''
        API rate limit reached - ClientDataId: {client_api_limit.client_id}-
        availablePermits: {client_api_limit.available_permits}-
        maxPermits: {client_api_limit.max_permits}-
        limitType: {client_api_limit.limit_type}-
        timeUnit: {client_api_limit.time_unit}-
    ''')

def log_when_request_passed(client_api_limit):
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.info(
        f'''API rate limit passed - ClientDataId: {client_api_limit.client_id}-
        availablePermits: {client_api_limit.available_permits}-
        maxPermits: {client_api_limit.max_permits}-
        limitType: {client_api_limit.limit_type}-
        timeUnit: {client_api_limit.time_unit}'''
    )

def convert_time(milliseconds: int, time_unit: TimeUnit):
    if time_unit is None:
        raise ValueError("Invalid timeUnit supplied for conversion")

    if time_unit == TimeUnit.SEC:
        return milliseconds / 1000.0
    elif time_unit == TimeUnit.MIN:
        return milliseconds / (60 * 1000.0)
    elif time_unit == TimeUnit.HOUR:
        return milliseconds / (3600 * 1000.0)
    else:
        return -1