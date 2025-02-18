from odoo import models, fields
from odoo.exceptions import UserError
import requests
import logging

_logger = logging.getLogger(__name__)

class WeatherInfo(models.Model):
    _name = 'weather.info'
    _description = 'Weather Information'