from rest_framework import serializers
from transactions.models import Post

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['transaction_date','description', 'amount', 'user']