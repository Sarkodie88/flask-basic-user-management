"""
    Defines the various responses to be passed across.
    The necessay response codes should be seen here.

    200 - response for success
    201 - response for created
    202 - response for accepted
    400 - response for failure
    422 - response for validation error
"""

def success(msg="Operation Successful", metadata=None, data=None):
    """ response for success """
    response_payload = {"response_code": 200, "response_message": msg}
    if data:
        response_payload["data"] = data
    if metadata:
        response_payload["metadata"] = metadata

    return response_payload


def created(msg="Creation Successful", metadata=None, data=None):
    """ response for success """
    response_payload = {"response_code": 201, "response_message": msg}
    if data:
        response_payload["data"] = data
    if metadata:
        response_payload["metadata"] = metadata

    return response_payload


def accepted(msg="Operation Successful", metadata=None, data=None):
    """ response for accepted """
    response_payload = {"response_code": 202, "response_message": msg}
    if data:
        response_payload["data"] = data
    if metadata:
        response_payload["metadata"] = metadata
        
    return response_payload


def failure(msg="Operation failed", metadata=None, data=None):
    """ response for failure """
    response_payload = {"response_code": 400, "response_message": msg}
    if data:
        response_payload["data"] = data
    if metadata:
        response_payload["metadata"] = metadata
        
    return response_payload


def not_found(msg="Not Found", metadata=None, data=None):
    """ response for not_found """
    response_payload = {"response_code": 404, "response_message": msg}
    if data:
        response_payload["data"] = data
    if metadata:
        response_payload["metadata"] = metadata
        
    return response_payload
    

def no_content(msg="Not Found", metadata=None, data=None):
    """ response for not_found """
    response_payload = {"response_code": 404, "response_message": msg}
    if data:
        response_payload["data"] = data
    if metadata:
        response_payload["metadata"] = metadata
        
    return response_payload


def unauthorised(msg="Not Found", metadata=None, data=None):
    """ response for not_found """
    response_payload = {"response_code": 404, "response_message": msg}
    if data:
        response_payload["data"] = data
    if metadata:
        response_payload["metadata"] = metadata
        
    return response_payload