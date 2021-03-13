from rest_framework import serializers
from  .models import YEAR_IN_SCHOOL_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=YEAR_IN_SCHOOL_CHOICES, default='python')
    style = serializers.ChoiceField(choices=YEAR_IN_SCHOOL_CHOICES, default='friendly')