from rest_pandas import PandasSimpleView
from server.models import Pandas
from rest_framework.permissions import IsAuthenticated

class PandasView(PandasSimpleView):
    permission_classes = [IsAuthenticated]

    def get_data(self, request, *args, **kwargs):
        return Pandas.objects.all()
