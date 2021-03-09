from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User, Animal, UserAnimal


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ('id',)
    list_display = ('email',)
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('important dates', {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    fields = (
        'id', 'animal_name', 'description',
    )
    list_display = (
        'id', 'animal_name', 'description',
    )
    readonly_fields = (
        'id',
    )

@admin.register(UserAnimal)
class UserAnimalAdmin(admin.ModelAdmin):
    fields = (
        'id', 'users', 'animals', 'picture_url',
        'x_coordinate', 'y_coordinate', 'created_date'
    )
    list_display = (
        'id', 'picture_url',
        'x_coordinate', 'y_coordinate', 'created_date'
    )
    readonly_fields = (
        'id', 'created_date'
    )
