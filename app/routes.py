from flask import render_template, flash, redirect, url_for
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import youtube_dl


def humanize_bytes(bytes, precision=1):
    """Return a humanized string representation of a number of bytes.

    Assumes `from __future__ import division`.

    >>> humanize_bytes(1)
    '1 byte'
    >>> humanize_bytes(1024)
    '1.0 kB'
    >>> humanize_bytes(1024*123)
    '123.0 kB'
    >>> humanize_bytes(1024*12342)
    '12.1 MB'
    >>> humanize_bytes(1024*12342,2)
    '12.05 MB'
    >>> humanize_bytes(1024*1234,2)
    '1.21 MB'
    >>> humanize_bytes(1024*1234*1111,2)
    '1.31 GB'
    >>> humanize_bytes(1024*1234*1111,1)
    '1.3 GB'
    """
    abbrevs = (
        (1<<50, 'PB'),
        (1<<40, 'TB'),
        (1<<30, 'GB'),
        (1<<20, 'MB'),
        (1<<10, 'kB'),
        (1, 'bytes')
    )
    if bytes == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytes >= factor:
            break
    return '%.*f %s' % (precision, bytes / factor, suffix)

def humanize_time(seconds):
    """Return a humanized string representation of a number of seconds"""
    abbrevs = (
        (60*60*24, 'd'),
        (60*60, 'h'),
        (60, 'm'),
        (1, 's')
    )
    if seconds == 1:
        return '1s'
    s = ''
    for factor, suffix in abbrevs:
        if seconds >= factor:
            tmp = seconds
            s += str(int(seconds/factor)) + suffix
            seconds -= factor*int(seconds/factor)
    return s


class InputURL(FlaskForm):
    url = StringField('Video URL', validators=[DataRequired()])
    submit = SubmitField('Get')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputURL()
    if form.validate_on_submit():
        #return redirect(url_for('dl'))
        ydl_opts = {\
            #'requested_subtitles' : True,\
            'writesubtitles' : True,\
            'writeautomaticsub' : True,\
            'skip_download' : True\
            }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            test_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            info = ydl.extract_info(form.url.data, download=False)

        return dl(info)
    return render_template('index.html', form=form, general=None)

@app.route('/dl', methods=['GET', 'POST'])
def dl(info=None):
    if not info:
        return redirect(url_for('index'))

    if 'duration' in info:
        info['duration'] = humanize_time(info['duration'])
    for f in info['formats']:
        if 'filesize' in f:
            f['filesize'] = humanize_bytes(f['filesize'])
    return render_template('dl.html', info=info)



'''
todo:
    subtitles
    downloading in parallel
    check of filesize by range trick (download one byte or 413 http error) - usebinary search
'''
