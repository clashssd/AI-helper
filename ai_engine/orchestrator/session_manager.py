"""AI-helper/orchestrator/session_manager.py"""
import json
import os
import logging
from dataclasses import asdict
from .models import Session
#logger conf
logger = logging.getLogger(__name__)
#main class
class SessionManager:
    def __init__(self, save_dir="sessions"):
        self.save_dir = save_dir
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
    def save_session(self, session: Session):
        """Saves the session to a JSON file."""
        filepath = os.path.join(self.save_dir, f"session_{session.session_id}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            # asdict recursively converts a dataclass into a dictionary
            json.dump(asdict(session), f, ensure_ascii=False, indent=4)
        logger.info(f"Session {session.session_id} saved to {filepath}")
    def load_session(self, session_id: str) -> Session:
        """Loads a session from JSON."""
        filepath = os.path.join(self.save_dir, f"session_{session_id}.json")
        if not os.path.exists(filepath):
            logger.error(f"Session {session_id} not found.")
            return None
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        #Reconstructing objects from dictionaries
        from .models import Task, AgentState
        tasks = [Task(**t) for t in data.get("tasks", [])]
        agents = {k: AgentState(**v) for k, v in data.get("agents", {}).items()}
        session = Session(
            session_id=data["session_id"],
            main_goal=data["main_goal"],
            tasks=tasks,
            agents=agents,
            current_task_index=data["current_task_index"],
            status=data["status"]
        )
        logger.info(f"Session {session_id} loaded.")
        return session