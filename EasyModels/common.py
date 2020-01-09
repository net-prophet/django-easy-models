from .base import EasyModel
from django.db import models
import uuid

def cutePk():
    return str(uuid.uuid4())[-12:]

class CutePKModel(EasyModel):
    id = models.CharField(max_length=12, primary_key=True, default=cutePk, editable=False)
    setattr(id, '_search', True)

    class Meta:
        abstract = True


class StrongPKModel(EasyModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    setattr(id, '_search', True)
    
    class Meta:
        abstract = True

class TimestampedModel(EasyModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
