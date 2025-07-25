# Generated by Django 5.2.3 on 2025-06-26 07:47

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.URLField()),
                ('date', models.DateField(auto_now_add=True)),
                ('more_link', models.URLField()),
            ],
            options={
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(choices=[('BATTLEFIELD', 'Battlefield'), ('NHL', 'NHL'), ('OTHER', 'Other')], default='BATTLEFIELD', max_length=20)),
                ('title', models.CharField(max_length=255)),
                ('max_players', models.IntegerField()),
                ('registered_players', models.IntegerField(default=0)),
                ('mode', models.CharField(choices=[('SOLO', 'Solo'), ('TEAM', 'Team')], max_length=10)),
                ('region', models.CharField(choices=[('NA', 'North America'), ('EU', 'Europe'), ('ASIA', 'Asia'), ('OCE', 'Oceania'), ('GLOBAL', 'Global')], max_length=10)),
                ('level', models.CharField(choices=[('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced'), ('PRO', 'Professional')], max_length=15)),
                ('platform', models.CharField(choices=[('PC', 'PC'), ('CONSOLE', 'Console'), ('MOBILE', 'Mobile'), ('CROSS', 'Cross-Platform')], max_length=10)),
                ('start_date', models.DateTimeField()),
                ('language', models.CharField(max_length=100)),
                ('tournament_type', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bracket_structure', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_team_lead', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_online', models.BooleanField(default=False)),
                ('last_activity', models.DateTimeField(auto_now=True)),
                ('last_login_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='player_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='player_permissions', to='auth.permission')),
            ],
            options={
                'db_table': 'tournaments_player',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=30)),
                ('uid', models.CharField(max_length=100, unique=True)),
                ('extra_data', models.JSONField(default=dict)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament_social_accounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'social_account',
            },
        ),
        migrations.CreateModel(
            name='SocialToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=30)),
                ('uid', models.CharField(max_length=100, unique=True)),
                ('access_token', models.TextField()),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='social_token', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('join_code', models.CharField(default='AC7F762C76', max_length=10, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('lead_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='led_teams', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('RED', 'Red'), ('BLUE', 'Blue')], max_length=10)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament_teams', to='tournaments.tournament')),
            ],
            options={
                'unique_together': {('tournament', 'color')},
            },
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squad_type', models.CharField(choices=[('INFANTRY', 'Infantry'), ('ARMOR', 'Armor'), ('HELI', 'Heli'), ('JET', 'Jet')], max_length=15)),
                ('tournament_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='squads', to='tournaments.tournamentteam')),
            ],
            options={
                'verbose_name': 'Squad',
                'verbose_name_plural': 'Squads',
                'unique_together': {('tournament_team', 'squad_type')},
            },
        ),
        migrations.CreateModel(
            name='SquadMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('CAPTAIN', 'Team Captain'), ('LEADER', 'Squad Leader'), ('NONE', 'No Role')], default='NONE', max_length=10)),
                ('rank', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('kill_death_ratio', models.FloatField(default=0.0)),
                ('win_rate', models.FloatField(default=0.0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='squad_memberships', to=settings.AUTH_USER_MODEL)),
                ('squad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='tournaments.squad')),
            ],
            options={
                'constraints': [models.UniqueConstraint(condition=models.Q(('role', 'CAPTAIN')), fields=('squad',), name='unique_captain_per_squad'), models.UniqueConstraint(condition=models.Q(('role', 'LEADER')), fields=('squad',), name='unique_leader_per_squad')],
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='tournaments.team')),
            ],
            options={
                'unique_together': {('team', 'player')},
            },
        ),
        migrations.CreateModel(
            name='TournamentMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.IntegerField()),
                ('match_number', models.IntegerField()),
                ('team1_score', models.IntegerField(default=0)),
                ('team2_score', models.IntegerField(default=0)),
                ('mode', models.CharField(blank=True, choices=[('SOLO', 'Solo'), ('TEAM', 'Team')], max_length=30)),
                ('is_completed', models.BooleanField(default=False)),
                ('scheduled_time', models.DateTimeField(blank=True, null=True)),
                ('team1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1_matches', to='tournaments.team')),
                ('team2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team2_matches', to='tournaments.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='tournaments.tournament')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='won_matches', to='tournaments.team')),
            ],
            options={
                'unique_together': {('tournament', 'round_number', 'match_number')},
            },
        ),
        migrations.CreateModel(
            name='TournamentParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournaments', to='tournaments.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='tournaments.tournament')),
            ],
            options={
                'unique_together': {('team', 'tournament')},
            },
        ),
    ]
