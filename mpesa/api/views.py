from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from mpesa.api.serializers import LNMonlineSerializer
from mpesa.models import LNMonline



class LNMCallbackAPIView(CreateAPIView):
    queryset = LNMonline.objects.all()
    serializer_class = LNMonlineSerializer
    permission_classes = [AllowAny]
    def create(self, request):
        print(request.data, "this is request.data")