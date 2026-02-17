from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
from .models import Property, PropertyImage
from bookings.models import Booking, Inquiry
from bookings.forms import BookingForm, InquiryForm


def home(request):
    """Home page with featured properties"""
    featured_properties = Property.objects.filter(status='sale')[:6]
    total_properties = Property.objects.count()
    total_agents = Property.objects.values('agent').distinct().count()
    
    context = {
        'featured_properties': featured_properties,
        'total_properties': total_properties,
        'total_agents': total_agents,
    }
    return render(request, 'properties/home.html', context)


def property_list(request):
    """Property listing page with search and filters"""
    properties = Property.objects.all()
    
    # Search by keyword
    search_query = request.GET.get('search', '')
    if search_query:
        properties = properties.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    
    # Filter by price
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)
    
    # Filter by property type
    property_type = request.GET.get('property_type')
    if property_type:
        properties = properties.filter(property_type=property_type)
    
    # Filter by bedrooms
    bedrooms = request.GET.get('bedrooms')
    if bedrooms:
        properties = properties.filter(bedrooms__gte=bedrooms)
    
    # Filter by status
    status = request.GET.get('status')
    if status:
        properties = properties.filter(status=status)
    
    # Filter by location
    location = request.GET.get('location')
    if location:
        properties = properties.filter(location__icontains=location)
    
    # Sorting
    sort_by = request.GET.get('sort_by', '-created_at')
    properties = properties.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    properties = paginator.get_page(page_number)
    
    context = {
        'properties': properties,
        'search_query': search_query,
        'property_types': Property.PROPERTY_TYPE,
        'status_choices': Property.STATUS_CHOICES,
        'min_price': min_price,
        'max_price': max_price,
        'bedrooms': bedrooms,
    }
    return render(request, 'properties/property_list.html', context)


def property_detail(request, pk):
    """Property detail page"""
    property_obj = get_object_or_404(Property, pk=pk)
    images = property_obj.images.all()
    inquiries_count = property_obj.inquiries.count()
    
    # Check if user has already booked this property
    user_booking = None
    booking_form = BookingForm()
    inquiry_form = InquiryForm()
    
    if request.user.is_authenticated:
        user_booking = property_obj.bookings.filter(user=request.user).first()
    
    # Split features into list
    features_list = []
    if property_obj.features:
        features_list = [f.strip() for f in property_obj.features.split(',')]
    
    context = {
        'property': property_obj,
        'images': images,
        'inquiries_count': inquiries_count,
        'booking_form': booking_form,
        'inquiry_form': inquiry_form,
        'user_booking': user_booking,
        'google_maps_key': settings.GOOGLE_MAPS_API_KEY,
        'features_list': features_list,
    }
    return render(request, 'properties/property_detail.html', context)


@login_required
def book_property(request, property_id):
    """Book a property visit"""
    property_obj = get_object_or_404(Property, pk=property_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.property = property_obj
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking request submitted! Agent will review shortly.')
            return redirect('property_detail', pk=property_id)
    
    return redirect('property_detail', pk=property_id)


@login_required
def send_inquiry(request, property_id):
    """Send inquiry about a property"""
    property_obj = get_object_or_404(Property, pk=property_id)
    
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.property = property_obj
            inquiry.user = request.user
            inquiry.save()
            messages.success(request, 'Inquiry sent successfully! We will contact you soon.')
            return redirect('property_detail', pk=property_id)
    
    return redirect('property_detail', pk=property_id)


def agent_properties(request, agent_id):
    """View all properties by an agent"""
    from agents.models import Agent
    agent = get_object_or_404(Agent, pk=agent_id)
    properties = agent.properties.all()
    
    # Pagination
    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    properties = paginator.get_page(page_number)
    
    context = {
        'agent': agent,
        'properties': properties,
    }
    return render(request, 'properties/agent_properties.html', context)

