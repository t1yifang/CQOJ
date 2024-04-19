from utils.api import APIView, validate_serializer

class ImageAdminAPI(APIView):
    def get(self, request):
        return self.success("123")