"""
Hierarchical Text Classification Package
"""

from .capabilities import (
    BFSClassificationCapability,
    BundledClassificationCapability,
    CapabilityRegistry,
    ClassificationCapability,
    create_default_registry,
)
from .capabilities.classification import (
    BatchClassificationResult,
    ClassificationOutput,
    SingleClassificationResult,
)
from .orchestration import CapabilityOrchestrator
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
from .utils import (
    NodeConfig,
    build_tree_from_paths,
    format_tree_as_string,
    get_all_leaf_paths,
    get_node_path,
    load_topic_hierarchy,
    validate_hierarchy,
)

__version__ = "1.0.0"

__all__ = [
    # Models
    "SingleClassificationResult",
    "ClassificationOutput",
    "NodeConfig",
    "BatchClassificationResult",
    # Policies
    "AcceptancePolicy",
    "DefaultPolicy",
    "ConfidenceThresholdPolicy",
    "KeywordInReasoningPolicy",
    "ExcerptRequiredPolicy",
    "MinimumReasoningLengthPolicy",
    "CompositePolicy",
    "AnyPolicy",
    # Schema Tools
    "load_topic_hierarchy",
    "get_node_path",
    "get_all_leaf_paths",
    "build_tree_from_paths",
    "format_tree_as_string",
    "validate_hierarchy",
    # Classification
    "ClassificationCapability",
    "BFSClassificationCapability",
    "BundledClassificationCapability",
    # Orchestration
    "CapabilityOrchestrator",
    # Registry
    "CapabilityRegistry",
    "create_default_registry",
]
