from django.db import models

class Rating(models.TextChoices):
    G= "G"
    PG = "PG"
    PG13 = "PG-13"
    R  = "R"
    NC17 = "NC-17"


class Movie(models.Model):

    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default=None, null=True)
    rating = models.CharField(default=Rating.G, choices=Rating.choices, max_length=20)
    synopsis = models.CharField(null=True, default=None, max_length=200)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    movieOrder = models.ManyToManyField("users.User", through="movies.MovieOrder", related_name="order_movie")    


class MovieOrder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_orders')
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='user_movie_order')  
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self) -> str:
        return f"{self.price}"