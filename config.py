"""
Configuration management for the trading engine.
Centralized configuration with type safety and validation.
"""
import os
from typing import Dict, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import logging

class TradingMode(Enum):
    """Trading operation modes"""
    BACKTEST = "backtest"
    PAPER = "paper"
    LIVE = "live"

class RiskLevel