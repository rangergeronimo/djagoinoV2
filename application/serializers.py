import ast

from rest_framework.serializers import (CharField, HyperlinkedIdentityField,
                                        ModelSerializer, ValidationError)

from .models import Sensor


class SensorListSerializer(ModelSerializer):
    details = HyperlinkedIdentityField(view_name='app:detail',
                                       lookup_field='pk')

    class Meta:
        model = Sensor
        fields = ['name', 'details']


class SensorDetailSerializer(ModelSerializer):

    values = CharField()

    def validate_values(self, values):
        try:
            value = ast.literal_eval(values)
        except ValueError:
            raise ValidationError("List MUST contain Numbers only! ")
        return value

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'kind', 'values']
