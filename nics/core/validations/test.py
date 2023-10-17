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


def if_settings_not_found():

    TD = tempfile.mkdtemp()
    DIR = os.path.join(TD, 'nics_dir')

    os.mkdir(os.path.join(DIR, 'pages'))
    open(os.path.join(DIR, 'favicon.ico'), 'w').close()
    tt.both_are_equal(sorted(os.listdir(DIR)), ['favicon.ico', 'pages'])

    with tt.these_will_raise(AssertionError) as its: validations(DIR)
    tt.both_are_equal(its.exception_msg, "The folder should only contain favicon.ico, pages, and settings.txt")


def if_favicon_not_found():

    TD = tempfile.mkdtemp()
    DIR = os.path.join(TD, 'nics_dir')

    os.mkdir(os.path.join(DIR, 'pages'))
    open(os.path.join(DIR, 'settings.txt'), 'w').close()
    tt.both_are_equal(sorted(os.listdir(DIR)), ['pages', 'settings.txt'])

    with tt.these_will_raise(AssertionError) as its: validations(DIR)
    tt.both_are_equal(its.exception_msg, "The folder should only contain favicon.ico, pages, and settings.txt")


def if_pages_dir_not_found():

    TD = tempfile.mkdtemp()
    DIR = os.path.join(TD, 'nics_dir')

    open(os.path.join(DIR, 'favicon.ico'), 'w').close()
    open(os.path.join(DIR, 'settings.txt'), 'w').close()
    tt.both_are_equal(sorted(os.listdir(DIR)), ['favicon.ico', 'settings.txt'])

    with tt.these_will_raise(AssertionError) as its: validations(DIR)
    tt.both_are_equal(its.exception_msg, "The folder should only contain favicon.ico, pages, and settings.txt")


def if_pages_dir_empty():

    TD = tempfile.mkdtemp()
    DIR = os.path.join(TD, 'nics_dir')

    os.mkdir(os.path.join(DIR, 'pages'))
    open(os.path.join(DIR, 'favicon.ico'), 'w').close()
    open(os.path.join(DIR, 'settings.txt'), 'w').close()

    with tt.these_will_raise(AssertionError) as its: validations(DIR)
    tt.both_are_equal(its.exception_msg, "pages/ folder shouldn't be empty")


def if_nonfile_found_in_pages_dir():

    TD = tempfile.mkdtemp()
    DIR = os.path.join(TD, 'nics_dir')

    os.mkdir(os.path.join(DIR, 'pages'))
    open(os.path.join(DIR, 'favicon.ico'), 'w').close()
    open(os.path.join(DIR, 'settings.txt'), 'w').close()

    os.mkdir(os.path.join(DIR, 'pages', 'foo'))
    open(os.path.join(DIR, 'pages', 'about.md'), 'w').close()
    tt.both_are_equal(sorted(os.listdir(os.path.join(DIR, 'pages'))), ['about.md', 'foo'])

    with tt.these_will_raise(AssertionError) as its: validations(DIR)
    tt.both_are_equal(its.exception_msg, "This 'foo' is not a file")


def if_nonmarkdown_found_in_pages_dir():

    TD = tempfile.mkdtemp()
    DIR = os.path.join(TD, 'nics_dir')

    os.mkdir(os.path.join(DIR, 'pages'))
    open(os.path.join(DIR, 'favicon.ico'), 'w').close()
    open(os.path.join(DIR, 'settings.txt'), 'w').close()

    open(os.path.join(DIR, 'pages', 'about.md'), 'w').close()
    open(os.path.join(DIR, 'pages', 'foo.txt'), 'w').close()
    tt.both_are_equal(sorted(os.listdir(os.path.join(DIR, 'pages'))), ['about.md', 'foo.txt'])

    with tt.these_will_raise(AssertionError) as its: validations(DIR)
    tt.both_are_equal(its.exception_msg, "This 'foo.txt' is not a markdown")
