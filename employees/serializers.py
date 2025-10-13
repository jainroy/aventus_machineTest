from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(
        required=False,
        allow_null=True,
        help_text="Upload employee photo max 5mb."
    )
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'photo']

    def validate_photo(self, value):
        if value and value.size > 5*1024*1024: #1024bytes*1024bytes=1mb
            raise serializers.ValidationError("Photo size must be less than 5MB")
        return value
    def validate_email(self, value):
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exists.")
        return value
