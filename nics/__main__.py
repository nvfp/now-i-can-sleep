try:
    from nics.main import main
except ModuleNotFoundError:  # This exception occurred during development ('nics' isn't installed via pip)
    from main import main


if __name__ == '__main__':
    main()