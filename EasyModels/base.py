from collections import OrderedDict

from django.db import models
import collections

"""
EasyLookupBase provides common methods for doing
"""
class EasyLookupBase(object):
    @classmethod
    def all(cls):
        return cls.get_model().default_queryset().all()

    @classmethod
    def search(cls, lookup, **fields):
        return cls.all().search(lookup, **fields)


class EasyQuerySet(models.QuerySet, EasyLookupBase):
    def search(self, lookup, **fields):
        search_filter = models.Q()
        for name, field in self.model.get_search_fields().items():
            if isinstance(field, (models.CharField, models.TextField)):
                search_filter = search_filter | models.Q(
                        **{'%s__icontains'%name: lookup})
        return self.filter(search_filter).filter(**fields)
            
    @classmethod
    def get_model(cls):
        return cls.model

class EasyModelManager(models.Manager, EasyLookupBase):
    use_for_related_fields = True

    @classmethod
    def get_model(cls):
        return cls.model
    
    def get_queryset(self):
        qs = EasyQuerySet(self.model, using=self._db)
        return qs

class EasyModel(models.Model, EasyLookupBase):
    objects = EasyModelManager()

    @classmethod
    def get_fields(cls):
        return collections.OrderedDict([
            (field.name, field) for field in cls._meta.get_fields()
        ])
    
    @classmethod
    def get_search_fields(cls):
        return collections.OrderedDict([
            (field.name, field) for field in cls.get_fields().values() if getattr(field, '_search', False)
        ])

    @classmethod
    def get_model(cls):
        return cls
    
    @classmethod
    def default_queryset(cls):
        return cls.objects.all()

    class Meta:
        abstract = True