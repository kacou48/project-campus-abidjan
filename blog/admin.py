from django.contrib import admin
from . models import Post, Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'contenu', 'date', 'cover', )
    list_filter = ('date', 'titre' )
    search_fields = ('titre', 'contenu', )

    prepopulated_fields = {'slug': ('titre', ), }




class CommentAdmin(admin.ModelAdmin):
    list_display = ('contenu', 'publie', 'activate', )
    list_filter = ('activate', 'publie')
    search_fields = ('contenu', )
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(activate=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)



