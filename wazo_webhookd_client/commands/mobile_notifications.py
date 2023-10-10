# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

from typing import TypedDict, Any

from wazo_webhookd_client.command import WebhookdCommand


class NotificationDict(TypedDict):
    notification_type: str
    user_uuid: str
    title: str
    body: str
    extra: dict[str, Any]


class MobileNotificationCommand(WebhookdCommand):
    resource = 'mobile/notifications'

    def send(self, notification: NotificationDict) -> None:
        headers = self._get_headers()
        r = self.session.post(
            self.base_url,
            json=notification,
            headers=headers,
        )
        self.raise_from_response(r)
