class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    media = models.ImageField(upload_to='posts/', blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"
