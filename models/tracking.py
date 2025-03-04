from odoo import models, fields, api
from odoo.exceptions import UserError
import requests
import logging

_logger = logging.getLogger(__name__)

class TrackingInfo(models.Model):
    _name = 'tracking.info'
    _description = 'Tracking Information'
    
    api_key = fields.Char(string="API Key", required=True)
    ip = fields.Char(string="Dirección IP")
    pais = fields.Char(string="País")
    ciudad = fields.Char(string="Ciudad")
    longitud = fields.Float(string="Longitud")
    latitud = fields.Float(string="Latitud")
    proveedor = fields.Char(string="Proveedor de Servicios")
    organizacion = fields.Char(string="Organización")
    hora_visita = fields.Datetime(string="Hora de la Visita", default=fields.Datetime.now)

    @api.model
    def get_public_ip(self):
        """Obtiene la IP pública del servidor."""
        try:
            response = requests.get('https://api64.ipify.org?format=json', timeout=5)
            response.raise_for_status()
            return response.json().get("ip")
        except requests.RequestException as e:
            _logger.error(f"Error obteniendo la IP pública: {e}")
            raise UserError("No se pudo obtener la IP pública del servidor.")

    def get_tracking_data(self):
        """Obtiene los datos de geolocalización desde la API y los almacena en el registro."""
        if not self.api_key:
            raise UserError("Debe proporcionar una clave API válida.")

        ip_address = self.get_public_ip()
        api_url = f"https://api.ipgeolocation.io/ipgeo?apiKey={self.api_key}&ip={ip_address}"

        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            data = response.json()

            self.write({
                'ip': ip_address,
                'pais': data.get('country_name'),
                'ciudad': data.get('city'),
                'longitud': data.get('longitude'),
                'latitud': data.get('latitude'),
                'proveedor': data.get('isp'),
                'organizacion': data.get('organization'),
                'hora_visita': fields.Datetime.now(),
            })
        except requests.RequestException as e:
            _logger.error(f"Error al obtener datos de IP Geolocation: {e}")
            raise UserError("No se pudo obtener la información de geolocalización. Verifique su clave API y su conexión a internet.")
