from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from .models import BookView, CategoryAnalytics, AuthorAnalytics, RecommendationLog
from library.models import Book, Category, Author

@login_required
def analytics_dashboard(request):
    # Estadísticas generales
    total_views = BookView.objects.count()
    popular_categories = CategoryAnalytics.objects.order_by('-popularity_score')[:5]
    popular_authors = AuthorAnalytics.objects.order_by('-total_views')[:5]
    
    # Recomendaciones recientes
    recent_recommendations = RecommendationLog.objects.order_by('-timestamp')[:10]
    
    # Libros más vistos
    most_viewed_books = Book.objects.annotate(view_count=Count('views')).order_by('-view_count')[:5]
    
    context = {
        'total_views': total_views,
        'popular_categories': popular_categories,
        'popular_authors': popular_authors,
        'recent_recommendations': recent_recommendations,
        'most_viewed_books': most_viewed_books,
    }
    
    return render(request, 'analytics/dashboard.html', context)