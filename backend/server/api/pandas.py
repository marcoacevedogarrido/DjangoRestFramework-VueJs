from rest_pandas import PandasSimpleView
from server.models import Pandas

class PandasView(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
        return Pandas.objects.all()
