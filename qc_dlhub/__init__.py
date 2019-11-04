from .base_config import BASE_CONFIG
from .model_lookup import MODEL_LOOKUP

CONFIG = BASE_CONFIG
CONFIG["MODEL_METADATA"] = MODEL_LOOKUP

from .client import QcDlhubClient  # noqa: F401 (import unused)
