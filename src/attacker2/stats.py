"""
Statistics that can be computed from the logs.
"""

def number_timeouts(logs : str) -> int:
    return logs.count("timeout")

def number_responses(logs: str) -> int:
    return logs.count("response")

def exec_time(logs : str):
    rows = logs.split("\n")
    rows[0]
    rows[1]
    # TODO: finish this