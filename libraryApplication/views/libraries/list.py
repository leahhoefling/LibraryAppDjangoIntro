import sqlite3
from django.shortcuts import render
from libraryApplication.models import Book
from ..connection import Connection


def library_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                lib.id,
                lib.title,
                lib.address
            from libraryApplication_library lib
            """)

            all_libraries = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                library = library()
                library.id = row['id']
                library.title = row['title']
                library.location = row['location']

                all_libraries.append(library)

        # this tells it which data we're wanting to give to the template
        template = 'libraries/list.html'
        context = {
            'all_libraries': all_libraries
        }

        return render(request, template, context)
