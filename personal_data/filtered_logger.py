#!/usr/bin/env python3
from re import sub


def filter_datum(fields: list[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns the log message with certain parts obfuscated.
    :param fields: List of strings representing all fields to obfuscate
    :param redaction: String representing by what the field will be obfuscated
    :param message: The log line
    :param separator: Which character is separating all fields in the log line
    :return: Obfuscated log message
    """
    return sub(rf'({"|".join(fields)})=.*?{separator}',
               lambda m: f"{m.group(1)}={redaction}{separator}",
               message)
