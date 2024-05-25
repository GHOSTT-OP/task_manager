# from rest_framework import serializers
# from .models import Task
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']  

# class TaskSerializer(serializers.ModelSerializer):
#     to_user = UserSerializer(read_only=True)
#     from_user = UserSerializer(read_only=True)

#     class Meta:
#         model = Task
#         fields = '__all__'
from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    to_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    from_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        validated_data['from_user'] = self.context['request'].user
        return super().create(validated_data)





    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     validated_data['from_user'] = request.user
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     request = self.context.get('request')
    #     validated_data['from_user'] = request.user
    #     return super().update(instance, validated_data)
