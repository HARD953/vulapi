class PurchaseList(generics.ListAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Purchase.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(purchaser__username=username)
        return queryset


def recensers(request):
    if request.method=="GET":
        recenser=DonateurUser.objects.all()
        serializer1 = DonateurOrSerializer(recenser,many=True)
        serializer2 = DonateurOrSerializer(recenser,many=True)
        data1=[dict(i) for i in serializer1.data]
        data2=[dict(i) for i in serializer2.data]
        data={}
        data['data1']=data1
        data['data2']=data2

        for i in data1:
            print(i['id'])
        return JsonResponse(data,safe=False)