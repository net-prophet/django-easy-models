from .base import EasyModel, models
from django.utils import timezone

class ArchivableModel(EasyModel):
    archived_at = models.DateTimeField(null=True, blank=True, db_index=True)
    class Meta:
        abstract = True

    def __str__(self):
        archived = (self.archived_at and '(archived) ' or '')
        return '%s%s' % (archived, super(ArchivableModel, self).__str__())

    def delete(self, archive=True):
        if archive:
            self.set_archived()
        else:
            super(ArchivableModel, self).delete()
            return None

    def set_archived(self, commit=True):
        if not self.archived_at:
            self.archived_at = timezone.now()
            if commit:
                self.save()
                return True

    def set_unarchived(self, commit=True):
        self.archived_at = None
        if commit:
            self.save()
            return True

    def delete_forever(self):
        return self.delete(False)

    def restore(self, commit=True):
        return self.set_unarchived(commit)
