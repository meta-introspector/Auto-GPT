"""
Memory tool for document search
"""
from typing import List

import os
from ..forge_log import ForgeLogger
from .registry import ability

from forge.sdk.memory.memstore import ChromaMemStore

logger = ForgeLogger(__name__)

@ability(
    name="mem_search",
    description="Search documents stored in memory",
    parameters=[
        {
            "name": "query",
            "description": "search query",
            "type": "string",
            "required": True,
        }
    ],
    output_type="list[str]",
)
async def mem_search(agent, task_id: str, query: str) -> List[str]:
    mem_docs = []

    try:
        chromadb_path = f"{os.getenv('AGENT_WORKSPACE')}/{task_id}"

        memory = ChromaMemStore(chromadb_path)
        memory_resp = memory.query(
            task_id=task_id,
            query=query
        )

        mem_docs = memory_resp["documents"][0]
    except Exception as err:
        logger.error(f"mem_search filed: {err}")

    return mem_docs

