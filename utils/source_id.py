"""
Source ID utilities.

We use stable, verifiable identifiers for evidence citations returned from the local
Chroma-backed RAG database.

Canonical format (one chunk = one evidence item):
  rag:chroma/<collection>/doi:<doc_id>#chunk:<chunk_id>
Where:
  - collection: Chroma collection name
  - doc_id: DOI string stored in metadata (e.g. "10.1021/....") or "unknown"
  - chunk_id: integer chunk index within the document
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional


_CHROMA_SOURCE_ID_RE = re.compile(
    r"^rag:chroma/(?P<collection>[^/]+)/doi:(?P<doc_id>[^#]+)#chunk:(?P<chunk_id>\d+)$"
)


@dataclass(frozen=True)
class ChromaSourceRef:
    collection: str
    doc_id: str
    chunk_id: int

    def to_source_id(self) -> str:
        return build_chroma_source_id(self.collection, self.doc_id, self.chunk_id)


def build_chroma_source_id(collection: str, doc_id: str, chunk_id: int) -> str:
    collection = (collection or "unknown").strip()
    doc_id = (doc_id or "unknown").strip()
    return f"rag:chroma/{collection}/doi:{doc_id}#chunk:{int(chunk_id)}"


def parse_chroma_source_id(source_id: str) -> Optional[ChromaSourceRef]:
    if not source_id:
        return None
    match = _CHROMA_SOURCE_ID_RE.match(source_id.strip())
    if not match:
        return None
    return ChromaSourceRef(
        collection=match.group("collection"),
        doc_id=match.group("doc_id"),
        chunk_id=int(match.group("chunk_id")),
    )


def is_valid_chroma_source_id(source_id: str) -> bool:
    return parse_chroma_source_id(source_id) is not None

