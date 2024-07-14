from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'about', 'faqs', 'report-dp', 'know-about-dp', 'loginUser', 
                'registerUser', 'detected-dp', 'dashboard', 'verify-email', 
                'password_reset', 'privacy-policy', 'terms-of-use']

    def location(self, item):
        return reverse(f'home:{item}')

    def priority(self, item):
        priorities = {
            'home': 1.0,
            'about': 0.9,
            'faqs': 0.8,
            'report-dp': 0.8,
            'know-about-dp': 0.8,
            'privacy-policy': 0.7,
            'terms-of-use': 0.7,
        }
        return priorities.get(item, 0.5)

    def changefreq(self, item):
        frequencies = {
            'home': 'daily',
            'about': 'weekly',
            'faqs': 'weekly',
        }
        return frequencies.get(item, 'monthly')