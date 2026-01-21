"""
Core domain concepts for hierarchical text classification.

This module contains the fundamental building blocks that don't depend on
specific infrastructure or capability implementations.
"""

from .policies import (
    AcceptancePolicy,
    AnyPolicy,
    CompositePolicy,
    ConfidenceThresholdPolicy,
    DefaultPolicy,
    ExcerptRequiredPolicy,
    KeywordInReasoningPolicy,
    MinimumReasoningLengthPolicy,
)

__all__ = [
    # Acceptance policies
    "AcceptancePolicy",
    "DefaultPolicy",
    "ConfidenceThresholdPolicy",
    "KeywordInReasoningPolicy",
    "ExcerptRequiredPolicy",
    "MinimumReasoningLengthPolicy",
    "CompositePolicy",
    "AnyPolicy",
]
