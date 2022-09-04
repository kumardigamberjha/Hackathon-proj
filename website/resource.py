from import_export import resources

from website.models import DBModel

class SalaryResources(resources.ModelResource):
    class Meta:
        model = DBModel
        fields = "__all__"