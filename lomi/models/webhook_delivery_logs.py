from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class WebhookDeliveryLogs(BaseModel):
    """Webhook event log - history of webhook deliveries model"""
    amount: Optional[float] = Field(default=None)
    attempt_number: float = Field(default=None)
    compte_paye: Optional[str] = Field(default=None)
    compte_payeur: Optional[str] = Field(default=None)
    created_at: str = Field(default=None)
    event_type: str = Field(default=None)
    headers: Optional[Dict[str, Any]] = Field(default=None)
    ip_address: Optional[str] = Field(default=None)
    log_id: str = Field(default=None)
    organization_id: str = Field(default=None)
    payload: Dict[str, Any] = Field(default=None)
    request_duration_ms: Optional[float] = Field(default=None)
    response_body: Optional[str] = Field(default=None)
    response_status: Optional[float] = Field(default=None)
    spi_tx_id: Optional[str] = Field(default=None)
    success: bool = Field(default=None)
    user_agent: Optional[str] = Field(default=None)
    webhook_id: str = Field(default=None)

class WebhookDeliveryLogsCreate(BaseModel):
    amount: Optional[float] = None
    attempt_number: Optional[float] = None
    compte_paye: Optional[str] = None
    compte_payeur: Optional[str] = None
    created_at: Optional[str] = None
    event_type: str
    headers: Optional[Dict[str, Any]] = None
    ip_address: Optional[str] = None
    log_id: Optional[str] = None
    organization_id: str
    payload: Dict[str, Any]
    request_duration_ms: Optional[float] = None
    response_body: Optional[str] = None
    response_status: Optional[float] = None
    spi_tx_id: Optional[str] = None
    success: Optional[bool] = None
    user_agent: Optional[str] = None
    webhook_id: str

class WebhookDeliveryLogsUpdate(BaseModel):
    amount: Optional[float] = None
    attempt_number: Optional[float] = None
    compte_paye: Optional[str] = None
    compte_payeur: Optional[str] = None
    created_at: Optional[str] = None
    event_type: Optional[str] = None
    headers: Optional[Dict[str, Any]] = None
    ip_address: Optional[str] = None
    log_id: Optional[str] = None
    organization_id: Optional[str] = None
    payload: Optional[Dict[str, Any]] = None
    request_duration_ms: Optional[float] = None
    response_body: Optional[str] = None
    response_status: Optional[float] = None
    spi_tx_id: Optional[str] = None
    success: Optional[bool] = None
    user_agent: Optional[str] = None
    webhook_id: Optional[str] = None

