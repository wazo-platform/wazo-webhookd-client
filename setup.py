#!/usr/bin/env python3
# Copyright 2017-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from setuptools import find_packages, setup

setup(
    name='wazo_webhookd_client',
    version='1.0',
    description='a simple client library for the wazo webhookd HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'wazo_webhookd_client.commands': [
            'config = wazo_webhookd_client.commands.config:ConfigCommand',
            'status = wazo_webhookd_client.commands.status:StatusCommand',
            'subscriptions = wazo_webhookd_client.commands.subscriptions:SubscriptionsCommand',
            (
                'mobile_notifications = '
                'wazo_webhookd_client.commands.mobile_notifications:MobileNotificationCommand'
            ),
        ]
    },
)
