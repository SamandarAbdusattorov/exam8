from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=128)

class Team(models.Model):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="teams")
    city = models.CharField(max_length=256)
    logo = models.ImageField(upload_to='logo/%Y/%m/%d', null=True, blank=True)
    points = models.IntegerField(default=0)
    leagues = models.ManyToManyField("League", related_name="teams")

    def __str__(self):
        return self.name

class League(models.Model):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="leagues")
    winner = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="league_winner", null=True, blank=True)

    def __str__(self):
        return self.name

class Football(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)

class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateField()
    time = models.TimeField()
    home_goals = models.IntegerField(default=0)
    away_goals = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    players = models.ManyToManyField("Player", related_name="matches")

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date}"

    def winner(self):
        if self.home_goals > self.away_goals:
            return self.home_team
        elif self.away_goals > self.home_goals:
            return self.away_team
        else:
            return None

class Player(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    number = models.IntegerField()
    position = models.CharField(max_length=128)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="players")

class News(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news/%Y/%m/%d')

class Results(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name= "results")
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="results")

class LatestScores(models.Model):
    team_id = models.ManyToManyField(Team, related_name="latest_scores")
    league_id = models.ManyToManyField(League, related_name="latest_scores")
    score = models.IntegerField()

    def __str__(self):
        return ', '.join([team.name for team in self.team_id.all()])

class Standings(models.Model):
    team_id = models.ManyToManyField(Team, related_name="statistics")
    mp = models.IntegerField()
    w = models.IntegerField()
    d = models.IntegerField()
    l = models.IntegerField()
    gd = models.IntegerField()
    pts = models.IntegerField()
