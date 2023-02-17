from rest_framework.views import APIView, Response, Request, status
from .models import Movie
from .serializers import MovieSerializer, OrderMovieSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsSuperUserOrReadOnly, IsNotSuperUser
from rest_framework.pagination import PageNumberPagination

class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    def get(self, request):
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        serializer.save(user=user)
        return Response(serializer.data, status.HTTP_201_CREATED)

class MovieDetailView(APIView):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsSuperUserOrReadOnly]

        def get(self, request: Request, movie_id):
            movieValidate = get_object_or_404(Movie, id=movie_id)
            serializer = MovieSerializer(movieValidate)
            return Response(serializer.data)
        
        def delete(self, request: Request, movie_id: int) -> Response:
            movie = get_object_or_404(Movie, id=movie_id)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
class OrderMovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsNotSuperUser]

    def post(self, request: Request, movie_id: int):
        movieValidate = get_object_or_404(Movie, id=movie_id)
        order_movie = OrderMovieSerializer(data=request.data)
        order_movie.is_valid(raise_exception=True)
        order_movie.save(user=request.user, movie=movieValidate)
        return Response(order_movie.data, status.HTTP_201_CREATED)