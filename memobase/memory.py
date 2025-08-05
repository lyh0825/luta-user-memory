"""
User memory functionality.
"""

from typing import Dict, List, Optional
import json
from datetime import datetime

class UserMemory:
    """
    User memory management class.
    """
    
    def __init__(self, user_id: Optional[str] = None):
        """Initialize user memory."""
        self.user_id = user_id
        self.memories: Dict = {}
    
    def add_memory(self, key: str, value: str, metadata: Optional[Dict] = None) -> None:
        """Add a memory entry."""
        self.memories[key] = {
            "value": value,
            "metadata": metadata or {},
            "timestamp": datetime.now().isoformat()
        }
    
    def get_memory(self, key: str) -> Optional[Dict]:
        """Get a memory entry by key."""
        return self.memories.get(key)
    
    def search_memories(self, query: str) -> List[Dict]:
        """Search memories by query."""
        results = []
        query_lower = query.lower()
        
        for key, memory in self.memories.items():
            if query_lower in key.lower() or query_lower in memory["value"].lower():
                results.append({
                    "key": key,
                    **memory
                })
        
        return results
    
    def delete_memory(self, key: str) -> bool:
        """Delete a memory entry."""
        if key in self.memories:
            del self.memories[key]
            return True
        return False
    
    def export_memories(self) -> str:
        """Export memories as JSON string."""
        return json.dumps(self.memories, indent=2, ensure_ascii=False)
    
    def import_memories(self, data: str) -> None:
        """Import memories from JSON string."""
        self.memories = json.loads(data)