from django.contrib.auth import authenticate, login
from accounts.models import Profile, Address
from django.contrib.auth.models import User
from rest_framework import serializers, generics



class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('user','permanent_address', 'company_address', 'profile_pic', 'friends',     )


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['city']

class ProfileListSerializer(serializers.ModelSerializer):
    is_friend = serializers.SerializerMethodField()
    mutual_friends = serializers.SerializerMethodField()
    permanent_city = serializers.SerializerMethodField()


    class Meta:
        model = Profile
        fields = ['id', 'name', 'gender', 'profile_pic', 'permanent_city', 'is_friend', 'mutual_friends']


    def get_is_friend(self,data):
        friend_user = data
        my_user = self.context['my_user']
        my_user_profile = Profile.objects.get(user=my_user)
        friends = my_user_profile.friends.all()
        for f in friends:
            if f == friend_user:
                return True
        
        return False

    def get_mutual_friends(self, data):
        friend_user = data
        my_user = self.context['my_user']
        my_user_profile = Profile.objects.get(user=my_user)
        count = 0
        for i in friend_user.friends.all():
            for j in my_user_profile.friends.all():
                if i==j:
                    count += 1

        return count

    def get_permanent_city(self, data):
        friend_user = data

        if friend_user.permanent_address:
            permanent_address = friend_user.permanent_address
            if permanent_address.city:
                return permanent_address.city
        
        return None

    



class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}




    def create(self, validated_data):

        user = User.objects.create_user(username=validated_data['username'], password= validated_data['password'])

        profile_data = validated_data.pop('profile')
        
        name = profile_data['name']
        email = profile_data['email']
        mobile = profile_data['mobile']
        try:
            gender = profile_data['gender']
        except:
            gender = None
        try:
            dob = profile_data['dob']
        except:
            dob=None

        profile = Profile.objects.create(
            user = user,
            name = name,
            email = email,
            mobile = mobile,
            gender = gender,
            dob = dob
        )
            
        

        return user

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'password']   

        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            request = self.context['request']
            login(request, user)
            return user
        raise serializers.ValidationError("Invalid Credentials")



class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password',]




"""class CreateStudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['enrollment_no', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'], validated_data['enrollment_no'])
        return user

class CreateFacultyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'])
        return user

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credentials wrong")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password',]

class StudentProfileSerialzer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class ExtraInfoSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = '__all__'

class MarkSheetSerialzer(serializers.ModelSerializer):
    class Meta:
        model = MarkSheet
        fields = '__all__'

class WorkExperienceSerialzer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class SchoolEducationSerialzer(serializers.ModelSerializer):
    class Meta:
        model = SchoolEducation
        fields = '__all__'

class CollegeEducationSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CollegeEducation
        fields = '__all__'
"""