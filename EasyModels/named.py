from .base import EasyModel, models

class NamedModelBase(EasyModel):
    def get_display_name_field(self):
        raise '%s must implement abstract NamedModelBase.get_display_name_field'%self._meta.object_name

    def get_display_name(self):
        return getattr(self, self.get_display_name_field())
    
    def __str__(self):
        return '<%s %s>'%(self._meta.object_name, self.get_display_name() or "No %s"%self.get_display_name_field())

    class Meta:
        abstract = True

class UniqueNamedModelBase(NamedModelBase):
    class Meta:
        abstract = True

class TitleModel(NamedModelBase):
    title = models.CharField(max_length=255, null=True, blank=True)
    setattr(title, '_search', True)
    
    def get_display_name_field(self):
        return 'title'

    class Meta:
        abstract = True

class UniqueStubModel(UniqueNamedModelBase):
    stub = models.CharField(max_length=255, unique=True)
    setattr(stub, '_search', True)
    
    def get_display_name_field(self):
        return 'stub'

    class Meta:
        abstract = True

class UniqueTitleModel(UniqueNamedModelBase):
    title = models.CharField(max_length=255, unique=True)
    setattr(title, '_search', True)
    
    def get_display_name_field(self):
        return 'title'

    class Meta:
        abstract = True

class FullNameModel(NamedModelBase):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    setattr(full_name, '_search', True)

    def get_display_name_field(self):
        return 'full_name'

    class Meta:
        abstract = True

class UniqueFullNameModel(UniqueNamedModelBase):
    full_name = models.CharField(max_length=255, unique=True)
    setattr(full_name, '_search', True)
    
    def get_display_name_field(self):
        return 'full_name'

    class Meta:
        abstract = True