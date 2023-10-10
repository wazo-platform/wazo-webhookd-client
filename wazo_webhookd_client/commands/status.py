# Copyright 2017-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

from typing import TYPE_CHECKING

from wazo_webhookd_client.command import WebhookdCommand

if TYPE_CHECKING:
    from webhookd.plugins.status.http import StatusResponse


class StatusCommand(WebhookdCommand):
    resource = 'status'

    def get(self) -> StatusResponse:
        headers = self._get_headers()
        r = self.session.get(self.base_url, headers=headers)
        self.raise_from_response(r)
        return r.json()
