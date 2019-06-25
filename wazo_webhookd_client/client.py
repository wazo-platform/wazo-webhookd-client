# -*- coding: utf-8 -*-
# Copyright 2017-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from xivo_lib_rest_client.client import BaseClient


class WebhookdClient(BaseClient):

    namespace = 'wazo_webhookd_client.commands'

    def __init__(self, host, port=9300, version='1.0', **kwargs):
        super(WebhookdClient, self).__init__(
            host=host, port=port, version=version, **kwargs
        )
