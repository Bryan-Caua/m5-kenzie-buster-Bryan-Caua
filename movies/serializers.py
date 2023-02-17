from rest_framework import serializers
from .models import Rating
from .models import Movie, MovieOrder 

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(choices=Rating.choices, default=Rating.G)
    synopsis = serializers.CharField(max_length=200, allow_null=True,default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, movie):
        return movie.user.email
    
    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie

class OrderMovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_title(self, obj: MovieOrder):
        return obj.movie.title
    
    def get_buyed_by(self, obj: MovieOrder):
        return obj.user.email
    
    def create(self, validated_data):
        movieOrder = MovieOrder.objects.create(**validated_data)
        return movieOrder