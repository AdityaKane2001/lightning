"""Root package info."""
import logging
import os

from lightning_utilities import module_available

if os.path.isfile(os.path.join(os.path.dirname(__file__), "__about__.py")):
    from lightning.fabric.__about__ import *  # noqa: F401, F403
if os.path.isfile(os.path.join(os.path.dirname(__file__), "__version__.py")):
    from lightning.fabric.__version__ import version as __version__
elif module_available("lightning"):
    from lightning import __version__  # type: ignore[misc] # noqa: F401

_root_logger = logging.getLogger()
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)

if not _root_logger.hasHandlers():
    _logger.addHandler(logging.StreamHandler())
    _logger.propagate = False


# In PyTorch 2.0+, setting this variable will force `torch.cuda.is_available()` and `torch.cuda.device_count()`
# to use an NVML-based implementation that doesn't poison forks.
# https://github.com/pytorch/pytorch/issues/83973
os.environ["PYTORCH_NVML_BASED_CUDA_CHECK"] = "1"


from lightning.fabric.fabric import Fabric  # noqa: E402
from lightning.fabric.utilities.seed import seed_everything  # noqa: E402

__all__ = ["Fabric", "seed_everything"]

# for compatibility with namespace packages
__import__("pkg_resources").declare_namespace(__name__)
