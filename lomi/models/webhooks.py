from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class Webhooks(BaseModel):
    """Webhook configuration - receive real-time event notifications model"""
    authorized_events: WebhookEvent = Field(default=None)
    created_at: str = Field(default=None)
    created_by: Optional[str] = Field(default=None)
    deleted_at: Optional[str] = Field(default=None)
    environment: str = Field(default=None)
    is_active: bool = Field(default=None)
    last_payload: Optional[Dict[str, Any]] = Field(default=None)
    last_response_body: Optional[str] = Field(default=None)
    last_response_status: Optional[float] = Field(default=None)
    last_triggered_at: Optional[str] = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    organization_id: str = Field(default=None)
    retry_count: Optional[float] = Field(default=None)
    spi_event_types: Optional[List[str]] = Field(default=None)
    supports_spi: bool = Field(default=None)
    updated_at: str = Field(default=None)
    url: str = Field(default=None)
    verification_token: str = Field(default=None)
    webhook_id: str = Field(default=None)

class WebhooksCreate(BaseModel):
    authorized_events: Optional[WebhookEvent] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    deleted_at: Optional[str] = None
    environment: Optional[str] = None
    is_active: Optional[bool] = None
    last_payload: Optional[Dict[str, Any]] = None
    last_response_body: Optional[str] = None
    last_response_status: Optional[float] = None
    last_triggered_at: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    organization_id: str
    retry_count: Optional[float] = None
    spi_event_types: Optional[List[str]] = None
    supports_spi: Optional[bool] = None
    updated_at: Optional[str] = None
    url: str
    verification_token: str
    webhook_id: Optional[str] = None

class WebhooksUpdate(BaseModel):
    authorized_events: Optional[WebhookEvent] = None
    created_at: Optional[str] = None
    created_by: Optional[str] = None
    deleted_at: Optional[str] = None
    environment: Optional[str] = None
    is_active: Optional[bool] = None
    last_payload: Optional[Dict[str, Any]] = None
    last_response_body: Optional[str] = None
    last_response_status: Optional[float] = None
    last_triggered_at: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    organization_id: Optional[str] = None
    retry_count: Optional[float] = None
    spi_event_types: Optional[List[str]] = None
    supports_spi: Optional[bool] = None
    updated_at: Optional[str] = None
    url: Optional[str] = None
    verification_token: Optional[str] = None
    webhook_id: Optional[str] = None

