from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
import time

from webUI.auth import login_required
from webUI.db import get_db
from webUI.systemInfo import SystemInfo

bp = Blueprint('webUI', __name__)

@bp.route('/')
def index():
    """
    Index (start) page for webUI.
    """
    sysinf = SystemInfo()
    sysinf.start()

    # return render_template('webUI/index.html')
    while True:
        print(sysinf.staleData)
        renderStats()
        time.sleep(1.0)


def renderStats():
    return render_template('webUI/index.html')
