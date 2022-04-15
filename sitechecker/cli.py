"""This module implements the command line for for the site checker."""

import argparse

def read_user_cli_args():
    """Handle CLI args and options"""
    parser = argparse.ArgumentParser(
        prog="sitechecker",
        description="Check the connectivity of websites." 
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter one or more website URLs"
    )
    parser.add_argument(
        "-f",
        "--input_file",
        metavar="FILE",
        type=str,
        default="",
        help="reads URLs from a file"
    )
    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="run the connectivity check asynchronously",
    )
    return parser.parse_args()

def display_check_result(result, url, error=""):
    """Display the result of a connectivity check
    Args:
        result (bool): true = success, false = error
        url (string): url checked
        error (str, optional): the error returned. Defaults to "".
    """
    print(f'The status of "{url}" is: ', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline!" 👎 \n Error: "{error}"')
