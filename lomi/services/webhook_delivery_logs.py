from typing import List, Optional
from ..models import WebhookDeliveryLogs, WebhookDeliveryLogsCreate, WebhookDeliveryLogsUpdate
from ..client_base import ClientBase

class WebhookDeliveryLogsService(ClientBase):
    """webhook_delivery_logs API service"""
    
    
    def list(self, **params) -> List[WebhookDeliveryLogs]:
        """List webhook_delivery_logs"""
        return self._request("GET", "/webhook-delivery-logs", model=WebhookDeliveryLogs, params=params)
    
    
    def get(self, id: str) -> WebhookDeliveryLogs:
        """Get a single webhook_delivery_log"""
        return self._request("GET", f"/webhook-delivery-logs/{id}", model=WebhookDeliveryLogs)
    
    
    
    
