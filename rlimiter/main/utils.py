import logging

def log_when_limit_reached():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.warning(f'''
        API rate limit reached - ClientDataId: {client_api_limit.client_id}-
        availablePermits: {client_api_limit.available_permits}-
        maxPermits: {client_api_limit.max_permits}-
        limitType: {client_api_limit.limit_type}-
        timeUnit: {client_api_limit.time_unit}-
    ''')

def log_when_request_passed():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.info(
        f'''API rate limit passed - ClientDataId: {client_api_limit.client_id}-
        availablePermits: {client_api_limit.available_permits}-
        maxPermits: {client_api_limit.max_permits}-
        limitType: {client_api_limit.limit_type}-
        timeUnit: {client_api_limit.time_unit}'''
    )