from django.contrib import admin
from publications.models import Publications, RubricPublications, Author, TypesOfSports, Athlete, InfoAboutJournal


class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'author', 'category')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


class RubricpublicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Publications, PublicationsAdmin)
admin.site.register(RubricPublications, RubricpublicationsAdmin)
admin.site.register(Author)
admin.site.register(TypesOfSports)
admin.site.register(Athlete)
admin.site.register(InfoAboutJournal)
