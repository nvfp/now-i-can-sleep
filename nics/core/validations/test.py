import TurboTest as tt
from . import validations

import os
import tempfile


def nics__dir_should_be_a_valid_dir():
    TD = tempfile.mkdtemp()
    DIR = os.path.join(TD, 'not_found')
    tt.this_is_False(os.path.isdir(DIR))
    with tt.these_will_raise(AssertionError) as its: validations(DIR)
    tt.both_are_equal(its.exception_msg, 'not a dir')


def if_favicon_not_found():

    TD = tempfile.mkdtemp()
    DIR = os.path.join(TD, 'nics_dir')

    os.mkdir(os.path.join(DIR, 'pages'))
    open(os.path.join(DIR, 'foo-bar.txt'), 'w').close()
    tt.both_are_equal(sorted(os.listdir(DIR)), ['foo-bar.txt', 'pages'])

    with tt.these_will_raise(AssertionError) as its: validations(DIR)
    tt.both_are_equal(its.exception_msg, "favicon.ico not found")


def if_pages_dir_not_found():

    TD = tempfile.mkdtemp()
    DIR = os.path.join(TD, 'nics_dir')

    open(os.path.join(DIR, 'favicon.ico'), 'w').close()
    open(os.path.join(DIR, 'foo-bar.txt'), 'w').close()
    tt.both_are_equal(sorted(os.listdir(DIR)), ['favicon.ico', 'foo-bar.txt'])

    with tt.these_will_raise(AssertionError) as its: validations(DIR)
    tt.both_are_equal(its.exception_msg, "pages/ not found")


def if_pages_dir_empty():

    TD = tempfile.mkdtemp()
    DIR = os.path.join(TD, 'nics_dir')

    os.mkdir(os.path.join(DIR, 'pages'))
    open(os.path.join(DIR, 'favicon.ico'), 'w').close()
    open(os.path.join(DIR, 'foobar.json'), 'w').close()

    with tt.these_will_raise(AssertionError) as its: validations(DIR)
    tt.both_are_equal(its.exception_msg, "pages/ folder shouldn't be empty")


def if_nonmarkdown_file_found_in_pages_dir():

    TD = tempfile.mkdtemp()
    DIR = os.path.join(TD, 'nics_dir')

    os.mkdir(os.path.join(DIR, 'pages'))
    open(os.path.join(DIR, 'favicon.ico'), 'w').close()

    open(os.path.join(DIR, 'pages', 'about.md'), 'w').close()
    open(os.path.join(DIR, 'pages', 'foo.txt'), 'w').close()
    tt.both_are_equal(sorted(os.listdir(os.path.join(DIR, 'pages'))), ['about.md', 'foo.txt'])

    with tt.these_will_raise(AssertionError) as its: validations(DIR)
    tt.both_are_equal(its.exception_msg, "Only Markdown files allowed in the `pages/` folder.")


def if_a_dir_found_in_pages_dir():

    TD = tempfile.mkdtemp()
    DIR = os.path.join(TD, 'nics_dir')

    os.mkdir(os.path.join(DIR, 'pages'))
    open(os.path.join(DIR, 'favicon.ico'), 'w').close()

    open(os.path.join(DIR, 'pages', 'about.md'), 'w').close()
    os.mkdir(os.path.join(DIR, 'pages', 'foobar'))
    tt.both_are_equal(sorted(os.listdir(os.path.join(DIR, 'pages'))), ['about.md', 'foobar'])

    with tt.these_will_raise(AssertionError) as its: validations(DIR)
    tt.both_are_equal(its.exception_msg, "Only Markdown files allowed in the `pages/` folder.")
