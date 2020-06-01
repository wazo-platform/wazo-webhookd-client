# -*- coding: utf-8 -*-
# Copyright 2017-2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from wazo_lib_rest_client.client import BaseClient


class WebhookdClient(BaseClient):

    namespace = 'wazo_webhookd_client.commands'

    def __init__(self, host, port=443, prefix='/api/webhookd', version='1.0', **kwargs):
        super(WebhookdClient, self).__init__(
            host=host, port=port, prefix=prefix, version=version, **kwargs
        )
