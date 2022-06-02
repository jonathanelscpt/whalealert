import ast


def handle_error_response(response):
    """
    Translate requests.exceptions.HTTPError responses to WhaleAlertAPIException
    :param response:
    :return:
    """
    resp_dict = ast.literal_eval(response.text)
    message = resp_dict['message']
    reason = response.reason
    status_code = response.status_code
    result = resp_dict['result']
    raise WhaleAlertAPIException(message=message, status_code=status_code, response=response, reason=reason,
                                 result=result)


class WhaleAlertAPIException(Exception):
    """
    Wrapper for requests.exceptions.HTTPError
    """

    def __init__(self, message=None, status_code=None, response=None, reason=None, result=None):
        self.response = response
        if message:
            self.message = message or "An unknown error occurred"
        if status_code:
            self.status_code = status_code
        if reason:
            self.reason = reason
        if result:
            self.result = result

    def __str__(self):
        if self.status_code:
            return f'HTTP {self.status_code} {self.reason}: {self.message}'
        return self.message
