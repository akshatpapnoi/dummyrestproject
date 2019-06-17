from django.contrib import admin
from .models import Address, Profile
from django.utils.safestring import mark_safe
from django.utils.html import format_html


class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'country')


admin.site.register(Address, AddressAdmin)
#admin.site.register(Profile)
#admin.site.register(Profile,list_display=['name', 'email', 'mobile', 'gender'], search_fields=('name',), list_filter = ('gender', 'permanent_address',))

class ProfileAdmin(admin.ModelAdmin):
    

    def profile_thumbnail(self, obj):
        try:
            return mark_safe('<img src={} height="40" />'.format(obj.profile_pic.url) )
        except:
            return ''
    profile_thumbnail.allow_tags = True

    def profile_pic_tag(self, obj):
        try:
            return mark_safe('<img src={} height="150" />'.format(obj.profile_pic.url) )
        except:
            return ''
    profile_pic_tag.allow_tags = True

    list_display = ('name', 'email', 'mobile', 'gender', 'profile_thumbnail', )
    list_filter = ('gender', 'permanent_address',)
    search_fields=('name',)
    #fields = ( 'profile_thumbnail',)
    readonly_fields = ('profile_pic_tag',)



admin.site.register(Profile, ProfileAdmin)