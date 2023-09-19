from .models import *
from .serializers import *
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions


class StockPriceConsumer(GenericAsyncAPIConsumer):
    queryset = StockPrice.objects.all()
    permission_classes = [permissions.AllowAny()]

    async def connect(self, **kwargs):
        await self.model_chanage.subscribe()
        await super().connect()

    @model_observer(StockPrice)
    async def model_change(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @model_change.serialize
    def model_serialize(self, instance, action, **kwargs):
        return dict(StockPriceSerializer(instance=instance).data, action=action.value)