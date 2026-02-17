from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Inquiry


@login_required
def my_bookings(request):
    """View user's bookings"""
    if request.user.role != 'buyer':
        messages.error(request, 'Only buyers can view bookings.')
        return redirect('home')
    
    bookings = request.user.bookings.all().order_by('-created_at')
    
    context = {
        'bookings': bookings,
    }
    return render(request, 'bookings/my_bookings.html', context)


@login_required
def agent_bookings(request):
    """View bookings for agent's properties"""
    if request.user.role != 'agent':
        messages.error(request, 'Only agents can view this page.')
        return redirect('home')
    
    if not hasattr(request.user, 'agent'):
        messages.error(request, 'Agent profile not found.')
        return redirect('home')
    
    agent = request.user.agent
    bookings = Booking.objects.filter(
        property__agent=agent
    ).order_by('-created_at')
    
    context = {
        'bookings': bookings,
        'agent': agent,
    }
    return render(request, 'bookings/agent_bookings.html', context)


@login_required
def booking_detail(request, booking_id):
    """View booking details"""
    booking = get_object_or_404(Booking, pk=booking_id)
    
    # Check if user has permission to view this booking
    if request.user != booking.user and request.user != booking.property.agent.user:
        messages.error(request, 'You do not have permission to view this booking.')
        return redirect('home')
    
    context = {
        'booking': booking,
    }
    return render(request, 'bookings/booking_detail.html', context)


@login_required
def update_booking_status(request, booking_id):
    """Update booking status (approve/reject)"""
    if request.method != 'POST':
        return redirect('home')
    
    booking = get_object_or_404(Booking, pk=booking_id)
    
    # Check if user is the agent who owns this property
    if request.user != booking.property.agent.user:
        messages.error(request, 'You do not have permission to update this booking.')
        return redirect('home')
    
    status = request.POST.get('status')
    if status in ['approved', 'rejected', 'completed', 'cancelled']:
        booking.status = status
        booking.save()
        messages.success(request, f'Booking has been marked as {status}.')
    
    return redirect('booking_detail', booking_id=booking_id)


@login_required
def agent_inquiries(request):
    """View inquiries for agent's properties"""
    if request.user.role != 'agent':
        messages.error(request, 'Only agents can view this page.')
        return redirect('home')
    
    if not hasattr(request.user, 'agent'):
        messages.error(request, 'Agent profile not found.')
        return redirect('home')
    
    agent = request.user.agent
    inquiries = Inquiry.objects.filter(
        property__agent=agent
    ).order_by('-created_at')
    
    context = {
        'inquiries': inquiries,
        'agent': agent,
    }
    return render(request, 'bookings/agent_inquiries.html', context)


@login_required
def mark_inquiry_as_read(request, inquiry_id):
    """Mark inquiry as read"""
    inquiry = get_object_or_404(Inquiry, pk=inquiry_id)
    
    # Check if user is the agent who owns this property
    if request.user != inquiry.property.agent.user:
        messages.error(request, 'You do not have permission to update this inquiry.')
        return redirect('home')
    
    inquiry.is_read = True
    inquiry.save()
    messages.success(request, 'Inquiry marked as read.')
    
    return redirect('agent_inquiries')

