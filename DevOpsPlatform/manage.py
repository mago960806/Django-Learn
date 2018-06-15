#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    #创建日志目录,如已创建则pass
    try:
        os.makedirs('../logs')
    except:
        pass

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DevOpsPlatform.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        #上面导入异常也可能是由其他原因导致的.
        #确保这个异常确实是由于缺少Django包导致的,而不是由Python2导致的.
        try:
            import django
        except ImportError:
            raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
