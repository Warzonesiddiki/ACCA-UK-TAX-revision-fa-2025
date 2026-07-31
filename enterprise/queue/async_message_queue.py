"""
ASYNC MESSAGE QUEUE — Enterprise Distribution Layer
Simulated with file-based persistent queue (zero external dependency, fully decoupled)
Supports multi-region message replay and dead-letter handling.
"""
import os, json, time, uuid
from typing import Optional

class AsyncMessageQueue:
    def __init__(self, queue_path="enterprise/queue/persisted.q"):
        self.path = queue_path
        os.makedirs(os.path.dirname(queue_path) or ".", exist_ok=True)
        self.queue = []
        self.dead_letter = []
    def enqueue(self, payload: dict, region: str = "global") -> str:
        msg = {"id": str(uuid.uuid4()), "region": region, "payload": payload, "ts": time.time()}
        self.queue.append(msg)
        self._persist()
        return msg["id"]
    def dequeue(self, region_filter: Optional[str] = None) -> Optional[dict]:
        for i, msg in enumerate(self.queue):
            if region_filter is None or msg.get("region") == region_filter:
                self.queue.pop(i)
                self._persist()
                return msg
        return None
    def replay_dead_letter(self, msg_id: str) -> bool:
        for msg in self.dead_letter:
            if msg["id"] == msg_id:
                self.enqueue(msg["payload"], msg.get("region", "global"))
                return True
        return False
    def _persist(self):
        with open(self.path, 'w') as f:
            json.dump({"queue": self.queue, "dead_letter": self.dead_letter}, f)
