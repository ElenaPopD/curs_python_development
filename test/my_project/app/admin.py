from typing import Any  # noqa: F401
from django.contrib import admin
from django.db.models.query import QuerySet  # noqa: F401
from django.http import HttpRequest  # noqa: F401

# Register your models here.
from .models import Produs, Favorit, Question, Answer, UserProfile, Curs, Student, Recenzie, Elev, ElevCurs, Post, Producator, Intrebare


admin.site.register(Favorit)

admin.site.register(UserProfile)

class StudentAdmin(admin.TabularInline):
    model = Student.cursuri.through
    extra = 1

class CursAdmin(admin.ModelAdmin):
    inlines = (StudentAdmin, )

admin.site.register(Curs, CursAdmin)

admin.site.register(Recenzie)
admin.site.register(Elev)
admin.site.register(ElevCurs)
admin.site.register(Post)
admin.site.register(Producator)

def retrage_din_oferta(modeladmin, request, queryset):
    # for produs in queryset:
    #     produs.stoc = 0
    #     produs.save()

    queryset.update(stoc=0)

class IntrebareInline(admin.TabularInline):
    model = Intrebare
    extra = 1
    readonly_fields = ("text_intrebare", )

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)  # noqa: F841
        return super().get_queryset(request).filter(text_raspuns__isnull=True)

class ProdusAdmin(admin.ModelAdmin):
    search_fields = ("titlu", "producator__nume")
    list_display = ("producator", "titlu", "stoc")
    list_filter = ("producator", )
    list_per_page = 3
    change_list_template = "admin/produs_change_list.html"
    list_select_related = ("producator", )
    list_editable = ("titlu", "stoc")
    actions = (retrage_din_oferta, )
    inlines = (IntrebareInline, )



    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        if request.user.is_superuser is False:
            return qs.none()
            
        return qs
    
    
admin.site.register(Produs, ProdusAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ("nume", "an")
    list_filter = ("an", )

admin.site.register(Student, StudentAdmin)


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)