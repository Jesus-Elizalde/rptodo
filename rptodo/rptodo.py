"""This module provides the RP To-Do model-controller"""
# retodo/rptodo.py

from typing import Any, Dict, NamedTuple

class CurrentTodo(NamedTuple):
    todo: Dict[str,Any]
    error: int