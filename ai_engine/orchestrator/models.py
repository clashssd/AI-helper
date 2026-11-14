"""AI-helper/orchestrator/models.py"""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import uuid

@dataclass
class Task:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    description: str = ""
    status: str = "pending" # pending, in_progress, completed, failed
    result: Optional[str] = None
    assigned_to: Optional[str] = None

@dataclass
class AgentState:
    name: str
    system_prompt: str
    tools: List[Dict[str, Any]] = field(default_factory=list)
    #history for agent
    messages: List[Dict[str, Any]] = field(default_factory=list)

@dataclass
class Session:
    session_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    main_goal: str = ""
    tasks: List[Task] = field(default_factory=list)
    agents: Dict[str, AgentState] = field(default_factory=dict)
    current_task_index: int = 0
    status: str = "active" # active, finished, failed