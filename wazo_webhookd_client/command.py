# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client.command import RESTCommand

from .exceptions import WebhookdError
from .exceptions import WebhookdServiceUnavailable
from .exceptions import InvalidWebhookdError


class WebhookdCommand(RESTCommand):

    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise WebhookdServiceUnavailable(response)

        try:
            raise WebhookdError(response)
        except InvalidWebhookdError:
            RESTCommand.raise_from_response(response)