from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from webUI.auth import login_required
from webUI.db import get_db

bp = Blueprint('webUI', __name__)

@bp.route('/')
def index():
    """
    Index (start) page for webUI.
    """
    return render_template('webUI/index.html')
