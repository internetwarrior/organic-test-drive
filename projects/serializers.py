from rest_framework import serializers
from .models import Project, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'  

class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True) 
    state = serializers.SerializerMethodField()


    class Meta:
        model = Project
        fields = '__all__'  
        
    def get_state(self, obj):
        return obj.get_state_display()