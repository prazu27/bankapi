from rest_framework import serializers
from .models import Bank, Customer

class BankSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bank 
		fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = '__all__'
		extra_kwargs = {'password':{'write_only': True}}

	def create(self, validated_data):
		validated_data['password'] = make_password(validated_data['password'])
		return super(CustomerSerializer, self).create(validated_data)


if __name__ == '__main__':
	main()