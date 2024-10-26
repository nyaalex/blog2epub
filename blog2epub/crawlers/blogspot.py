#!/usr/bin/env python3
# -*- coding : utf-8 -*-
from blog2epub.crawlers.crawler import Crawler


class CrawlerBlogspot(Crawler):
    """Blogspot.com crawler."""

    content_xpath = (
        "//div[contains(concat(' ',normalize-space(@class),' '),'post-body')]"
    )
    images_regex = r'<table[^>]*><tbody>[\s]*<tr><td[^>]*><a href="([^"]*)"[^>]*><img[^>]*></a></td></tr>[\s]*<tr><td class="tr-caption" style="[^"]*">([^<]*)'
    articles_regex = r"<h3 class=\'post-title entry-title\' itemprop=\'name\'>[\s]*<a href=\'([^\']*)\'>([^>^<]*)</a>[\s]*</h3>"

    ignore_downloads = [
        r"https:\/\/zblogowani\.pl\/[a-z]+\/[0-9]+x[0-9]+\/[a-z]+\/[0-9]+\/btn\.png",
        r"https:\/\/www.blogger.com\/img\/blogger_logo_[a-z]+_[0-9]+\.png",
        r"https:\/\/resources.blogblog.com\/img\/[a-z0-9_]+.gif",
        r"https:\/\/www.paypalobjects.com\/[a-zA-Z_]+\/i\/scr\/pixel.gif",
        r"https:\/\/resources.blogblog.com\/img\/widgets\/[a-zA-Z0-9\-\.]+",
        r"https:\/\/[a-zA-Z0-9\.\/\-\_]+icon[0-9]+_[a-z]+.gif",
    ]
