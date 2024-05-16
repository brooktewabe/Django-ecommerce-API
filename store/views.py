from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDetail(request,pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializer(items,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateItem(request,pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item,data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteItem(request,pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response('Data with id '+ str(pk)+ ' deleted')