# Copyright 2017-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from requests import Response
from wazo_lib_rest_client.command import RESTCommand

from .exceptions import InvalidWebhookdError, WebhookdError, WebhookdServiceUnavailable


class WebhookdCommand(RESTCommand):
    @staticmethod
    def raise_from_response(response: Response) -> None:
        if response.status_code == 503:
            raise WebhookdServiceUnavailable(response)

        try:
            raise WebhookdError(response)
        except InvalidWebhookdError:
            RESTCommand.raise_from_response(response)
