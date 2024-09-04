# Copyright 2017-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from wazo_lib_rest_client.client import BaseClient

if TYPE_CHECKING:
    from .commands.config import ConfigCommand
    from .commands.mobile_notifications import MobileNotificationCommand
    from .commands.status import StatusCommand
    from .commands.subscriptions import SubscriptionsCommand


class WebhookdClient(BaseClient):
    namespace = 'wazo_webhookd_client.commands'

    config: ConfigCommand
    mobile_notifications: MobileNotificationCommand
    status: StatusCommand
    subscriptions: SubscriptionsCommand

    def __init__(
        self,
        host: str,
        port: int = 443,
        prefix: str = '/api/webhookd',
        version: str = '1.0',
        **kwargs: Any,
    ) -> None:
        super().__init__(host=host, port=port, prefix=prefix, version=version, **kwargs)
