from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.ControllerAlmacen import ControllerAlmacen

from db import db

almacen_bp = Blueprint('almacen', __name__)