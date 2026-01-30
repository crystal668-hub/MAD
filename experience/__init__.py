"""
经验模块初始化文件
"""

from experience.experience_store import ExperienceStore

# ExperienceExtractor depends on optional multi-agent frameworks (e.g. autogen).
# Keep the package importable even when those dependencies are not installed.
try:
    from experience.experience_extractor import ExperienceExtractor
except Exception:  # pragma: no cover
    ExperienceExtractor = None  # type: ignore

__all__ = ['ExperienceStore', 'ExperienceExtractor']
