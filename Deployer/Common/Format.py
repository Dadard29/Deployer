def format_response(msg, payload):
    return dict(status='ok', message=msg, content=payload)


def format_error(msg):
    return dict(status='ko', message=msg, content={})
