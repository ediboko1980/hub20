import factory

from blockchain.factories.providers import EthereumProvider
from ethereum_money.factories import EthereumTokenValueModelFactory
from hub20 import models

from .base import UserFactory

factory.Faker.add_provider(EthereumProvider)


class InternalTransferFactory(EthereumTokenValueModelFactory):
    sender = factory.SubFactory(UserFactory)
    receiver = factory.SubFactory(UserFactory)

    class Meta:
        model = models.InternalTransfer


class ExternalTransferFactory(EthereumTokenValueModelFactory):
    sender = factory.SubFactory(UserFactory)
    recipient_address = factory.Faker("ethereum_address")

    class Meta:
        model = models.ExternalTransfer


__all__ = ["InternalTransferFactory", "ExternalTransferFactory"]
