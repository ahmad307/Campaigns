from rest_framework import viewsets, status
from rest_framework.response import Response
from campaign import serializers, models
import requests


class CampaignView(viewsets.ModelViewSet):
    serializer_class = serializers.CampaignSerializer
    queryset = models.Campaign.objects.all()

    def create(self, request, *args, **kwargs):
        # Handle unspecified category
        data = request.data.copy()
        if len(data['category']) == 0:
            data['category'] = get_campaign_category(data['name'])

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def get_campaign_category(name):
    """
    Gets campaign category through Cognetiv (fake) category
    extraction end-point.
    """
    name = name.replace(' ', '')
    # Generate fake url to get category for
    website = 'https://' + name + '.com'
    url = 'https://ngkc0vhbrl.execute-api.eu-west-1.amazonaws.com/api/?url=' + website

    response = requests.get(url).json()
    return response['category']['name']
