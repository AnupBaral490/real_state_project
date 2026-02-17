from django.contrib import admin
from .models import Booking, Inquiry

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('property', 'user', 'requested_date', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'requested_date')
    search_fields = ('property__title', 'user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Booking Information', {
            'fields': ('property', 'user', 'requested_date', 'status')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_approved', 'mark_as_rejected']
    
    def mark_as_approved(self, request, queryset):
        queryset.update(status='approved')
    mark_as_approved.short_description = 'Mark selected bookings as approved'
    
    def mark_as_rejected(self, request, queryset):
        queryset.update(status='rejected')
    mark_as_rejected.short_description = 'Mark selected bookings as rejected'

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'email', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('user__username', 'property__title', 'email', 'message')
    readonly_fields = ('created_at', 'user', 'property')
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('user', 'email', 'phone')
        }),
        ('Inquiry', {
            'fields': ('property', 'message', 'is_read')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
