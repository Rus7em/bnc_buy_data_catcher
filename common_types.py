from dataclasses import dataclass


@dataclass
class Config:
    log_file: str = None
    request_time_delay: float = None
    db_ip: str = None
    db_port: int = None
    db_name: str = None
    db_collection: str = None




