from django.db import models
from .options import COLORS, SIZES, SHAPES
from EasyModels import TitleModel, ArchivableModel

class Widget(ArchivableModel, TitleModel):
    color = models.CharField(choices=COLORS, max_length=30)
    size = models.CharField(choices=SIZES, max_length=30)
    shape = models.CharField(choices=SHAPES, max_length=30)
    cost = models.FloatField(default=0,
                             blank=True)

    def save(self, *args, **kwargs):
        if self.title == '':
            self.title = '%s.%s.%s' % (self.color, self.size, self.shape)

        color_sum = sum([ord(x) for x in self.color])
        size_sum = sum([ord(x) for x in self.size])
        shape_sum = sum([ord(x) for x in self.shape])
        self.cost = color_sum + size_sum + shape_sum
        super(Widget, self).save(*args, **kwargs)

