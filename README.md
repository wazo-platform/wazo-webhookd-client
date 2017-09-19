# wazo-webhookd-client

A python client library to access wazo-webhookd

## Usage

### Creating a client

```python
from wazo_webhookd_client import Client
client = Client('localhost', verify_certificate=False, token=<xivo-auth-token>)
```

## Subscriptions

### Listing hook subscriptions

```python
client.subscriptions.list()
client.subscriptions.list_as_user()  # same thing, but only the subscriptions regarding the user making the request are considered
```

### Add a new hook subscription

```python
subscription = {
    'name': 'test',
    'service': 'http',
    'config': {
        'url': 'http://test.example.com',
        'method': 'get'
    },
    'events': ['confd.users.create']
}
client.subscriptions.create(subscription)
client.subscriptions.create_as_user(subscription)  # same thing, but only the events regarding the user making the request are considered
```

### Get hook subscription

```python
subscription = client.subscriptions.get(subscription_uuid)
```

### Update hook subscription

```python
subscription = client.subscriptions.update(subscription_uuid, new_subscription)
```

### Delete hook subscription

```python
client.subscriptions.delete(subscription_uuid)
```

## Config

### Getting the service configuration

```python
client.config.get()
```

## Debian package

Follow the following steps to build a debian package for wazo-webhookd-client manually.

1. Copy the source directory to a machine with all dependencies installed

```sh
rsync -av . <builder-host>:~/wazo-webhookd-client
```

2. On the host, increment the changelog

```sh
dch -i
```

3. Build the package

```sh
dpkg-buildpackage -us -uc
```
