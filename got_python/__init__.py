"""
got_python package
A small package to collect Python code for the Game_of_thrones repository.
"""

__all__ = ["characters", "utils"]

__version__ = "0.1.0"

# Optional: keep package import lightweight. Individual modules can be added
# under got_python/ (for example: characters.py, utils.py, etc.)
try:
    # Expose commonly-used helpers if present
    from . import characters  # noqa: F401
    from . import utils       # noqa: F401
except Exception:
    # Modules may not exist yet; importing here is optional
    pass
