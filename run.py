#!/usr/bin/env python
import sys

from app import create_app
from setting import *

app = create_app()

if __name__ == '__main__':
  port = int(sys.argv[1]) if len(sys.argv) > 1 else DEV_PORT
  app.run(host = DEV_HOST, port = port)