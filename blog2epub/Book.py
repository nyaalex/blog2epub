#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from ebooklib import epub
from blog2epub.Cover import Cover


class Book(object):
    """
    Book class used in Blogspot2Epub class.
    """

    style = '''
    @namespace epub "http://www.idpf.org/2007/ops";
    body {
        font-family: Cambria, Liberation Serif, Bitstream Vera Serif, Georgia, Times, Times New Roman, serif;
    }
    h2 {
         text-align: left;
         text-transform: uppercase;
         font-weight: 200;     
    }
    ol {
            list-style-type: none;
    }
    ol > li:first-child {
            margin-top: 0.3em;
    }
    nav[epub|type~='toc'] > ol > li > ol  {
        list-style-type:square;
    }
    nav[epub|type~='toc'] > ol > li > ol > li {
            margin-top: 0.3em;
    }
    '''

    def __init__(self, name, title, url, start, end, language, images=[], chapters=[]):
        self.name = name
        self.title = title
        self.url = url
        self.start = start
        self.end = end
        self.images = images
        self.cover = Cover(name, title, images)
        self.language = language
        self.chapters = chapters

    def addChapter(self, article, language):
        number = len(self.chapters) + 1
        self.end = article.date
        self.chapters.append(Chapter(article, number, language))

    def create(self):
        self.book = epub.EpubBook()
        for chapter in self.chapters:
            self.book.add_item(chapter.epub)
            self.book.spine.append(chapter.epub)
            self.book.table_of_contents.append(chapter.epub)

    def get_cover_title(self):
        cover_title = self.title + ' '
        if self.start == self.end:
            cover_title = cover_title + str(self.start)
        else:
            end_date = self.end.split(' ')
            start_date = start.split(' ')
            if len(end_date) == len(start_date):
                ed = []
                for i, d in enumerate(end_date):
                    if d != start_date[i]:
                        ed.append(d)
            ed = ' '.join(ed)
            cover_title = cover_title + ed + '-' + start
        return cover_title

    def _get_book_title(self):
        book.set_title(get_cover_title(title, START_DATE, END_DATE))
        try:
            start_date_obj = datetime.strptime(translate_month(START_DATE,BLOG_LANGUAGE), '%d %B %Y')
            end_date_obj = datetime.strptime(translate_month(END_DATE,BLOG_LANGUAGE), '%d %B %Y')
            if START_DATE == END_DATE:
                book_file_name = book_file_name + '_' + start_date_obj.strftime('%Y.%m.%d')
            else:
                book_file_name = book_file_name + '_' + end_date_obj.strftime('%Y.%m.%d') + '-' + start_date_obj.strftime('%Y.%m.%d')
        except:
            pass

# Add cover - if file exist
book.spine.append('nav')
generate_cover(book_file_name, all_image_files)
book.set_cover(book_file_name + '.jpg', open(book_file_name + '.jpg', 'rb').read())
book.spine.append('cover')
book.spine.reverse()
# os.remove(book_file_name + '.jpg')

# Add table of contents
table_of_contents.reverse()
book.toc = table_of_contents

# Add default NCX and Nav file
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# Add css file
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
book.add_item(nav_css)

# Add images do epub file_name
if INCLUDE_IMAGES:
    try:
        converted_images = [f for f in listdir(images_path) if isfile(join(images_path, f))]
    except NameError:
        converted_images = []
    for i, image in enumerate(converted_images):
        if image in images_included:
            image_cont = None
            with open(images_path + image, 'r') as content_file:
                image_cont = content_file.read()
            epub_img = epub.EpubItem(uid="img" + str(i), file_name="images/" + image, media_type="image/jpeg",
                                     content=image_cont)
            book.add_item(epub_img)

# Save damn ebook
epub.write_epub(book_file_name + '.epub', book, {})
fix_cover(book_file_name)


class Chapter(object):

    def __init__(self, article, number, language):
        """
        :param article: Article class
        """
        self.epub = epub.EpubHtml(title=article.title, file_name='chap_' + str(number) + '.xhtml', lang=language)
        self.epub.content = '<h2>{}</h2>{}<p><i><a href="{}">{}</a></i></p>'.format(article.title, article.date,
                                                                                    article.url, article.url)

