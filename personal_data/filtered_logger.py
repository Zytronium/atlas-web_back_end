#!/usr/bin/env python3
"""
Filtered logger
"""

import re
from typing import List
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "ssn", "password", "phone")


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filter out certain fields from incoming log records
        :param record: Log message to filter
        :return: Filtered log message
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)

        return super().format(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns the log message with certain parts obfuscated.
    :param fields: List of strings representing all fields to obfuscate
    :param redaction: String representing by what the field will be obfuscated
    :param message: The log line
    :param separator: Which character is separating all fields in the log line
    :return: Obfuscated log message
    """
    return re.sub(rf'({"|".join(fields)})=.*?{separator}',
                  lambda m: f"{m.group(1)}={redaction}{separator}",
                  message)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger for user data
    :return: A new logger for user date
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=list(PII_FIELDS)))
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Creates and returns a MySQL connection to a database
    :return: A MySQL connection
    """
    DB_USERNAME = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    DB_PASSWORD = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    DB_HOST = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    DB_NAME = os.getenv("PERSONAL_DATA_DB_NAME", "my_db")
    return mysql.connector.connect(
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME,
    )


def main():
    """
    Main function
    """
    db_connection = get_db()
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    logger = get_logger()

    for row in cursor:
        msg = "; ".join([f"{key}={value}" for key, value in row.items()]) + ";"
        logger.info(msg)

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
