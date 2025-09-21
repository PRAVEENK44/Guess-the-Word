from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, GameWord, GameSession, GameGuess

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'created_at')
    list_filter = ('role', 'is_active', 'created_at')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'created_at')}),
    )
    readonly_fields = ('created_at',)

@admin.register(GameWord)
class GameWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'created_at')
    search_fields = ('word',)
    ordering = ('word',)

@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'is_won', 'is_completed', 'created_at')
    list_filter = ('is_won', 'is_completed', 'created_at')
    search_fields = ('user__username', 'word__word')
    readonly_fields = ('created_at', 'completed_at')

@admin.register(GameGuess)
class GameGuessAdmin(admin.ModelAdmin):
    list_display = ('session', 'word', 'is_correct', 'created_at')
    list_filter = ('is_correct', 'created_at')
    search_fields = ('session__user__username', 'word')
    readonly_fields = ('created_at',)
