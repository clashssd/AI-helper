"""AI-helper/ai_engine/orchestrator/core/agent_graph.py"""
import asyncio
import uuid
import logging
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
logger = logging.getLogger(__name__)
@dataclass
class AgentNode:
    agent_id: str
    name: str
    parent_id: Optional[str]
    status: str = "running"
    inbox: asyncio.Queue = field(default_factory=asyncio.Queue)
    task: Optional[str] = None
    result: Optional[str] = None
    children: List[str] = field(default_factory=list)
    history: List[Dict[str, Any]] = field(default_factory=list)

class AgentCoordinator:
    def __init__(self):
        self.agents: Dict[str, AgentNode] = {}
        self.root_id: Optional[str] = None
        self.lock = asyncio.Lock()

    def create_agent(self, name: str, parent_id: Optional[str] = None) -> AgentNode:
        agent_id = str(uuid.uuid4())[:8]
        node = AgentNode(agent_id=agent_id, name=name, parent_id=parent_id)
        self.agents[agent_id] = node
        if parent_id:
            self.agents[parent_id].children.append(agent_id)
        else:
            self.root_id = agent_id
        logger.info(f"[Coordinator] Created agent {name} ({agent_id}) with parent {parent_id}")
        return node

    def get_agent(self, agent_id: str) -> Optional[AgentNode]:
        return self.agents.get(agent_id)

    def update_status(self, agent_id: str, status: str):
        if agent_id in self.agents:
            self.agents[agent_id].status = status

    async def send_message(self, target_id: str, message: dict):
        if target_id in self.agents:
            await self.agents[target_id].inbox.put(message)
            logger.info(f"[Coordinator] Sent message to {target_id}: {message.get('type')}")

    def get_tree_snapshot(self) -> dict:
        return {
            aid: {"name": a.name, "status": a.status, "parent": a.parent_id, "children": a.children}
            for aid, a in self.agents.items()
        }