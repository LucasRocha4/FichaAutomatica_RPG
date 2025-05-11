import logging

class SafeRequestFormatter(logging.Formatter):
    def format(self, record):
        if not hasattr(record, 'request_id'):
            record.request_id = '--------'
        if not hasattr(record, 'view'):
            record.view = '--------'
        return super().format(record)
